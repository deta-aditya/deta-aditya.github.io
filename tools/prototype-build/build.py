"""Assemble hero-b.html from template.html and the specimen sprite.

Composition follows the encyclopedia cover pattern, not a scatter:
  * one HERO per plate, large, fixed, allowed to bleed off the plate edge
  * SATELLITES (mid size) and MICRO items (small) in the space the title leaves
  * nothing touches: satellites keep clear space from each other, the hero
    and the title block
The hero is placed by hand. A small packer only settles the other items
around it. Plate shapes are fixed per layout (landscape 2:1, portrait
100:128), so percent placement is the same on every viewport. Units: 1 = 1cqmin.
"""
import math
import sys
import xml.dom.minidom as minidom
from pathlib import Path

import shapepack
import specimens as sp

HERE = Path(__file__).parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "hero-b.html"

# plate W, H, title rect (cx, cy, w, h), zone for non-hero items (x0, y0, x1, y1), all in units
LAYOUTS = {
    "l": (200.0, 100.0, (51.0, 46.0, 102.0, 46.0), (106.0, 2.0, 198.0, 98.0)),
    "p": (100.0, 128.0, (50.0, 31.0, 100.0, 48.0), (2.0, 57.0, 98.0, 126.0)),
}
GAP = 2.6          # clear space between any two silhouettes and around the title
TUCK = 2.2         # clear space between a hero and its satellites (nothing touches)
Z_MICRO, Z_SAT, Z_HERO = 1, 2, 3

