"""Functional stage specimens: composition, purity, immutability, mathematics.

Imported at the bottom of specimens.py (it reuses n() and DEFS gradients).
Exports DEFS (extra gradients), SIZES and FUNCS.
"""
import math

from specimens import n, polar

DEFS = """
<radialGradient id="gFViolet" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#D9C2FF"/><stop offset=".5" stop-color="#8B5CF6"/><stop offset="1" stop-color="#3C1F8C"/></radialGradient>
<radialGradient id="gFLilac" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#C7A8FA"/><stop offset="1" stop-color="#7A4FCB"/></radialGradient>
<linearGradient id="gFBone" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E8DFC8"/></linearGradient>
<linearGradient id="gFPawn" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8B6BC8"/><stop offset=".45" stop-color="#4A2F86"/><stop offset="1" stop-color="#241446"/></linearGradient>
<radialGradient id="gFBall" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#B8C2CC"/><stop offset="1" stop-color="#5A6673"/></radialGradient>
"""

SIZES = {
    "egg": (240, 290),
    "astrolabe": (190, 210),
    "sliderule": (330, 64),
    "dominoes": (160, 120),
    "dice": (150, 136),
    "pawn": (100, 170),
    "tuningfork": (100, 230),
    "metronome": (120, 190),
    "newtons": (200, 170),
    "blocklambda": (110, 140),
    "blocksigma": (110, 140),
    "blockcompose": (110, 140),
    "blockarrow": (110, 140),
    "blockpi": (110, 140),
}


def egg():
    lid = "M45 140C45 62 82 30 120 30C158 30 195 62 195 140Z"
    return f"""<g id="sp-egg">
<path d="M64 284C76 262 98 258 120 258C142 258 164 262 176 284Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.6" stroke-linejoin="round"/>
<rect x="106" y="226" width="28" height="36" rx="4" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4"/>
<g transform="rotate(26 195 140)">
<path d="{lid}" fill="url(#gFViolet)" stroke="#2A1260" stroke-width="2.2"/>
<path d="M45 140C45 100 62 66 90 48M195 140C195 100 178 66 150 48M120 30V140" fill="none" stroke="url(#gBrass)" stroke-width="3.2" stroke-linecap="round"/>
<path d="M58 112H182" stroke="url(#gBrass)" stroke-width="3.2"/>
<circle cx="120" cy="38" r="6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1"/>
<ellipse cx="86" cy="76" rx="14" ry="24" fill="#fff" opacity=".28" transform="rotate(24 86 76)"/>
</g>
<path d="M45 140A75 15 0 0 1 195 140Z" fill="#2A1260"/>
<ellipse cx="120" cy="140" rx="75" ry="15" fill="#2B1560"/>
<path d="M76 138C76 100 92 72 120 72C148 72 164 100 164 138Z" fill="url(#gFLilac)" stroke="#4B2A9A" stroke-width="2"/>
<path d="M76 108H164" stroke="url(#gBrass)" stroke-width="3"/>
<path d="M120 72V138" stroke="url(#gBrass)" stroke-width="2.4" opacity=".8"/>
<circle cx="120" cy="80" r="5" fill="#fff" stroke="#9C86D6" stroke-width="1"/>
<path d="M45 140C45 205 80 228 120 228C160 228 195 205 195 140A75 15 0 0 1 45 140Z" fill="url(#gFViolet)" stroke="#2A1260" stroke-width="2.4"/>
<path d="M45 140A75 15 0 0 0 195 140" fill="none" stroke="url(#gBrass)" stroke-width="3.6"/>
<path d="M120 155V228M82 150C80 190 98 222 120 228M158 150C160 190 142 222 120 228" fill="none" stroke="url(#gBrass)" stroke-width="3" stroke-linecap="round"/>
<path d="M56 190C80 204 160 204 184 190" fill="none" stroke="url(#gBrass)" stroke-width="3" stroke-linecap="round"/>
<circle cx="120" cy="192" r="11" fill="url(#gSG)" stroke="#8D5F1E" stroke-width="3"/>
<ellipse cx="74" cy="184" rx="9" ry="22" fill="#fff" opacity=".3" transform="rotate(-14 74 184)"/>
</g>"""


