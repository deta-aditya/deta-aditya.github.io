"""Encyclopedia specimen illustrations as SVG groups.

Each function returns an SVG <g id="sp-..."> that is rendered through <use>.
Gradients and filters live in DEFS and are referenced by id.
"""
import math
import random


def n(x):
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def circle_sub(cx, cy, r):
    return f"M{n(cx - r)} {n(cy)}a{n(r)} {n(r)} 0 1 0 {n(2 * r)} 0a{n(r)} {n(r)} 0 1 0 {n(-2 * r)} 0Z"


def polar(cx, cy, r, a):
    return cx + r * math.cos(a), cy + r * math.sin(a)


DEFS = """
<linearGradient id="gBrass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBEBB0"/><stop offset=".42" stop-color="#D8A944"/><stop offset="1" stop-color="#8D5F1E"/></linearGradient>
<linearGradient id="gBrassV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7DE8E"/><stop offset=".5" stop-color="#C99634"/><stop offset="1" stop-color="#8A5C1B"/></linearGradient>
<linearGradient id="gSteel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6F8FA"/><stop offset=".5" stop-color="#B0BAC3"/><stop offset="1" stop-color="#68747F"/></linearGradient>
<linearGradient id="gSteelDark" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2C3239"/><stop offset=".45" stop-color="#6E7983"/><stop offset="1" stop-color="#242A30"/></linearGradient>
<linearGradient id="gWood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E7BB84"/><stop offset="1" stop-color="#A56E38"/></linearGradient>
<linearGradient id="gWoodDark" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A8723A"/><stop offset="1" stop-color="#5E3A1A"/></linearGradient>
<radialGradient id="gGlass" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".92"/><stop offset=".5" stop-color="#CFE9FF" stop-opacity=".5"/><stop offset="1" stop-color="#7FB6E8" stop-opacity=".38"/></radialGradient>
<radialGradient id="gSclera" cx=".5" cy=".5" r=".6"><stop offset=".55" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EBBDB2"/></radialGradient>
<radialGradient id="gIris" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#2A2412"/><stop offset=".35" stop-color="#7C9A3A"/><stop offset=".8" stop-color="#3F7F55"/><stop offset="1" stop-color="#1D4A38"/></radialGradient>
<radialGradient id="gSG" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#D4F9BC"/><stop offset=".55" stop-color="#34B25A"/><stop offset="1" stop-color="#0E6B34"/></radialGradient>
<radialGradient id="gSB" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#C6E4FF"/><stop offset=".55" stop-color="#2F7FE0"/><stop offset="1" stop-color="#123F8E"/></radialGradient>
<radialGradient id="gSR" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFD2C8"/><stop offset=".55" stop-color="#E4513A"/><stop offset="1" stop-color="#8E1F12"/></radialGradient>
<radialGradient id="gSoma" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#F8DCE8"/><stop offset=".6" stop-color="#D98AB2"/><stop offset="1" stop-color="#A24A7C"/></radialGradient>
<radialGradient id="gPlasma" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#C77A0C"/><stop offset=".55" stop-color="#5A2F06"/><stop offset="1" stop-color="#140A02"/></radialGradient>
<radialGradient id="gCore" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#FFE08A"/><stop offset="1" stop-color="#E08A10" stop-opacity="0"/></radialGradient>
<radialGradient id="gOcean" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#9BD6FA"/><stop offset=".6" stop-color="#3F95DE"/><stop offset="1" stop-color="#1F5FAE"/></radialGradient>
<radialGradient id="gLand" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#9CD36B"/><stop offset="1" stop-color="#4C9A45"/></radialGradient>
<radialGradient id="gDial" cx=".5" cy=".4" r=".7"><stop offset="0" stop-color="#FFFDF4"/><stop offset="1" stop-color="#EDE3C6"/></radialGradient>
<radialGradient id="gBead" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#F29A8C"/><stop offset=".5" stop-color="#B3362B"/><stop offset="1" stop-color="#5E140E"/></radialGradient>
<linearGradient id="gParch" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7EBCB"/><stop offset="1" stop-color="#E0C994"/></linearGradient>
<linearGradient id="gCrysL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9DB6EE"/><stop offset="1" stop-color="#6F8BD2"/></linearGradient>
<linearGradient id="gCrysR" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#EAF3FF"/><stop offset="1" stop-color="#B6D0F7"/></linearGradient>
<linearGradient id="gMorpho" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8BE9FF"/><stop offset=".5" stop-color="#2A78E8"/><stop offset="1" stop-color="#0C2C7E"/></linearGradient>
<radialGradient id="gShell" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#FFF1D8"/><stop offset=".6" stop-color="#F0C48C"/><stop offset="1" stop-color="#D98A45"/></radialGradient>
<linearGradient id="gHoney" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE08A"/><stop offset="1" stop-color="#E69A1E"/></linearGradient>
<linearGradient id="gCover" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7B2420"/><stop offset=".15" stop-color="#A8382F"/><stop offset="1" stop-color="#8E2B26"/></linearGradient>
<filter id="fGlow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
"""

SIZES = {
    "lens": (200, 250), "typeblock3": (110, 140), "typeblock4": (110, 140), "typeblock5": (110, 140), "cursor": (94, 118), "setsquare": (176, 132), "monitor": (260, 232), "ruler": (320, 52), "brush": (320, 40), "typeblock2": (110, 140),
    "eye": (220, 130), "prism": (260, 150), "fan": (160, 160), "magnifier": (150, 190),
    "pencil": (300, 44), "palette": (220, 170), "typeblock": (110, 140),
    "gears": (240, 180), "key": (280, 90), "padlock": (130, 170), "abacus": (240, 170),
    "watch": (150, 180), "card": (220, 100), "coins": (120, 140), "ledger": (150, 170),
    "neuron": (280, 210), "plasma": (200, 245), "crystal": (200, 210), "molecule": (190, 170),
    "butterfly": (248, 180), "nautilus": (220, 200), "tree": (240, 170), "honey": (180, 170),
    "world": (240, 130), "compass": (170, 170),
}


# ------------------------------------------------------------------ frontend
def eye():
    almond = "M10 65C45 12 175 12 210 65C175 118 45 118 10 65Z"
    rays = "".join(
        f'<line x1="{n(polar(110, 65, 16, a)[0])}" y1="{n(polar(110, 65, 16, a)[1])}" '
        f'x2="{n(polar(110, 65, 39, a)[0])}" y2="{n(polar(110, 65, 39, a)[1])}"/>'
        for a in [i * math.pi / 16 for i in range(32)]
    )
    return f"""<g id="sp-eye">
<defs><clipPath id="cpEye"><path d="{almond}"/></clipPath></defs>
<path d="{almond}" fill="url(#gSclera)" stroke="#7A4B3A" stroke-width="2.5"/>
<g clip-path="url(#cpEye)">
<path d="M16 62q16-5 34-2M20 70q18 3 32-3M204 62q-16-5-34-2M200 70q-18 3-32-3" stroke="#D86A6A" stroke-width="1" fill="none" opacity=".5"/>
<circle cx="110" cy="65" r="40" fill="url(#gIris)"/>
<g stroke="#D4EBB0" stroke-width="1.2" opacity=".35">{rays}</g>
<circle cx="110" cy="65" r="40" fill="none" stroke="#12301F" stroke-width="3" opacity=".6"/>
<circle cx="110" cy="65" r="16" fill="#080808"/>
<path d="M10 65C45 12 175 12 210 65" fill="none" stroke="#000" stroke-width="14" opacity=".12"/>
</g>
<ellipse cx="94" cy="50" rx="10" ry="6.5" fill="#fff" opacity=".92" transform="rotate(-20 94 50)"/>
<circle cx="124" cy="78" r="3.5" fill="#fff" opacity=".6"/>
<path d="M10 65C45 12 175 12 210 65" fill="none" stroke="#5A3626" stroke-width="3"/>
</g>"""


def prism():
    rainbow = [("#E8332B", 62), ("#F58B1F", 74), ("#F7D117", 86), ("#3BAA4C", 98), ("#2F7FE0", 110), ("#6A3CC2", 122)]
    rays = "".join(
        f'<line x1="138" y1="82" x2="258" y2="{y}" stroke="{c}"/>' for c, y in rainbow
    )
    return f"""<g id="sp-prism">
<path d="M0 108L74 90" stroke="#B9C0C8" stroke-width="3.5" stroke-linecap="round"/>
<g stroke-width="5.5" stroke-linecap="butt" opacity=".92">{rays}</g>
<polygon points="108,16 50,128 168,128" fill="url(#gGlass)" stroke="#8DB9E0" stroke-width="2.5" stroke-linejoin="round"/>
<polygon points="108,16 50,128 68,128 108,52" fill="#fff" opacity=".55"/>
<polygon points="108,16 168,128 150,128 108,50" fill="#9CC9F0" opacity=".28"/>
</g>"""


