"""Architecture stage specimens: structure, layers, boundaries, drafting.

Imported at the bottom of specimens.py (it reuses n() and DEFS gradients).
Exports DEFS (extra gradients), SIZES and FUNCS.
"""
import math

from specimens import n, polar

DEFS = """
<linearGradient id="gAStone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBF6E8"/><stop offset="1" stop-color="#DCCFB0"/></linearGradient>
<linearGradient id="gAStoneH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFBF0"/><stop offset=".55" stop-color="#EADFC4"/><stop offset="1" stop-color="#C4B48E"/></linearGradient>
<radialGradient id="gAPatina" cx=".4" cy=".3" r=".9"><stop offset="0" stop-color="#FBC4DF"/><stop offset=".5" stop-color="#DD52A5"/><stop offset="1" stop-color="#8A2063"/></radialGradient>
<linearGradient id="gABrick" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E98F66"/><stop offset="1" stop-color="#B14E2C"/></linearGradient>
<linearGradient id="gABlue" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2E9AAE"/><stop offset="1" stop-color="#0F5E70"/></linearGradient>
"""

SIZES = {
    "rotunda": (260, 250),
    "blueprint": (240, 100),
    "dividers": (130, 220),
    "plumb": (80, 190),
    "spiritlevel": (290, 56),
    "bricks": (150, 112),
    "archstone": (170, 132),
    "ionic": (160, 140),
    "protractor": (190, 104),
    "theodolite": (130, 200),
    "trowel": (230, 90),
    "tsquare": (200, 150),
}


def rotunda():
    cols, tri = [], []
    for x in (55, 85, 115, 145, 175, 205):
        x += 0
        cols.append(
            f'<rect x="{x - 7}" y="134" width="14" height="72" fill="url(#gAStoneH)" stroke="#9A8C6A" stroke-width="1"/>'
            f'<path d="M{x - 3.5} 138V204M{x} 138V204M{x + 3.5} 138V204" stroke="#B5A785" stroke-width=".8"/>'
            f'<rect x="{x - 10}" y="129" width="20" height="6" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1"/>'
            f'<rect x="{x - 10}" y="205" width="20" height="5" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1"/>'
        )
    for x in range(46, 220, 14):
        tri.append(f'<path d="M{x} 121V131M{x + 4} 121V131" stroke="#A89A78" stroke-width="1.6"/>')
    wins = "".join(
        f'<path d="M{x - 6} 92V76Q{x - 6} 66 {x} 66Q{x + 6} 66 {x + 6} 76V92Z" fill="#4A1D3C" stroke="#8C7F5E" stroke-width="1.2"/>'
        for x in (84, 107, 130, 153, 176)
    )
    ribs = "".join(
        f'<path d="M130 18C{n(130 + dx * .5)} 24 {n(130 + dx)} 40 {n(130 + dx * 1.05)} 58" fill="none" stroke="#8A2063" stroke-width="1.4" opacity=".7"/>'
        for dx in (-52, -30, -10, 10, 30, 52)
    )
    return f"""<g id="sp-rotunda">
<rect x="11" y="228" width="238" height="12" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.4"/>
<rect x="23" y="218" width="214" height="10" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.4"/>
<rect x="35" y="210" width="190" height="8" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.4"/>
<rect x="66" y="58" width="128" height="40" fill="url(#gAStoneH)" stroke="#9A8C6A" stroke-width="1.4"/>
{wins}
<rect x="60" y="54" width="140" height="7" rx="2" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.4"/>
<path d="M66 54C66 30 96 18 130 18C164 18 194 30 194 54Z" fill="url(#gAPatina)" stroke="#681748" stroke-width="2"/>
{ribs}
<ellipse cx="100" cy="32" rx="18" ry="7" fill="#fff" opacity=".3" transform="rotate(-22 100 32)"/>
<rect x="122" y="8" width="16" height="12" rx="2" fill="url(#gAPatina)" stroke="#681748" stroke-width="1.4"/>
<path d="M130 8V0" stroke="#681748" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="130" cy="0" r="2.6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width=".8"/>
{''.join(cols)}
<rect x="38" y="116" width="184" height="14" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.4"/>
{''.join(tri)}
<polygon points="30,116 130,82 230,116" fill="url(#gAStone)" stroke="#9A8C6A" stroke-width="1.8" stroke-linejoin="round"/>
<polygon points="48,111 130,86 212,111" fill="#D9CDAE" stroke="#A89A78" stroke-width="1.2"/>
<circle cx="130" cy="102" r="7" fill="url(#gAPatina)" stroke="#681748" stroke-width="1.2"/>
</g>"""


