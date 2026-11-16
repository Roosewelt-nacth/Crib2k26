import re, sys, html, datetime
sys.argv = ["pack.py", "x"]
import pack as P
import drawings_fix as DR
E = html.escape
base = datetime.date(2026, 11, 16)
wd = lambda k: (base + datetime.timedelta(days=k)).strftime("%d %b")

md = open(r"C:/Users/amduser2/AppData/Local/Claude-Data/claude_pzs8sxrjxfjjc/scratch-workspaces/4ad7ba32-c86f-4a39-9bac-b23909acc345/5f20155b-e0b2-450a-9469-eb64ffac141a/scratch-2026-11-05-2bf6fb/crib-2026-image-prompts.md", encoding="utf-8").read()
prompts = re.findall(r"## (Prompt \d[^\n]*)\n(?:.*?\n)*?```\n(.*?)```", md, re.S)
keyblock = re.search(r"Block-out key:.*?```", md, re.S).group(0).rstrip("`").strip()

CSS = """
:root{--bg:#f6f4ee;--panel:#fffdf8;--fg:#25242b;--mute:#5d5b66;--line:#d9d4c6;--accent:#8a5a12;--accent2:#2f5aa8;--warn:#a8322c;--warnbg:#fbeeeb;--ok:#3f6b3a;--sheet:#fffef9;--chip:#ece7d8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17171c;--panel:#202027;--fg:#ebe8df;--mute:#a4a1ad;--line:#3a3a45;--accent:#e0a64a;--accent2:#8fb2ff;--warn:#ff9a8f;--warnbg:#33201e;--ok:#8cc784;--chip:#2c2c36;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#17171c;--panel:#202027;--fg:#ebe8df;--mute:#a4a1ad;--line:#3a3a45;--accent:#e0a64a;--accent2:#8fb2ff;--warn:#ff9a8f;--warnbg:#33201e;--ok:#8cc784;--chip:#2c2c36;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 Inter,'Segoe UI',Arial,sans-serif;padding-block:0;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1,h2,h3{font-family:'Space Grotesk','Segoe UI',Arial,sans-serif;text-wrap:balance;margin:0}
.wrap{max-width:1180px;margin:0 auto}
header.top{padding:28px 0 12px}
header.top h1{font-size:clamp(28px,5vw,46px);letter-spacing:-.02em}
header.top p{margin:8px 0 0;color:var(--mute);max-width:70ch}
nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line);display:flex;gap:4px;overflow-x:auto;padding:8px 0}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
nav a{white-space:nowrap;padding:6px 12px;border-radius:999px;color:var(--fg);text-decoration:none;font-size:14px;background:var(--chip)}
nav a:hover,nav a:focus-visible{outline:2px solid var(--accent)}
section{padding:34px 0 8px;scroll-margin-top:56px}
section>h2{font-size:clamp(22px,3.4vw,30px);margin-bottom:6px}
.lead{color:var(--mute);max-width:75ch;margin:0 0 18px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:18px 0}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.stat b{display:block;font:600 24px 'Space Grotesk',sans-serif}
.stat span{color:var(--mute);font-size:13px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:18px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;min-width:0}
.card.warn{background:var(--warnbg);border-color:var(--warn)}
.card h3{font-size:17px;margin-bottom:6px}
.card.warn h3{color:var(--warn)}
ul,ol{margin:6px 0 0;padding-left:20px}li{margin-bottom:4px}
img.fig{width:100%;height:auto;display:block;border:1px solid var(--line);border-radius:6px;background:#fff}
figure{margin:0}figcaption{font-size:13px;color:var(--mute);margin-top:6px}
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--chip);font-weight:600}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr.tot td{font-weight:700;background:var(--chip)}
details{background:var(--panel);border:1px solid var(--line);border-radius:10px;margin-bottom:10px}
summary{cursor:pointer;padding:12px 16px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;list-style:none}
summary::-webkit-details-marker{display:none}
summary:focus-visible{outline:2px solid var(--accent)}
summary .t{font:600 18px 'Space Grotesk',sans-serif}
summary .m{color:var(--mute);font-size:13px;margin-left:auto}
summary::before{content:"+";font:600 20px 'Space Grotesk';width:18px;color:var(--accent)}
details[open]>summary::before{content:"–"}
.pb{padding:4px 16px 16px;display:grid;gap:16px;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr)}
@media(max-width:900px){.pb{grid-template-columns:minmax(0,1fr)}}
.draw{background:var(--sheet);border:1px solid var(--line);border-radius:6px;overflow-x:auto;margin-bottom:10px;color:#2b2a33}
.draw svg{display:block;width:100%;min-width:640px;height:auto}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px}
.chips span{background:var(--chip);border-radius:999px;padding:3px 10px;font-size:13px}
.bar{height:10px;border-radius:3px;background:var(--accent)}.bar.l{background:var(--ok)}
.gantt{display:grid;grid-template-columns:230px 1fr;gap:0 10px;font-size:13px;align-items:center}
.gantt .lab{padding:7px 0;border-bottom:1px solid var(--line)}
.gantt .trk{position:relative;height:100%;min-height:30px;border-bottom:1px solid var(--line)}
.gantt .gb{position:absolute;top:9px;height:12px;border-radius:4px;background:var(--accent)}
.gantt .hd{font-weight:600;color:var(--mute)}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:12px}
.steps li{counter-increment:s;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px 12px 54px;position:relative}
.steps li::before{content:counter(s);position:absolute;left:14px;top:10px;width:28px;height:28px;border-radius:50%;background:var(--accent);color:var(--bg);font:600 15px 'Space Grotesk';display:grid;place-items:center}
.steps li b{display:block}
.steps li .when{font-size:12.5px;color:var(--accent);font-weight:600}
.steps label{display:flex;gap:8px;align-items:center;font-size:13px;color:var(--mute);margin-top:6px}
pre{white-space:pre-wrap;background:var(--chip);border-radius:8px;padding:12px;font:13px/1.5 ui-monospace,Consolas,monospace;margin:8px 0;max-height:320px;overflow:auto}
button{font:inherit;background:var(--accent);color:var(--bg);border:0;border-radius:6px;padding:6px 12px;cursor:pointer}
button:focus-visible{outline:2px solid var(--fg)}
footer{padding:30px 0 40px;color:var(--mute);font-size:13px}
.theme{margin-left:auto;background:var(--chip);color:var(--fg)}
"""