def fan():
    colors = ["#2D6FD8", "#2FB1C9", "#39B26B", "#F2C230", "#F08A24", "#DE3F39", "#8B49B8"]
    parts = []
    for i, c in enumerate(colors):
        ang = -20 + i * 13.4
        parts.append(
            f'<g transform="rotate({n(ang)} 50 140)">'
            f'<rect x="41" y="26" width="18" height="118" rx="2.5" fill="#fff" stroke="#C9CED3" stroke-width="1"/>'
            f'<rect x="41" y="26" width="18" height="66" rx="2.5" fill="{c}"/>'
            f'<rect x="41" y="26" width="18" height="12" rx="2.5" fill="#fff" opacity=".25"/></g>'
        )
    return (
        '<g id="sp-fan">' + "".join(parts)
        + '<circle cx="50" cy="140" r="7" fill="url(#gSteel)" stroke="#66727D" stroke-width="1.5"/></g>'
    )


def magnifier():
    return """<g id="sp-magnifier">
<path d="M101 102L142 175" stroke="#4E2C12" stroke-width="15" stroke-linecap="round"/>
<path d="M104 104L143 173" stroke="#A8703A" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M98 97L110 118" stroke="url(#gBrassV)" stroke-width="17" stroke-linecap="round"/>
<circle cx="70" cy="70" r="52" fill="url(#gGlass)" stroke="url(#gBrass)" stroke-width="10"/>
<circle cx="70" cy="70" r="57" fill="none" stroke="#7B5218" stroke-width="1.2" opacity=".6"/>
<path d="M38 56A36 36 0 0 1 62 36" stroke="#fff" stroke-width="5" opacity=".85" fill="none" stroke-linecap="round"/>
</g>"""


def pencil():
    return """<g id="sp-pencil">
<rect x="0" y="9" width="24" height="26" rx="6" fill="#E58AA0"/>
<rect x="22" y="8" width="28" height="28" fill="url(#gSteel)"/>
<path d="M30 8v28M38 8v28M46 8v28" stroke="#5E6A75" stroke-width="1" opacity=".6"/>
<rect x="50" y="8" width="184" height="28" fill="#F2C230"/>
<rect x="50" y="8" width="184" height="8" fill="#FADF6E"/>
<rect x="50" y="28" width="184" height="8" fill="#C9971A"/>
<polygon points="234,8 296,22 234,36" fill="url(#gWood)"/>
<polygon points="274,17.5 296,22 274,26.5" fill="#2E2E2E"/>
<polygon points="234,8 296,22 234,16" fill="#fff" opacity=".18"/>
</g>"""


def palette():
    dabs = [(100, 62, 13, "gSG"), (140, 44, 13, "gSR"), (172, 74, 13, "gSB"), (128, 88, 12, "gSG"), (72, 58, 11, "gSR"), (160, 104, 11, "gSB")]
    body = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{g})"/><ellipse cx="{x - 3}" cy="{y - 4}" rx="4" ry="2.4" fill="#fff" opacity=".55"/>'
        for x, y, r, g in dabs
    )
    return f"""<g id="sp-palette">
<path d="M30 90C20 40 80 8 140 14C200 20 214 70 190 108C172 136 140 120 128 138C116 158 70 168 44 142C32 130 32 108 30 90Z" fill="url(#gWood)" stroke="#7B4B22" stroke-width="2.5"/>
<ellipse cx="70" cy="122" rx="15" ry="10" fill="#fff" stroke="#7B4B22" stroke-width="2.5"/>
{body}
<circle cx="112" cy="116" r="10" fill="#fff" stroke="#C9A878" stroke-width="1.2"/>
</g>"""


def typeblock():
    return """<g id="sp-typeblock">
<polygon points="10,30 90,30 100,18 20,18" fill="#F0CD9C"/>
<polygon points="90,30 100,18 100,118 90,130" fill="#8A5A2A"/>
<rect x="10" y="30" width="80" height="100" fill="url(#gWood)"/>
<rect x="10" y="30" width="80" height="100" fill="none" stroke="#6E4520" stroke-width="1.5"/>
<text x="50" y="112" text-anchor="middle" font-family="Cinzel, Georgia, serif" font-weight="700" font-size="92" fill="#1B1B1B">A</text>
</g>"""


# ------------------------------------------------------------------- backend
def gear_path(cx, cy, ro, ri, teeth, holes):
    d = []
    step = 2 * math.pi / teeth
    for i in range(teeth):
        a0 = i * step
        pts = [(ri, a0), (ro, a0 + 0.16 * step), (ro, a0 + 0.38 * step), (ri, a0 + 0.54 * step)]
        for j, (r, a) in enumerate(pts):
            x, y = polar(cx, cy, r, a)
            d.append(("M" if (i == 0 and j == 0) else "L") + f"{n(x)} {n(y)}")
    d.append("Z")
    for hx, hy, hr in holes:
        d.append(circle_sub(hx, hy, hr))
    return "".join(d)


def gears():
    c1 = (92, 108)
    holes1 = [(92, 108, 13)] + [(polar(92, 108, 38, k * math.pi / 3 + 0.3) + (11,)) for k in range(6)]
    holes1 = [(h[0], h[1], h[2]) for h in holes1]
    c2 = (186, 58)
    holes2 = [(186, 58, 8)] + [(polar(186, 58, 23, k * 2 * math.pi / 5 + 0.2) + (6.5,)) for k in range(5)]
    holes2 = [(h[0], h[1], h[2]) for h in holes2]
    return f"""<g id="sp-gears">
<path d="{gear_path(c1[0], c1[1], 72, 59, 14, holes1)}" fill="url(#gBrass)" fill-rule="evenodd" stroke="#7B5218" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="92" cy="108" r="49" fill="none" stroke="#7B5218" stroke-width="1.5" opacity=".35"/>
<path d="{gear_path(c2[0], c2[1], 45, 36, 10, holes2)}" fill="url(#gSteel)" fill-rule="evenodd" stroke="#4E5964" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="186" cy="58" r="28" fill="none" stroke="#4E5964" stroke-width="1.2" opacity=".35"/>
</g>"""


def key():
    bow = circle_sub(45, 45, 34) + circle_sub(45, 31, 8.5) + circle_sub(45, 59, 8.5) + circle_sub(31, 45, 8.5) + circle_sub(59, 45, 8.5)
    return f"""<g id="sp-key">
<path d="{bow}" fill="url(#gBrass)" fill-rule="evenodd" stroke="#7B5218" stroke-width="1.5"/>
<circle cx="45" cy="45" r="27" fill="none" stroke="#7B5218" stroke-width="1" opacity=".4"/>
<rect x="76" y="40" width="186" height="11" rx="5" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="98" y="34" width="9" height="23" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="116" y="35" width="7" height="21" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<path d="M232 51h40v24h-12v-12h-9v12h-9v-12h-10z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2" stroke-linejoin="round"/>
</g>"""


def padlock():
    return """<g id="sp-padlock">
<path d="M32 78V50a33 33 0 0 1 66 0V78" fill="none" stroke="url(#gSteel)" stroke-width="14" stroke-linecap="round"/>
<path d="M32 78V50a33 33 0 0 1 66 0V78" fill="none" stroke="#fff" stroke-width="3" opacity=".6" transform="translate(-2 -1)"/>
<rect x="10" y="74" width="110" height="88" rx="12" fill="url(#gBrass)" stroke="#7B5218" stroke-width="2"/>
<rect x="20" y="84" width="90" height="12" rx="4" fill="#fff" opacity=".28"/>
<circle cx="65" cy="116" r="10" fill="#2A1C0A"/>
<path d="M60 120h10l4 28h-18z" fill="#2A1C0A"/>
</g>"""


def abacus():
    rows = []
    splits = [3, 5, 2, 6, 4]
    for i, left in enumerate(splits):
        y = 38 + i * 24
        rows.append(f'<line x1="14" y1="{y}" x2="226" y2="{y}" stroke="#5A3A1A" stroke-width="3"/>')
        xs = [30 + 20 * k for k in range(left)] + [210 - 20 * k for k in range(8 - left)]
        for x in xs:
            rows.append(
                f'<ellipse cx="{x}" cy="{y}" rx="10" ry="12" fill="url(#gBead)" stroke="#4A1510" stroke-width="1"/>'
            )
    return (
        '<g id="sp-abacus">' + "".join(rows)
        + '<rect x="8" y="8" width="224" height="154" rx="8" fill="none" stroke="url(#gWoodDark)" stroke-width="12"/></g>'
    )


def watch():
    ticks = []
    for i in range(12):
        a = i * math.pi / 6
        r0 = 43 if i % 3 == 0 else 46
        x0, y0 = polar(75, 112, r0, a)
        x1, y1 = polar(75, 112, 50, a)
        ticks.append(
            f'<line x1="{n(x0)}" y1="{n(y0)}" x2="{n(x1)}" y2="{n(y1)}" stroke="#2A2A2A" stroke-width="{3 if i % 3 == 0 else 1.6}"/>'
        )
    return f"""<g id="sp-watch">
<rect x="66" y="3" width="18" height="16" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<ellipse cx="75" cy="31" rx="15" ry="14" fill="none" stroke="url(#gBrass)" stroke-width="6"/>
<rect x="64" y="40" width="22" height="14" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<circle cx="75" cy="112" r="64" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5"/>
<circle cx="75" cy="112" r="54" fill="url(#gDial)" stroke="#6B4A1A" stroke-width="2"/>
{''.join(ticks)}
<line x1="75" y1="112" x2="58" y2="86" stroke="#1C1C1C" stroke-width="4.5" stroke-linecap="round"/>
<line x1="75" y1="112" x2="104" y2="94" stroke="#1C1C1C" stroke-width="3" stroke-linecap="round"/>
<circle cx="75" cy="112" r="4.5" fill="#B3362B"/>
<path d="M38 92A44 44 0 0 1 68 66" stroke="#fff" stroke-width="5" opacity=".55" fill="none" stroke-linecap="round"/>
</g>"""


