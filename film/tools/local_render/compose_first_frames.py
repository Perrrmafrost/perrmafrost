#!/usr/bin/env python3
"""Compose each shot's first frame from approved stills (file 05 §12 step 4), for image-to-video.

  python compose_first_frames.py ../../shots/seq_01_shots.jsonl [--only 01.01.001,...] [--takes 2]
  python compose_first_frames.py --approve 01.01.001=2 01.01.002=1
  python compose_first_frames.py ../../shots/seq_01_shots.jsonl --auto   # unattended: approve candidate 1

For every shot that is not an EXTEND child (those start from the parent's last frame in render_queue.py),
the image-edit workflow gets up to three references: the location plate from Refs as image 1, then the
first two subjects in Refs (characters first, then units, then props) as images 2 and 3. The prompt is
the shot's derived motion prompt, framed as "the opening moment of this shot". Candidates go to
<stills_dir>/_first_frames/<id>/cNN.png with a contact sheet; the approved one becomes <stills_dir>/<id>.png,
which render_queue.py uses as the start image.
"""
import sys, json, random, shutil, argparse, pathlib
import comfy_client as cc

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from shots_md2jsonl import load_fixed  # noqa: E402  (the compact suffix, read from the bible)

WIDE = ("EWS", "WS", "LS", "FS", "wide", "full")


def token_of(ref, tokens):
    """The bible token a Refs id belongs to (longest match: CHAR_TUT_CHILD_9_front -> CHAR_TUT_CHILD_9)."""
    hits = [t for t in tokens if ref == t or ref.startswith(t + "_")]
    return max(hits, key=len) if hits else ref


def pick_refs(shot, stills, tokens):
    plate, subjects, seen = None, [], set()
    wide = any(w in shot.get("shot", "") for w in WIDE)
    refs = shot.get("refs", [])
    for ref in refs:
        if ref.startswith("LOC_") and plate is None:
            plate = cc.resolve_still(stills, ref)
    for kind in ("CHAR", "UNIT", "PROP"):
        for ref in refs:
            if not ref.startswith(kind + "_"):
                continue
            token = token_of(ref, tokens)
            if token in seen:
                continue
            same = [r for r in refs if token_of(r, tokens) == token]
            pref = [r for r in same if r.endswith("_full")] if wide else [r for r in same if r.endswith("_front")]
            path = next((p for p in (cc.resolve_still(stills, r) for r in pref + same) if p), None)
            if path:
                seen.add(token); subjects.append(path)
    return plate, subjects[:2]


def edit_prompt(shot, compact_suffix, plate, n_subjects):
    scene = shot.get("motion_prompt") or shot["prompt"]
    scene = scene.replace(compact_suffix, "").strip()
    parts = ["Create one photorealistic frame from a live-action feature film, 16:9 full frame, no text, no letterbox bars."]
    if plate:
        parts.append("Use image 1 as the location: keep its architecture, layout and lighting.")
    if n_subjects:
        imgs = " and ".join(f"image {i}" for i in range(2 if plate else 1, (2 if plate else 1) + n_subjects))
        parts.append(f"The people, machines and objects shown in {imgs} keep exactly the same face, hair, body, "
                     "clothing and design as in those reference images, placed naturally into the scene and lit by its light.")
    parts.append("Show the opening moment of this shot: " + scene)
    return " ".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="*")
    ap.add_argument("--config")
    ap.add_argument("--only", default="")
    ap.add_argument("--takes", type=int, default=2)
    ap.add_argument("--approve", nargs="*", default=[], metavar="ID=N")
    ap.add_argument("--auto", action="store_true", help="approve candidate 1 of every shot without review")
    a = ap.parse_args()

    cfg = cc.load_config(a.config)
    base = cfg.get("comfy_url", "http://127.0.0.1:8188")
    stills = HERE / cfg.get("stills_dir", "stills")
    root = stills / "_first_frames"

    if a.approve:
        for item in a.approve:
            sid, n = item.split("=")
            src = root / sid / f"c{int(n):02d}.png"
            if not src.exists():
                raise SystemExit(f"{src} does not exist")
            shutil.copyfile(src, stills / f"{sid}.png")
            print(f"approved first frame {sid} <- candidate {n}")
        return

    fixed, locks = load_fixed()
    template = json.loads((HERE / cfg.get("edit_workflow", "workflow_edit_api.json")).read_text())
    en = cfg["edit_nodes"]
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    groups, missing = [], []
    for path in a.jsonl:
        for line in open(path, encoding="utf-8"):
            if not line.strip():
                continue
            shot = json.loads(line); sid = shot["id"]
            if only and sid not in only:
                continue
            if any(f.startswith("EXTEND:") for f in shot.get("flags", [])):
                continue
            plate, subjects = pick_refs(shot, stills, locks)
            imgs = ([plate] if plate else []) + subjects
            if not imgs:
                missing.append(f"{sid}: no approved still for any of {shot.get('refs')}")
                continue
            have = sorted((root / sid).glob("c*.png")) if (root / sid).exists() else []
            if not (stills / f"{sid}.png").exists():
                for n in range(len(have) + 1, a.takes + 1):
                    wf = json.loads(json.dumps(template))
                    keys = ["image1", "image2", "image3"]
                    for key, img in zip(keys, imgs):
                        cc.set_input(wf, en[key], cc.upload_image(base, img))
                    for key in keys[len(imgs):]:        # fewer than three references: drop the unused loaders
                        wf.pop(en[key].split(".", 1)[0], None)
                        for nd in wf.values():
                            nd["inputs"].pop(key, None)
                    cc.set_input(wf, en["prompt"], edit_prompt(shot, fixed["SUFFIX_COMPACT"], plate, len(subjects)))
                    cc.set_input(wf, en["width"], 1280); cc.set_input(wf, en["height"], 720)
                    cc.set_input(wf, en["seed"], random.randint(0, 2**31 - 1))
                    cc.set_input(wf, en["filename_prefix"], f"HEREAMI_first_frames/{sid}_c{n:02d}")
                    cc.download(base, cc.run(base, wf)[0], root / sid / f"c{n:02d}.png")
                    print(f"{sid}: first-frame candidate {n} from {[p.stem for p in imgs]}", flush=True)
                if a.auto and (root / sid / "c01.png").exists():
                    shutil.copyfile(root / sid / "c01.png", stills / f"{sid}.png")
            cands = sorted((root / sid).glob("c*.png")) if (root / sid).exists() else []
            shown = ([("APPROVED", stills / f"{sid}.png")] if (stills / f"{sid}.png").exists() else []) + \
                    [(c.stem, c) for c in cands] + [(f"ref: {p.stem}", p) for p in imgs]
            groups.append((f"{sid} — {shot.get('title', shot.get('action', ''))[:80]}", shown))
    if groups:
        print("contact sheet:", cc.contact_sheet(stills / "first_frames.html", "HERE AM I — first frames", groups))
    if missing:
        print("shots with no approved reference still yet:\n  " + "\n  ".join(missing))
    print("approve with: python compose_first_frames.py --approve <shot id>=<candidate number> ...")


if __name__ == "__main__":
    main()
