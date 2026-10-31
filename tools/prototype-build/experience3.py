"""One-screen Experience page, selector left / content right, no specimens."""
import json, html, pathlib
import experience as E
OUT = pathlib.Path(__file__).resolve().parent.parent / "experience.html"
R = E.ROLES
def seg(r):
    left = E.pct(r["a"]); right = E.pct((r["b"][0], r["b"][1]+1) if r["b"][1] < 12 else (r["b"][0]+1, 1))
    return left, right-left
def yrs(r):
    return f'{r["a"][0]} to ' + ("now" if r["b"][0] >= 2026 else str(r["b"][0]))
def role_btn(i, r):
    return (f'<li><button type="button" class="role" data-i="{i}" style="--a:var(--{r["acc"]})" aria-pressed="false">'
            f'<span class="role__org">{html.escape(r["short"])}</span>'
            f'<span class="role__when">{yrs(r)}</span>'
            f'<span class="role__track" aria-hidden="true"><span class="role__bar" style="left:{seg(r)[0]:.2f}%;width:{seg(r)[1]:.2f}%"></span></span>'
            f'</button></li>')
years = "".join(f'<span class="tick" style="left:{E.pct((y,1)):.2f}%">{str(y)[2:]}</span>' for y in range(2020,2027))
data = [dict(acc=r["acc"], title=r["title"], org=r["org"], place=r["place"], span=r["span"], dur=r["dur"], kind=r["kind"], pts=r["pts"], tools=r["tools"], stats=r["stats"]) for r in R]