def card():
    rng = random.Random(11)
    holes = []
    for col in range(36):
        for row in range(6):
            if rng.random() < 0.36:
                holes.append(f'<rect x="{n(14 + col * 5.5)}" y="{n(26 + row * 11)}" width="3.6" height="7" fill="#2B2B2B"/>')
    return f"""<g id="sp-card">
<path d="M26 4H214a4 4 0 0 1 4 4V92a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V28Z" fill="#F0E4C2" stroke="#B9A678" stroke-width="2"/>
<rect x="6" y="12" width="210" height="2.5" fill="#C8473B"/>
{''.join(holes)}
<path d="M26 4V28H2" fill="none" stroke="#B9A678" stroke-width="1.2" opacity=".6"/>
</g>"""


def coins():
    parts = []
    for i in range(6):
        y = 112 - i * 13
        parts.append(
            f'<path d="M16 {y}v13a44 12 0 0 0 88 0v-13z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1"/>'
            f'<ellipse cx="60" cy="{y}" rx="44" ry="12" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1"/>'
            f'<ellipse cx="60" cy="{y}" rx="34" ry="8.5" fill="none" stroke="#fff" stroke-width="1" opacity=".4"/>'
        )
    return '<g id="sp-coins">' + "".join(parts) + "</g>"


def ledger():
    lines = "".join(f'<line x1="130" y1="{22 + i * 8}" x2="138" y2="{24 + i * 8}" stroke="#C9B98E" stroke-width="1"/>' for i in range(16))
    return f"""<g id="sp-ledger">
<polygon points="128,14 140,19 140,166 128,161" fill="#F2E8CE" stroke="#C9B98E" stroke-width="1"/>
{lines}
<rect x="12" y="10" width="118" height="150" rx="4" fill="url(#gCover)" stroke="#4A1512" stroke-width="1.5"/>
<rect x="12" y="10" width="16" height="150" rx="3" fill="#5F1B18"/>
<rect x="12" y="30" width="16" height="4" fill="url(#gBrassV)"/><rect x="12" y="136" width="16" height="4" fill="url(#gBrassV)"/>
<rect x="44" y="48" width="70" height="38" rx="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1"/>
<path d="M52 60h54M52 68h54M52 76h36" stroke="#7B5218" stroke-width="2" opacity=".7"/>
<rect x="44" y="106" width="70" height="3" fill="url(#gBrassV)"/>
</g>"""


# ---------------------------------------------------------------- AI native
def neuron():
    rng = random.Random(7)
    paths = []

    def branch(x, y, ang, length, depth, w):
        x2, y2 = x + length * math.cos(ang), y + length * math.sin(ang)
        cx = (x + x2) / 2 + rng.uniform(-5, 5)
        cy = (y + y2) / 2 + rng.uniform(-5, 5)
        paths.append(f'<path d="M{n(x)} {n(y)}Q{n(cx)} {n(cy)} {n(x2)} {n(y2)}" stroke-width="{n(w)}"/>')
        if depth > 0:
            for da in (-0.5 + rng.uniform(-0.15, 0.15), 0.45 + rng.uniform(-0.15, 0.15)):
                branch(x2, y2, ang + da, length * 0.72, depth - 1, max(w * 0.7, 1.2))

    for ang in [math.pi * 0.55, math.pi * 0.78, math.pi * 1.05, math.pi * 1.3, math.pi * 1.55]:
        sx, sy = 125 + 26 * math.cos(ang), 108 + 25 * math.sin(ang)
        branch(sx, sy, ang, 28, 3, 5)
    myelin = "".join(
        f'<ellipse cx="{x}" cy="{y}" rx="11" ry="8" fill="#F8E7B0" stroke="#C9A85E" stroke-width="1.2"/>'
        for x, y in [(169, 105), (188, 108), (208, 111)]
    )
    terminals = "".join(
        f'<path d="M232 108L{x} {y}" stroke="#C97AA4" stroke-width="3" fill="none"/><circle cx="{x}" cy="{y}" r="4.5" fill="#C97AA4"/>'
        for x, y in [(254, 94), (260, 110), (252, 128)]
    )
    return f"""<g id="sp-neuron">
<g fill="none" stroke="#B4558A" stroke-linecap="round">{''.join(paths)}</g>
<path d="M150 108C176 98 198 118 232 108" stroke="#C97AA4" stroke-width="6" fill="none" stroke-linecap="round"/>
{myelin}
{terminals}
<path d="M99 108c0-22 14-34 28-30c16-4 34 8 30 30c4 22-16 34-32 30c-18 4-28-8-26-30z" fill="url(#gSoma)" stroke="#8A3A66" stroke-width="2"/>
<circle cx="128" cy="108" r="11" fill="#7C2F5B"/><circle cx="130" cy="106" r="4" fill="#4D1738"/>
<ellipse cx="116" cy="92" rx="8" ry="4" fill="#fff" opacity=".45" transform="rotate(-25 116 92)"/>
</g>"""


def plasma():
    rng = random.Random(5)
    fil = []
    for k in range(11):
        a = k * 2 * math.pi / 11 + rng.uniform(-0.15, 0.15)
        ex, ey = polar(100, 100, 86, a)
        mx, my = polar(100, 100, 46, a + rng.uniform(-0.5, 0.5))
        fil.append(f'<path d="M100 100Q{n(mx)} {n(my)} {n(ex)} {n(ey)}" stroke-width="{n(rng.uniform(1.2, 2.4))}"/>')
        bx, by = polar(100, 100, 62, a)
        cx2, cy2 = polar(bx, by, 20, a + rng.uniform(-1.0, 1.0))
        fil.append(f'<path d="M{n(bx)} {n(by)}L{n(cx2)} {n(cy2)}" stroke-width="1"/>')
    return f"""<g id="sp-plasma">
<path d="M66 192h68l16 50h-100z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.5" stroke-linejoin="round"/>
<rect x="86" y="176" width="28" height="20" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.2"/>
<circle cx="100" cy="100" r="92" fill="url(#gPlasma)" stroke="#E8B33C" stroke-width="2.4"/>
<g filter="url(#fGlow)" fill="none" stroke="#FFE08A" stroke-linecap="round">{''.join(fil)}</g>
<circle cx="100" cy="100" r="20" fill="url(#gCore)"/>
<ellipse cx="66" cy="50" rx="28" ry="15" fill="#fff" opacity=".2" transform="rotate(-35 66 50)"/>
</g>"""


def crystal():
    def one(bx, by, ang, w, L):
        tip = 0.75 * w
        return (
            f'<g transform="translate({bx} {by}) rotate({ang})" stroke="#5C78B8" stroke-width="1" stroke-linejoin="round">'
            f'<polygon points="{n(-w / 2)},0 {n(-w / 2)},{n(-L)} 0,{n(-L - tip)} 0,0" fill="url(#gCrysL)"/>'
            f'<polygon points="0,0 0,{n(-L - tip)} {n(w / 2)},{n(-L)} {n(w / 2)},0" fill="url(#gCrysR)"/>'
            f'<polygon points="{n(-w / 2)},{n(-L)} 0,{n(-L - tip)} {n(w / 2)},{n(-L)} 0,{n(-L + w * 0.3)}" fill="#fff" opacity=".6" stroke="none"/>'
            f"</g>"
        )

    specs = [(34, 204, -48, 20, 64), (168, 202, 46, 20, 70), (62, 200, -24, 26, 92), (140, 200, 22, 28, 100), (100, 206, 8, 34, 124), (84, 208, -8, 16, 50)]
    return '<g id="sp-crystal">' + "".join(one(*s) for s in specs) + "</g>"


def molecule():
    atoms = [(95, 85, 26, "gSG"), (50, 60, 20, "gSB"), (140, 55, 20, "gSG"), (60, 125, 18, "gSR"), (135, 125, 20, "gSG"), (95, 28, 14, "gSB")]
    bonds = "".join(
        f'<line x1="95" y1="85" x2="{x}" y2="{y}" stroke="#8A8F94" stroke-width="7" stroke-linecap="round"/><line x1="95" y1="85" x2="{x}" y2="{y}" stroke="#E4E8EB" stroke-width="2.5" stroke-linecap="round"/>'
        for x, y, r, g in atoms[1:]
    )
    balls = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{g})"/><ellipse cx="{x - r * 0.32:.1f}" cy="{y - r * 0.4:.1f}" rx="{r * 0.28:.1f}" ry="{r * 0.17:.1f}" fill="#fff" opacity=".6"/>'
        for x, y, r, g in atoms
    )
    return f'<g id="sp-molecule">{bonds}{balls}</g>'


