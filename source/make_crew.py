"""Owner guide (with prices): START HERE pages + two pages per block (what/size/cost/when, then buy/check/prompt).
Run after make_views.py: python source/make_crew.py -> 2026/owner/ (owner-guide.pdf, <letter>-card.pdf, owner-prompts.md): the full version with prices, for the project owner"""
import os, sys, re, html, math, shutil, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_blocks as mb
import make_views as mv
import make_prompts as mp

ROOT = mb.ROOT; OUT = os.path.join(ROOT, '2026', 'owner'); os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
GENDIR = os.path.join(ROOT, '2026', 'images', 'generated')
GEN = {'A': ['stage-bare-3q'], 'B': ['B-cave-holy-family', 'B-rock-hill-empty'], 'C': ['C-upper-house'], 'E': ['E-shepherds-field'], 'F': ['F-angel-choir'], 'G': ['G-village-street'], 'H': ['H-lights-control'], 'I': ['I-sky-cascade'], 'J': ['J-backdrop'], 'K': ['K-far-village-magi'], 'L': ['L-foreground-view-spot'], 'N': ['N-foreground']}
def have(n): return os.path.exists(os.path.join(GENDIR, n + '.jpg'))

def crew_pic(b):
    mine = [e for e in mv.E if e['b'] == b]
    xs = [x for e in mine for x, y in e['poly']]; ys = [y for e in mine for x, y in e['poly']]
    x0, x1, y0, y1 = min(xs)-0.8, max(xs)+0.8, min(ys)-0.8, max(ys)+0.8
    if b in ('A', 'J', 'I', 'H', 'L'): x0, x1, y0, y1 = -0.3, 9.3, -0.3, 16.3
    S = min(780/(x1-x0), 560/(y1-y0)); W, H = 1800, 680
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{mv.DEFS}<rect width="{W}" height="{H}" fill="#ffffff"/>']
    s.append(mv.T(20, 30, 'FROM THE PUBLIC SPOT', 20, weight='bold'))
    s.append('<rect x="20" y="46" width="900" height="600" fill="#f3f1ea" stroke="#2b2a33"/>')
    s.append(mv.persp_panel(mv.E, lambda e: '#fff2c8' if e.get('gold') else mv.light(mv.COL[b]), lambda e: mv.dark(mv.COL[b]), W=900, H=600, ghost=lambda e: e['b'] != b, letters=False, x0=20, y0=46))
    s.append(mv.T(960, 30, 'WHERE IT GOES (TOP VIEW, 1 SQUARE = 1 FT)', 20, weight='bold'))
    vw = mv.View('top', S, 960, 70, (x0, x1, y0, y1)); pw, ph = (x1-x0)*S, (y1-y0)*S
    s.append(f'<rect x="960" y="70" width="{pw:.1f}" height="{ph:.1f}" fill="#fcfcfa" stroke="#bbb"/><clipPath id="tc"><rect x="960" y="70" width="{pw:.1f}" height="{ph:.1f}"/></clipPath><g clip-path="url(#tc)">')
    for i in range(int(math.floor(x0)), int(math.ceil(x1))+1): s.append(f'<line x1="{vw.X(i):.1f}" y1="70" x2="{vw.X(i):.1f}" y2="{70+ph:.1f}" stroke="#e3e6ee"/>')
    for j in range(int(math.floor(y0)), int(math.ceil(y1))+1):
        yy = 70+(j-y0)*S; s.append(f'<line x1="960" y1="{yy:.1f}" x2="{960+pw:.1f}" y2="{yy:.1f}" stroke="#e3e6ee"/>')
    ctx = [e for e in mv.E if e['b'] != b and not e.get('dark')]
    s.append(mv.draw_view(vw, ctx, lambda e: '#f1f1f1', lambda e: '#c4c4c4', ghost=lambda e: True))
    s.append(mv.draw_view(vw, [e for e in mine if not e.get('dark')], lambda e: '#fff2c8' if e.get('gold') else mv.light(mv.COL[b]), lambda e: mv.dark(mv.COL[b])))
    s.append('</g></svg>')
    path = os.path.join(OUT, 'img', f'{b}-pic.png'); mv.png('\n'.join(s), W, H, path); return f'img/{b}-pic.png'

