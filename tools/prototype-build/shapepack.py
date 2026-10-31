"""Shape-aware placement. Each specimen is rasterised (its real silhouette, at
its rotation) and placed on an occupancy grid of the plate, so an item may sit
inside the hollow of another one while still keeping a clear gap everywhere.

Units: 1 = 1cqmin, the same units build.py uses. The grid runs at PX pixels
per unit. Silhouettes are rendered once with headless Chromium and cached.
"""
import hashlib
import math
import pickle
from pathlib import Path

import cv2
import numpy as np
from scipy.signal import fftconvolve

import specimens as sp

HERE = Path(__file__).parent
CACHE = HERE / ".mask_cache.pkl"
PX = 4            # grid pixels per plate unit
PAD_U = 24        # extra grid margin (units) so heroes can bleed off the plate
HI = 1.5          # render scale: px per viewBox unit for the master silhouettes
ALPHA_MIN = 24    # alpha (0..255) that counts as "ink"

_masks = {}


def _sig():
    return hashlib.md5(b"".join((HERE / f).read_bytes() for f in ("specimens.py", "specimens_fn.py", "specimens_ar.py", "globe_data.py", "photos.py") if (HERE / f).exists()) + b"".join(p.read_bytes() for p in sorted((HERE / "img-src").glob("*.webp")))).hexdigest()


def _load_cache():
    if CACHE.exists():
        try:
            d = pickle.loads(CACHE.read_bytes())
            if d.get("sig") == _sig():
                return d["m"]
        except Exception:
            pass
    return {}


def _render(missing):
    from playwright.sync_api import sync_playwright
    out = {}
    html = f"<body style='margin:0;background:transparent'>{sp.sprite()}<div id=b></div></body>"
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 900, "height": 900})
        pg.set_content(html)
        for sym, r in missing:
            w, h = sp.SIZES[sym]
            wp, hp = w * HI, h * HI
            s = int(math.ceil(math.hypot(wp, hp))) + 8
            pg.evaluate(
                """([sym, w, h, wp, hp, r, s]) => {
                  const b = document.getElementById('b');
                  b.style.cssText = `position:relative;width:${s}px;height:${s}px;background:transparent`;
                  b.innerHTML = `<svg viewBox="0 0 ${w} ${h}" style="position:absolute;left:50%;top:50%;width:${wp}px;height:${hp}px;overflow:visible;transform:translate(-50%,-50%) rotate(${r}deg)"><use href="#sp-${sym}"/></svg>`;
                }""", [sym, w, h, wp, hp, r, s])
            png = pg.locator("#b").screenshot(omit_background=True)
            arr = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_UNCHANGED)
            out[(sym, r)] = (arr[:, :, 3] >= ALPHA_MIN)
        br.close()
    return out


def prepare(pairs):
    """Make sure silhouettes exist for every (symbol, rotation)."""
    global _masks
    if not _masks:
        _masks = _load_cache()
    missing = sorted({(s, round(float(r), 1)) for s, r in pairs} - set(_masks))
    if missing:
        _masks.update(_render(missing))
        CACHE.write_bytes(pickle.dumps({"sig": _sig(), "m": _masks}))


def silhouette(sym, r, width_u, pad_px=0):
    """Boolean mask of the specimen at width_u plate units, centred on its element centre."""
    m = _masks[(sym, round(float(r), 1))].astype(np.uint8) * 255
    w_vb = sp.SIZES[sym][0]
    ratio = (width_u * PX) / (HI * w_vb)
    nh, nw = max(3, int(round(m.shape[0] * ratio))), max(3, int(round(m.shape[1] * ratio)))
    small = cv2.resize(m, (nw, nh), interpolation=cv2.INTER_AREA) >= 40
    if nh % 2 == 0:  # odd sizes keep the centre on a pixel
        small = np.pad(small, ((0, 1), (0, 0)))
    if small.shape[1] % 2 == 0:
        small = np.pad(small, ((0, 0), (0, 1)))
    if pad_px:
        small = np.pad(small, pad_px)
    return small


def _dilate(mask, gap_px):
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * gap_px + 1, 2 * gap_px + 1))
    return cv2.dilate(mask.astype(np.uint8), k) > 0