def butterfly():
    spots = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".9"/>' for x, y, r in [(216, 40, 3), (225, 50, 2.4), (206, 34, 2.2), (196, 144, 3), (186, 152, 2.4), (206, 134, 2.2)])
    return f"""<g id="sp-butterfly">
<g id="bwR">
<path d="M124 90C140 40 190 12 226 30C240 58 200 90 124 100Z" fill="url(#gMorpho)" stroke="#0B1020" stroke-width="3" stroke-linejoin="round"/>
<path d="M124 102C170 100 208 118 196 148C182 172 146 156 124 116Z" fill="url(#gMorpho)" stroke="#0B1020" stroke-width="3" stroke-linejoin="round"/>
<path d="M126 94L212 42M126 96L226 70M126 106L190 140M126 110L170 156" stroke="#0B1020" stroke-width="1.2" opacity=".5" fill="none"/>
{spots}
</g>
<use href="#bwR" transform="translate(248 0) scale(-1 1)"/>
<ellipse cx="124" cy="100" rx="5" ry="42" fill="#1B1511"/><circle cx="124" cy="56" r="6" fill="#1B1511"/>
<path d="M121 52Q110 30 98 24M127 52Q138 30 150 24" stroke="#1B1511" stroke-width="2" fill="none"/>
<circle cx="98" cy="24" r="3" fill="#1B1511"/><circle cx="150" cy="24" r="3" fill="#1B1511"/>
</g>"""


def nautilus():
    cx, cy, a, b = 108, 100, 7.0, 0.19

    def pt(th):
        r = a * math.exp(b * th)
        return cx + r * math.cos(th), cy + r * math.sin(th)

    def frange(lo, hi, steps):
        return [lo + (hi - lo) * i / steps for i in range(steps + 1)]

    outer = [pt(t) for t in frange(2 * math.pi, 4 * math.pi, 120)]
    sil = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in outer) + "Z"
    spiral = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in [pt(t) for t in frange(0, 4 * math.pi, 220)])
    septa = []
    t = math.pi
    while t < 4 * math.pi - 0.1:
        x1, y1 = pt(t)
        x0, y0 = pt(t - 2 * math.pi)
        mx, my = (x1 + x0) / 2, (y1 + y0) / 2
        nx, ny = -(y1 - y0), (x1 - x0)
        ln = math.hypot(nx, ny) or 1
        qx, qy = mx + nx / ln * 6, my + ny / ln * 6
        septa.append(f"M{n(x0)} {n(y0)}Q{n(qx)} {n(qy)} {n(x1)} {n(y1)}")
        t += math.pi / 6
    return f"""<g id="sp-nautilus">
<path d="{sil}" fill="url(#gShell)" stroke="#7A3E17" stroke-width="3" stroke-linejoin="round"/>
<path d="{spiral}" fill="none" stroke="#7A3E17" stroke-width="2.6" stroke-linejoin="round"/>
<path d="{''.join(septa)}" fill="none" stroke="#9A5A25" stroke-width="1.6"/>
<path d="{sil}" fill="none" stroke="#fff" stroke-width="5" opacity=".22" transform="translate(-3 -3)"/>
</g>"""


def tree():
    rng = random.Random(3)
    out = []
    leaf = ["#2F8F4E", "#C0392B", "#E3A21A", "#2F6FD0"]

    def br(x, y, ang, length, depth, w):
        x2, y2 = x + length * math.cos(ang), y + length * math.sin(ang)
        out.append(f'<line x1="{n(x)}" y1="{n(y)}" x2="{n(x2)}" y2="{n(y2)}" stroke="#3B2A18" stroke-width="{n(w)}" stroke-linecap="round"/>')
        if depth > 0:
            br(x2, y2, ang - 0.45 + rng.uniform(-0.1, 0.1), length * 0.76, depth - 1, w * 0.72)
            br(x2, y2, ang + 0.5 + rng.uniform(-0.1, 0.1), length * 0.76, depth - 1, w * 0.72)
        else:
            out.append(f'<circle cx="{n(x2)}" cy="{n(y2)}" r="3" fill="{rng.choice(leaf)}" stroke="#3B2A18" stroke-width=".8"/>')

    br(120, 150, -math.pi / 2, 32, 4, 5)
    return f"""<g id="sp-tree">
<path d="M8 10Q60 4 120 9T232 8L233 160Q180 166 120 160T7 162Z" fill="url(#gParch)" stroke="#B59A62" stroke-width="2"/>
<ellipse cx="48" cy="130" rx="30" ry="18" fill="#B08A3E" opacity=".12"/><ellipse cx="200" cy="40" rx="26" ry="16" fill="#B08A3E" opacity=".1"/>
{''.join(out)}
<path d="M22 150h40M22 156h28M178 150h40M190 156h28" stroke="#8A6B35" stroke-width="1.6" opacity=".6"/>
</g>"""


def honey():
    s = 24
    w = math.sqrt(3) * s
    cells = [(0, 0), (1, 0), (-1, 0), (0, 1), (-1, 1), (0, -1), (1, -1), (2, -1)]
    parts = []
    for i, (q, r) in enumerate(cells):
        cx = 90 + q * w + r * w / 2
        cy = 85 + r * 1.5 * s
        pts = " ".join(f"{n(polar(cx, cy, s, math.radians(60 * k - 30))[0])},{n(polar(cx, cy, s, math.radians(60 * k - 30))[1])}" for k in range(6))
        parts.append(f'<polygon points="{pts}" fill="url(#gHoney)" stroke="#8A5A10" stroke-width="2.5" stroke-linejoin="round"/>')
        if i % 3 != 1:
            ip = " ".join(f"{n(polar(cx, cy, s * 0.66, math.radians(60 * k - 30))[0])},{n(polar(cx, cy, s * 0.66, math.radians(60 * k - 30))[1])}" for k in range(6))
            parts.append(f'<polygon points="{ip}" fill="#C9780F" opacity=".75"/>')
    return '<g id="sp-honey">' + "".join(parts) + "</g>"


# ----------------------------------------------------------------- fullstack
def world():
    grat = "".join(
        f'<ellipse cx="120" cy="65" rx="{rx}" ry="61" fill="none" stroke="#fff" stroke-width="1" opacity=".35"/>' for rx in (30, 62, 92)
    ) + '<line x1="4" y1="65" x2="236" y2="65" stroke="#fff" stroke-width="1" opacity=".35"/>'
    return f"""<g id="sp-world">
<defs><clipPath id="cpWorld"><ellipse cx="120" cy="65" rx="116" ry="61"/></clipPath></defs>
<ellipse cx="120" cy="65" rx="116" ry="61" fill="url(#gOcean)"/>
<g clip-path="url(#cpWorld)" fill="url(#gLand)" stroke="#2F6E34" stroke-width="1.2" stroke-linejoin="round">
<path d="M32 30C48 14 80 16 92 28C100 38 90 48 80 52C74 62 62 66 56 60C46 52 30 46 32 30Z"/>
<path d="M72 70C86 66 98 76 96 90C94 104 84 116 78 112C70 100 62 84 72 70Z"/>
<path d="M118 28C132 22 146 28 148 40C158 48 154 62 146 72C140 88 130 104 124 100C116 90 118 70 108 58C104 44 108 34 118 28Z"/>
<path d="M150 24C176 14 208 22 214 40C216 54 200 62 184 60C170 58 160 52 152 40Z"/>
<path d="M184 86C196 80 210 86 208 98C204 108 190 108 184 98Z"/>
</g>
{grat}
<ellipse cx="120" cy="65" rx="116" ry="61" fill="none" stroke="#1F5FAE" stroke-width="2"/>
<ellipse cx="82" cy="34" rx="40" ry="12" fill="#fff" opacity=".22" transform="rotate(-12 82 34)"/>
</g>"""


def compass():
    ticks = []
    for i in range(36):
        a = i * math.pi / 18
        r0 = 62 if i % 9 == 0 else (66 if i % 3 == 0 else 69)
        x0, y0 = polar(85, 85, r0, a)
        x1, y1 = polar(85, 85, 73, a)
        ticks.append(f'<line x1="{n(x0)}" y1="{n(y0)}" x2="{n(x1)}" y2="{n(y1)}" stroke="#3A2A12" stroke-width="{2 if i % 3 == 0 else 1}"/>')
    return f"""<g id="sp-compass">
<circle cx="85" cy="85" r="80" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5"/>
<circle cx="85" cy="85" r="73" fill="url(#gDial)" stroke="#6B4A1A" stroke-width="2"/>
{''.join(ticks)}
<polygon points="85,18 92,78 85,85 78,78" fill="#C8372D"/>
<polygon points="85,152 92,92 85,85 78,92" fill="#2A3A5A"/>
<polygon points="18,85 78,78 85,85 78,92" fill="#8A8F94"/>
<polygon points="152,85 92,78 85,85 92,92" fill="#8A8F94"/>
<polygon points="85,85 108,62 94,85 108,108" fill="none"/>
<circle cx="85" cy="85" r="6" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1"/>
<path d="M44 52A52 52 0 0 1 80 30" stroke="#fff" stroke-width="5" opacity=".5" fill="none" stroke-linecap="round"/>
</g>"""


# ------------------------------------------------- frontend hero set (v2)
EXTRA_DEFS = """
<linearGradient id="gBlueRing" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9CCBFF"/><stop offset=".45" stop-color="#2F7DE8"/><stop offset="1" stop-color="#123C8C"/></linearGradient>
<linearGradient id="gNavy" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A4A8C"/><stop offset=".5" stop-color="#16264A"/><stop offset="1" stop-color="#0B1530"/></linearGradient>
<radialGradient id="gVig" cx=".5" cy=".5" r=".5"><stop offset=".55" stop-color="#3F7FE0" stop-opacity="0"/><stop offset="1" stop-color="#1F4FA8" stop-opacity=".24"/></radialGradient>
<linearGradient id="gRule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F8E8BC"/><stop offset="1" stop-color="#E0C07A"/></linearGradient>
<linearGradient id="gBrushH" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6FB0FF"/><stop offset=".5" stop-color="#2F7DE8"/><stop offset="1" stop-color="#15408F"/></linearGradient>
<linearGradient id="gBristle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0D3A0"/><stop offset="1" stop-color="#B07E42"/></linearGradient>
"""