page = f'''<title>Experience Plates</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400..900&family=EB+Garamond:ital,wght@0,400..700;1,400..600&display=swap" rel="stylesheet">
<style>
/* Concept: role selector on the left (each role carries a mini strata bar), the selected role on the right. One screen on desktop, a short scroll on phones. */
:root {{
  --paper: #ffffff; --ink: #11161d; --mute: #5b6470; --rule: #dfe3e8; --mast: #11161d; --sel: #f4f6f8;
  --ui: #2f8cff; --srv: #e4513a; --ai: #e0a800; --fn: #8b5cf6; --ar: #d8409d; --leaf: #2fae6a;
  --pop: #ffffff; --pop-line: #11161d;
  --font-caps: "Cinzel", "Trajan Pro", Georgia, serif; --font-text: "EB Garamond", Georgia, "Times New Roman", serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --paper: #0f1319; --ink: #eceae4; --mute: #98a1ad; --rule: #263039; --mast: #070a0e; --sel: #18202a; --pop: #161c24; --pop-line: #eceae4;
  --ui: #5aa5ff; --srv: #f0705b; --ai: #f3c13a; --fn: #a88bfa; --ar: #e873b8; --leaf: #4cc98a; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --paper: #0f1319; --ink: #eceae4; --mute: #98a1ad; --rule: #263039; --mast: #070a0e; --sel: #18202a; --pop: #161c24; --pop-line: #eceae4;
  --ui: #5aa5ff; --srv: #f0705b; --ai: #f3c13a; --fn: #a88bfa; --ar: #e873b8; --leaf: #4cc98a; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
html, body {{ height: 100%; }}
body {{ margin: 0; background: var(--paper); color: var(--ink); font: 400 clamp(1.05rem, 1.55vh + 0.35rem, 1.3rem)/1.5 var(--font-text); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; }} button {{ font: inherit; color: inherit; }}
:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 3px; }}
.gutter {{ padding-left: max(clamp(1rem, 4vw, 3.5rem), env(safe-area-inset-left, 0px)); padding-right: max(clamp(1rem, 4vw, 3.5rem), env(safe-area-inset-right, 0px)); }}
.app {{ min-height: 100%; display: grid; grid-template-rows: auto 1fr; }}

.mast {{ background: var(--mast); color: #fff; font-family: var(--font-caps); position: relative; z-index: 5; }}
.mast__in {{ display: flex; align-items: center; gap: 1.5rem; padding-block: 0.7rem; }}
.mast__name {{ margin: 0; font-size: clamp(1.05rem, 2.4vw, 1.6rem); letter-spacing: 0.05em; text-transform: uppercase; white-space: nowrap; }}
.mast__name b {{ font-weight: 900; }} .mast__name span {{ font-weight: 400; margin-left: 0.4em; }}
.nav {{ display: flex; gap: clamp(1rem, 2.4vw, 2.2rem); margin-inline: auto; overflow-x: auto; scrollbar-width: none; }}
.nav a {{ font-size: clamp(0.62rem, 1.1vw, 0.85rem); font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; text-decoration: none; color: rgba(255,255,255,.7); padding-block: 0.4rem; border-bottom: 2px solid transparent; white-space: nowrap; }}
.nav a:hover {{ color: #fff; }}
.nav a[aria-current="page"] {{ color: #fff; border-bottom-color: var(--a, #fff); }}
.nav a[aria-disabled="true"] {{ opacity: 0.45; cursor: default; }}
.hirewrap {{ position: relative; }}
.hire {{ background: transparent; border: 1px solid rgba(255,255,255,.85); padding: 0.55em 1.1em; font: 600 clamp(0.62rem, 1.3vw, 0.9rem)/1 var(--font-caps); letter-spacing: 0.12em; text-transform: uppercase; color: #fff; cursor: pointer; transition: background-color .2s, color .2s; white-space: nowrap; }}
.hire:hover, .hire[aria-expanded="true"] {{ background: #fff; color: #11161d; }}
.pop {{ position: absolute; right: 0; top: calc(100% + 0.7rem); width: min(22rem, calc(100vw - 32px)); background: var(--pop); color: var(--ink); border: 1px solid var(--pop-line); padding: 1.1rem 1.2rem 1.2rem; font-family: var(--font-text); box-shadow: 0 0.8rem 2rem rgba(0,0,0,.25); }}
.pop h2 {{ margin: 0 0 0.6rem; font: 600 0.75rem/1.2 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--mute); }}
.pop p {{ margin: 0 0 0.4rem; overflow-wrap: anywhere; }}
.pop .email {{ font-size: 1.2rem; user-select: all; }}
.pop__row {{ display: flex; align-items: center; gap: 1rem; margin-top: 0.8rem; flex-wrap: wrap; }}
.copy {{ font: 600 0.72rem/1 var(--font-caps); letter-spacing: 0.14em; text-transform: uppercase; padding: 0.7em 1.1em; background: transparent; border: 1px solid var(--ink); cursor: pointer; }}
.copy:hover {{ background: var(--ink); color: var(--paper); }}
.band {{ height: 0.5rem; background: linear-gradient(90deg, var(--ui) 0 16.667%, var(--srv) 16.667% 33.333%, var(--ai) 33.333% 50%, var(--fn) 50% 66.667%, var(--ar) 66.667% 83.333%, var(--leaf) 83.333% 100%); }}

.eyebrow {{ margin: 0; font: 600 0.74rem/1.2 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--mute); }}
.main {{ min-height: 0; display: grid; grid-template-columns: clamp(13rem, 20vw, 19rem) minmax(0, 1fr); gap: clamp(1.5rem, 4vw, 4rem); padding-block: clamp(1rem, 3vh, 2.2rem); }}

.side {{ min-height: 0; display: flex; flex-direction: column; gap: 1rem; }}
.side h1 {{ margin: 0; font: 500 clamp(1.5rem, 3.6vh + 0.5rem, 2.4rem)/1 var(--font-caps); }}
.roles {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 0.2rem; min-height: 0; overflow-y: auto; }}
.role {{ width: 100%; display: grid; gap: 0.1rem; text-align: left; padding: 0.7rem 0.8rem 0.8rem 0.9rem; background: none; border: 0; border-left: 4px solid transparent; cursor: pointer; transition: background-color .15s, border-color .15s; }}
.role:hover {{ background: var(--sel); }}
.role[aria-pressed="true"] {{ background: var(--sel); border-left-color: var(--a); }}
.role__org {{ font: 700 0.9rem/1.2 var(--font-caps); letter-spacing: 0.14em; text-transform: uppercase; }}
.role[aria-pressed="true"] .role__org {{ color: var(--a); }}
.role__track {{ position: relative; display: block; height: 0.45rem; margin-top: 0.5rem; background: var(--rule); }}
.role__bar {{ position: absolute; top: 0; bottom: 0; background: var(--a); opacity: 0.55; min-width: 4px; transition: opacity .15s; }}
.role:hover .role__bar, .role[aria-pressed="true"] .role__bar {{ opacity: 1; }}
.role__when {{ font-size: 0.9em; color: var(--mute); line-height: 1.25; }}
.detail {{ min-height: 0; min-width: 0; overflow-y: auto; padding-right: 0.5rem; transition: opacity .22s, transform .22s; }}
.swap .detail {{ opacity: 0; transform: translateY(0.4rem); }}
.detail__kind {{ margin: 0 0 0.6rem; display: flex; flex-wrap: wrap; gap: 0.3rem 1rem; align-items: baseline; font: 700 0.82rem/1 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--a); }}
.detail__kind span {{ font: italic 400 1rem/1 var(--font-text); letter-spacing: 0; text-transform: none; color: var(--mute); }}
.detail h2 {{ margin: 0; font: 500 clamp(1.7rem, 4.2vh + 0.7rem, 3rem)/1.08 var(--font-caps); text-wrap: balance; border-bottom: 3px solid var(--a); padding-bottom: 0.7rem; }}
.detail__org {{ margin: 0.8rem 0 0; font-size: 1.2em; font-weight: 500; }}
.detail__when {{ margin: 0.15rem 0 0; display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; color: var(--mute); font-size: 0.95em; }}
.dot {{ width: 0.28rem; height: 0.28rem; border-radius: 50%; background: var(--a); }}
.detail__pts {{ margin: 1.1rem 0 0; padding: 0; list-style: none; display: grid; gap: 0.6rem; max-width: 56rem; }}
.detail__pts li {{ position: relative; padding-left: 1.4rem; }}
.detail__pts li::before {{ content: ""; position: absolute; left: 0; top: 0.72em; width: 0.65rem; border-top: 2px solid var(--a); }}
.cvlink {{ margin-top: 0.9rem; display: flex; width: 100%; box-sizing: border-box; justify-content: center; align-items: center; gap: 0.5em; padding: 0.75em 1em; border: 2px solid var(--ink); color: var(--ink); text-decoration: none; font: 700 0.8rem/1 var(--font-caps); letter-spacing: 0.14em; text-transform: uppercase; transition: background-color .15s, color .15s; }}
.cvlink:hover, .cvlink:focus-visible {{ background: var(--ink); color: var(--paper); }}
.cvlink--pop {{ margin-top: 0.8rem; display: flex; border-width: 1px; }}
.detail {{ display: flex; flex-direction: column; }}
.stats {{ list-style: none; margin: auto 0 0; padding: 1.1rem 0 0.3rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(9.5rem, 1fr)); gap: 1rem 2rem; max-width: 56rem; }}
.stats li {{ display: grid; gap: 0.15rem; border-top: 1px solid var(--rule); padding-top: 0.7rem; }}
.stats b {{ font: 500 clamp(1.7rem, 4vh + 0.5rem, 2.6rem)/1 var(--font-caps); color: var(--a); }}
.stats span {{ font-size: 0.85em; line-height: 1.25; color: var(--mute); }}
.detail.compact .stats {{ display: none; }}
.detail.tight {{ font-size: 0.92em; }} .detail.tight .detail__pts {{ gap: 0.35rem; margin-top: 0.7rem; }}
.detail__tools {{ margin: 1rem 0 0; font-size: 0.9em; color: var(--mute); max-width: 56rem; }}
.detail__tools b {{ margin-right: 0.6rem; font: 700 0.68rem/1 var(--font-caps); letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink); }}

@media (min-width: 900px) and (min-height: 540px) {{ .app {{ height: 100%; overflow: hidden; }} }}
@media (max-width: 899px), (max-height: 539px) {{
  .mast__in {{ flex-wrap: wrap; row-gap: 0.4rem; }}
  .nav {{ order: 3; flex-basis: 100%; margin: 0; }}
  .hirewrap {{ margin-left: auto; }}
  .main {{ grid-template-columns: minmax(0, 1fr); gap: 1.2rem; }}
  .roles {{ display: flex; flex-wrap: wrap; overflow: visible; gap: 0.4rem; }}
  .roles li {{ flex: 1 1 6.4rem; min-width: 0; }}
  .roles li {{ display: flex; }}
  .role {{ align-content: start; padding: 0.6rem 0.6rem 0.7rem 0.7rem; }}
  .role__org {{ font-size: 0.78rem; letter-spacing: 0.1em; }}
    .detail {{ overflow: visible; }}
  .stats {{ margin-top: 1.2rem; }}
  .detail h2 {{ font-size: 1.9rem; }}
  .side, .roles {{ min-height: auto; flex: none; height: auto; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>

<div class="app">
<header class="mast"><div class="gutter"><div class="mast__in">
  <p class="mast__name"><b>Deta</b><span>Aditya</span></p>
  <nav class="nav" aria-label="Pages">
    <a href="https://claude.ai/artifact/WuoNf6obKc4WS2SLUqginh">Home</a>
    <a href="#experience" aria-current="page">Experience</a>
    <a href="#projects" aria-disabled="true" title="Coming soon">Projects</a>
    <a href="#writing" aria-disabled="true" title="Coming soon">Writing</a>
  </nav>
  <div class="hirewrap">
    <button class="hire" id="hire" type="button" aria-expanded="false" aria-controls="pop">Hire me &rarr;</button>
    <div class="pop" id="pop" hidden>
      <h2>Contact</h2>
      <p class="email" id="mail">muhammaddetaaditya@gmail.com</p>
      <p>Jakarta, Indonesia</p>
      <div class="pop__row"><button class="copy" id="copy" type="button">Copy email</button>
        <a href="https://www.linkedin.com/in/deta-aditya">LinkedIn</a><a href="https://github.com/deta-aditya">GitHub</a></div>
      <a class="cvlink cvlink--pop" href="cv/Deta_Aditya_CV.pdf" download="Deta_Aditya_CV.pdf">Download CV (PDF)</a>
    </div>
  </div>
</div></div></header>

<main class="main gutter" id="experience">
  <aside class="side" aria-label="Roles">
    <div><h1>Experience</h1><p class="eyebrow" style="margin-top:0.5rem">July 2019 to now</p>
    <a class="cvlink" href="cv/Deta_Aditya_CV.pdf" download="Deta_Aditya_CV.pdf">Download full CV <span aria-hidden="true">&darr;</span></a></div>
    <ul class="roles">{"".join(role_btn(i, r) for i, r in enumerate(R))}</ul>
  </aside>
  <article class="detail-wrap" id="wrap" style="min-height:0;display:grid;grid-template-rows:minmax(0,1fr)" aria-live="polite">
    <div class="detail" id="detail">
      <p class="detail__kind" id="d-kind"></p>
      <h2 id="d-title"></h2>
      <p class="detail__org" id="d-org"></p>
      <p class="detail__when" id="d-when"></p>
      <ul class="detail__pts" id="d-pts"></ul>
      <p class="detail__tools" id="d-tools"></p>
      <ul class="stats" id="d-stats"></ul>
    </div>
  </article>
</main>
</div>
<script>
const DATA = {json.dumps(data, ensure_ascii=False)};
const $ = (id) => document.getElementById(id);
const btns = [...document.querySelectorAll(".role")];
const wrap = $("wrap");
const esc = (s) => s.replace(/[&<>]/g, (c) => ({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]));
let cur = -1;
function fit() {{
  const d = $("detail"); d.classList.remove("compact", "tight");
  if (matchMedia("(max-width: 899px), (max-height: 539px)").matches) return;
  if (d.scrollHeight > d.clientHeight) d.classList.add("compact");
  if (d.scrollHeight > d.clientHeight) d.classList.add("tight");
}}
addEventListener("resize", fit);
if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
addEventListener("load", fit);
function fill(i) {{
  const r = DATA[i];
  wrap.style.setProperty("--a", "var(--" + r.acc + ")");
  document.documentElement.style.setProperty("--a", "var(--" + r.acc + ")");
  $("d-kind").innerHTML = esc(r.kind);
  $("d-title").textContent = r.title;
  $("d-org").textContent = r.org + ", " + r.place;
  $("d-when").innerHTML = "<time>" + esc(r.span) + "</time><span class=dot></span>" + esc(r.dur);
  $("d-pts").innerHTML = r.pts.map((p) => "<li>" + esc(p) + "</li>").join("");
  $("d-tools").innerHTML = "<b>Tools</b>" + esc(r.tools);
  $("d-stats").innerHTML = r.stats.map((s) => "<li><b>" + esc(s[0]) + "</b><span>" + esc(s[1]) + "</span></li>").join("");
  fit();
  btns.forEach((l, k) => l.setAttribute("aria-pressed", String(k === i)));
  $("detail").scrollTop = 0;
}}
function select(i, instant) {{
  if (i < 0 || i >= DATA.length || i === cur) return;
  const first = cur < 0; cur = i;
  try {{ history.replaceState(null, "", "#experience-" + i); }} catch (_) {{}}
  if (first || instant || matchMedia("(prefers-reduced-motion: reduce)").matches) {{ fill(i); return; }}
  wrap.classList.add("swap");
  setTimeout(() => {{ fill(i); wrap.classList.remove("swap"); }}, 180);
}}
btns.forEach((l) => l.addEventListener("click", () => select(+l.dataset.i)));
addEventListener("keydown", (e) => {{
  if (e.key === "ArrowUp" || e.key === "ArrowLeft") {{ e.preventDefault(); select(cur - 1); }}
  if (e.key === "ArrowDown" || e.key === "ArrowRight") {{ e.preventDefault(); select(cur + 1); }}
}});
const m = /^#experience-(\\d+)$/.exec(location.hash);
select(m && +m[1] < DATA.length ? +m[1] : 0, true);

const hire = $("hire"), pop = $("pop");
function togglePop(open) {{ pop.hidden = !open; hire.setAttribute("aria-expanded", String(open)); }}
hire.addEventListener("click", () => togglePop(pop.hidden));
addEventListener("keydown", (e) => {{ if (e.key === "Escape") togglePop(false); }});
document.addEventListener("click", (e) => {{ if (!pop.hidden && !e.target.closest(".hirewrap")) togglePop(false); }});
$("copy").addEventListener("click", async (e) => {{
  const t = $("mail"), b = e.currentTarget;
  try {{ await navigator.clipboard.writeText(t.textContent); }}
  catch (_) {{ const r = document.createRange(); r.selectNodeContents(t); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }}
  b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy email"), 1600);
}});
</script>
'''
OUT.write_text(page)
print("wrote", OUT, len(page))