# ---- parts
parts = ""
for m in P.MODS:
    svgs = getattr(DR, m["fn"])()
    rows = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td class='n'>{P.ind(p)}</td><td class='n'>{P.ind(c)}</td><td class='n'>{P.ind(d)}</td></tr>" for a, b, c, d, p in m["lines"])
    steps = "".join(f"<li>{E(s)}</li>" for s in m["steps"])
    d0, d1 = m["when"]
    parts += (f'<details id="part{m["id"]}"><summary><span class="t">Part {m["id"]} · {E(m["name"])}</span><span class="m">{P.fmt(m["prop"])} · {P.fmt(m["lean"])} · {P.fmt(m["full"])} · {m["days"]} person-days</span></summary>'
              f'<div class="pb"><div>{"".join(f"<div class=draw>{s}</div>" for s in svgs)}</div><div>'
              f'<div class="chips"><span>Items: {E(m["covers"])}</span><span>Scale: {E(m["zone"])}</span><span>Build {wd(d0)} → {wd(d1)}</span></div>'
              f'<div class="scroll"><table><tr><th>Item</th><th>Qty</th><th class="n">Prop-only ₹</th><th class="n">Lean ₹</th><th class="n">Full ₹</th></tr>{rows}<tr class="tot"><td colspan="2">Total</td><td class="n">{P.ind(m["prop"])}</td><td class="n">{P.ind(m["lean"])}</td><td class="n">{P.ind(m["full"])}</td></tr></table></div>'
              f'<h3 style="margin:14px 0 4px;font-size:15px">How to build it</h3><ol>{steps}</ol>'
              f'<div class="card warn" style="margin-top:12px"><h3>Check before cutting</h3>{E(m["check"])}</div></div></div></details>')

