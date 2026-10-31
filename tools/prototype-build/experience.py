"""Builds experience.html from structured CV data (data first, markup second)."""
import html, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "experience.html"

# (start y, m), (end y, m)
ROLES = [
  dict(n="V", short="Kredivo", stats=[('8+', 'services maintained across 3 squads'), ('20+', 'design system components'), ('80%+', 'unit test coverage'), ('50%', 'less Rive development time')], acc="fn", img="egg", ratio="496/900",
       title="Senior Fullstack Engineer", org="PT Finaccel Finance Indonesia (Kredivo)", place="Jakarta",
       span="August 2024 to now", dur="Over 2 years", a=(2024,8), b=(2026,10), kind="Full time",
       pts=["Maintain 8+ front end and back end services across 3 squads (Growth, B2B International, Biller) for 4 markets: Indonesia, Thailand, the Philippines and Vietnam.",
            "Started the company design system, a private npm package with 20+ components used by every fullstack project, and wrote its governance and contribution guide.",
            "Automated design system publishing with JumpCloud SSO, Bitbucket Pipelines and AWS CodeArtifact, cutting 50% of the manual work.",
            "Reached 80%+ unit test coverage with a functional programming convention and Functional Core, Imperative Shell architecture.",
            "Supervised 10+ large projects end to end. A standard animator-to-frontend contract cut Rive project development time by 50%.",
            "As a Fullstack Guild core member, set quality standards for 20+ projects, ran a session for 100+ engineers and wrote 6+ knowledge base documents and 4+ shared libraries."],
       tools="React, TypeScript, Go, Express, Emotion, Storybook, Rive, AWS CodeArtifact, GitHub Copilot, Claude Code"),
  dict(n="IV", short="Habilis", stats=[('4', 'products built'), ('6', 'third party integrations'), ('50%', 'less effort per feature change')], acc="srv", img="gears", ratio="1/1",
       title="Back End Engineer", org="PT Habilis Solutions Indonesia", place="Jakarta",
       span="August 2023 to January 2025", dur="About 1.5 years", a=(2023,8), b=(2025,1), kind="Part time",
       pts=["Built back end services for four products: an artist music royalty system, a B2B health consultation system, a micro e-commerce system and an online taxi service, with Node.js, TypeScript, Express and PostgreSQL.",
            "Integrated Stripe payments, Brevo email campaigns, Google Maps distance lookup, S3 file storage, Twilio SMS and WebSocket real-time updates.",
            "Designed maintainable, testable codebases around Functional Core, Imperative Shell and Clean Architecture, which reduced the effort of each feature change by 50%."],
       tools="Node.js, TypeScript, Express, PostgreSQL, Stripe, Twilio, WebSocket"),
  dict(n="III", short="Tokopedia", stats=[('80%+', 'unit test coverage'), ('25+', 'modules on clean architecture'), ('20+', 'services on one TypeScript config'), ('4th', 'place, GoTo DevCamp 2023')], acc="leaf", img="globe", ratio="656/900",
       title="Software Engineer, Web Platform & Back End", org="PT GoTo Gojek Tokopedia (Tokopedia)", place="Jakarta",
       span="July 2021 to August 2024", dur="About 3 years", a=(2021,7), b=(2024,8), kind="Full time",
       pts=["Built the TopAds Seller Dashboard front end, an ads platform dashboard that kept growing, with React, TypeScript, Emotion, Zustand and GraphQL.",
            "Built the TopAds Display Search back end in Go with NSQ, gRPC, PostgreSQL and ElasticSearch, with over 80% unit test coverage across both services.",
            "Introduced a clean architecture standard across 25+ modules.",
            "Standardized the TypeScript linter and configuration used by 20+ services across the company's front end.",
            "Contributed to the Tokopedia Academy mobile app in Flutter.",
            "Mentored a team of 3 fresh graduates to 4th place in the GoTo DevCamp 2023 hackathon."],
       tools="React, TypeScript, Go, GraphQL, gRPC, PostgreSQL, ElasticSearch, NSQ, Flutter, Jest"),
  dict(n="II", short="Livein.id", stats=[('7', 'engineers managed'), ('2 mo', 'to ship the MVP'), ('20%', 'less work effort')], acc="ai", img="compass", ratio="886/900",
       title="IT Division Manager", org="PT Kreasi Anak Dalam (Livein.id)", place="Jakarta",
       span="November 2020 to March 2021", dur="5 months", a=(2020,11), b=(2021,3), kind="Full time",
       pts=["Managed a team of 7 engineers building a tourist app for Android and iOS, with a PostgreSQL database, a Laravel dashboard and a Go back end.",
            "Shipped the MVP in under 2 months, including the admin dashboard, a Midtrans transaction system and Google Maps integration.",
            "Cut 20% of the work effort with a standardized code base built for unit testing and scalability."],
       tools="Go, PostgreSQL, Laravel, Android, iOS"),
  dict(n="I", short="Procura", stats=[('20+', 'clients served'), ('10+', 'React and TypeScript modules'), ('5+', 'Ruby on Rails tasks')], acc="ui", img="monitor", ratio="1/1",
       title="Front End Engineer", org="PT Virkea Empresa Sistema (Procura)", place="Jakarta",
       span="July 2019 to December 2020", dur="1.5 years", a=(2019,7), b=(2020,12), kind="Full time",
       pts=["Developed a procurement system, a core ERP component, for 20+ clients, including large businesses, national companies and multinational corporations, with AngularJS and CoffeeScript.",
            "Contributed to 10+ modules of the React and TypeScript procurement 2.0 research, to ship a more maintainable and standardized product.",
            "Contributed to 5+ back end tasks in Ruby on Rails."],
       tools="AngularJS, CoffeeScript, React, TypeScript, Ruby on Rails"),
]
START, END = (2019,7), (2026,11)
mi = lambda ym: ym[0]*12 + ym[1]-1
T0, T1 = mi(START), mi(END)
pct = lambda ym: (mi(ym)-T0)/(T1-T0)*100