def astrolabe():
    ticks = "".join(
        f'<path d="M{n(95 + (70 if i % 6 else 66) * math.cos(math.radians(i * 5)))} {n(118 + (70 if i % 6 else 66) * math.sin(math.radians(i * 5)))}'
        f'L{n(95 + 77 * math.cos(math.radians(i * 5)))} {n(118 + 77 * math.sin(math.radians(i * 5)))}" stroke="#5E3A10" stroke-width="{1.4 if i % 6 == 0 else .8}"/>'
        for i in range(72)
    )
    rete = "".join(
        f'<path d="M95 118Q{n(95 + 22 * math.cos(math.radians(a + 20)))} {n(118 + 22 * math.sin(math.radians(a + 20)))} {n(95 + 56 * math.cos(math.radians(a)))} {n(118 + 56 * math.sin(math.radians(a)))}" fill="none" stroke="#7B5218" stroke-width="2.4" stroke-linecap="round"/>'
        f'<circle cx="{n(95 + 56 * math.cos(math.radians(a)))}" cy="{n(118 + 56 * math.sin(math.radians(a)))}" r="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/>'
        for a in (-70, -10, 55, 120, 180, 235)
    )
    return f"""<g id="sp-astrolabe">
<path d="M78 46Q95 4 112 46" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.6"/>
<circle cx="95" cy="14" r="11" fill="none" stroke="url(#gBrassV)" stroke-width="5"/>
<circle cx="95" cy="118" r="82" fill="url(#gBrass)" stroke="#7B5218" stroke-width="2"/>
<circle cx="95" cy="118" r="64" fill="url(#gParch)" stroke="#7B5218" stroke-width="1.4"/>
{ticks}
<circle cx="95" cy="118" r="50" fill="none" stroke="#9A7432" stroke-width="1"/>
<circle cx="95" cy="118" r="34" fill="none" stroke="#9A7432" stroke-width="1"/>
<circle cx="95" cy="118" r="18" fill="none" stroke="#9A7432" stroke-width="1"/>
<circle cx="95" cy="106" r="38" fill="none" stroke="#7B5218" stroke-width="1.6"/>
<path d="M95 54V182M31 118H159" stroke="#9A7432" stroke-width="1"/>
{rete}
<g transform="rotate(-38 95 118)"><path d="M10 118L24 111H166L180 118L166 125H24Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4" stroke-linejoin="round"/><circle cx="30" cy="118" r="3" fill="#7B5218"/><circle cx="160" cy="118" r="3" fill="#7B5218"/></g>
<circle cx="95" cy="118" r="7" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5"/>
<path d="M38 70C50 52 66 44 82 40" fill="none" stroke="#fff" stroke-width="4" opacity=".5" stroke-linecap="round"/>
</g>"""


def sliderule():
    top, bot, mid = [], [], []
    for i in range(0, 91):
        v = 1 + i / 10
        x = 14 + 292 * math.log10(v)
        major = i % 10 == 0
        h = 11 if major else (7 if i % 5 == 0 else 4.5)
        top.append(f'<path d="M{n(x)} 20v-{h}" stroke="#3A2A14" stroke-width="{1.2 if major else .7}"/>')
        bot.append(f'<path d="M{n(x)} 38v{h}" stroke="#3A2A14" stroke-width="{1.2 if major else .7}"/>')
    return f"""<g id="sp-sliderule">
<rect x="4" y="4" width="322" height="54" rx="4" fill="url(#gRule)" stroke="#9A7432" stroke-width="1.6"/>
<rect x="8" y="20" width="314" height="18" fill="#FFFDF2" stroke="#9A7432" stroke-width="1"/>
<path d="M8 29H322" stroke="#C9B27A" stroke-width=".8"/>
{''.join(top)}{''.join(bot)}
<rect x="196" y="1" width="30" height="60" rx="3" fill="url(#gGlass)" stroke="#6F8FB0" stroke-width="1.4"/>
<path d="M211 2V60" stroke="#C23C28" stroke-width="1.1"/>
</g>"""


