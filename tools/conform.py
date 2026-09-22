# -*- coding: utf-8 -*-
"""
Conform: assembles the episode from the EDL with ffmpeg.

For every shot it takes the Veo clip if one exists (renders/SHxxxx.mp4), else
the previs board (boards/SHxxxx.png), trims it to the shot's exact duration,
fits it to the 2.00:1 master, and concatenates in EDL order. Then it lays a
temp sound track (room tone, rain, the chirp, the doorbell, the knock, the
countdown pulse, and the authored silences including the half-second hole
where her name should be), attaches the subtitles, and normalises to -24 LUFS.

    python3 tools/conform.py --source auto     # Veo clips where present, boards elsewhere
    python3 tools/conform.py --source boards   # pure previs
    python3 tools/conform.py --source renders --audio clips --burn-subs

The same code path produces the previs master today and the picture master when
the clips exist. Only the source changes.
"""
import argparse, json, os, subprocess, sys, wave, math
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from platform_tools import find_ffmpeg, ffconcat_line
FF = find_ffmpeg()
W, H, FPS, SR = 1920, 960, 24, 48000
VF = f"scale={W}:1080:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        sys.exit(f"ffmpeg failed:\n{' '.join(cmd)}\n{r.stderr[-1500:]}")

def has_audio(path):
    r = subprocess.run([FF, "-i", path], capture_output=True, text=True)
    return "Audio:" in r.stderr

# ------------------------------------------------------------- picture
def build_segments(shots, source, segdir, limit):
    os.makedirs(segdir, exist_ok=True); used = {"clip": 0, "board": 0}; segs = []
    for s in shots[:limit] if limit else shots:
        seg = os.path.join(segdir, f"{s['id']}.mp4"); segs.append((s, seg))
        clip = P("renders", f"{s['id']}.mp4"); board = P("boards", f"{s['id']}.png")
        use_clip = source in ("auto", "renders") and os.path.exists(clip)
        if os.path.exists(seg) and os.path.getmtime(seg) > os.path.getmtime(clip if use_clip else board):
            used["clip" if use_clip else "board"] += 1; continue
        if use_clip:
            # Clips can be shorter than their shot (Wan makes ~5s). Hold the last
            # frame and pad the audio so every segment is exactly the EDL length;
            # a short segment would push every later shot out of sync.
            cmd = [FF, "-y", "-loglevel", "error", "-i", clip]
            if not has_audio(clip):
                cmd += ["-f", "lavfi", "-t", str(s["d"]), "-i", f"anullsrc=r={SR}:cl=stereo"]
            cmd += ["-vf", VF + f",tpad=stop_mode=clone:stop_duration={s['d']}",
                    "-af", "apad", "-t", str(s["d"]),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                    "-c:a", "aac", "-ar", str(SR), "-ac", "2", seg]
            used["clip"] += 1
        else:
            if not os.path.exists(board):
                sys.exit(f"no source for {s['id']}: neither {clip} nor {board}")
            cmd = [FF, "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS), "-t", str(s["d"]),
                   "-i", board, "-f", "lavfi", "-t", str(s["d"]), "-i", f"anullsrc=r={SR}:cl=stereo",
                   "-vf", VF, "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-crf", "20",
                   "-c:a", "aac", "-ar", str(SR), "-ac", "2", "-shortest", seg]
            used["board"] += 1
        run(cmd)
    return segs, used

def concat(segs, out):
    lst = out + ".txt"
    open(lst, "w").write("".join(ffconcat_line(p) for _, p in segs))
    run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])

# ------------------------------------------------------------- temp sound
def db(x): return 10 ** (x / 20)
def env(n, a=0.005, r=0.02):
    e = np.ones(n); ia, ir = int(a*SR), int(r*SR)
    e[:ia] = np.linspace(0, 1, ia); e[-ir:] = np.linspace(1, 0, ir); return e
def tone(f, d, amp): 
    t = np.arange(int(d*SR)) / SR; return np.sin(2*np.pi*f*t) * amp * env(len(t))