A_GLYPH = ["...###...", "..##.##..", "..##.##..", ".##...##.", ".#######.", ".#######.",
           "##.....##", "##.....##", "##.....##"]


def lens():
    cell, x0 = 14, 32
    dark = {(r, c) for r, row in enumerate(A_GLYPH) for c, ch in enumerate(row) if ch == "#"}
    cells = []
    for r in range(9):
        for c in range(9):
            near = any((r + dr, c + dc) in dark for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            fill = "#10151C" if (r, c) in dark else "#E6EEFB"
            cells.append(f'<rect x="{n(x0 + c * cell)}" y="{n(x0 + r * cell)}" width="{cell}" height="{cell}" fill="{fill}" stroke="#D3E0F6" stroke-width=".7"/>')
    return f"""<g id="sp-lens">
<clipPath id="lensClip"><circle cx="95" cy="95" r="80"/></clipPath>
<path d="M142 148L172 232" stroke="#0B1530" stroke-width="20" stroke-linecap="round"/>
<path d="M142 148L172 232" stroke="url(#gNavy)" stroke-width="17" stroke-linecap="round"/>
<path d="M139 152L165 226" stroke="#6C8FD8" stroke-width="3" stroke-linecap="round" opacity=".55"/>
<path d="M134 134L152 176" stroke="url(#gBlueRing)" stroke-width="22" stroke-linecap="round"/>
<circle cx="95" cy="95" r="80" fill="#fff"/>
<g clip-path="url(#lensClip)">{"".join(cells)}<circle cx="95" cy="95" r="80" fill="url(#gVig)"/></g>
<circle cx="95" cy="95" r="85" fill="none" stroke="url(#gBlueRing)" stroke-width="12"/>
<circle cx="95" cy="95" r="91.5" fill="none" stroke="#163F91" stroke-width="1.2" opacity=".7"/>
<circle cx="95" cy="95" r="78.5" fill="none" stroke="#0E2E70" stroke-width="1.2" opacity=".6"/>
<path d="M40 64A62 62 0 0 1 80 32" stroke="#fff" stroke-width="6" opacity=".8" fill="none" stroke-linecap="round"/>
</g>"""


def ruler():
    ticks = []
    for i in range(0, 41):
        x = 10 + i * 7.5
        major, mid = i % 10 == 0, i % 5 == 0
        h = 17 if major else (12 if mid else 8)
        ticks.append(f'<path d="M{n(x)} 4V{4 + h}" stroke="#5B4120" stroke-width="{1.4 if major else 1}"/>')
        if major:
            ticks.append(f'<text x="{n(x)}" y="36" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-weight="600" font-size="11" fill="#5B4120">{i // 10 * 10 or 0}</text>')
    return f"""<g id="sp-ruler">
<rect x="2" y="4" width="316" height="44" rx="3" fill="url(#gRule)" stroke="#A07A34" stroke-width="1.5"/>
<rect x="2" y="42" width="316" height="6" rx="2" fill="#B88B3A" opacity=".35"/>
{"".join(ticks)}
</g>"""


def brush():
    return """<g id="sp-brush">
<path d="M70 12L300 17Q312 20 300 23L70 28Z" fill="url(#gBrushH)" stroke="#102F70" stroke-width="1.2"/>
<path d="M76 15L290 19" stroke="#fff" stroke-width="2.4" opacity=".45" stroke-linecap="round"/>
<rect x="44" y="9" width="30" height="22" rx="3" fill="url(#gSteel)" stroke="#5E6A75" stroke-width="1"/>
<path d="M54 9v22M62 9v22M70 9v22" stroke="#5E6A75" stroke-width="1" opacity=".6"/>
<path d="M46 10C30 7 14 14 3 20C14 26 30 33 46 30Z" fill="url(#gBristle)" stroke="#7A5A30" stroke-width="1"/>
<path d="M3 20C9 17 15 14 22 12L22 28C15 26 9 23 3 20Z" fill="#2F6BDB"/>
</g>"""


def typeblock2():
    return typeblock().replace('id="sp-typeblock"', 'id="sp-typeblock2"').replace('font-size="92"', 'font-size="84"').replace(">A</text>", ">&amp;</text>")


# ------------------------------------------------- frontend hero v3: vintage monitor
EXTRA_DEFS += """
<linearGradient id="gBeige" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3EAD2"/><stop offset=".6" stop-color="#E0D3AE"/><stop offset="1" stop-color="#C9B98F"/></linearGradient>
<linearGradient id="gBeigeH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C9B98F"/><stop offset=".5" stop-color="#EADFC0"/><stop offset="1" stop-color="#BBAA7E"/></linearGradient>
<linearGradient id="gShot" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9CCBFF"/><stop offset="1" stop-color="#2F7DE8"/></linearGradient>
<radialGradient id="gScreenVig" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#0B1E4A" stop-opacity="0"/><stop offset="1" stop-color="#0B1E4A" stop-opacity=".30"/></radialGradient>
"""


def monitor():
    dots = "".join(f'<circle cx="{46 + i * 10}" cy="38" r="3" fill="#fff" opacity=".9"/>' for i in range(3))
    side = "".join(
        f'<rect x="42" y="{56 + i * 14}" width="28" height="6" rx="3" fill="{"#2F8CFF" if i == 0 else "#9DB7E8"}"/>' for i in range(5))
    vents = "".join(f'<rect x="{138 + i * 8}" y="164" width="4.5" height="15" rx="2.2" fill="#A39574"/>' for i in range(8))
    return f"""<g id="sp-monitor">
<path d="M94 184L166 184L180 212L80 212Z" fill="url(#gBeigeH)" stroke="#8F8060" stroke-width="1.5"/>
<rect x="60" y="208" width="140" height="20" rx="10" fill="url(#gBeige)" stroke="#8F8060" stroke-width="1.5"/>
<rect x="8" y="6" width="244" height="182" rx="18" fill="url(#gBeige)" stroke="#8F8060" stroke-width="1.6"/>
<path d="M22 12H238" stroke="#fff" stroke-width="3" opacity=".6" stroke-linecap="round"/>
<rect x="26" y="22" width="208" height="134" rx="12" fill="#232830" stroke="#0F1318" stroke-width="1.5"/>
<clipPath id="monClip"><rect x="34" y="30" width="192" height="118" rx="8"/></clipPath>
<g clip-path="url(#monClip)">
<rect x="34" y="30" width="192" height="118" fill="#F6F9FE"/>
<rect x="34" y="30" width="192" height="16" fill="#2F8CFF"/>{dots}
<rect x="34" y="46" width="44" height="102" fill="#E6EEFB"/>{side}
<text x="92" y="80" font-family="EB Garamond, Georgia, serif" font-weight="700" font-size="32" fill="#10151C">Aa</text>
<rect x="92" y="88" width="62" height="5" rx="2.5" fill="#9AA6B8"/>
<rect x="92" y="98" width="52" height="4" rx="2" fill="#CBD3E0"/>
<rect x="92" y="106" width="44" height="4" rx="2" fill="#CBD3E0"/>
<rect x="92" y="118" width="38" height="14" rx="7" fill="#2F8CFF"/><rect x="100" y="124" width="22" height="3" rx="1.5" fill="#fff" opacity=".9"/>
<rect x="160" y="54" width="58" height="42" rx="5" fill="url(#gShot)"/>
<polygon points="160,96 176,74 189,88 199,78 218,96" fill="#fff" opacity=".78"/><circle cx="205" cy="64" r="5" fill="#FFE27A"/>
<rect x="160" y="102" width="58" height="30" rx="5" fill="#fff" stroke="#D3DDF0" stroke-width="1.2"/>
<rect x="167" y="110" width="30" height="4" rx="2" fill="#9AA6B8"/><rect x="167" y="119" width="42" height="3" rx="1.5" fill="#CBD3E0"/>
<polygon points="146,112 146,134 151.5,129.5 155.5,138 160,136 156,127.5 163,127.5" fill="#10151C" stroke="#fff" stroke-width="1.2"/>
<rect x="34" y="30" width="192" height="118" fill="url(#gScreenVig)"/>
<path d="M34 30H128L66 148H34Z" fill="#fff" opacity=".13"/>
</g>
<rect x="34" y="30" width="192" height="118" rx="8" fill="none" stroke="#0F1318" stroke-width="1.4"/>
<rect x="24" y="164" width="40" height="13" rx="4" fill="#CDBE96" stroke="#A39574" stroke-width="1"/>
{vents}
<circle cx="224" cy="171" r="5" fill="#46DD78" stroke="#1E8A47" stroke-width="1.2"/><circle cx="222.5" cy="169.5" r="1.6" fill="#fff" opacity=".8"/>
</g>"""


# ------------------------------------------------- filler specimens (small pool items)
EXTRA_DEFS += """
<linearGradient id="gAmber" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE9A0"/><stop offset="1" stop-color="#E8B83A"/></linearGradient>
<linearGradient id="gCursor" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#B9CBEA"/></linearGradient>
"""


def glyph_block(ident, glyph, size=78):
    return typeblock().replace('id="sp-typeblock"', f'id="sp-{ident}"').replace('font-size="92"', f'font-size="{size}"').replace(">A</text>", f">{glyph}</text>")


def typeblock3():
    return glyph_block("typeblock3", "{}", 70)


def typeblock4():
    return glyph_block("typeblock4", "#", 84)


def typeblock5():
    return glyph_block("typeblock5", "?", 88)


def cursor():
    return """<g id="sp-cursor">
<polygon points="10,6 10,96 34,72 50,110 68,102 52,66 84,66" fill="url(#gCursor)" stroke="#10151C" stroke-width="7" stroke-linejoin="round"/>
<path d="M19 28V70L32 57" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
</g>"""


def setsquare():
    ticks = "".join(f'<path d="M{14 + i * 10} 124v-{7 if i % 5 else 12}" stroke="#7A5A10" stroke-width="1.2"/>' for i in range(15))
    return f"""<g id="sp-setsquare">
<path d="M6 124H170L6 10Z M34 102H108L34 52Z" fill="url(#gAmber)" fill-rule="evenodd" stroke="#A07A1E" stroke-width="2" stroke-linejoin="round" opacity=".96"/>
{ticks}
<path d="M10 20L10 118" stroke="#fff" stroke-width="3" opacity=".5"/>
</g>"""



# ----------------------------------------------------- gap-filling specimens
EXTRA_DEFS += """
<linearGradient id="gFossil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EBD7AE"/><stop offset=".55" stop-color="#C79B62"/><stop offset="1" stop-color="#8A5F33"/></linearGradient>
<linearGradient id="gFeather" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B9ECE4"/><stop offset=".5" stop-color="#4FB3C4"/><stop offset="1" stop-color="#1F6C94"/></linearGradient>
<radialGradient id="gBeetle" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#D6F7A8"/><stop offset=".45" stop-color="#2FAE6A"/><stop offset="1" stop-color="#0A4A3C"/></radialGradient>
<radialGradient id="gStar" cx=".5" cy=".45" r=".7"><stop offset="0" stop-color="#FFD9B8"/><stop offset=".6" stop-color="#F2894F"/><stop offset="1" stop-color="#C8512B"/></radialGradient>
<linearGradient id="gLeaf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B7E48A"/><stop offset="1" stop-color="#3C9A4A"/></linearGradient>
"""


def database():
    discs = []
    for i in (2, 1, 0):
        y0 = 24 + i * 38
        discs.append(
            f'<path d="M12 {y0}v30a48 14 0 0 0 96 0v-30z" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="1.5"/>'
            f'<ellipse cx="60" cy="{y0}" rx="48" ry="14" fill="#E9EEF2" stroke="#4E5A66" stroke-width="1.5"/>'
            f'<ellipse cx="60" cy="{y0}" rx="36" ry="9.5" fill="none" stroke="#fff" stroke-width="1.2" opacity=".7"/>'
            f'<circle cx="28" cy="{y0 + 22}" r="3.4" fill="#34B25A" stroke="#0E6B34" stroke-width=".8"/>'
            f'<circle cx="40" cy="{y0 + 23}" r="3.4" fill="#FFC93C" stroke="#9A6E10" stroke-width=".8"/>'
            f'<path d="M62 {y0 + 22}h30" stroke="#4E5A66" stroke-width="2.4" stroke-linecap="round"/>'
        )
    return ('<g id="sp-database"><rect x="44" y="30" width="32" height="104" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>'
            + "".join(discs) + "</g>")


def telegraph():
    return """<g id="sp-telegraph">
<rect x="8" y="72" width="184" height="30" rx="6" fill="url(#gWoodDark)" stroke="#3E2410" stroke-width="1.5"/>
<rect x="8" y="72" width="184" height="11" rx="6" fill="url(#gWood)" stroke="#3E2410" stroke-width="1.2"/>
<rect x="88" y="46" width="24" height="30" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="146" y="58" width="28" height="18" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<path d="M26 50L178 40V50L26 60Z" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4" stroke-linejoin="round"/>
<circle cx="100" cy="52" r="5" fill="#FBEBB0" stroke="#7B5218" stroke-width="1"/>
<ellipse cx="30" cy="38" rx="17" ry="13" fill="#232933" stroke="#0C0F14" stroke-width="1.5"/>
<ellipse cx="26" cy="33" rx="8" ry="4" fill="#fff" opacity=".35"/>
<circle cx="24" cy="87" r="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/>
<circle cx="176" cy="87" r="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/>
</g>"""


def spool():
    lines = "".join(
        f'<path d="M26 {25 + i * 9}H104" stroke="#B3362B" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M30 {22.5 + i * 9}H100" stroke="#F29A8C" stroke-width="1.6" stroke-linecap="round" opacity=".7"/>'
        for i in range(9)
    )
    return f"""<g id="sp-spool">
<rect x="26" y="20" width="78" height="92" fill="#8E2B26"/>
{lines}
<rect x="8" y="6" width="114" height="17" rx="4" fill="url(#gWood)" stroke="#5E3A1A" stroke-width="1.5"/>
<rect x="8" y="109" width="114" height="17" rx="4" fill="url(#gWoodDark)" stroke="#3E2410" stroke-width="1.5"/>
<path d="M104 70C128 70 130 94 112 104" fill="none" stroke="#B3362B" stroke-width="6" stroke-linecap="round"/>
<path d="M112 104l-6 8" stroke="#E7BB84" stroke-width="4" stroke-linecap="round"/>
</g>"""


def hourglass():
    return """<g id="sp-hourglass">
<rect x="10" y="4" width="90" height="13" rx="4" fill="url(#gWood)" stroke="#5E3A1A" stroke-width="1.5"/>
<rect x="10" y="153" width="90" height="13" rx="4" fill="url(#gWoodDark)" stroke="#3E2410" stroke-width="1.5"/>
<rect x="12" y="16" width="6" height="138" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1"/>
<rect x="92" y="16" width="6" height="138" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1"/>
<path d="M22 17C22 62 52 70 52 85C52 100 22 108 22 153H88C88 108 58 100 58 85C58 70 88 62 88 17Z" fill="url(#gGlass)" stroke="#4F80AA" stroke-width="2" stroke-linejoin="round"/>
<path d="M28 24H82C78 46 62 58 57 72H53C48 58 32 46 28 24Z" fill="url(#gAmber)"/>
<path d="M55 72V128" stroke="#E8B83A" stroke-width="1.8"/>
<path d="M27 151C42 122 68 122 83 151Z" fill="url(#gAmber)"/>
<path d="M30 30C32 54 42 70 48 84" fill="none" stroke="#fff" stroke-width="3" opacity=".6" stroke-linecap="round"/>
</g>"""


def scales():
    return """<g id="sp-scales">
<path d="M52 152H138Q130 132 95 130Q60 132 52 152Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.5"/>
<rect x="89" y="30" width="12" height="104" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="16" y="33" width="158" height="9" rx="4.5" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.3"/>
<circle cx="95" cy="26" r="9" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.3"/>
<path d="M22 42L4 106M22 42L42 106M168 42L148 106M168 42L186 106" fill="none" stroke="#7B5218" stroke-width="1.3"/>
<path d="M2 106H44Q42 126 23 126Q4 126 2 106Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<path d="M146 106H188Q186 126 167 126Q148 126 146 106Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<circle cx="23" cy="98" r="8" fill="url(#gBead)" stroke="#5E140E" stroke-width="1"/>
<circle cx="167" cy="98" r="8" fill="url(#gSB)" stroke="#123F8E" stroke-width="1"/>
</g>"""


def vault():
    bolts = "".join(
        f'<circle cx="{n(75 + 60 * math.cos(math.radians(a)))}" cy="{n(75 + 60 * math.sin(math.radians(a)))}" r="3.4" fill="url(#gBrass)" stroke="#7B5218" stroke-width=".8"/>'
        for a in range(0, 360, 30)
    )
    spokes = "".join(
        f'<path d="M75 75L{n(75 + 34 * math.cos(math.radians(a)))} {n(75 + 34 * math.sin(math.radians(a)))}" stroke="url(#gBrass)" stroke-width="6" stroke-linecap="round"/>'
        f'<circle cx="{n(75 + 34 * math.cos(math.radians(a)))}" cy="{n(75 + 34 * math.sin(math.radians(a)))}" r="6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1"/>'
        for a in (-90, 30, 150)
    )
    return f"""<g id="sp-vault">
<rect x="0" y="38" width="12" height="22" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<rect x="0" y="92" width="12" height="22" rx="3" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
<circle cx="78" cy="75" r="68" fill="url(#gSteelDark)" stroke="#1B2026" stroke-width="2"/>
<circle cx="78" cy="75" r="56" fill="url(#gSteel)" stroke="#4E5A66" stroke-width="1.5"/>
<circle cx="78" cy="75" r="44" fill="none" stroke="#fff" stroke-width="1.5" opacity=".6"/>
<g transform="translate(3 0)">{bolts}</g>
<g transform="translate(3 0)">{spokes}
<circle cx="75" cy="75" r="13" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.5"/>
<circle cx="75" cy="75" r="5" fill="#232933"/></g>
</g>"""


def trilobite():
    def hh(x):
        if x <= 136:
            return 36 - (x - 70) * 0.1
        return 29.4 * math.sqrt(max(0, 1 - ((x - 136) / 52) ** 2))

    xs = [66 + i * 2 for i in range(62)]
    top = [(x, 70 - hh(x)) for x in xs]
    bot = [(x, 70 + hh(x)) for x in reversed(xs)]
    body = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in top + bot) + "Z"
    grooves = "".join(
        f'<path d="M{n(x)} {n(70 - hh(x))}Q{n(x + 3)} 70 {n(x)} {n(70 + hh(x))}" fill="none" stroke="#6B4524" stroke-width="1.7"/>'
        for x in [76 + k * 8 for k in range(8)]
    )
    ribs = "".join(
        f'<path d="M{n(x)} {n(70 - hh(x) * .86)}Q{n(x + 3)} 70 {n(x)} {n(70 + hh(x) * .86)}" fill="none" stroke="#6B4524" stroke-width="1.2" opacity=".85"/>'
        for x in (142, 150, 158, 166, 174)
    )
    return f"""<g id="sp-trilobite">
<path d="{body}" fill="url(#gFossil)" stroke="#5E3F1D" stroke-width="2.6" stroke-linejoin="round"/>
{grooves}{ribs}
<path d="M72 58H176M72 82H176" stroke="#6B4524" stroke-width="1.5" fill="none"/>
<path d="M56 22L102 6L76 34Z M56 118L102 134L76 106Z" fill="url(#gFossil)" stroke="#5E3F1D" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M72 16A62 54 0 0 0 72 124Q66 70 72 16Z" fill="url(#gFossil)" stroke="#5E3F1D" stroke-width="2.8" stroke-linejoin="round"/>
<ellipse cx="54" cy="70" rx="17" ry="34" fill="#fff" opacity=".2" stroke="#6B4524" stroke-width="1.8"/>
<path d="M50 50C52 56 52 62 50 66M50 74C52 78 52 84 50 90" fill="none" stroke="#6B4524" stroke-width="1.3"/>
<ellipse cx="64" cy="40" rx="5" ry="8.5" fill="#3F2814" transform="rotate(20 64 40)"/><ellipse cx="64" cy="100" rx="5" ry="8.5" fill="#3F2814" transform="rotate(-20 64 100)"/><circle cx="62" cy="37" r="1.6" fill="#fff" opacity=".7"/><circle cx="62" cy="97" r="1.6" fill="#fff" opacity=".7"/>
<path d="M24 36C36 22 56 20 68 26" fill="none" stroke="#fff" stroke-width="4" opacity=".35" stroke-linecap="round"/>
</g>"""