def blueprint():
    grid = "".join(f'<path d="M{54 + i * 18} {22 - i * .3}V{82 - i * .1}" stroke="#fff" stroke-width=".7" opacity=".35"/>' for i in range(11))
    grid += "".join(f'<path d="M48 {26 + j * 14}L{232} {18 + j * 14}" stroke="#fff" stroke-width=".7" opacity=".35"/>' for j in range(5))
    plan = (
        '<path d="M80 36H150V70H80Z M150 48H196V70H150Z" fill="none" stroke="#fff" stroke-width="1.6" opacity=".95"/>'
        '<path d="M96 36V70M80 52H96" stroke="#fff" stroke-width="1.2" opacity=".9"/>'
        '<circle cx="214" cy="40" r="10" fill="none" stroke="#fff" stroke-width="1.4" opacity=".9"/>'
        '<path d="M80 80H150M80 77V83M150 77V83" stroke="#fff" stroke-width="1" opacity=".9"/>'
    )
    return f"""<g id="sp-blueprint">
<polygon points="46,20 236,12 230,84 46,88" fill="url(#gABlue)" stroke="#0A4452" stroke-width="1.6" stroke-linejoin="round"/>
{grid}{plan}
<path d="M10 12H54V86H10Z" fill="#E5F3F6" stroke="#0A4452" stroke-width="1.6"/>
<path d="M10 12H54V86H10Z" fill="url(#gABlue)" opacity=".28"/>
<ellipse cx="32" cy="88" rx="22" ry="7" fill="#CFE6EC" stroke="#0A4452" stroke-width="1.6"/>
<ellipse cx="32" cy="12" rx="22" ry="7" fill="#F4FBFC" stroke="#0A4452" stroke-width="1.6"/>
<path d="M32 12m-14 0a14 4.4 0 1 0 28 0M32 12m-7 0a7 2.2 0 1 0 14 0" fill="none" stroke="#6FA8B6" stroke-width="1.2"/>
<rect x="8" y="42" width="48" height="9" fill="url(#gSR)" stroke="#8E1F12" stroke-width="1"/>
</g>"""


def dividers():
    return """<g id="sp-dividers">
<path d="M65 28L22 204M65 28L108 204" fill="none" stroke="#3A444E" stroke-width="12" stroke-linecap="round"/>
<path d="M65 28L22 204M65 28L108 204" fill="none" stroke="url(#gSteel)" stroke-width="8" stroke-linecap="round"/>
<path d="M22 204L19 216M108 204L111 216" stroke="#3A444E" stroke-width="2.6" stroke-linecap="round"/>
<path d="M40 128Q65 152 90 128" fill="none" stroke="#7B5218" stroke-width="7" stroke-linecap="round"/>
<path d="M40 128Q65 152 90 128" fill="none" stroke="url(#gBrass)" stroke-width="4" stroke-linecap="round"/>
<circle cx="65" cy="22" r="14" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.8"/>
<circle cx="65" cy="22" r="6" fill="#FBEBB0" stroke="#7B5218" stroke-width="1.2"/>
<rect x="55" y="6" width="20" height="9" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
</g>"""


def plumb():
    return """<g id="sp-plumb">
<circle cx="40" cy="8" r="6" fill="none" stroke="url(#gBrassV)" stroke-width="3"/>
<path d="M40 14V70" stroke="#EADFC4" stroke-width="2.4"/><path d="M40 14V70" stroke="#9A8C6A" stroke-width=".7"/>
<rect x="30" y="68" width="20" height="26" rx="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5"/>
<path d="M30 94H50L41.5 152H38.5Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.5" stroke-linejoin="round"/>
<path d="M38.5 152L40 176L41.5 152Z" fill="#3A444E"/>
<path d="M33 98L38 148" stroke="#fff" stroke-width="2.4" opacity=".55" stroke-linecap="round"/>
</g>"""


def spiritlevel():
    return """<g id="sp-spiritlevel">
<rect x="4" y="8" width="282" height="42" rx="7" fill="url(#gWood)" stroke="#5E3A1A" stroke-width="2"/>
<rect x="4" y="8" width="16" height="42" rx="6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<rect x="270" y="8" width="16" height="42" rx="6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<rect x="104" y="15" width="82" height="28" rx="14" fill="#FFF1B8" stroke="#7B5218" stroke-width="2"/>
<rect x="104" y="15" width="82" height="28" rx="14" fill="url(#gGlass)"/>
<ellipse cx="145" cy="31" rx="13" ry="7" fill="#fff" stroke="#B88A2A" stroke-width="1.2"/>
<path d="M128 17V41M162 17V41" stroke="#7B5218" stroke-width="1.4"/>
<circle cx="56" cy="29" r="9" fill="#FFF1B8" stroke="#7B5218" stroke-width="1.8"/><circle cx="56" cy="29" r="4" fill="#fff" stroke="#B88A2A" stroke-width="1"/>
<circle cx="234" cy="29" r="9" fill="#FFF1B8" stroke="#7B5218" stroke-width="1.8"/><circle cx="234" cy="29" r="4" fill="#fff" stroke="#B88A2A" stroke-width="1"/>
<path d="M12 12H278" stroke="#fff" stroke-width="2" opacity=".35"/>
</g>"""