H = "H"  # marks the hero placement
F = "F"  # marks a hand placed starting position (the packer may still nudge it)
# (symbol, stage, landscape home, landscape fullstack, portrait home, portrait fullstack)
# placement = (x, y, width, rotation[, H]) in plate units, or None when absent
ITEMS = [
    # frontend: hero is the vintage monitor; every item is hand placed (F)
    ("monitor",   "fe", (172, 52, 68, 0, H),  (192, 22, 22, 0),    (76, 92, 52, 0, H),  None),
    ("eye",       "fe", (121, 12, 32, -4, F), (122, 16, 28, -4),   (28, 68, 36, -4, F), (26, 68, 38, -4)),
    ("prism",     "fe", (127, 36, 34, 3, F),  None,                (27, 89, 28, 3, F),  None),
    ("palette",   "fe", (120, 59, 26, -8, F), None,                (24, 110, 24, -8, F), None),
    ("fan",       "fe", (116, 80.8, 18, -10, F), None,             (48, 108, 17, -10, F), None),
    ("ruler",     "fe", (118, 95.4, 38, -2, F), None,              (21, 123.5, 34, -2, F), None),
    ("brush",     "fe", (172, 9, 38, -3, F),  None,                (62, 119.5, 24, -4, F), None),
    ("pencil",    "fe", (160, 92.5, 30, 3, F), None,               (88, 122, 20, 4, F),  None),
    ("typeblock", "fe", (190, 14, 12, 6, F),  None,                (52, 86, 11, 6, F),   None),
    ("typeblock2", "fe", (184, 98, 8, -10, F), None,              (92, 63, 9, -10, F),  None),
    ("typeblock3", "fe", (134, 62, 11, 4, F),  None,                (20, 80, 10, 4, F),   None),
    ("cursor",    "fe", (140, 30, 12, -4, F), None,                (14, 100, 10, -4, F), None),
    ("setsquare", "fe", (164, 15, 16, 6, F),  None,                (90, 100, 14, 6, F),  None),
    # backend: hero is the mainframe cabinet (red lacquer, matches the accent)
    ("mainframe", "be", (175, 60, 52, 0, H),  (124, 54, 30, 0),    (76, 96, 44, 0, H),  None),
    ("gears",     "be", (126, 50, 32, 0, F),  None,                (26, 72, 28, 0, F),  None),
    ("key",       "be", (140, 16, 34, -7, F), (160, 94, 30, -7),   (72, 66, 34, -7),    (46, 118, 30, -7)),
    ("card",      "be", (176, 14, 26, -5, F), None,                (28, 112, 26, -5),   None),
    ("padlock",   "be", (122, 84, 19, 10, F), None,                (14, 70, 18, 10),    None),
    ("watch",     "be", (150, 88, 19, 7, F),  (190, 92, 14, 7),    (22, 92, 18, 7),     (14, 114, 16, 7)),
    ("coins",     "be", (190, 92, 12, 0, F),  None,                (6, 116, 10, 0),     None),
    ("abacus",    "be", (134, 92, 24, -4, F), None,                (28, 36, 26, -4),    None),
    ("ledger",    "be", (118, 66, 16, 4, F),  None,                (16, 96, 18, 4),     None),
    ("vault",     "be", (150, 70, 18, 0, F),  None,                (48, 100, 20, 0),    None),
    ("hourglass", "be", (176, 94, 12, 6, F),  None,                (92, 30, 12, 6),     None),
    ("scales",    "be", (156, 22, 16, 0, F),  None,                (60, 24, 14, 0),     None),
    ("telegraph", "be", (150, 10, 16, 4, F),  None,                (46, 70, 18, 4),     None),
    # AI native: hero is the plasma globe (amber glass, matches the accent)
    ("plasma",    "ai", (176, 60, 48, 0, H),  (190, 90, 20, 0),    (78, 96, 40, 0, H),  None),
    ("neuron",    "ai", (130, 20, 30, -5, F), (128, 86, 28, -3),   (30, 68, 32, -5, F), (28, 92, 30, -3)),
    ("butterfly", "ai", (126, 52, 24, -12, F), None,               (26, 96, 24, -12, F), None),
    ("nautilus",  "ai", (134, 84, 17, 10, F), None,                (52, 112, 16, 10, F), None),
    ("molecule",  "ai", (178, 14, 16, -10, F), (186, 14, 16, -10), (86, 66, 14, -10, F), (88, 66, 16, -10)),
    ("crystal",   "ai", (150, 50, 15, 3, F),  (118, 94, 14, 3),    (48, 92, 14, 3, F),  None),
    ("honey",     "ai", (190, 44, 12, 8, F),  None,                (14, 30, 12, 8, F),  None),
    ("tree",      "ai", (162, 8, 26, -3, F),  None,                (26, 14, 28, -3, F), None),
    ("trilobite", "ai", (186, 10, 20, 8, F),  None,                (70, 14, 20, 8, F),  None),
    ("feather",   "ai", (122, 72, 24, -10, F), None,               (18, 52, 24, -10, F), None),
    ("telescope", "ai", (140, 94, 26, 6, F),  None,                (30, 120, 28, 6, F), None),
    ("samara",    "ai", (118, 38, 14, 20, F), None,                (88, 40, 12, 20, F), None),
    ("starfish",  "ai", (190, 96, 14, 0, F),  None,                (10, 100, 14, 0, F), None),
    ("beetle",    "ai", (150, 76, 13, 12, F), None,                (88, 54, 12, 12, F), None),
    ("fern",      "ai", (118, 18, 12, -8, F), None,                (8, 76, 12, -8, F),  None),
    # functional: hero is the nested enamel egg (violet, matches the accent)
    ("egg",        "fn", (175, 54, 40, 0, H),  (118, 90, 13, 0),    (78, 82, 38, 0, H),  None),
    ("astrolabe",  "fn", (128, 24, 30, 8, F),  None,                (26, 72, 30, 8, F),  None),
    ("sliderule",  "fn", (148, 9, 44, -4, F),  None,                (30, 118, 44, -4, F), None),
    ("newtons",    "fn", (148, 88, 24, 0, F),  None,                (24, 98, 28, 0, F),  None),
    ("metronome",  "fn", (122, 68, 18, 3, F),  None,                (88, 72, 18, 3, F),  None),
    ("dominoes",   "fn", (146, 30, 20, -6, F), None,                (52, 112, 20, -6, F), None),
    ("dice",       "fn", (118, 45, 14, 0, F),  None,                (60, 80, 18, 0, F),  None),
    ("pawn",       "fn", (192, 10, 9, 0, F),   None,                None,                None),
    ("tuningfork", "fn", (140, 66, 11, 8, F),  None,                (14, 114, 14, 12, F), None),
    ("blocklambda","fn", (112, 92, 10, 4, F),  None,                (16, 60, 10, 4, F),  None),
    ("blockcompose","fn", (164, 94, 9, -6, F), None,                (92, 100, 10, -6, F), None),
    ("blockpi",    "fn", (130, 90, 9, 6, F),   None,                (70, 60, 10, 6, F),  None),
    # architecture: hero is the verdigris rotunda (teal, matches the accent)
    ("rotunda",    "ar", (168, 64, 64, 0, H),  (134, 22, 28, 0),    (76, 96, 46, 0, H),  None),
    ("blueprint",  "ar", (128, 12, 40, -4, F), None,                (30, 70, 44, -4, F), None),
    ("theodolite", "ar", (122, 58, 22, 3, F),  None,                (22, 106, 22, 3, F), None),
    ("dividers",   "ar", (140, 88, 18, 10, F), None,                (52, 100, 20, 10, F), None),
    ("archstone",  "ar", (126, 36, 26, 0, F),  None,                (48, 70, 30, 0, F),  None),
    ("ionic",      "ar", (128, 90, 18, 0, F),  None,                None,                None),
    ("spiritlevel", "ar", (166, 10, 42, -3, F), None,               (30, 120, 40, -3, F), None),
    ("tsquare",    "ar", (152, 94, 18, 0, F),  None,                None,                None),
    ("plumb",      "ar", (113, 86, 4.5, 0, F),   None,                (14, 90, 6, 0, F),   None),
    ("protractor", "ar", (150, 96, 16, 0, F),  None,                (60, 118, 20, 0, F), None),
    ("trowel",     "ar", (112, 22, 20, -8, F), None,                (60, 94, 22, -8, F), None),
    ("bricks",     "ar", (132, 74, 12, 0, F),  None,                (88, 100, 16, 0, F), None),
    # fullstack: hero is the globe (green seas, matches the accent); earlier heroes become satellites
    ("globe",     "all", None,                (172, 54, 50, 0, H), None,                (72, 84, 40, 0, H)),
    ("compass",   "all", None,                (152, 17, 24, -8),   None,                (76, 66, 22, -8)),
]