def _pips(cx, cy, k, r=4.2, d=12):
    pos = {
        1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)],
        4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
        6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)],
    }[k]
    return "".join(f'<circle cx="{n(cx + px * d)}" cy="{n(cy + py * d)}" r="{r}" fill="#1B1B1B"/>' for px, py in pos)


def dominoes():
    def one(tx, ty, rot, a, b):
        return (f'<g transform="translate({tx} {ty}) rotate({rot})">'
                '<rect x="0" y="0" width="100" height="52" rx="7" fill="url(#gFBone)" stroke="#8A7F66" stroke-width="1.6"/>'
                '<path d="M50 5V47" stroke="#8A7F66" stroke-width="1.8"/>'
                f'{_pips(25, 26, a)}{_pips(75, 26, b)}</g>')
    return f'<g id="sp-dominoes">{one(8, 58, -9, 6, 3)}{one(46, 8, 15, 4, 5)}</g>'


def dice():
    def cube(ox, oy, s, ft, fl, fr):
        a, h = 0.866 * s, 0.5 * s
        T, L, R, C = (ox, oy), (ox - a, oy + h), (ox + a, oy + h), (ox, oy + 2 * h)

        def poly(pts, fill):
            return f'<polygon points="{" ".join(f"{n(x)},{n(y)}" for x, y in pts)}" fill="{fill}" stroke="#8A7F66" stroke-width="1.6" stroke-linejoin="round"/>'

        def pips(m, k):
            body = _pips(0.5, 0.5, k, r=.085, d=.24)
            return f'<g transform="matrix({n(m[0])} {n(m[1])} {n(m[2])} {n(m[3])} {n(m[4])} {n(m[5])})">{body}</g>'

        return (poly([T, R, C, L], "#FFFFFF")
                + poly([L, C, (C[0], C[1] + s), (L[0], L[1] + s)], "#E4DCC8")
                + poly([R, C, (C[0], C[1] + s), (R[0], R[1] + s)], "#CFC6AE")
                + pips((a, h, -a, h, T[0], T[1]), ft)
                + pips((a, h, 0, s, L[0], L[1]), fl)
                + pips((-a, h, 0, s, R[0], R[1]), fr))
    return f'<g id="sp-dice">{cube(46, 6, 52, 1, 2, 3)}{cube(108, 52, 40, 6, 4, 5)}</g>'


def pawn():
    return """<g id="sp-pawn">
<path d="M12 162C12 150 24 146 30 144H70C76 146 88 150 88 162Z" fill="url(#gFPawn)" stroke="#1C0F38" stroke-width="2" stroke-linejoin="round"/>
<ellipse cx="50" cy="142" rx="24" ry="5" fill="#4A2F86" stroke="#1C0F38" stroke-width="1.6"/>
<path d="M34 142C40 112 42 98 40 82H60C58 98 60 112 66 142Z" fill="url(#gFPawn)" stroke="#1C0F38" stroke-width="2" stroke-linejoin="round"/>
<ellipse cx="50" cy="82" rx="21" ry="6" fill="#6B4BA8" stroke="#1C0F38" stroke-width="1.8"/>
<circle cx="50" cy="52" r="23" fill="url(#gFPawn)" stroke="#1C0F38" stroke-width="2"/>
<ellipse cx="43" cy="44" rx="7" ry="10" fill="#fff" opacity=".3" transform="rotate(-22 43 44)"/>
<path d="M12 156H88" stroke="url(#gBrass)" stroke-width="3"/>
</g>"""


def tuningfork():
    return """<g id="sp-tuningfork">
<path d="M30 16V94Q30 122 50 122Q70 122 70 94V16" fill="none" stroke="#4E5A66" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M30 16V94Q30 122 50 122Q70 122 70 94V16" fill="none" stroke="url(#gSteel)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M27 20V92" stroke="#fff" stroke-width="2.4" opacity=".8" stroke-linecap="round"/>
<rect x="43" y="120" width="14" height="86" rx="3" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="1.6"/>
<circle cx="50" cy="214" r="10" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="1.8"/>
<path d="M7 62Q0 80 7 98M93 62Q100 80 93 98M16 70Q11 80 16 90M84 70Q89 80 84 90" fill="none" stroke="#8B5CF6" stroke-width="2.4" stroke-linecap="round"/>
</g>"""