# ---------- numbers ----------
def n(x): return int(str(x).replace(',', '') or 0)
def inr(v):
    s = str(int(v))
    if len(s) <= 3: return '₹' + s
    h, t = s[:-3], s[-3:]; out = []
    while len(h) > 2: out.insert(0, h[-2:]); h = h[:-2]
    if h: out.insert(0, h)
    return '₹' + ','.join(out + [t])
def totals(k): return [sum(n(r[i]) for r in mb.B[k]['rows'] if r[0] != 'Total') for i in (2, 3, 4)]
TOOLS = {'prop': 1600, 'lean': 3000, 'full': 6000}   # tools + transport lines from the pack cost table
def grand():
    t = [sum(totals(k)[i] for k in mb.ORDER) for i in range(3)]
    base = [t[0] + TOOLS['prop'], t[1] + TOOLS['lean'], t[2] + TOOLS['full']]
    return t, base, [round(x * 1.1) for x in base]

def dims_lines(k):
    out = {}
    for e in mv.E:
        if e['b'] != k: continue
        nm = e['name']; p = e['poly']; z = e['z1'] - e['z0']
        if e['kind'] == 'strands': txt = '30 strands, each 6 ft long, on a 1.8 ft ring'
        elif e['kind'] == 'spiral': txt = '2.5 ft wide, 3 turns, about 6.5 ft tall, 30 small angels'
        elif e['kind'] == 'star': txt = '2 ft wide'
        elif e['kind'] == 'flat': txt = '0.5 ft wide × 7.7 ft long, flat in the deck'
        elif e['kind'] == 'tree': txt = f'canopy about {math.hypot(p[0][0]-p[len(p)//2][0], p[0][1]-p[len(p)//2][1])*1.25:.1f} ft wide, {z:.1f} ft tall'
        else:
            if len(p) == 4:
                w = math.hypot(p[1][0]-p[0][0], p[1][1]-p[0][1]); d = math.hypot(p[2][0]-p[1][0], p[2][1]-p[1][1])
            elif len(p) >= 8 and nm in ('well', 'watchtower', 'campfire'):
                w = d = math.hypot(p[0][0]-p[len(p)//2][0], p[0][1]-p[len(p)//2][1])
            else:
                xs = [q[0] for q in p]; ys = [q[1] for q in p]; w = max(xs)-min(xs); d = max(ys)-min(ys)
            if nm == 'deck + skirting': txt = '9 ft wide at the front × 16 ft deep; skirting 2 ft'
            elif nm in ('right-wall print', 'back-wall print'): txt = '5 ft high; wall length ' + ('16 ft' if 'right' in nm else '9 ft')
            elif nm in ('right-wall drape', 'back-wall drape'): txt = 'from 5 ft up to the ceiling (about 13 ft); wall length ' + ('16 ft' if 'right' in nm else '9 ft')
            else: txt = f'{max(w,d):.1f} × {min(w,d):.1f} ft, {z:.1f} ft high' if z > 0.05 else f'{max(w,d):.1f} × {min(w,d):.1f} ft'
        out.setdefault((nm, txt), 0); out[(nm, txt)] += 1
    return [(nm + (f' (×{c})' if c > 1 else ''), t) for (nm, t), c in out.items()]

MONTHS = {'Nov': 11, 'Dec': 12}
def window(k):
    m = re.search(r'(\d+) (Nov|Dec) → (\d+) (Nov|Dec)', mb.B[k]['window'])
    a = dt.date(2026, MONTHS[m.group(2)], int(m.group(1))); b = dt.date(2026, MONTHS[m.group(4)], int(m.group(3))); return a, b
def fd(a, b):
    if a == b: return f'{a.day} {a.strftime("%b")}'
    return f'{a.day}–{b.day} {b.strftime("%b")}' if a.month == b.month else f'{a.day} {a.strftime("%b")} – {b.day} {b.strftime("%b")}'
def step_dates(k, cnt):
    a, b = window(k); span = (b - a).days + 1; out = []
    for i in range(cnt):
        s = a + dt.timedelta(days=int(i * span / cnt)); e = a + dt.timedelta(days=max(int((i + 1) * span / cnt) - 1, int(i * span / cnt)))
        out.append(fd(s, e))
    return out

def short(t, lim=150):
    t = re.sub(r'\s+', ' ', t).strip()
    return t if len(t) <= lim else t[:lim-3].rsplit(' ', 1)[0] + '...'

CSS = ('@page{size:297mm 210mm;margin:6mm}*{box-sizing:border-box}body{margin:0;font:13px/1.35 "Segoe UI",Arial,sans-serif;color:#1d1d22}'
       '.pg{page-break-after:always;height:196mm;overflow:hidden}.pg:last-child{page-break-after:auto}'
       '.head{display:flex;align-items:center;gap:16px;padding:6px 14px;color:#fff;border-radius:6px}.L{font:700 42px/1 "Segoe UI";width:60px;text-align:center}'
       '.head h1{margin:0;font-size:25px}.head p{margin:2px 0 0;font-size:13px}.head .pgn{margin-left:auto;font-size:13px;opacity:.9}'
       '.top{display:grid;grid-template-columns:.7fr 1.3fr;gap:8px;margin:6px 0;align-items:start}.gen img{width:100%;display:block;border:1px solid #cfc9b8;border-radius:5px}'
       '.gen.two{display:grid;grid-template-columns:1fr 1fr;gap:4px}.gen.two img{height:30mm;object-fit:cover}.pic{width:100%;max-height:57mm;object-fit:contain;display:block;border:1px solid #cfc9b8;border-radius:5px}'
       '.cap{font-size:10px;color:#555;margin:0 0 2px;text-transform:uppercase;letter-spacing:.05em}.nogen{border:2px dashed #bbb;border-radius:5px;padding:14mm 6mm;text-align:center;color:#777}'
       '.stats{display:grid;grid-template-columns:1.2fr 1.4fr 1fr 1fr;gap:8px;margin:6px 0}.stat{border:2px solid #2b2a33;border-radius:8px;padding:6px 10px}.stat .t{font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#555}'
       '.stat .v{font:700 19px/1.15 "Segoe UI"}.stat .s{font-size:11.5px;color:#444}.cols{display:grid;grid-template-columns:1fr 1.25fr;gap:10px}.cols2{display:grid;grid-template-columns:1.5fr 1fr;gap:10px}'
       '.box{border:1px solid #cfc9b8;border-radius:6px;padding:7px 10px;margin-bottom:8px}.box h2{margin:0 0 4px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#555}'
       'table{border-collapse:collapse;width:100%;font-size:12px}th,td{border-bottom:1px solid #e2ddcf;padding:3px 5px;text-align:left;vertical-align:top}th{background:#efece3}td.n,th.n{text-align:right;white-space:nowrap}tr.tot td{font-weight:700;border-top:2px solid #777}'
       'ol,ul{margin:2px 0 0;padding-left:18px}li{margin-bottom:3px}.steps{list-style:none;padding:0}.steps li{display:grid;grid-template-columns:84px 1fr;gap:6px;margin-bottom:4px}.steps .d{font-weight:700;color:#8a5a12;font-size:12px}'
       '.chk li{list-style:none;margin-left:-18px}.chk li:before{content:"\\2610  "}pre{white-space:pre-wrap;font:9px/1.3 Consolas,monospace;background:#f6f4ee;border:1px solid #d9d4c6;border-radius:5px;padding:6px;margin:0}'
       '.gantt{display:grid;grid-template-columns:150px repeat(37,1fr);gap:0;font-size:11px}.gantt .c{border-bottom:1px solid #eee;min-height:17px}.gantt .bar{border-radius:3px;margin:2px 0;color:#fff;font-size:10px;padding-left:3px;overflow:hidden;white-space:nowrap}'
       '.gantt .h{font-size:9px;text-align:center;color:#555;border-left:1px solid #ddd}')

def head(k, sub, pgn):
    return f'<div class="head" style="background:{mb.rgb(k)}"><div class="L">{k}</div><div><h1>{html.escape(mv.NAMES[k])}</h1><p>{html.escape(sub)}</p></div><div class="pgn">{pgn}</div></div>'

def top_crop(k):
    from PIL import Image
    src = os.path.join(GENDIR, 'crib-final-top.jpg')
    if not os.path.exists(src): return None
    im = Image.open(src); L, Rr, Tp, Bt = 135, 960, 88, 1348
    els = [e for e in mv.E if e['b'] == k and e['name'] != 'selfie mirror']
    xs = [x for e in els for x, y in e['poly']]; ys = [y for e in els for x, y in e['poly']]
    if not xs and k not in ('A', 'H', 'J'): return None
    if k in ('A', 'H', 'J'): x0, x1, y0, y1 = 0, 9, 0, 16
    else: x0, x1, y0, y1 = max(min(xs)-1.0, 0), min(max(xs)+1.0, 9), max(min(ys)-1.0, 0), min(max(ys)+1.0, 16)
    box = (int(L+x0/9*(Rr-L)), int(Tp+y0/16*(Bt-Tp)), int(L+x1/9*(Rr-L)), int(Tp+y1/16*(Bt-Tp)))
    path = os.path.join(OUT, 'img', f'{k}-above.jpg'); im.crop(box).save(path, quality=90); return f'img/{k}-above.jpg'

def gen_html(k):
    names = [x for x in GEN.get(k, []) if have(x)]
    if not names:
        c = top_crop(k)
        if c: return f'<div class="gen one"><img src="{c}" style="height:58mm;width:100%;object-fit:cover;object-position:center"><p class="cap" style="margin-top:2px">cut from the final top view</p></div>'
        return '<div class="nogen">No picture yet.<br>Generate it with the prompt on page 2.</div>'
    for x in names: shutil.copy(os.path.join(GENDIR, x + '.jpg'), os.path.join(OUT, 'img', x + '.jpg'))
    return f'<div class="gen {"two" if len(names) > 1 else "one"}">' + ''.join(f'<img src="img/{x}.jpg">' for x in names) + '</div>'

def card(k):
    b = mb.B[k]; look, mat = mp.LOOK[k]; pic = crew_pic(k); tt = totals(k); a, e = window(k)
    steps = [short(s) for s in b['steps'] if not s.isupper()][:(10 if k == 'H' else 8)]; sd = step_dates(k, len(steps))
    dl = dims_lines(k)
    prompt = ('Stage: 9 ft wide at the SHORT front, 16 ft DEEP along the long left side (do not swap). Attached: (1) the final photo of the whole crib, to match its look and materials; (2) a picture of ONE block, to match its shape and place. '
              'Create ONE real-looking phone photograph of just this block as built, seen from the front-left at a three-quarter angle, turned about 33 degrees as in the attached picture, on a plain light-grey background with soft warm light. '
              f'BLOCK {k}, {mv.NAMES[k]}: {look} {"" if k == "A" else "Size and place: " + b["where"] + " "}Materials: {mat}. Real physical handmade model, not CGI, not an illustration. No Christmas tree, no snow, no text. '
              'Palette: lamp gold, warm white, Mary blue, midnight blue, dusk violet, mist blue, limestone, sand, ochre, olive; no red, bright green or pink. 16:9.')
    extra_dim = ''
    if k == 'A': extra_dim = '<tr><td>Frame heights</td><td>0 ft for the first 5.5 ft from the front, ramp up to 3.0 ft by 9 ft, 3.0 ft to the back; left terrace boxes 0.8 / 1.2 / 1.6 / 2.0 ft</td></tr>'
    drows = ''.join(f'<tr><td>{html.escape(nm)}</td><td>{html.escape(t)}</td></tr>' for nm, t in dl[:12]) + extra_dim
    srows = ''.join(f'<li><span class="d">{d}</span><span>{html.escape(t)}</span></li>' for d, t in zip(sd, steps))
    items = ''.join('<tr><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % (html.escape(r[0]), html.escape(r[1]), inr(n(r[2])), inr(n(r[3])), inr(n(r[4]))) for r in b['rows'] if r[0] != 'Total')
    items += f'<tr class="tot"><td colspan="2">Total</td><td class="n">{inr(tt[0])}</td><td class="n">{inr(tt[1])}</td><td class="n">{inr(tt[2])}</td></tr>'
    li = lambda xs, c='': f'<ul class="{c}">' + ''.join(f'<li>{html.escape(x)}</li>' for x in xs) + '</ul>'
    p1 = (f'<section class="pg">{head(k, b["items"], "Page 1 of 2 · see it and plan it")}'
          f'<div class="top"><div><p class="cap">Target look (generated)</p>{gen_html(k)}</div><div><p class="cap">How it looks from the public spot, and where it goes</p><img class="pic" src="{pic}"></div></div>'
          f'<div class="stats"><div class="stat"><div class="t">Where</div><div class="v" style="font-size:12px;font-weight:600">{html.escape(short(b["where"], 190))}</div></div>'
          f'<div class="stat"><div class="t">Budget (₹)</div><div class="v">{inr(tt[1])} <span style="font-size:12px;font-weight:400">lean</span></div><div class="s">{inr(tt[0])} if you reuse · {inr(tt[2])} if all new</div></div>'
          f'<div class="stat"><div class="t">Time</div><div class="v">{fd(a, e)}</div><div class="s">about {b["days"]} person-days</div></div>'
          f'<div class="stat"><div class="t">Team</div><div class="v" style="font-size:13px;font-weight:600">{html.escape(b["team"])}</div></div></div>'
          f'<div class="cols"><div class="box"><h2>Parts and sizes (feet)</h2><table>{drows}</table></div>'
          f'<div class="box"><h2>What to do, and when</h2><ol class="steps">{srows}</ol></div></div></section>')
    p2 = (f'<section class="pg">{head(k, "Buy it, check it, picture it", "Page 2 of 2 · buy and check")}'
          f'<div class="cols2" style="margin-top:8px"><div class="box"><h2>Shopping list and cost (₹): reuse · lean · all new</h2><table><tr><th>Item</th><th>Qty</th><th class="n">Reuse</th><th class="n">Lean</th><th class="n">New</th></tr>{items}</table>'
          f'<p style="margin:6px 0 0;font-size:11.5px;color:#444"><b>Tools:</b> {html.escape(b["tools"])}</p></div>'
          f'<div><div class="box"><h2>Before you start</h2>{li(b["before"])}</div><div class="box"><h2>Done when (tick each)</h2>{li(b["done"], "chk")}</div>'
          f'<div class="box"><h2>Hands over to</h2>{html.escape(b["hands"])}</div></div></div>'
          f'<div class="box"><h2>Prompt to generate the end result (attach the final crib photo and this block\'s picture)</h2><pre>{html.escape(prompt)}</pre></div></section>')
    return p1 + p2, prompt

def start_pages():
    t, base, tot = grand()
    rows = ''.join('<tr><td><b>%s</b></td><td>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % (k, html.escape(mv.NAMES[k]), inr(totals(k)[0]), inr(totals(k)[1]), inr(totals(k)[2])) for k in mb.ORDER)
    rows += f'<tr><td></td><td>Tools and transport</td><td class="n">{inr(TOOLS["prop"])}</td><td class="n">{inr(TOOLS["lean"])}</td><td class="n">{inr(TOOLS["full"])}</td></tr>'
    rows += f'<tr><td></td><td>Spare (10%)</td><td class="n">{inr(tot[0]-base[0])}</td><td class="n">{inr(tot[1]-base[1])}</td><td class="n">{inr(tot[2]-base[2])}</td></tr>'
    rows += f'<tr class="tot"><td></td><td>TOTAL TO BUDGET</td><td class="n">{inr(tot[0])}</td><td class="n">{inr(tot[1])}</td><td class="n">{inr(tot[2])}</td></tr>'
    thumbs = ''
    p1 = (f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>Crib 2026 · That Night in Bethlehem · START HERE</h1><p>Opens 24 December 2026 · stage 9 ft wide × 16 ft deep · 13 blocks (A, B, C, E to N; there is no D, the rock hill is part of B)</p></div></div>'
          f'<div class="cols" style="margin-top:6px"><div><img src="img/final-look.jpg" style="width:100%;border-radius:6px;border:1px solid #cfc9b8"><div style="display:flex;gap:6px;margin-top:5px;align-items:flex-start"><img src="img/final-top.jpg" style="height:96mm;border-radius:6px;border:1px solid #cfc9b8"><div style="font-size:11.5px;color:#444"><b>Final look</b>: the finished crib from the public spot (above) and from directly above (left). Generated pictures; the crew builds to the blueprints in the crew pack.</div></div></div>'
          f'<div class="box"><h2>What it costs (₹, rough, ±25%)</h2><table><tr><th>Block</th><th>Name</th><th class="n">Reuse</th><th class="n">Lean</th><th class="n">New</th></tr>{rows}</table>'
          '<p style="font-size:11.5px;margin:4px 0 0"><b>Reuse</b> = figures from 2023, stage and lights rented. <b>Lean</b> = reuse and make it yourself, own lights. <b>New</b> = buy everything new. Pick one with the committee.</p></div></div></section>')
    d0 = dt.date(2026, 11, 18); days = (dt.date(2026, 12, 24) - d0).days + 1
    cells = '<div class="c"></div>' + ''.join(f'<div class="c h">{(d0 + dt.timedelta(days=i)).day if (i % 3 == 0) else ""}</div>' for i in range(days))
    for k in mb.ALL:
        a, e = window(k); s = max((a - d0).days, 0) + 2; w = (e - a).days + 1
        cells += f'<div class="c"><b>{k}</b> {html.escape(mv.NAMES[k])[:20]}</div><div class="c" style="grid-column:{s} / span {w}"><div class="bar" style="background:{mb.rgb(k)}">{fd(a, e)}</div></div>'
    cells += '<div class="c"><b>Install</b></div><div class="c" style="grid-column:%d / span 4"><div class="bar" style="background:#555">14–17 Dec</div></div>' % ((dt.date(2026, 12, 14) - d0).days + 2)
    cells += '<div class="c"><b>Wire, aim, rehearse</b></div><div class="c" style="grid-column:%d / span 6"><div class="bar" style="background:#555">18–23 Dec</div></div>' % ((dt.date(2026, 12, 18) - d0).days + 2)
    cells += '<div class="c"><b>OPEN</b></div><div class="c" style="grid-column:%d / span 1"><div class="bar" style="background:#a8322c">24</div></div>' % ((dt.date(2026, 12, 24) - d0).days + 2)
    checks = ['The church socket right behind the stage (back-left corner): exact spot and circuit rating', 'Deck height (2 ft assumed), size, level, and whether you may screw into it', 'Ceiling height (about 15 ft assumed) and ceiling type', 'Altar centred on the front wall; crib at its right end', 'Exit and the deck load rating', 'Work-at-height rules for hanging block I', 'How much 2023 plywood still exists']
    p2 = (f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>When: who builds what</h1><p>18 Nov to 24 Dec. Bars show the build window of each block.</p></div></div>'
          f'<div class="box" style="margin-top:6px"><div class="gantt">{cells}</div></div>'
          f'<div class="cols2"><div class="box"><h2>How to use a card</h2><ol><li>Find your letter. Page 1 shows what it looks like, its size, cost, time and what to do on which days.</li><li>Page 2 is the shopping list with prices, the checks, and a prompt if you want a picture of the finished block.</li><li>Do the steps in order and tick "done when". Then hand over to the next block.</li></ol></div>'
          f'<div class="box"><h2>Check on site first</h2>{"".join("<div>☐ " + html.escape(c) + "</div>" for c in checks)}</div></div></section>')
    return p1 + p2

if __name__ == '__main__':
    shutil.copy(os.path.join(GENDIR, 'crib-final-3q.jpg'), os.path.join(OUT, 'img', 'final-look.jpg')); shutil.copy(os.path.join(GENDIR, 'crib-final-top.jpg'), os.path.join(OUT, 'img', 'final-top.jpg'))
    for k in mb.ORDER:
        for x in GEN.get(k, []):
            if have(x): shutil.copy(os.path.join(GENDIR, x + '.jpg'), os.path.join(OUT, 'img', x + '.jpg'))
    whole = re.search(r'```\n(.*?)\n```', open(os.path.join(ROOT, '2026', 'docs', 'eye-view-prompt.md'), encoding='utf8').read(), flags=re.S).group(1)
    md = ['# Crew prompts: one per block, plus the whole crib', '', '## Whole crib (corner view)', 'Attach: `2026/images/view1-visitor.png`, `2026/share/final-blueprint-3-views.png`, `2026/images/church-key-plan.png`, two style images.', '', '```', whole, '```', '']
    bodies = []
    for k in mb.ALL:
        body, prompt = card(k); bodies.append(body)
        md += [f'## Block {k} · {mv.NAMES[k]}', f'Attach: `2026/images/generated/crib-final-3q.jpg` and `2026/crew/img/{k}-pic.png`. Target look already generated: `2026/images/generated/`', '', '```', prompt, '```', '']
        hp = os.path.join(OUT, f'{k}-card.html'); open(hp, 'w', encoding='utf8').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{body}')
        mb.pdf(hp, os.path.join(OUT, f'{k}-card.pdf')); print(k)
    full = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{start_pages()}{"".join(bodies)}'
    open(os.path.join(OUT, 'owner-guide.html'), 'w', encoding='utf8').write(full); mb.pdf(os.path.join(OUT, 'owner-guide.html'), os.path.join(OUT, 'owner-guide.pdf'))
    open(os.path.join(OUT, 'owner-prompts.md'), 'w', encoding='utf8').write('\n'.join(md)); print('done')