def feather():
    def q(t):
        x = (1 - t) ** 2 * 6 + 2 * (1 - t) * t * 110 + t * t * 216
        y = (1 - t) ** 2 * 68 + 2 * (1 - t) * t * 44 + t * t * 30
        return x, y

    ups, dns, barbs = [], [], []
    steps = 34
    for i in range(steps + 1):
        t = 0.1 + 0.88 * i / steps
        x, y = q(t)
        ln = 30 * math.sin(math.pi * min(1, t * 1.02)) ** 0.75 + 2
        ux, uy = x + ln * math.cos(math.radians(-62)), y + ln * math.sin(math.radians(-62))
        dx, dy = x + ln * 0.92 * math.cos(math.radians(62)), y + ln * 0.92 * math.sin(math.radians(62))
        ups.append((ux, uy)); dns.append((dx, dy))
        barbs.append(f"M{n(x)} {n(y)}L{n(ux)} {n(uy)}M{n(x)} {n(y)}L{n(dx)} {n(dy)}")
    qx = [q(t / 20) for t in range(0, 21)]
    vane = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in ups) + "L" + "L".join(f"{n(x)} {n(y)}" for x, y in reversed(dns)) + "Z"
    quill = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in qx)
    return f"""<g id="sp-feather">
<path d="{vane}" fill="url(#gFeather)" stroke="#1F6C94" stroke-width="1.6" stroke-linejoin="round"/>
<path d="{''.join(barbs)}" stroke="#1F6C94" stroke-width=".8" opacity=".55"/>
<path d="{quill}" fill="none" stroke="#F3E6C4" stroke-width="3.4" stroke-linecap="round"/>
<path d="{quill}" fill="none" stroke="#9A7C42" stroke-width=".9" stroke-linecap="round"/>
</g>"""


