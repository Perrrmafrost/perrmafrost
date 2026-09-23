"""Minimal ComfyUI API client shared by the local render scripts (stdlib only, talks to 127.0.0.1 only)."""
import json, time, uuid, html, pathlib, mimetypes, urllib.request, urllib.parse

HERE = pathlib.Path(__file__).parent


def load_config(path=None):
    p = pathlib.Path(path) if path else HERE / "config.json"
    if not p.exists():
        p = HERE / "config.example.json"
    return json.loads(p.read_text())


def http(url, data=None, headers=None, timeout=60):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def upload_image(base, path):
    path = pathlib.Path(path)
    boundary = uuid.uuid4().hex
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{path.name}\"\r\n"
            f"Content-Type: {mimetypes.guess_type(path.name)[0] or 'image/png'}\r\n\r\n").encode() + path.read_bytes() + \
           f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{boundary}--\r\n".encode()
    res = json.loads(http(f"{base}/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return res["name"]


def set_input(wf, spec, value):
    node, key = spec.split(".", 1)
    wf[node]["inputs"][key] = value


def run(base, wf, poll=3):
    """Queue a workflow, wait for it, and return the list of output file descriptors (filename/subfolder/type)."""
    res = json.loads(http(f"{base}/prompt", json.dumps({"prompt": wf, "client_id": "hereami"}).encode(),
                          {"Content-Type": "application/json"}))
    if res.get("node_errors"):
        raise RuntimeError(f"ComfyUI rejected the workflow: {json.dumps(res['node_errors'])[:800]}")
    pid = res["prompt_id"]
    while True:
        time.sleep(poll)
        hist = json.loads(http(f"{base}/history/{pid}")).get(pid)
        if not hist:
            continue
        if hist.get("status", {}).get("status_str") == "error":
            raise RuntimeError("ComfyUI error, see its console")
        if hist.get("outputs"):
            break
    files = []
    for node_out in hist["outputs"].values():
        for items in node_out.values():
            for it in items if isinstance(items, list) else []:
                if isinstance(it, dict) and "filename" in it:
                    files.append(it)
    return files


def download(base, item, dst):
    q = urllib.parse.urlencode({k: item.get(k, "") for k in ("filename", "subfolder", "type")})
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(http(f"{base}/view?{q}"))
    return dst


def contact_sheet(path, title, groups):
    """Write an HTML contact sheet. groups: [(label, [(caption, image_path), ...]), ...]. Opens in any browser."""
    path = pathlib.Path(path)
    rows = []
    for label, imgs in groups:
        cells = "".join(
            f'<figure><img loading="lazy" src="{html.escape(pathlib.Path(p).resolve().as_uri())}">'
            f'<figcaption>{html.escape(c)}</figcaption></figure>' for c, p in imgs)
        rows.append(f"<section><h2>{html.escape(label)}</h2><div class=row>{cells}</div></section>")
    path.write_text(
        "<!doctype html><meta charset=utf-8><title>" + html.escape(title) + "</title><style>"
        "body{font:14px system-ui;background:#111;color:#eee;margin:16px}h2{font-size:15px;margin:18px 0 6px}"
        ".row{display:flex;flex-wrap:wrap;gap:8px}figure{margin:0;width:260px}img{width:100%;border-radius:4px}"
        "figcaption{font-size:12px;color:#aaa}</style><h1>" + html.escape(title) + "</h1>" + "".join(rows),
        encoding="utf-8")
    return path


def resolve_still(stills, ref):
    """Map a Refs id to its approved still file: CHAR_NOUR_A_front.png, UNIT_JACKAL -> UNIT_JACKAL_REF_A.png,
    PROP_X -> PROP_X_REF.png, LOC_X_NIGHT -> LOC_X_NIGHT_plate.png. Returns None when nothing is approved yet."""
    stills = pathlib.Path(stills)
    for name in (ref, f"{ref}_plate", f"{ref}_REF_A", f"{ref}_REF"):
        p = stills / f"{name}.png"
        if p.exists():
            return p
    return None