# --- fill guide: after the main items are placed, empty circles bigger than
# MAX_HOLE_R (units) get a small filler specimen, never closer than GAP to anything,
# and never more than FILL_CAP fillers per plate so it stays an encyclopedia, not a heap.
MAX_HOLE_R = 7.0
FILL_CAP = {"l": 12, "p": 6}
MAX_REPEAT = 2   # a specimen may appear at most this many times as filler per plate
FILL_W_MIN, FILL_W_MAX = 7.0, 22.0
ROTS = [-14.0, 8.0, -6.0, 12.0, 0.0, -20.0, 18.0]
POOLS = {
    "fe": ["typeblock3", "cursor", "setsquare", "pencil", "fan"],
    "be": ["abacus", "ledger", "coins", "padlock", "watch", "key", "telegraph", "hourglass", "scales", "vault"],
    "ai": ["tree", "honey", "nautilus", "crystal", "butterfly", "molecule", "trilobite", "feather", "telescope", "samara", "beetle", "fern", "starfish"],
    "fn": [],
    "ar": [],
    "fs": ["typeblock3", "cursor", "abacus", "nautilus", "ledger", "butterfly", "honey", "setsquare", "hourglass", "beetle", "scales", "starfish"],
}
NO_NEST = {"plumb", "egg"}   # thin items keep their own start position
MICRO_W = 17.0     # items this small (at their starting width) nestle against the hero
MIN_W = 3.5
SHRINK = 0.95


def pack(layout, entries, pool=None):
    """Shape-aware: place every non-hero item at the free spot nearest its starting
    position (micro items: nearest the hero), keeping GAP clear of all silhouettes."""
    W, Hh, title, zone = LAYOUTS[layout]
    shapepack.prepare([(e["sym"], e["r"]) for e in entries])
    plate = shapepack.Plate(W, Hh, title, zone, GAP)
    heroes = [e for e in entries if e["hero"]]
    for h in heroes:
        plate.add_fixed(h["sym"], h["r"], h["w"], h["x"], h["y"])
        h["cx"], h["cy"] = h["x"], h["y"]
    hc = (sum(h["x"] for h in heroes) / len(heroes), sum(h["y"] for h in heroes) / len(heroes)) if heroes else None
    rest = [e for e in entries if not e["hero"]]
    rest.sort(key=lambda e: -int(shapepack.silhouette(e["sym"], e["r"], e["w"]).sum()))
    for e in rest:
        w0 = e["w"]
        target = hc if (hc and w0 <= MICRO_W and e["sym"] not in NO_NEST) else (e["x"], e["y"])
        w = w0
        while w >= MIN_W:
            pos = plate.place(e["sym"], e["r"], w, target)
            if pos:
                e["cx"], e["cy"], e["w"] = pos[0], pos[1], w
                break
            w *= SHRINK
        else:
            e["cx"] = e["cy"] = None
            print(f"  dropped {e['sym']} in {layout}", file=sys.stderr)
    for e in entries:
        if e.get("cx") is None:
            e["x"] = e["y"] = None
            continue
        e["x"], e["y"], e["w"] = round(e["cx"], 2), round(e["cy"], 2), round(e["w"], 2)

    fillers = []
    if pool:
        shapepack.prepare([(sym, r) for sym in POOLS[pool] for r in ROTS])
        n0, cnt, start, guard = 0, 0, 0, 0
        used = {e["sym"] for e in entries if e.get("cx") is not None}
        r_before, _ = plate.largest_hole()
        while cnt < FILL_CAP[layout] and guard < 60:
            guard += 1
            R, centre = plate.largest_hole()
            if R <= MAX_HOLE_R:
                break
            w_cap = min(2 * R * 1.1, FILL_W_MAX)
            best = None
            for k in range(len(POOLS[pool])):
                sym = POOLS[pool][(start + k) % len(POOLS[pool])]
                r = ROTS[(cnt + k) % len(ROTS)]
                if sym in used or any(f["sym"] == sym for f in fillers):
                    continue   # every specimen is unique within a stage
                w = w_cap
                while w >= FILL_W_MIN:
                    pos = plate.place_near(sym, r, w, centre, commit=False)
                    if pos and math.hypot(pos[0] - centre[0], pos[1] - centre[1]) <= R:
                        break
                    w *= 0.9
                else:
                    continue
                if best is None or w > best[0]:
                    best = (w, sym, r)
                if w >= 0.85 * w_cap:
                    break
            if best:
                w, sym, r = best
                pos = plate.place_near(sym, r, w, centre, commit=True)
                fillers.append(dict(sym=sym, x=round(pos[0], 2), y=round(pos[1], 2), w=round(w, 2), r=r))
                cnt += 1
                start += 1
            else:
                plate.skip_hole(centre, R)
        r_after, _ = plate.largest_hole()
        print(f"  fill {layout}/{pool}: +{len(fillers)} fillers, largest hole {r_before:.1f} -> {r_after:.1f} units", file=sys.stderr)
    return fillers