def metronome():
    ticks = "".join(f'<path d="M{n(62 - 8)} {50 + i * 13}h{16 if i % 2 == 0 else 10}" stroke="#5E3A1A" stroke-width="1.4"/>' for i in range(8))
    return f"""<g id="sp-metronome">
<path d="M26 176L94 176L76 20L44 20Z" fill="url(#gWoodDark)" stroke="#2E1A0A" stroke-width="2" stroke-linejoin="round"/>
<path d="M44 20L76 20L72 8L48 8Z" fill="#A8723A" stroke="#2E1A0A" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M50 30L70 30L82 160L38 160Z" fill="url(#gParch)" stroke="#5E3A1A" stroke-width="1.4"/>
{ticks}
<path d="M60 150L74 4" stroke="url(#gSteel)" stroke-width="3.4" stroke-linecap="round"/>
<path d="M60 150L74 4" stroke="#4E5A66" stroke-width=".8" stroke-linecap="round"/>
<rect x="63" y="46" width="18" height="14" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.3" transform="rotate(6 72 53)"/>
<circle cx="60" cy="150" r="5" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.2"/>
<circle cx="97" cy="124" r="9" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4"/>
<path d="M97 124L102 120" stroke="#5E3A10" stroke-width="3" stroke-linecap="round"/>
<rect x="18" y="176" width="84" height="10" rx="3" fill="#5E3A1A" stroke="#2E1A0A" stroke-width="1.6"/>
</g>"""


def newtons():
    balls = []
    xs = [60, 80, 100, 120, 140]
    for i, x in enumerate(xs):
        if i == 0:
            cx, cy = 60 - 100 * math.sin(math.radians(28)), 18 + 100 * math.cos(math.radians(28))
        else:
            cx, cy = x, 118
        balls.append(
            f'<path d="M{x} 18L{n(cx)} {n(cy - 10)}" stroke="#5A6673" stroke-width="1.1"/>'
            f'<circle cx="{n(cx)}" cy="{n(cy)}" r="10" fill="url(#gFBall)" stroke="#47525E" stroke-width="1.2"/>'
        )
    return f"""<g id="sp-newtons">
<rect x="8" y="156" width="184" height="10" rx="3" fill="url(#gWoodDark)" stroke="#2E1A0A" stroke-width="1.6"/>
<rect x="12" y="10" width="7" height="148" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.1"/>
<rect x="181" y="10" width="7" height="148" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.1"/>
<rect x="8" y="6" width="184" height="9" rx="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4"/>
{''.join(balls)}
</g>"""


def _block(ident, shape):
    base = None
    from specimens import typeblock
    base = typeblock().replace('id="sp-typeblock"', f'id="sp-{ident}"')
    start = base.index("<text")
    end = base.index("</text>") + len("</text>")
    return base[:start] + shape + base[end:]


_INK = 'fill="none" stroke="#1B1B1B" stroke-linecap="round" stroke-linejoin="round"'


def blocklambda():
    return _block("blocklambda", f'<path d="M28 42L73 118M50.5 80L27 118" {_INK} stroke-width="11"/>')


def blocksigma():
    return _block("blocksigma", f'<path d="M72 44H30L54 80L30 118H74" fill="none" stroke="#1B1B1B" stroke-width="10" stroke-linecap="butt" stroke-linejoin="miter"/>')


def blockcompose():
    return _block("blockcompose", f'<circle cx="50" cy="82" r="20" {_INK} stroke-width="10"/>')


def blockarrow():
    return _block("blockarrow", f'<path d="M24 82H76M58 64L76 82L58 100" {_INK} stroke-width="10"/>')


def blockpi():
    return _block("blockpi", f'<path d="M24 50H76M38 50V114M62 50V108" {_INK} stroke-width="10"/>')


FUNCS = [egg, astrolabe, sliderule, dominoes, dice, pawn, tuningfork, metronome, newtons,
         blocklambda, blocksigma, blockcompose, blockarrow, blockpi]