def lane(r):
    left = pct(r["a"]); right = pct((r["b"][0], r["b"][1]+1) if r["b"][1] < 12 else (r["b"][0]+1,1))
    return (f'<li class="lane" style="--a:var(--{r["acc"]})">'
            f'<a class="lane__label" href="#plate-{r["n"]}">{html.escape(r["short"])}</a>'
            f'<span class="lane__track"><span class="lane__bar" style="left:{left:.2f}%;width:{right-left:.2f}%"></span></span></li>')

ticks = "".join(f'<span class="tick" style="left:{pct((y,1)):.2f}%">{y}</span>' for y in range(2020,2027))

def plate(r):
    pts = "".join(f"<li>{html.escape(p)}</li>" for p in r["pts"])
    return f'''
    <article class="plate" id="plate-{r["n"]}" style="--a:var(--{r["acc"]})">
      <figure class="plate__fig"><img src="img/{r["img"]}.webp" alt="" style="aspect-ratio:{r["ratio"]}" loading="lazy"></figure>
      <div class="plate__body">
        <p class="plate__no">Plate {r["n"]} <span>{html.escape(r["kind"])}</span></p>
        <h3>{html.escape(r["title"])}</h3>
        <p class="plate__org">{html.escape(r["org"])}, {html.escape(r["place"])}</p>
        <p class="plate__when"><time>{html.escape(r["span"])}</time><span class="dot"></span>{html.escape(r["dur"])}</p>
        <ul class="plate__pts">{pts}</ul>
        <p class="plate__tools"><b>Tools</b> {html.escape(r["tools"])}</p>
      </div>
    </article>'''

