"""Photographic specimens: processed WebP cut-outs that replace the SVG drawings.

Each file in img/<symbol>.webp (trimmed to its alpha bounding box) replaces the
SVG symbol of the same name. The symbol canvas keeps the old width and takes the
photo's aspect ratio, so the packer measures real photo silhouettes.
"""
import base64
import struct
from pathlib import Path

HERE = Path(__file__).parent
IMG = HERE / "img-src"          # master cut-outs (never shipped)
OUT = HERE.parent / "img"          # optimised files the page loads
MODE = "inline"                    # "inline": data URIs (mask rendering), "file": img/<sym>.webp


def _webp_size(b: bytes):
    if b[12:16] == b"VP8X":
        return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
    if b[12:16] == b"VP8 ":
        w, h = struct.unpack("<HH", b[26:30]); return w & 0x3FFF, h & 0x3FFF
    if b[12:16] == b"VP8L":
        v = int.from_bytes(b[21:25], "little"); return 1 + (v & 0x3FFF), 1 + ((v >> 14) & 0x3FFF)
    raise ValueError("unknown webp")


def load(old_sizes):
    """-> {symbol: (canvas_w, canvas_h, data_uri)}"""
    out = {}
    for f in sorted(IMG.glob("*.webp")):
        sym = f.stem
        if sym not in old_sizes:
            continue
        raw = f.read_bytes()
        pw, ph = _webp_size(raw)
        w = old_sizes[sym][0]
        h = max(1, round(w * ph / pw))
        out[sym] = (w, h, f)
    return out


def symbol(sym, w, h, path):
    if MODE == "file":
        uri = f"img/{sym}.webp"
    else:
        uri = "data:image/webp;base64," + base64.b64encode(Path(path).read_bytes()).decode()
    return (f'<g id="sp-{sym}"><image href="{uri}" x="0" y="0" width="{w}" height="{h}" '
            f'preserveAspectRatio="none"/></g>')


def optimise(max_units, px_per_unit=12, lo=140, hi=900, quality=80):
    """Write right-sized WebP files for the page. max_units: {symbol: widest placement in plate units}."""
    from PIL import Image
    OUT.mkdir(exist_ok=True)
    keep, total = set(), 0
    for f in sorted(IMG.glob("*.webp")):
        sym = f.stem
        if sym not in max_units:
            continue
        im = Image.open(f)
        target = int(min(hi, max(lo, max_units[sym] * px_per_unit)))
        if im.width > target:
            im = im.resize((target, max(1, round(im.height * target / im.width))), Image.LANCZOS)
        dst = OUT / f"{sym}.webp"
        im.save(dst, "WEBP", quality=quality, method=6)
        keep.add(dst.name); total += dst.stat().st_size
    for stale in OUT.glob("*.webp"):
        if stale.name not in keep:
            stale.unlink()
    return len(keep), total