def bricks():
    def brick(x, y):
        return (f'<polygon points="{x},{y + 8} {x + 12},{y} {x + 72},{y} {x + 60},{y + 8}" fill="#F2A27C" stroke="#7A3218" stroke-width="1.4" stroke-linejoin="round"/>'
                f'<polygon points="{x + 60},{y + 8} {x + 72},{y} {x + 72},{y + 26} {x + 60},{y + 34}" fill="#9A3F20" stroke="#7A3218" stroke-width="1.4" stroke-linejoin="round"/>'
                f'<rect x="{x}" y="{y + 8}" width="60" height="26" fill="url(#gABrick)" stroke="#7A3218" stroke-width="1.4"/>'
                f'<circle cx="{x + 14}" cy="{y + 18}" r="1.6" fill="#7A3218" opacity=".5"/><circle cx="{x + 38}" cy="{y + 26}" r="1.4" fill="#7A3218" opacity=".5"/><circle cx="{x + 50}" cy="{y + 16}" r="1.2" fill="#7A3218" opacity=".5"/>')
    return f'<g id="sp-bricks">{brick(3, 74)}{brick(75, 74)}{brick(39, 40)}</g>'


def archstone():
    cx, cy, ri, ro = 85, 98, 36, 62
    segs = 7
    wedges = []
    for k in range(segs):
        a0 = math.pi + k * math.pi / segs
        a1 = math.pi + (k + 1) * math.pi / segs
        p = [polar(cx, cy, ro, a0), polar(cx, cy, ro, a1), polar(cx, cy, ri, a1), polar(cx, cy, ri, a0)]
        fill = "url(#gAPatina)" if k == segs // 2 else ("#EADFC4" if k % 2 else "#F6EED8")
        d = f"M{n(p[0][0])} {n(p[0][1])}A{ro} {ro} 0 0 1 {n(p[1][0])} {n(p[1][1])}L{n(p[2][0])} {n(p[2][1])}A{ri} {ri} 0 0 0 {n(p[3][0])} {n(p[3][1])}Z"
        wedges.append(f'<path d="{d}" fill="{fill}" stroke="#8C7F5E" stroke-width="1.6" stroke-linejoin="round"/>')
    return f"""<g id="sp-archstone">
<rect x="4" y="122" width="162" height="9" rx="2" fill="url(#gAStone)" stroke="#8C7F5E" stroke-width="1.4"/>
<rect x="23" y="98" width="26" height="24" fill="url(#gAStoneH)" stroke="#8C7F5E" stroke-width="1.4"/>
<rect x="121" y="98" width="26" height="24" fill="url(#gAStoneH)" stroke="#8C7F5E" stroke-width="1.4"/>
<path d="M23 110H49M121 110H147" stroke="#8C7F5E" stroke-width="1"/>
{''.join(wedges)}
</g>"""