page = f'''<title>Experience Plates</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400..900&family=EB+Garamond:ital,wght@0,400..700;1,400..600&display=swap" rel="stylesheet">
<style>
/* Concept: the hero's encyclopedia plates continue below the fold. Each job is a numbered plate with its own specimen photo and plate colour; a strata ribbon on top shows how the jobs overlapped. */
:root {{
  --paper: #ffffff; --ink: #11161d; --mute: #5b6470; --rule: #dfe3e8; --mast: #11161d; --mast-ink: #ffffff;
  --ui: #2f8cff; --srv: #e4513a; --ai: #e0a800; --fn: #8b5cf6; --ar: #d8409d; --leaf: #2fae6a;
  --font-caps: "Cinzel", "Trajan Pro", Georgia, serif; --font-text: "EB Garamond", Georgia, "Times New Roman", serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --paper: #0f1319; --ink: #eceae4; --mute: #98a1ad; --rule: #263039; --mast: #070a0e; --mast-ink: #ffffff;
  --ui: #5aa5ff; --srv: #f0705b; --ai: #f3c13a; --fn: #a88bfa; --ar: #e873b8; --leaf: #4cc98a; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --paper: #0f1319; --ink: #eceae4; --mute: #98a1ad; --rule: #263039; --mast: #070a0e; --mast-ink: #ffffff;
  --ui: #5aa5ff; --srv: #f0705b; --ai: #f3c13a; --fn: #a88bfa; --ar: #e873b8; --leaf: #4cc98a; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink); font: 400 1.2rem/1.55 var(--font-text); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; }}
:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 3px; }}
.wrap {{ width: min(100%, 72rem); margin-inline: auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}

.mast {{ background: var(--mast); color: var(--mast-ink); font-family: var(--font-caps); }}
.mast .wrap {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding-block: 0.8rem; }}
.mast__name {{ margin: 0; font-size: clamp(1.05rem, 2.7vw, 1.7rem); letter-spacing: 0.05em; text-transform: uppercase; }}
.mast__name b {{ font-weight: 900; }} .mast__name span {{ font-weight: 400; margin-left: 0.4em; }}
.hire {{ border: 1px solid rgba(255,255,255,.85); padding: 0.55em 1.1em; font-size: clamp(0.62rem, 1.5vw, 0.95rem); font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none; color: inherit; line-height: 1; transition: background-color .2s, color .2s; }}
.hire:hover {{ background: #fff; color: #11161d; }}
.band {{ height: 0.5rem; background: linear-gradient(90deg, var(--ui) 0 16.667%, var(--srv) 16.667% 33.333%, var(--ai) 33.333% 50%, var(--fn) 50% 66.667%, var(--ar) 66.667% 83.333%, var(--leaf) 83.333% 100%); }}

.eyebrow {{ margin: 0; font: 600 0.8rem/1.2 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--mute); }}
.intro {{ padding-block: clamp(2.5rem, 7vw, 5rem) 1.5rem; display: grid; gap: 1rem; }}
.intro h1 {{ margin: 0; font: 500 clamp(2.4rem, 8vw, 5.2rem)/0.98 var(--font-caps); letter-spacing: 0.01em; text-wrap: balance; }}
.intro p.lead {{ margin: 0; max-width: 40rem; font-size: clamp(1.15rem, 2.4vw, 1.4rem); color: var(--mute); }}

.strata {{ padding-block: 1.5rem 3rem; }}
.strata__lanes {{ list-style: none; margin: 0.9rem 0 0; padding: 0; display: grid; gap: 0.55rem; position: relative; }}
.lane {{ display: grid; grid-template-columns: 7.5rem 1fr; align-items: center; gap: 0.9rem; }}
.lane__label {{ font: 600 0.78rem/1.2 var(--font-caps); letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none; color: var(--ink); }}
.lane__label:hover {{ color: var(--a); }}
.lane__track {{ position: relative; height: 0.9rem; border-bottom: 1px solid var(--rule); }}
.lane__bar {{ position: absolute; top: 0; height: 0.9rem; background: var(--a); border-radius: 1px; min-width: 3px; }}
.axis {{ position: relative; height: 1.4rem; margin-left: 8.4rem; margin-top: 0.4rem; }}
.tick {{ position: absolute; transform: translateX(-50%); font: 500 0.78rem/1 var(--font-caps); letter-spacing: 0.1em; color: var(--mute); font-variant-numeric: tabular-nums; }}
.tick::before {{ content: ""; position: absolute; left: 50%; bottom: 100%; height: 0.5rem; border-left: 1px solid var(--rule); margin-bottom: 0.1rem; }}
.strata__note {{ margin: 0.8rem 0 0; font-size: 1rem; color: var(--mute); font-style: italic; }}

.plates {{ display: grid; gap: clamp(2.5rem, 6vw, 4.5rem); padding-block: 1rem 4rem; }}
.plate {{ display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: clamp(1.5rem, 4vw, 3.5rem); align-items: start; border-top: 3px solid var(--a); padding-top: 1.5rem; scroll-margin-top: 1rem; }}
.plate__fig {{ margin: 0; display: grid; place-items: center; min-height: 14rem; padding: 1rem; }}
.plate__fig img {{ display: block; width: auto; max-width: min(100%, 22rem); max-height: 24rem; height: auto; filter: drop-shadow(0.25rem 0.55rem 0.5rem rgba(10,14,20,0.28)); }}
.plate__no {{ margin: 0 0 0.6rem; display: flex; flex-wrap: wrap; gap: 0.4rem 1rem; align-items: baseline; font: 700 0.85rem/1 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--a); }}
.plate__no span {{ font: italic 400 1rem/1 var(--font-text); letter-spacing: 0; text-transform: none; color: var(--mute); }}
.plate h3 {{ margin: 0; font: 500 clamp(1.5rem, 3.4vw, 2.3rem)/1.1 var(--font-caps); text-wrap: balance; }}
.plate__org {{ margin: 0.5rem 0 0; font-size: 1.3rem; font-weight: 500; }}
.plate__when {{ margin: 0.2rem 0 0; display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap; color: var(--mute); font-size: 1.05rem; }}
.dot {{ width: 0.28rem; height: 0.28rem; border-radius: 50%; background: var(--a); }}
.plate__pts {{ margin: 1.1rem 0 0; padding: 0; list-style: none; display: grid; gap: 0.6rem; max-width: 42rem; }}
.plate__pts li {{ position: relative; padding-left: 1.3rem; }}
.plate__pts li::before {{ content: ""; position: absolute; left: 0; top: 0.72em; width: 0.6rem; border-top: 2px solid var(--a); }}
.plate__tools {{ margin: 1.1rem 0 0; font-size: 1rem; color: var(--mute); max-width: 42rem; }}
.plate__tools b {{ margin-right: 0.6rem; font: 700 0.72rem/1 var(--font-caps); letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink); }}

.foot {{ border-top: 1px solid var(--rule); padding-block: 2.5rem 4rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr)); gap: 2rem 3rem; }}
.foot h2 {{ margin: 0 0 0.7rem; font: 600 0.8rem/1.2 var(--font-caps); letter-spacing: 0.22em; text-transform: uppercase; color: var(--mute); }}
.foot p {{ margin: 0 0 0.4rem; min-width: 0; overflow-wrap: anywhere; }}
.foot .big {{ font: 500 1.35rem/1.25 var(--font-caps); }}
.copy {{ margin-top: 0.6rem; font: 600 0.78rem/1 var(--font-caps); letter-spacing: 0.14em; text-transform: uppercase; padding: 0.7em 1.1em; background: transparent; color: var(--ink); border: 1px solid var(--ink); cursor: pointer; }}
.copy:hover {{ background: var(--ink); color: var(--paper); }}
.email {{ user-select: all; font-size: 1.25rem; }}

@media (max-width: 760px) {{
  .plate {{ grid-template-columns: minmax(0, 1fr); }}
  .plate__fig {{ min-height: 0; justify-items: start; padding: 0.5rem 0; }}
  .plate__fig img {{ max-height: 12rem; max-width: 14rem; }}
  .lane {{ grid-template-columns: 1fr; gap: 0.25rem; }}
  .axis {{ margin-left: 0; }}
  .strata__lanes {{ gap: 0.8rem; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>

<header class="mast"><div class="wrap">
  <p class="mast__name"><b>Deta</b><span>Aditya</span></p>
  <a class="hire" href="#contact">Hire me &rarr;</a>
</div></header>
<div class="band" aria-hidden="true"></div>

<main>
  <section class="wrap intro">
    <p class="eyebrow">Experience</p>
    <h1>Seven years, five plates</h1>
    <p class="lead">Front end, back end and everything between, from end users to C-level stakeholders. Newest plate first.</p>
  </section>

  <section class="wrap strata" aria-label="Timeline of roles">
    <p class="eyebrow">Strata, July 2019 to September 2024</p>
    <ol class="strata__lanes">{"".join(lane(r) for r in ROLES)}</ol>
    <div class="axis" aria-hidden="true">{ticks}</div>
    <p class="strata__note">Habilis and Digyata ran alongside the Tokopedia role.</p>
  </section>

  <section class="wrap plates" aria-label="Roles">{"".join(plate(r) for r in ROLES)}
  </section>

  <section class="wrap" id="contact"><div class="foot">
    <div><h2>Education</h2><p class="big">Universitas Pertamina</p><p>Bachelor of Computer Science, 2016 to 2021, GPA 3.68</p></div>
    <div><h2>Toolkit</h2><p>TypeScript, React, Next.js, Node.js, Go, PostgreSQL, GraphQL, gRPC. Also C#, F#, PHP, Ruby on Rails, Flutter and Elm. Clean Architecture, Domain Driven Design, Functional Programming, Test Driven Development.</p></div>
    <div><h2>Contact</h2>
      <p class="email" id="mail">muhammaddetaaditya@gmail.com</p>
      <p>Jakarta, Indonesia</p>
      <p><a href="https://www.linkedin.com/in/deta-aditya">LinkedIn</a> &nbsp; <a href="https://github.com/deta-aditya">GitHub</a></p>
      <button class="copy" id="copy" type="button">Copy email</button>
    </div>
  </div></section>
</main>
<script>
document.getElementById("copy").addEventListener("click", async (e) => {{
  const t = document.getElementById("mail"), b = e.currentTarget;
  try {{ await navigator.clipboard.writeText(t.textContent); }}
  catch (_) {{ const r = document.createRange(); r.selectNodeContents(t); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }}
  b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy email"), 1600);
}});
</script>
'''
OUT.write_text(page)
print("wrote", OUT, len(page))