def telescope():
    return """<g id="sp-telescope">
<path d="M6 46H40V64H6Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<ellipse cx="6" cy="55" rx="3.5" ry="9" fill="#232933" stroke="#7B5218" stroke-width="1"/>
<rect x="40" y="40" width="72" height="30" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4"/>
<rect x="112" y="34" width="70" height="42" fill="#243457" stroke="#0B1530" stroke-width="1.4"/>
<rect x="112" y="40" width="70" height="5" fill="#fff" opacity=".22"/>
<path d="M182 30L232 20V90L182 80Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.4" stroke-linejoin="round"/>
<ellipse cx="232" cy="55" rx="7" ry="35" fill="url(#gGlass)" stroke="#7B5218" stroke-width="1.6"/>
<path d="M40 40V70M112 34V76M182 30V80M76 40V70" stroke="#7B5218" stroke-width="1.6"/>
<path d="M114 38H180" stroke="#C9A24A" stroke-width="1.2" opacity=".7" stroke-dasharray="2 4"/>
</g>"""


def samara():
    veins = "".join(
        f'<path d="M{n(30 + i * 3)} {n(80 - i * 1.5)}C{n(52 + i * 6)} {n(54 - i * 4)} {n(86 + i * 5)} {n(30 - i * 2)} {n(124 - i * 2)} {n(12 + i * 6)}" fill="none" stroke="#B58A4A" stroke-width="1" opacity=".75"/>'
        for i in range(-1, 5)
    )
    return f"""<g id="sp-samara">
<path d="M28 76C34 42 72 14 130 8C134 34 98 70 40 94Z" fill="url(#gParch)" stroke="#9A7432" stroke-width="2" stroke-linejoin="round"/>
{veins}
<ellipse cx="26" cy="88" rx="14" ry="17" fill="url(#gWood)" stroke="#5E3A1A" stroke-width="2" transform="rotate(-22 26 88)"/>
<path d="M18 82C20 76 25 72 31 72" fill="none" stroke="#fff" stroke-width="2.4" opacity=".5" stroke-linecap="round"/>
</g>"""


def beetle():
    def legs(mx):
        out = []
        for (a, b, c) in (((40, 52), (12, 40), (4, 56)), ((36, 74), (8, 76), (2, 96)), ((42, 96), (16, 108), (8, 124))):
            pts = [(a[0], a[1]), (b[0], b[1]), (c[0], c[1])]
            if mx:
                pts = [(150 - x, y) for x, y in pts]
            out.append("M" + "L".join(f"{n(x)} {n(y)}" for x, y in pts))
        return "".join(out)

    return f"""<g id="sp-beetle">
<path d="{legs(False)}{legs(True)}" fill="none" stroke="#102A22" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M68 14L56 2M82 14L94 2" stroke="#102A22" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="75" cy="82" rx="42" ry="46" fill="url(#gBeetle)" stroke="#06302A" stroke-width="2.4"/>
<path d="M75 40V128" stroke="#06302A" stroke-width="2"/>
<ellipse cx="75" cy="36" rx="29" ry="14" fill="#12684A" stroke="#06302A" stroke-width="2.2"/>
<ellipse cx="75" cy="20" rx="15" ry="10" fill="#0B3B2E" stroke="#06302A" stroke-width="2"/>
<ellipse cx="58" cy="70" rx="12" ry="22" fill="#fff" opacity=".32" transform="rotate(14 58 70)"/>
</g>"""


def fern():
    def stem(t):
        x = (1 - t) ** 2 * 54 + 2 * (1 - t) * t * 40 + t * t * 72
        y = 196 - 188 * t
        return x, y

    parts = []
    for i in range(1, 17):
        t = i / 17
        x, y = stem(t)
        x2, y2 = stem(min(1, t + 0.02))
        ang = math.degrees(math.atan2(y2 - y, x2 - x))
        ln = 40 * (1 - t) ** 0.7 + 6
        for s in (-1, 1):
            a = ang + s * 62
            parts.append(
                f'<ellipse cx="{n(ln / 2)}" cy="0" rx="{n(ln / 2)}" ry="{n(max(2.6, ln * .2))}" fill="url(#gLeaf)" stroke="#2F7A3A" stroke-width="1" '
                f'transform="translate({n(x)} {n(y)}) rotate({n(a)})"/>'
            )
    pts = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in [stem(i / 30) for i in range(31)])
    return f'<g id="sp-fern"><path d="{pts}" fill="none" stroke="#2E6B34" stroke-width="3.4" stroke-linecap="round"/>' + "".join(parts) + "</g>"