def _entries(col, pick):
    out = []
    for i, it in enumerate(ITEMS):
        if not pick(it):
            continue
        p = it[col]
        mark = p[4] if len(p) > 4 else None
        out.append(dict(i=i, sym=it[0], x=p[0], y=p[1], w=p[2], r=p[3], hero=mark == H, fixed=mark == H))
    return out


def solve():
    """Return ({item index: {layout: {'home': p, 'fs': p}}}, extras). p = (x, y, w, r, z), units.
    extras are the filler specimens: dicts with layout, stage, sym, x, y, w, r."""
    out = {i: {"l": {}, "p": {}} for i in range(len(ITEMS))}
    extras = []
    for li, col in (("l", 2), ("p", 4)):
        plans = [(s, "home", col, lambda it, s=s: it[1] == s and it[col]) for s in ("fe", "be", "ai", "fn", "ar")]
        plans.append(("fs", "fs", col + 1, lambda it, c=col + 1: it[c]))
        for pool, key, c, pick in plans:
            es = _entries(c, pick)
            fillers = pack(li, es, pool)
            for e in es:
                if e["x"] is None:
                    continue
                z = Z_HERO if e["hero"] else (Z_SAT if e["w"] > 17 else Z_MICRO)
                out[e["i"]][li][key] = (e["x"], e["y"], e["w"], e["r"], z)
            for f in fillers:
                extras.append(dict(f, layout=li, stage="all" if pool == "fs" else pool))
    return out, extras


def render_extra(k, ex, kf=None):
    sym, lay, stage = ex["sym"], ex["layout"], ex["stage"]
    w, h = sp.SIZES[sym]
    W, Hh = LAYOUTS[lay][:2]
    x, y = round(ex["x"] / W * 100, 2), round(ex["y"] / Hh * 100, 2)
    props = [f"--k:{k}", f"--kf:{kf if kf is not None else k}", f"aspect-ratio:{w}/{h}",
             f"--{lay}x:{x}%", f"--{lay}y:{y}%", f"--{lay}w:{ex['w']}", f"--{lay}r:{ex['r']}deg", f"--{lay}z:{Z_MICRO}"]
    cls = ["s", f"s--{stage}", f"{lay}-only"]
    if stage == "all":
        cls.append("fs")
        props += [f"--{lay}fx:{x}%", f"--{lay}fy:{y}%", f"--{lay}fw:{ex['w']}", f"--{lay}fr:{ex['r']}deg", f"--{lay}fz:{Z_MICRO}"]
    return (f'      <svg class="{" ".join(cls)}" viewBox="0 0 {w} {h}" style="{";".join(props)}" aria-hidden="true">'
            f'<use href="#sp-{sym}"/></svg>')