# ---- cost rows
mx = max(m["full"] for m in P.MODS)
crow = "".join(f'<tr><td>{m["id"]}</td><td>{E(m["name"])}</td><td class="n">{m["days"]}</td><td class="n">{P.ind(m["prop"])}</td><td class="n">{P.ind(m["lean"])}</td><td class="n">{P.ind(m["full"])}</td><td style="min-width:150px"><div class="bar l" style="width:{m["lean"]/mx*100:.0f}%"></div><div class="bar" style="width:{m["full"]/mx*100:.0f}%;margin-top:3px"></div></td></tr>' for m in P.MODS)
crow += "".join(f'<tr><td></td><td>{E(a)}</td><td></td><td class="n">{P.ind(p)}</td><td class="n">{P.ind(b)}</td><td class="n">{P.ind(c)}</td><td></td></tr>' for a, b, c, p in P.MISC)

# ---- gantt
N = 39.0
wkl = ["16–22 Nov", "23–29 Nov", "30 Nov–6 Dec", "7–13 Dec", "14–20 Dec", "21–24 Dec"]
g = '<div class="lab hd">Part</div><div class="trk hd" style="display:flex">' + "".join(f'<div style="flex:{w}">{a}</div>' for a, w in zip(wkl, (7, 7, 7, 7, 7, 4))) + "</div>"
for m in P.MODS:
    a, b = m["when"]
    g += f'<div class="lab">{m["id"]} · {E(m["name"])}</div><div class="trk"><div class="gb" style="left:{a/N*100:.1f}%;width:{(b-a)/N*100:.1f}%"></div></div>'
g += f'<div class="lab" style="color:var(--warn)">Install in church (14–17 Dec)</div><div class="trk"><div class="gb" style="background:var(--warn);left:{28/N*100:.1f}%;width:{4/N*100:.1f}%"></div></div>'
g += f'<div class="lab" style="color:var(--accent2)">Wire, aim, rehearse (18–23 Dec)</div><div class="trk"><div class="gb" style="background:var(--accent2);left:{32/N*100:.1f}%;width:{6/N*100:.1f}%"></div></div>'

# ---- next steps
NEXT = [
 ("This week · by 22 Nov", "Confirm on site", "Measure the deck height, ceiling height and ceiling type; check the altar is centred on the front wall; find the power point and the exit; ask the church about working at height and the deck's load rating. Fix the assumptions on sheet 3 if any are wrong.", "site"),
 ("This week · by 20 Nov", "Generate the images", "Attach the three reference images to the image model and use Prompt 1 (wide shot) first, then Prompts 2 and 3. Send me what you get; I will check it against the blueprint and fix the wording if a prompt misled the model.", "img"),
 ("By 20 Nov", "Choose Lean or Full", "Take the cost summary to the parish committee. Decide which figures can be reused from 2023 (figures, frames, plywood, skirting) and mark them on the part sheets; each reused line drops out of the budget.", "budget"),
 ("By 22 Nov", "Order long-lead items", "Fibre-optic kit, UV bars, acrylic sheet, the 2 ft figures, the backdrop print and the drape fabric. Get two quotes for plywood, thermocol and the print.", "order"),
 ("By 23 Nov", "Form the crew", "6–8 volunteers in four groups: rock and plaster, figures and painting, electrics and show control, backdrop and rigging. Name one lead for each and one overall lead.", "crew"),
 ("23 Nov → 13 Dec", "Build in the workshop", "Follow the part sheets in the order of the schedule: frame first, then rock, house and field, then village, cascade and backdrop. Bench-test all electronics and the show by 13 Dec.", "build"),
 ("14 → 17 Dec", "Install in the church", "Frame, rock pieces, backdrop track and drape, then the cascade rig. Keep a list of anything that does not pass the door.", "install"),
 ("18 → 23 Dec", "Wire, aim, rehearse", "Aim the lights, check the angel, UV choir and cross-shadow from the public spot, set the sound level, run the show three times, walk the safety checklist.", "rehearse"),
 ("24 Dec", "Open", "Final dusting, rope and signage in place, extinguisher located, start button explained to the volunteer on duty.", "open"),
]
nxt = "".join(f'<li><span class="when">{w}</span><b>{E(t)}</b>{E(d)}<label><input type="checkbox" id="chk-{k}" data-k="{k}"> Done</label></li>' for w, t, d, k in NEXT)