class Plate:
    def __init__(self, W, H, title, zone, gap_u):
        self.W, self.H, self.gap = W, H, gap_u
        self.gp = int(round(gap_u * PX))
        self.occ = np.zeros((int((H + 2 * PAD_U) * PX), int((W + 2 * PAD_U) * PX)), bool)
        zx0, zy0, zx1, zy1 = zone
        ys, xs = np.mgrid[0:self.occ.shape[0], 0:self.occ.shape[1]]
        ux, uy = xs / PX - PAD_U, ys / PX - PAD_U
        self.occ |= ~((ux >= zx0) & (ux <= zx1) & (uy >= zy0) & (uy <= zy1))
        tcx, tcy, tw, th = title
        self.occ |= (abs(ux - tcx) < tw / 2) & (abs(uy - tcy) < th / 2)
        self.skip = np.zeros_like(self.occ)

    def _paste(self, m, cx_u, cy_u):
        h, w = m.shape
        top = int(round((cy_u + PAD_U) * PX)) - h // 2
        left = int(round((cx_u + PAD_U) * PX)) - w // 2
        y0, x0 = max(top, 0), max(left, 0)
        y1, x1 = min(top + h, self.occ.shape[0]), min(left + w, self.occ.shape[1])
        if y1 > y0 and x1 > x0:
            self.occ[y0:y1, x0:x1] |= m[y0 - top:y1 - top, x0 - left:x1 - left]

    def add_fixed(self, sym, r, w_u, cx_u, cy_u):
        # hero: ignore the zone/title block so it may bleed; it still blocks others
        self._paste(silhouette(sym, r, w_u), cx_u, cy_u)

    def place(self, sym, r, w_u, target, anchor=None):
        """Closest free centre to target (units). Returns (cx, cy) or None."""
        raw = silhouette(sym, r, w_u, pad_px=self.gp + 2)
        dil = _dilate(raw, self.gp)
        h, w = dil.shape
        if h >= self.occ.shape[0] or w >= self.occ.shape[1]:
            return None
        ov = fftconvolve(self.occ.astype(np.float32), dil[::-1, ::-1].astype(np.float32), mode="valid")
        free = ov < 0.5
        if not free.any():
            return None
        ys, xs = np.nonzero(free)
        cx = (xs + w // 2) / PX - PAD_U
        cy = (ys + h // 2) / PX - PAD_U
        d = (cx - target[0]) ** 2 + (cy - target[1]) ** 2
        i = int(np.argmin(d))
        self._paste(raw, cx[i], cy[i])
        return float(cx[i]), float(cy[i])


# ------------------------------------------------------------------ hole filling
def _largest_hole(self):
    """Radius (units) and centre of the biggest empty circle inside the free zone."""
    free = (~self.occ) & (~self.skip)
    dist = cv2.distanceTransform(free.astype(np.uint8), cv2.DIST_L2, 5)
    i = np.unravel_index(int(np.argmax(dist)), dist.shape)
    return float(dist[i]) / PX, (i[1] / PX - PAD_U, i[0] / PX - PAD_U)


def _skip_hole(self, centre, r_u):
    ys, xs = np.mgrid[0:self.occ.shape[0], 0:self.occ.shape[1]]
    cx, cy = (centre[0] + PAD_U) * PX, (centre[1] + PAD_U) * PX
    self.skip |= (xs - cx) ** 2 + (ys - cy) ** 2 <= (r_u * PX) ** 2


def _place_near(self, sym, r, w_u, centre, win_u=22.0, commit=True):
    """Free spot for the silhouette closest to centre, searched in a local window only."""
    raw = silhouette(sym, r, w_u, pad_px=self.gp + 2)
    dil = _dilate(raw, self.gp)
    h, w = dil.shape
    cx0, cy0 = int(round((centre[0] + PAD_U) * PX)), int(round((centre[1] + PAD_U) * PX))
    half = int(win_u * PX) + max(h, w) // 2
    y0, y1 = max(cy0 - half, 0), min(cy0 + half, self.occ.shape[0])
    x0, x1 = max(cx0 - half, 0), min(cx0 + half, self.occ.shape[1])
    win = self.occ[y0:y1, x0:x1]
    if h >= win.shape[0] or w >= win.shape[1]:
        return None
    ov = fftconvolve(win.astype(np.float32), dil[::-1, ::-1].astype(np.float32), mode="valid")
    ys, xs = np.nonzero(ov < 0.5)
    if not len(ys):
        return None
    px = xs + w // 2 + x0
    py = ys + h // 2 + y0
    d = (px - cx0) ** 2 + (py - cy0) ** 2
    i = int(np.argmin(d))
    pos = (px[i] / PX - PAD_U, py[i] / PX - PAD_U)
    if commit:
        self._paste(raw, pos[0], pos[1])
    return pos


Plate.largest_hole = _largest_hole
Plate.skip_hole = _skip_hole
Plate.place_near = _place_near
