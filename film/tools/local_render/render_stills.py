#!/usr/bin/env python3
"""Generate the production bible's reference stills and plates through a local ComfyUI (brief step 5).

  python render_stills.py                      # priority-1 stills, 4 candidates each (resumable)
  python render_stills.py --priority 2 --takes 2
  python render_stills.py --ids CHAR_NOUR_A_front,CHAR_NOUR_A_34 --takes 6
  python render_stills.py --approve CHAR_NOUR_A_front=3 UNIT_JACKAL_REF_A=1

Prompts come verbatim from stills_manifest.jsonl (built by extract_stills.py from files 01-04).
Candidates go to <stills_dir>/_candidates/<id>/cNN.png and <stills_dir>/contact_sheet.html shows them all;
--approve copies the chosen candidate to <stills_dir>/<id>.png, the name every other script looks for.
Stills the bible derives from a parent (method "edit_from:<parent>") wait until the parent is approved and
are then made with the image-edit workflow from the parent image.
"""
import json, random, shutil, argparse, pathlib
import comfy_client as cc

HERE = pathlib.Path(__file__).parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config")
    ap.add_argument("--manifest", default=str(HERE / "stills_manifest.jsonl"))
    ap.add_argument("--priority", type=int, default=1, help="render entries with priority <= this")
    ap.add_argument("--ids", default="", help="comma-separated still ids (overrides --priority)")
    ap.add_argument("--kind", default="", help="character, unit, prop, location or first_frame")
    ap.add_argument("--takes", type=int, default=4, help="candidates per still")
    ap.add_argument("--approve", nargs="*", default=[], metavar="ID=N")
    ap.add_argument("--redo", action="store_true", help="also re-render stills that are already approved")
    a = ap.parse_args()

    cfg = cc.load_config(a.config)
    base = cfg.get("comfy_url", "http://127.0.0.1:8188")
    stills = HERE / cfg.get("stills_dir", "stills")
    cand_root = stills / "_candidates"
    log_path = stills / "stills_log.json"
    stills.mkdir(parents=True, exist_ok=True)
    log = json.loads(log_path.read_text()) if log_path.exists() else {}
    entries = [json.loads(l) for l in open(a.manifest, encoding="utf-8") if l.strip()]
    by_id = {e["id"]: e for e in entries}

    if a.approve:
        for item in a.approve:
            sid, n = item.split("=")
            src = cand_root / sid / f"c{int(n):02d}.png"
            if not src.exists():
                raise SystemExit(f"{src} does not exist")
            shutil.copyfile(src, stills / f"{sid}.png")
            log.setdefault(sid, {"candidates": []})["approved"] = int(n)
            print(f"approved {sid} <- candidate {n}")
        log_path.write_text(json.dumps(log, indent=1))
        return

    ids = [s.strip() for s in a.ids.split(",") if s.strip()]
    todo = [by_id[i] for i in ids] if ids else [e for e in entries if e.get("priority", 2) <= a.priority]
    if a.kind:
        todo = [e for e in todo if e.get("kind") == a.kind]
    t_wf = json.loads((HERE / cfg.get("stills_workflow", "workflow_stills_api.json")).read_text())
    e_wf = json.loads((HERE / cfg.get("edit_workflow", "workflow_edit_api.json")).read_text())
    tn, en = cfg["stills_nodes"], cfg["edit_nodes"]

    waiting = []
    for e in todo:
        sid = e["id"]
        if (stills / f"{sid}.png").exists() and not a.redo:
            continue
        rec = log.setdefault(sid, {"candidates": []})
        method = e.get("method", "text")
        parent = method.split(":", 1)[1] if method.startswith("edit_from:") else None
        if parent and not (stills / f"{parent}.png").exists():
            waiting.append(f"{sid} (needs {parent}.png approved first)")
            continue
        for n in range(len(rec["candidates"]) + 1, a.takes + 1):
            seed = random.randint(0, 2**31 - 1)
            if parent:
                wf = json.loads(json.dumps(e_wf))
                cc.set_input(wf, en["prompt"], e["prompt"])
                cc.set_input(wf, en["image1"], cc.upload_image(base, stills / f"{parent}.png"))
                for extra in ("image2", "image3"):   # single-reference edit: drop the unused loaders
                    node, key = en[extra].split(".", 1)
                    wf.pop(node, None)
                    for nd in wf.values():
                        nd["inputs"].pop(extra, None)
                cc.set_input(wf, en["width"], e["width"]); cc.set_input(wf, en["height"], e["height"])
                cc.set_input(wf, en["seed"], seed); cc.set_input(wf, en["filename_prefix"], f"HEREAMI_stills/{sid}_c{n:02d}")
            else:
                wf = json.loads(json.dumps(t_wf))
                cc.set_input(wf, tn["prompt"], e["prompt"])
                cc.set_input(wf, tn["width"], e["width"]); cc.set_input(wf, tn["height"], e["height"])
                cc.set_input(wf, tn["seed"], seed); cc.set_input(wf, tn["filename_prefix"], f"HEREAMI_stills/{sid}_c{n:02d}")
            files = cc.run(base, wf)
            dst = cc.download(base, files[0], cand_root / sid / f"c{n:02d}.png")
            rec["candidates"].append({"n": n, "seed": seed, "file": str(dst), "method": method})
            log_path.write_text(json.dumps(log, indent=1))
            print(f"{sid}: candidate {n} -> {dst.name}", flush=True)

    groups = []
    for e in todo:
        sid = e["id"]
        imgs = [(f"c{c['n']:02d} seed {c['seed']}", c["file"]) for c in log.get(sid, {}).get("candidates", [])]
        if (stills / f"{sid}.png").exists():
            imgs.insert(0, ("APPROVED", stills / f"{sid}.png"))
        if imgs:
            groups.append((sid, imgs))
    sheet = cc.contact_sheet(stills / "contact_sheet.html", "HERE AM I — reference stills", groups)
    print(f"contact sheet: {sheet}")
    if waiting:
        print("waiting on a parent still:\n  " + "\n  ".join(waiting))
    print("approve with: python render_stills.py --approve <ID>=<candidate number> ...")


if __name__ == "__main__":
    main()