def render_item(k, it, placed, kf=None):
    sym, stage = it[0], it[1]
    w, h = sp.SIZES[sym]
    cls = ["s", f"s--{stage}"]
    props = [f"--k:{k}", f"--kf:{kf if kf is not None else k}", f"aspect-ratio:{w}/{h}"]
    sizes = {"l": LAYOUTS["l"][:2], "p": LAYOUTS["p"][:2]}
    for lay in ("l", "p"):
        home, fs = placed[lay].get("home"), placed[lay].get("fs")
        base = home or (fs if stage == "all" else None)
        if not base:
            continue
        W, Hh = sizes[lay]

        def pct(p):
            return (round(p[0] / W * 100, 2), round(p[1] / Hh * 100, 2))
        x, y = pct(base)
        props += [f"--{lay}x:{x}%", f"--{lay}y:{y}%", f"--{lay}w:{base[2]}", f"--{lay}r:{base[3]}deg", f"--{lay}z:{base[4]}"]
        if fs:
            fx, fy = pct(fs)
            props += [f"--{lay}fx:{fx}%", f"--{lay}fy:{fy}%", f"--{lay}fw:{fs[2]}", f"--{lay}fr:{fs[3]}deg", f"--{lay}fz:{fs[4]}"]
        elif lay == "p":
            cls.append("nfs-p")
    if placed["l"].get("fs") or placed["p"].get("fs"):
        cls.append("fs")
    if not (placed["p"].get("home") or placed["p"].get("fs")):
        cls.append("no-p")
    if not (placed["l"].get("home") or placed["l"].get("fs")):
        cls.append("p-only")
    return (f'      <svg class="{" ".join(cls)}" viewBox="0 0 {w} {h}" style="{";".join(props)}" aria-hidden="true">'
            f'<use href="#sp-{sym}"/></svg>')


def main():
    placed, extras = solve()
    # widest placement per symbol (plate units) decides each image's shipped resolution
    widest = {}
    for k, it in enumerate(ITEMS):
        for lay in ("l", "p"):
            for key in ("home", "fs"):
                pos = placed[k][lay].get(key)
                if pos:
                    widest[it[0]] = max(widest.get(it[0], 0), pos[2])
    for ex in extras:
        widest[ex["sym"]] = max(widest.get(ex["sym"], 0), ex["w"])
    import photos
    for stage in ("fe", "be", "ai", "fn", "ar"):
        want = {i[0] for i in ITEMS if i[1] == stage} | set(POOLS[stage])
        want = {w for w in want if (photos.IMG / f"{w}.webp").exists()}
        got = {it[0] for k, it in enumerate(ITEMS) if it[1] == stage and placed[k]["l"].get("home")} | {
            ex["sym"] for ex in extras if ex["layout"] == "l" and ex["stage"] == stage}
        if want - got:
            print(f"  WARNING {stage}: photographed but not shown on desktop: {sorted(want - got)}", file=sys.stderr)
    n_img, n_bytes = photos.optimise(widest)
    print(f"  images: {n_img} files, {n_bytes // 1024} KB in {photos.OUT}", file=sys.stderr)
    photos.MODE = "file"
    sprite = sp.sprite()
    minidom.parseString(sprite)
    # Entrance stagger is a rank inside the stage (--k) and, for the fullstack
    # arrival, a rank among everything that joins that stage (--kf). Global item
    # order must never drive the delay, or later stages would start later.
    krank, count = {}, {}
    for i, it in enumerate(ITEMS):
        krank[i] = count.get(it[1], 0)
        count[it[1]] = krank[i] + 1
    has_fs = [i for i, it in enumerate(ITEMS) if placed[i]["l"].get("fs") or placed[i]["p"].get("fs")]
    kfrank = {i: n for n, i in enumerate(has_fs)}
    items = "\n".join(render_item(krank[k], it, placed[k], kfrank.get(k)) for k, it in enumerate(ITEMS))
    groups = {}
    for j, ex in enumerate(extras):
        groups.setdefault((ex["layout"], ex["stage"]), []).append(j)
    ks, kfs = {}, {}
    for (lay, st), js in groups.items():
        if st == "all":
            span = len(has_fs)
            for n, j in enumerate(js):
                kfs[j] = round((n + 0.5) * span / len(js), 2)
                ks[j] = kfs[j]
        else:
            span = max(count.get(st, 1), 1)
            for n, j in enumerate(js):
                ks[j] = round((n + 0.5) * span / len(js), 2)
    items += "\n" + "\n".join(render_extra(ks[j], ex, kfs.get(j)) for j, ex in enumerate(extras))
    html = (HERE / "template.html").read_text().replace("%%SPRITE%%", sprite).replace("%%ITEMS%%", items)
    OUT.write_text(html)
    print(f"wrote {OUT} ({len(html) // 1024} KB, {len(ITEMS)} specimens + {len(extras)} fillers)")


if __name__ == "__main__":
    main()