def starfish():
    cx, cy = 70, 72
    pts = []
    for i in range(10):
        r = 62 if i % 2 == 0 else 25
        a = math.radians(-90 + i * 36)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d = "M" + "L".join(f"{n(x)} {n(y)}" for x, y in pts) + "Z"
    dots = []
    for i in range(5):
        a = math.radians(-90 + i * 72)
        for k in range(1, 6):
            r = 8 + k * 9
            dots.append(f'<circle cx="{n(cx + r * math.cos(a))}" cy="{n(cy + r * math.sin(a))}" r="{n(2.8 - k * .3)}" fill="#FFE3C8" stroke="#B8441F" stroke-width=".6"/>')
        dots.append(f'<path d="M{cx} {cy}L{n(cx + 56 * math.cos(a))} {n(cy + 56 * math.sin(a))}" stroke="#B8441F" stroke-width="1.2" opacity=".5"/>')
    return f"""<g id="sp-starfish">
<path d="{d}" fill="url(#gStar)" stroke="#C8512B" stroke-width="9" stroke-linejoin="round"/>
<path d="{d}" fill="url(#gStar)" stroke="#9A3A1C" stroke-width="1.6" stroke-linejoin="round"/>
{''.join(dots)}
<circle cx="{cx}" cy="{cy}" r="7" fill="#FFE3C8" stroke="#9A3A1C" stroke-width="1.2"/>
</g>"""


EXTRA_DEFS += """
<linearGradient id="gRed" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F27A62"/><stop offset=".12" stop-color="#E4513A"/><stop offset=".7" stop-color="#C23C28"/><stop offset="1" stop-color="#8E2616"/></linearGradient>
<linearGradient id="gRedTop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F58B74"/><stop offset="1" stop-color="#C23C28"/></linearGradient>
<radialGradient id="gSea" cx=".38" cy=".32" r=".85"><stop offset="0" stop-color="#B4EDD0"/><stop offset=".55" stop-color="#3FBF84"/><stop offset="1" stop-color="#15703F"/></radialGradient>
<linearGradient id="gSand" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBEFC0"/><stop offset="1" stop-color="#D4A650"/></linearGradient>
"""


def mainframe():
    cols = ["#34B25A", "#FFC93C", "#FFFFFF", "#34B25A", "#FFC93C", "#34B25A", "#FFFFFF", "#34B25A", "#FFC93C", "#34B25A", "#FFFFFF", "#34B25A"]
    lamps = "".join(
        f'<circle cx="{n(38 + i * 13.2)}" cy="150" r="4.4" fill="{c}" stroke="#5E140E" stroke-width="1"/>'
        f'<circle cx="{n(37 + i * 13.2)}" cy="148.6" r="1.3" fill="#fff" opacity=".75"/>'
        for i, c in enumerate(cols)
    )

    def reel(cx, cy):
        holes = "".join(
            f'<circle cx="{n(cx + 13 * math.cos(math.radians(a)))}" cy="{n(cy + 13 * math.sin(math.radians(a)))}" r="4.6" fill="#10151C"/>'
            for a in (-90, 30, 150)
        )
        return (f'<circle cx="{cx}" cy="{cy}" r="29" fill="#3A2A20" stroke="#14100C" stroke-width="1.5"/>'
                f'<circle cx="{cx}" cy="{cy}" r="21" fill="url(#gSteel)" stroke="#2C3239" stroke-width="1.5"/>'
                f'{holes}<circle cx="{cx}" cy="{cy}" r="5.5" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1"/>')

    return f"""<g id="sp-mainframe">
<rect x="22" y="212" width="176" height="14" rx="3" fill="url(#gSteelDark)" stroke="#14181D" stroke-width="1.2"/>
<rect x="32" y="226" width="22" height="7" rx="2" fill="#2C3239"/><rect x="166" y="226" width="22" height="7" rx="2" fill="#2C3239"/>
<rect x="10" y="24" width="200" height="190" rx="10" fill="url(#gRed)" stroke="#5E140E" stroke-width="2"/>
<rect x="4" y="6" width="212" height="24" rx="7" fill="url(#gRedTop)" stroke="#5E140E" stroke-width="2"/>
<path d="M18 17H202" stroke="url(#gBrassV)" stroke-width="3" stroke-linecap="round"/>
<rect x="28" y="42" width="164" height="84" rx="9" fill="#10151C" stroke="#4A0F09" stroke-width="2.5"/>
{reel(74, 84)}{reel(146, 84)}
<path d="M74 55L110 68L146 55M74 113L110 100L146 113" fill="none" stroke="#3A2A20" stroke-width="3" stroke-linejoin="round"/>
<circle cx="110" cy="69" r="5" fill="url(#gSteel)" stroke="#2C3239" stroke-width="1"/><circle cx="110" cy="99" r="5" fill="url(#gSteel)" stroke="#2C3239" stroke-width="1"/>
<path d="M34 48L120 48L96 120L34 120Z" fill="#fff" opacity=".07"/>
<rect x="24" y="136" width="172" height="30" rx="6" fill="#8E2616" stroke="#5E140E" stroke-width="1.5"/>
{lamps}
<rect x="24" y="172" width="172" height="3" fill="#8E2616" opacity=".6"/>
<path d="M110 178V210" stroke="#5E140E" stroke-width="2.2"/>
<rect x="100" y="190" width="5" height="14" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width=".8"/>
<rect x="115" y="190" width="5" height="14" rx="2" fill="url(#gBrassV)" stroke="#7B5218" stroke-width=".8"/>
<rect x="34" y="182" width="52" height="16" rx="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.2"/>
<path d="M42 188h36M42 193h22" stroke="#7B5218" stroke-width="2" opacity=".75"/>
<circle cx="174" cy="190" r="9" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.4"/><path d="M174 190L179 184" stroke="#5E3A10" stroke-width="2.2" stroke-linecap="round"/>
<path d="M14 40V200" stroke="#fff" stroke-width="3" opacity=".3" stroke-linecap="round"/>
</g>"""


def globe():
    import globe_data as gd
    return f"""<g id="sp-globe">
<defs><clipPath id="cpGlobe"><circle cx="110" cy="106" r="90"/></clipPath></defs>
<path d="M58 248C70 230 90 228 110 228C130 228 150 230 162 248Z" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.6" stroke-linejoin="round"/>
<rect x="100" y="200" width="20" height="32" rx="3" fill="url(#gBrass)" stroke="#7B5218" stroke-width="1.3"/>
<circle cx="110" cy="106" r="90" fill="url(#gSea)"/>
<g clip-path="url(#cpGlobe)">
<path d="{gd.GRAT}" fill="none" stroke="#fff" stroke-width="1" opacity=".32"/>
<path d="{gd.LAND}" fill="url(#gSand)" stroke="#8D5F1E" stroke-width="1" stroke-linejoin="round"/>
<path d="{gd.IDN}" fill="#F0BC4A" stroke="#8D5F1E" stroke-width="1.1" stroke-linejoin="round"/>
</g>
<circle cx="110" cy="106" r="90" fill="none" stroke="#0E5A32" stroke-width="2"/>
<ellipse cx="74" cy="52" rx="30" ry="13" fill="#fff" opacity=".15" transform="rotate(-32 78 58)"/>
<circle cx="110" cy="106" r="100" fill="none" stroke="url(#gBrass)" stroke-width="7"/>
<circle cx="110" cy="106" r="100" fill="none" stroke="#7B5218" stroke-width="1" opacity=".7"/>
<circle cx="110" cy="6" r="6" fill="url(#gBrassV)" stroke="#7B5218" stroke-width="1.2"/>
</g>"""


SIZES.update({
    "database": (120, 150), "telegraph": (200, 110), "spool": (130, 130), "hourglass": (110, 170),
    "scales": (190, 160), "vault": (156, 150), "trilobite": (196, 140), "feather": (222, 90),
    "telescope": (240, 110), "samara": (150, 110), "beetle": (150, 130), "fern": (120, 200),
    "starfish": (140, 140), "mainframe": (220, 236), "globe": (220, 250),
})

NEW = [mainframe, globe, database, telegraph, spool, hourglass, scales, vault,
       trilobite, feather, telescope, samara, beetle, fern, starfish]


ALL = [eye, prism, fan, magnifier, pencil, palette, typeblock, gears, key, padlock, abacus, watch, card, coins,
       ledger, neuron, plasma, crystal, molecule, butterfly, nautilus, tree, honey, world, compass,
       lens, ruler, brush, typeblock2, monitor, typeblock3, typeblock4, typeblock5, cursor, setsquare] + NEW


# new stages live in their own modules (they reuse n(), polar() and the gradients above)
import specimens_fn as _fn  # noqa: E402

import specimens_ar as _ar  # noqa: E402

EXTRA_DEFS += _fn.DEFS + _ar.DEFS
SIZES.update(_fn.SIZES)
SIZES.update(_ar.SIZES)
ALL = ALL + _fn.FUNCS + _ar.FUNCS

# Photographic replacements (img/<symbol>.webp). Remove a file to fall back to the SVG drawing.
import photos as _photos
PHOTOS = _photos.load(SIZES)
def _photo_fn(sym):
    w, h, uri = PHOTOS[sym]
    def f():
        return _photos.symbol(sym, w, h, uri)
    f.__name__ = sym
    return f
ALL = [(_photo_fn(f.__name__) if f.__name__ in PHOTOS else f) for f in ALL]
for _s, (_w, _h, _u) in PHOTOS.items():
    SIZES[_s] = (_w, _h)


def sprite():
    body = "".join(f() for f in ALL)
    return (
        '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">'
        f"<defs>{DEFS}{EXTRA_DEFS}{body}</defs></svg>"
    )