def noise_burst(d, amp, lp=1.0):
    n = np.random.default_rng(7).standard_normal(int(d*SR))
    if lp < 1.0:  # crude one-pole low-pass
        y = np.zeros_like(n); a = lp
        for i in range(1, len(n)): y[i] = y[i-1] + a*(n[i]-y[i-1])
        n = y / (np.abs(y).max() + 1e-9)
    return n * amp * env(len(n))

def temp_track(shots, total, srt_path, out_wav, cd_first, cd_zero):
    rng = np.random.default_rng(3)
    N = int(math.ceil(total * SR)); L = np.zeros(N, np.float32); R = np.zeros(N, np.float32)
    def add(t, sig, pan=0.0):
        i = int(t*SR); j = min(N, i+len(sig)); k = j - i
        if k <= 0: return
        L[i:j] += sig[:k] * (1 - max(0, pan)); R[i:j] += sig[:k] * (1 + min(0, pan))
    # room tone: 1/f noise (octave-summed white noise, Voss-McCartney), normalised
    # by RMS so the level is what the number says it is. A random walk normalised
    # by its peak - the previous version - collapses to -99 dB, which QC caught.
    def pink(n, octaves=10):
        acc = np.zeros(n, np.float64)
        for k in range(octaves):
            step = 2 ** k
            acc += np.repeat(rng.standard_normal(n // step + 1), step)[:n]
        return (acc / np.sqrt(np.mean(acc**2))).astype(np.float32)
    bed = pink(N) * db(-40)
    # rain from 03:15, slow modulation
    rain_on = 195.0
    rain = rng.standard_normal(N).astype(np.float32) * db(-46)
    tt = np.arange(N) / SR; rain *= (0.6 + 0.4*np.sin(2*np.pi*0.07*tt)) * (tt >= rain_on)
    # refrigerator hum in kitchen scenes
    hum = np.zeros(N, np.float32)
    for s in shots:
        if s["loc"] == "KITCHEN":
            i, j = int(s["t"]*SR), int((s["t"]+s["d"])*SR)
            t = np.arange(j-i)/SR; hum[i:j] = (np.sin(2*np.pi*50*t) + 0.4*np.sin(2*np.pi*100*t)) * db(-50)
    for arr in (bed, rain, hum): L += arr; R += arr
    # events
    for s in shots:
        a = (s["audio"] or ""); u = a.upper()
        if "DING-DONG" in u:
            add(s["t"]+0.4, tone(659, 0.28, db(-20))); add(s["t"]+0.7, tone(523, 0.42, db(-20)))
        if "CHIRP" in u:
            pan = 0.7 if ("off-screen" in a or "coffee table" in a) else 0.0
            add(s["t"] + (1.2 if "off-screen" in a else 0.3), tone(3200, 0.08, db(-18)), pan)
        if "knuckle knocks" in a:
            for k, off in enumerate([0, .38, .76, 1.7, 2.08]):
                add(s["t"]+0.6+off, noise_burst(0.07, db(-14), lp=0.18))
        if "Deadbolt" in a or "brass mechanism" in a:
            add(s["t"]+0.5, noise_burst(0.03, db(-18), lp=0.5)); add(s["t"]+0.62, noise_burst(0.05, db(-20), lp=0.35))
        if "Breaker" in a:
            add(s["t"]+0.3, noise_burst(0.05, db(-16), lp=0.4))
        if "Tape parting" in a:
            add(s["t"]+0.3, noise_burst(1.2, db(-24), lp=0.9))
    # countdown pulse: felt, not heard
    t = cd_first
    while t < cd_zero:
        add(t, tone(40, 0.06, db(-34))); t += 1.0
    # authored silences: the bed itself stops
    def mute(a, b):
        i, j = max(0, int(a*SR)), min(N, int(b*SR)); L[i:j] = 0; R[i:j] = 0
    for s in shots:
        u = (s["audio"] or "").upper()
        if "TOTAL SILENCE" in u or "HARD CUT TO ABSOLUTE SILENCE" in u or "SOUND BED CUTS" in u:
            mute(s["t"], s["t"] + s["d"])
    # the redaction: half a second of nothing where her name is
    try:
        blocks = open(srt_path).read().strip().split("\n\n")
        for b in blocks:
            if "[ - - - ]" in b:
                a, z = b.split("\n")[1].split(" --> ")
                h, m, rest = z.split(":"); sec, ms = rest.split(",")
                end = int(h)*3600 + int(m)*60 + int(sec) + int(ms)/1000
                mute(end - 0.5, end); break
    except FileNotFoundError:
        pass
    pcm = np.clip(np.stack([L, R], 1), -1, 1)
    with wave.open(out_wav, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((pcm * 32767).astype(np.int16).tobytes())

# ------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", choices=["auto", "renders", "boards"], default="auto")
    ap.add_argument("--audio", choices=["temp", "clips", "none"], default="temp")
    ap.add_argument("--burn-subs", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--limit", type=int, default=0, help="first N shots only (for tests)")
    a = ap.parse_args()

    data = json.load(open(P("production", "04-previs", "animatic.json")))
    shots = data["shots"]; total = sum(s["d"] for s in (shots[:a.limit] if a.limit else shots))
    srt = P("production", "07-post", "subtitles", "S01E01.srt")
    out = a.out or P("deliverables", "S01E01_%s_master.mp4" % ("previs" if a.source == "boards" else "picture"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    work = P("deliverables", "_work"); os.makedirs(work, exist_ok=True)

    segs, used = build_segments(shots, a.source, os.path.join(work, "seg"), a.limit)
    print(f"segments: {used['clip']} rendered clips, {used['board']} boards")
    picture = os.path.join(work, "picture.mp4"); concat(segs, picture)

    cdf = next(s for s in shots if s["cd"]); cd_first = cdf["t"]
    cd_zero = cd_first + int(cdf["cd"].split(":")[0])*60 + int(cdf["cd"].split(":")[1])
    inputs = ["-i", picture]; maps = ["-map", "0:v"]
    # The temp track is authored at delivery levels, so it is not normalised;
    # clip audio from the model is. Either way the audio is padded and the output
    # is cut to the picture's exact length: loudnorm's end-of-stream flush and
    # -shortest between them took 2.65s off the first master, and QC caught it.
    if a.audio == "temp":
        wav = os.path.join(work, "temp_track.wav")
        temp_track(shots[:a.limit] if a.limit else shots, total, srt, wav, cd_first, cd_zero)
        inputs += ["-i", wav]; maps += ["-map", "1:a"]
        afilter = ["-af", "apad"]
    elif a.audio == "clips":
        maps += ["-map", "0:a?"]; afilter = ["-af", "loudnorm=I=-24:TP=-2:LRA=11,aresample=48000,apad"]
    else:
        afilter = []
    sub_in = ["-i", srt] if os.path.exists(srt) else []
    sub_idx = 2 if a.audio == "temp" else 1
    vf = []
    if a.burn_subs and os.path.exists(srt):
        srt_rel = os.path.relpath(srt, ROOT).replace("\\", "/")
        vf = ["-vf", f"subtitles={srt_rel}:force_style='FontName=FreeSans,FontSize=22,PrimaryColour=&H00F0F3F6,OutlineColour=&H80000000,Outline=1,MarginV=36'"]
    cmd = [FF, "-y", "-loglevel", "error"] + inputs + sub_in + maps
    if sub_in:
        cmd += ["-map", f"{sub_idx}:s", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng"]
    cmd += vf + (["-c:v", "libx264", "-preset", "veryfast", "-crf", "18"] if vf else ["-c:v", "copy"])
    cmd += ["-c:a", "aac", "-b:a", "192k"] + afilter + ["-movflags", "+faststart", "-t", f"{total:.3f}", out]
    run(cmd)
    r = subprocess.run([FF, "-i", out], capture_output=True, text=True).stderr
    dur = [l for l in r.splitlines() if "Duration" in l]
    print(f"wrote {out}\n{dur[0].strip() if dur else ''}")
    print(f"audio: {a.audio}   subtitles: {'burned + soft' if a.burn_subs else 'soft track'}")

if __name__ == "__main__":
    main()