ptxt = ""
for i, (ttl, body) in enumerate(prompts):
    ptxt += f'<div class="card" style="margin-bottom:12px"><h3>{E(ttl)}</h3><pre id="p{i}">{E(body.strip())}</pre><button data-copy="p{i}">Copy prompt</button></div>'
ptxt = f'<div class="card" style="margin-bottom:12px"><h3>Block-out colour key (paste after the attachments)</h3><pre id="pk">{E(keyblock)}</pre><button data-copy="pk">Copy key</button></div>' + ptxt


colsec = '<section id="colour"><h2>Colour and composition</h2><p class="lead">Gold is the one complementary colour against the blue night. Everything else stays in related blues and earth tones. Twelve colours, no more.</p><div class="grid2"><div class="card"><h3>Palette</h3>' + "".join(f'<div style="display:flex;gap:12px;align-items:center;margin-bottom:8px"><div style="width:54px;height:34px;border-radius:6px;background:{h_};border:1px solid var(--line);flex:none"></div><div><b>{E(nm)}</b> <span style="color:var(--mute)">{h_} · {E(role)}</span><br><span style="font-size:13.5px">{E(use)}</span></div></div>' for role, nm, h_, use in P.PALETTE) + '<div style="display:flex;margin-top:10px;border-radius:6px;overflow:hidden"><div style="flex:60;background:#1F2F66;height:26px"></div><div style="flex:30;background:#D2BC8C"></div><div style="flex:10;background:#F2B84B"></div></div><div style="display:flex;font-size:12.5px;color:var(--mute)"><div style="flex:60">60% cool</div><div style="flex:30">30% earth</div><div style="flex:10">10% gold</div></div></div><div><div class="card"><h3>Composition rules</h3><ol>' + "".join(f"<li>{E(r)}</li>" for r in P.RULES) + '</ol></div><div class="card" style="margin-top:14px"><h3>Light colours</h3><table>' + "".join(f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in P.LIGHTS) + '</table></div></div></div><div class="card" style="margin-top:14px"><h3>Piece by piece</h3><div class="scroll"><table>' + "".join(f"<tr><td style='white-space:nowrap'><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in P.PIECES) + '</table></div></div></section>'

page = f"""<title>Crib 2026 Build Pack</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Space+Grotesk:wght@500;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header class="top"><h1>That Night in Bethlehem</h1><p>Crib 2026 build pack: where it sits, the blueprint, every part with materials and steps, cost, schedule and what to do next. Stage 9 × 16 ft in the right-hand corner of the church, opening 24 December 2026.</p>
<div class="stats"><div class="stat"><b>{P.fmt(P.TP)}</b><span>Prop-only: materials for props, with figures, stage and lights reused or rented</span></div><div class="stat"><b>{P.fmt(P.TL)}</b><span>Lean build, all-in</span></div><div class="stat"><b>{P.fmt(P.TF)}</b><span>Full build, all-in</span></div><div class="stat"><b>{P.DAYS} person-days</b><span>6–8 volunteers, 5 weeks</span></div><div class="stat"><b>4 minutes</b><span>light show, repeats</span></div></div></header>
<nav><a href="#next">What to do next</a><a href="#church">Church and views</a><a href="#blueprint">Blueprint</a><a href="#colour">Colour</a><a href="#parts">Parts</a><a href="#cost">Cost</a><a href="#schedule">Schedule</a><a href="#prompts">Image prompts</a><button class="theme" id="theme" type="button">Theme</button></nav>

<section id="next"><h2>What to do next</h2><p class="lead">Nine steps from today (16 Nov) to opening night. Ticks are saved in this browser only.</p><ol class="steps">{nxt}</ol>
<div class="card warn" style="margin-top:14px"><h3>Assumed, not yet checked</h3><ul><li>Deck height 2 ft and a free 9 × 16 ft</li><li>Ceiling about 15 ft; ceiling type unknown (affects the star hook and the drape)</li><li>Altar centred on the front wall; crib at the right end of that wall</li><li>Public stands 3 ft left and 3 ft in front of the stage corner</li></ul></div></section>

<section id="church"><h2>Church and the two views</h2><p class="lead">The grey block-outs are generated from the blueprint coordinates. Attach them to the image model so it keeps the layout.</p>
<div class="grid2"><figure><img class="fig" src="img/church.jpg" alt="Key plan of the church with the altar, the crib stage and the two camera positions"><figcaption>Key plan. Church size is a guess; only the stage is to scale.</figcaption></figure>
<div><figure><img class="fig" src="img/view1.jpg" alt="Grey block-out of the crib seen from the public viewing spot"><figcaption>View 1: from the public spot, 3 ft left and 3 ft in front of the stage corner.</figcaption></figure><figure style="margin-top:14px"><img class="fig" src="img/view2.jpg" alt="Grey block-out of the church seen from the centre aisle"><figcaption>View 2: wide shot from the centre aisle, altar centre-left, crib at the right end.</figcaption></figure></div></div>
<div class="card" style="margin-top:14px"><h3>Changed after the sight check</h3>From the public spot the cave's upper house hid the Magi caravan and the far village completely. Both now sit on the right-wall crest and a wall shelf (bearings 38–49°), clear of the house (25–41°). The floating-angel acrylic is 2.4 × 2 ft.</div></section>

<section id="blueprint"><h2>Master blueprint</h2><p class="lead">Top view, section along the sightline, 30-item schedule and the church key plan. Open the image in a new tab to zoom.</p>
<a href="img/blueprint.jpg" target="_blank"><img class="fig" src="img/blueprint.jpg" alt="Master blueprint of the crib layout"></a></section>

{colsec}
<section id="parts"><h2>Parts</h2><p class="lead">Twelve parts, each with its own plan and section, items required, build steps and cost. Open one at a time.</p>{parts}</section>

<section id="cost"><h2>Cost</h2><p class="lead">Rough estimate in rupees, ±25%. Prop-only counts prop materials only; Lean reuses and makes things; Full buys new. This adds up every line and replaces the earlier ₹40,000–70,000 first guess.</p>
<div class="scroll"><table><tr><th>#</th><th>Part</th><th class="n">Person-days</th><th class="n">Prop-only ₹</th><th class="n">Lean ₹</th><th class="n">Full ₹</th><th>Lean (green) vs Full</th></tr>{crow}
<tr class="tot"><td></td><td>Subtotal</td><td class="n">{P.DAYS}</td><td class="n">{P.ind(P.PROP)}</td><td class="n">{P.ind(P.LEAN)}</td><td class="n">{P.ind(P.FULL)}</td><td></td></tr><tr><td></td><td>Contingency 10%</td><td></td><td class="n">{P.ind(P.CP)}</td><td class="n">{P.ind(P.CL)}</td><td class="n">{P.ind(P.CF)}</td><td></td></tr><tr class="tot"><td></td><td>Total</td><td></td><td class="n">{P.ind(P.TP)}</td><td class="n">{P.ind(P.TL)}</td><td class="n">{P.ind(P.TF)}</td><td></td></tr></table></div>
<div class="card" style="margin-top:14px"><h3>Prop-only tier: what it assumes</h3><ul><li>Not counted: all figures (reused from 2023), the rented stage and skirting, rented lights (wash, spots, UV bars), speakers, electrician, extinguisher, ladder hire</li><li>Half of the plywood is reused from 2023; the other half is bought</li><li>Smaller rock (hill 5 sheets, terraces 2, village 2), painted hills, cheaper drape, 25 bead strands, 15 angels, one ESP32, borrowed tools</li><li>Dropping contingency to 5% brings it to about ₹79,000; skipping the far village and Magi shelf saves about ₹2,100 more</li></ul></div><div class="grid2" style="margin-top:14px"><div class="card warn"><h3>Biggest swings</h3><ul><li>2 ft Holy Family figures: ₹8,000 repainted from 2023, ₹18,000 new</li><li>Drape: about ₹280 per foot of drop; polyester vs velvet</li><li>Floating-angel screen: free with an old tablet, ₹7,000 new</li><li>Crystal strands and mini angels: ₹4,000 made, ₹9,500 bought</li></ul></div><div class="card"><h3>Ways to lower it</h3><ul><li>Reuse 2023 plywood, frames, skirting, figures: about ₹10,000–15,000</li><li>Borrow wash lights and spots: up to ₹6,300</li><li>Make the Magi caravan from clay: about ₹2,000</li></ul></div></div></section>

<section id="schedule"><h2>Schedule</h2><p class="lead">Build in the workshop, install from 14 Dec, rehearse 21–23 Dec, open 24 Dec.</p><div class="scroll"><div class="gantt" style="min-width:640px">{g}</div></div>
<div class="grid2" style="margin-top:14px"><div class="card"><h3>Main risks</h3><ul><li>Ceiling higher than 15 ft: longer strands, more drape</li><li>Print or figures arrive late: order by 22 Nov</li><li>Fire: retardant on all thermocol, cotton and cloth; no open flames</li><li>Mist near electrics: sealed trays with a float switch</li><li>Door width: build the hill in pieces that pass the door</li></ul></div><div class="card"><h3>Dress rehearsal checklist</h3>Run the show three times. Stand at the public spot and check the angel, the UV choir, the path, the cave glow and the cross-shadow from the rope. Check the sound level and test the manual override.</div></div></section>

<section id="prompts"><h2>Image prompts</h2><p class="lead">Attach the three images above, then say: the grey block-outs are the exact composition; keep every position and replace the boxes with real materials. Part-by-part prompts for each component are in crib-2026-component-prompts.md.</p>{ptxt}</section>
<footer>Crib 2026 · build pack · rough estimate, confirm with local quotes.</footer></div>
<script>
(function(){{
var root=document.documentElement;
document.getElementById('theme').addEventListener('click',function(){{var dark=root.getAttribute('data-theme')?root.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme:dark)').matches;root.setAttribute('data-theme',dark?'light':'dark');}});
document.querySelectorAll('button[data-copy]').forEach(function(b){{b.addEventListener('click',function(){{var el=document.getElementById(b.dataset.copy);var t=el.textContent;function sel(){{var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected: press Ctrl+C';}}
try{{navigator.clipboard.writeText(t).then(function(){{b.textContent='Copied';setTimeout(function(){{b.textContent='Copy prompt';}},1500);}},sel);}}catch(e){{sel();}}}});}});
document.querySelectorAll('input[data-k]').forEach(function(c){{try{{c.checked=localStorage.getItem('crib26-'+c.dataset.k)==='1';}}catch(e){{}}c.addEventListener('change',function(){{try{{localStorage.setItem('crib26-'+c.dataset.k,c.checked?'1':'0');}}catch(e){{}}}});}});
if(location.hash){{var d=document.querySelector(location.hash);if(d&&d.tagName==='DETAILS')d.open=true;}}
}})();
</script>"""
open("crib_page.html", "w", encoding="utf-8").write(page)
print(len(page))