def ionic():
    def volute(cx, cy, flip):
        pts = []
        t = 0.0
        while t < 4.6 * math.pi:
            r = 21 * math.exp(-0.2 * t)
            pts.append((cx + (-1 if flip else 1) * r * math.cos(t + math.pi / 2), cy + r * math.sin(t + math.pi / 2)))
            t += 0.16
        d = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in pts)
        return (f'<circle cx="{cx}" cy="{cy}" r="22" fill="url(#gAStoneH)" stroke="#8C7F5E" stroke-width="1.6"/>'
                f'<path d="{d}" fill="none" stroke="#8C7F5E" stroke-width="1.8" stroke-linecap="round"/>'
                f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="#8C7F5E"/>')
    flutes = "".join(f'<path d="M{x} 70V134" stroke="#B5A785" stroke-width="1"/>' for x in (62, 72, 80, 88, 98))
    return f"""<g id="sp-ionic">
<rect x="48" y="62" width="64" height="72" fill="url(#gAStoneH)" stroke="#8C7F5E" stroke-width="1.5"/>
{flutes}
<path d="M34 34H126L118 62H42Z" fill="url(#gAStone)" stroke="#8C7F5E" stroke-width="1.5" stroke-linejoin="round"/>
{volute(32, 48, False)}{volute(128, 48, True)}
<path d="M44 50Q80 64 116 50" fill="none" stroke="#8C7F5E" stroke-width="1.6"/>
<rect x="10" y="10" width="140" height="16" rx="2" fill="url(#gAStone)" stroke="#8C7F5E" stroke-width="1.6"/>
<path d="M14 18H146" stroke="#B5A785" stroke-width="1"/>
</g>"""


def protractor():
    ticks = []
    for deg in range(0, 181, 5):
        a = math.radians(180 + deg)
        r1 = 78 if deg % 10 == 0 else 82
        x0, y0 = polar(95, 96, r1, a)
        x1, y1 = polar(95, 96, 87, a)
        ticks.append(f'<path d="M{n(x0)} {n(y0)}L{n(x1)} {n(y1)}" stroke="#7B5218" stroke-width="{1.2 if deg % 10 == 0 else .8}"/>')
    spokes = "".join(
        f'<path d="M95 96L{n(95 + 42 * math.cos(math.radians(180 + d)))} {n(96 + 42 * math.sin(math.radians(180 + d)))}" stroke="#7B5218" stroke-width=".8" opacity=".55"/>'
        for d in range(30, 180, 30)
    )
    return f"""<g id="sp-protractor">
<path d="M6 98A89 89 0 0 1 184 98Z" fill="url(#gGlass)" stroke="#7B5218" stroke-width="3" stroke-linejoin="round"/>
<path d="M6 98A89 89 0 0 1 184 98Z" fill="url(#gAmber)" opacity=".38"/>
{''.join(ticks)}{spokes}
<path d="M58 98A37 37 0 0 1 132 98" fill="none" stroke="#7B5218" stroke-width="1.4"/>
<path d="M6 98H184" stroke="#7B5218" stroke-width="2"/>
<circle cx="95" cy="96" r="3.4" fill="#C23C28"/>
</g>"""


def theodolite():
    return """<g id="sp-theodolite">
<path d="M65 112L18 194M65 112L112 194M65 112L65 196" fill="none" stroke="#3E2410" stroke-width="9" stroke-linecap="round"/>
<path d="M65 112L18 194M65 112L112 194M65 112L65 196" fill="none" stroke="url(#gWood)" stroke-width="5.4" stroke-linecap="round"/>
<ellipse cx="65" cy="112" rx="28" ry="7" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.6"/>
<rect x="56" y="72" width="18" height="40" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<rect x="36" y="38" width="12" height="46" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<rect x="82" y="38" width="12" height="46" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<path d="M36 84H94V72H36Z" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4"/>
<g transform="rotate(-14 65 50)">
<rect x="8" y="42" width="96" height="16" rx="4" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.5"/>
<path d="M104 38L122 34V66L104 62Z" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5" stroke-linejoin="round"/>
<ellipse cx="122" cy="50" rx="4" ry="16" fill="url(#gGlass)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="2" y="45" width="10" height="10" rx="2" fill="#232933" stroke="#7B5218" stroke-width="1"/>
</g>
<circle cx="88" cy="58" r="17" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="1.6" opacity=".92"/>
<circle cx="88" cy="58" r="12" fill="none" stroke="#4E5A66" stroke-width=".9"/>
<circle cx="88" cy="58" r="3" fill="#4E5A66"/>
</g>"""


def trowel():
    return """<g id="sp-trowel">
<path d="M6 46L84 16Q116 12 118 46Q116 80 84 76Z" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="2" stroke-linejoin="round"/>
<path d="M18 46L86 28" stroke="#fff" stroke-width="3" opacity=".55" stroke-linecap="round"/>
<path d="M118 46H146" stroke="#4E5A66" stroke-width="5" stroke-linecap="round"/>
<rect x="142" y="40" width="10" height="12" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="150" y="34" width="76" height="24" rx="12" fill="url(#gWood)" stroke="#5E3A1A" stroke-width="2"/>
<path d="M160 40H216" stroke="#fff" stroke-width="2" opacity=".35" stroke-linecap="round"/>
</g>"""


def tsquare():
    ticks = "".join(f'<path d="M{40 + i * 8} 54v{9 if i % 5 == 0 else 5}" stroke="#5E3A1A" stroke-width="1"/>' for i in range(19))
    return f"""<g id="sp-tsquare">
<rect x="4" y="52" width="192" height="30" rx="2" fill="url(#gRule)" stroke="#9A7432" stroke-width="1.6"/>
{ticks}
<rect x="4" y="6" width="30" height="140" rx="3" fill="url(#gWoodDark)" stroke="#2E1A0A" stroke-width="2"/>
<path d="M10 12V140" stroke="#fff" stroke-width="2" opacity=".25"/>
<circle cx="19" cy="24" r="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/><circle cx="19" cy="128" r="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/>
<circle cx="180" cy="67" r="4" fill="#fff" stroke="#9A7432" stroke-width="1.2"/>
</g>"""


FUNCS = [rotunda, blueprint, dividers, plumb, spiritlevel, bricks, archstone, ionic, protractor, theodolite, trowel, tsquare]
