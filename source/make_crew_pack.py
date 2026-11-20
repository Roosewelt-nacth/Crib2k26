"""Crew pack (no prices): per block 4 pages: (1) simple card with picture and image prompt, (2) blueprint drawing, (3) parts table + cut list with exact sizes, (4) exact build sequence.
Run after make_views.py and make_crew.py: python source/make_crew_pack.py -> 2026/crew/ (crew-pack.pdf, <letter>-crew.pdf, crew-prompts.md)"""
import os, sys, re, html, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_blocks as mb
import make_views as mv
import make_prompts as mp
import make_crew as mc
import crew_steps as cs
import object_guide as og
import team_pages as tp

ROOT = mb.ROOT; OUT = os.path.join(ROOT, '2026', 'crew'); os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
mc.OUT = OUT   # reuse the picture helpers, writing into the crew folder

CSS = mc.CSS + ('.ob svg{display:block;margin:0 0 2px}.ob{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:6px}.ob .box{font-size:11.5px;margin:0}.ob h2{font-size:13px}.ob p{margin:2px 0}.ob ol{margin:3px 0 0;padding-left:17px}.ob li{margin-bottom:2px}.re{color:#3d6b2a}' + 'pre{font-size:7.6px!important;line-height:1.25!important}.pg .top .gen.two img{height:26mm!important}.pic{max-height:52mm!important}' + '.pg{height:197mm}.pic{max-height:62mm}.bp{width:100%;max-height:96mm;object-fit:contain;display:block;border:1px solid #cfc9b8;border-radius:5px}'
                '.three{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}.cols3{display:grid;grid-template-columns:1fr 1.1fr;gap:10px}'
                '.parts{font-size:11px}.parts td,.parts th{padding:2px 4px}.two-col{column-count:2;column-gap:12px}.note{background:#fbf3df;border:1px solid #e0c98a;border-radius:6px;padding:6px 10px;font-size:11.5px;margin-top:6px}'
                '.steps2{margin:2px 0 0;padding-left:20px}.steps2 li{margin-bottom:5px}')

def nop(s): return re.sub(r'\s*\([^)]*₹[^)]*\)', '', s)
def li(xs, c=''): return f'<ul class="{c}">' + ''.join(f'<li>{html.escape(x)}</li>' for x in xs) + '</ul>'

def page1(k):
    b = mb.B[k]; look, mat = mp.LOOK[k]; pic = mc.crew_pic(k)
    steps = [mc.short(s, 120) for s in b['steps'] if not s.isupper()][:5]
    items = [f'{r[0]} ({r[1]})' for r in b['rows'] if r[0] != 'Total'][:7]
    prompt = ('Stage: 9 ft wide at the SHORT front, 16 ft DEEP along the long left side (do not swap). Attached: (1) the final photo of the whole crib, to match its look and materials; (2) a picture of ONE block, to match its shape and place. '
              'Create ONE real-looking phone photograph of just this block as built, seen from the front-left at a three-quarter angle, turned about 33 degrees as in the attached picture, on a plain light-grey background with soft warm light. '
              f'BLOCK {k}, {mv.NAMES[k]}: {look} {"" if k == "A" else "Size and place: " + b["where"] + " "}Materials: {mat}. Real physical handmade model, not CGI, not an illustration. No Christmas tree, no snow, no text. '
              'Palette: lamp gold, warm white, Mary blue, midnight blue, dusk violet, mist blue, limestone, sand, ochre, olive; no red, bright green or pink. 16:9.')
    a, e = mc.window(k); ph = (' (' + html.escape(b['phase']) + ')') if b.get('phase') else ''
    body = (f'<section class="pg">{mc.head(k, b["items"], f"Page 1 of {npg(k)} · what it is")}'
            f'<div class="top"><div><p class="cap">Target look (generated)</p>{mc.gen_html(k)}</div><div><p class="cap">How it looks from the public spot, and where it goes</p><img class="pic" src="{pic}"></div></div>'
            f'<div class="meta" style="margin:4px 0"><b>Size and place:</b> {html.escape(b["where"])} &nbsp; <b>Build:</b> {mc.fd(a, e)}{ph} &nbsp; <b>Team:</b> {html.escape(b["team"])}</div>'
            f'<div class="three"><div class="box"><h2>In short</h2><ol>{"".join(f"<li>{html.escape(x)}</li>" for x in steps)}</ol></div>'
            f'<div class="box"><h2>You need</h2>{li(items)}<h2 style="margin-top:6px">Done when</h2>{li(b["done"][:3], "chk")}</div>'
            f'<div class="box"><h2>Prompt to generate the end result</h2><pre>{html.escape(prompt)}</pre></div></div></section>')
    return body, prompt

def page2(k):
    svg, w, h = mv.frame_svg() if k == 'A' else mv.blueprint_svg(k); path = os.path.join(OUT, 'img', f'{k}-blueprint.png'); mv.png(svg, w, h, path)
    return (f'<section class="pg">{mc.head(k, "Blueprint with exact measurements", f"Page 2 of {npg(k)} · the drawing")}'
            f'<div class="box" style="margin-top:6px"><img class="bp" style="max-height:165mm" src="img/{k}-blueprint.png"></div>'
            '<p style="margin:2px 0 0;font-size:11.5px;color:#444">Feet. x is measured from the LEFT edge of the stage, y from the BACK wall. Heights are above the deck. Numbers match the parts table on the next page.</p></section>')

def page3(k):
    x = cs.X[k]
    groups = mv.frame_groups() if k == 'A' else mv.part_groups(k)
    rows = ''
    for g in groups:
        wh = g['wheres'][0] if g['count'] == 1 else (f'{g["count"]} places, e.g. ' + g['wheres'][0] + (f'; {g["wheres"][1]}' if len(g['wheres']) > 1 else ''))
        rows += f'<tr><td><b>{g["no"]}</b></td><td>{html.escape(g["name"])}{" ×" + str(g["count"]) if g["count"] > 1 else ""}</td><td>{html.escape(g["size"])}</td><td>{html.escape(wh)}</td><td>{html.escape(g["base"])}</td></tr>'
    cut = ''.join(f'<tr><td><b>{html.escape(i)}</b></td><td>{html.escape(q)}</td></tr>' for i, q in x['cut'])
    stack = f'<div class="note">{html.escape(cs.STACK_NOTE)}</div>' if k in ('B', 'C') else ''
    return (f'<section class="pg">{mc.head(k, "Every part: size and place", f"Page 3 of {npg(k)} · the numbers")}'
            f'<div class="box" style="margin-top:6px"><h2>Parts table (x from the LEFT edge, y from the BACK wall, heights above the deck)</h2><table class="parts" style="font-size:12px"><tr><th>No.</th><th>Part</th><th>Size</th><th>Where</th><th>Sits at</th></tr>{rows}</table>{stack}</div>'
            f'<div class="box"><h2>Cut and make list (exact sizes)</h2><table class="parts" style="font-size:12px">{cut}</table></div></section>')

def page4(k):
    x = cs.X[k]; b = mb.B[k]
    mats = ', '.join(f'{r[0]} ({r[1]})' for r in b['rows'] if r[0] != 'Total')
    steps = ''.join(f'<li>{html.escape(s)}</li>' for s in (x['steps'] or b['steps']))
    return (f'<section class="pg">{mc.head(k, "Exact build: do this, in this order", f"Page 4 of {npg(k)} · build it")}'
            f'<div class="cols3" style="margin-top:8px"><div class="box"><h2>Do exactly this</h2><ol class="steps2" style="font-size:12.5px">{steps}</ol></div>'
            f'<div><div class="box"><h2>Before you start</h2>{li([nop(s) for s in b["before"]])}</div><div class="box"><h2>Materials to get</h2><div style="font-size:11.5px">{html.escape(mats)}</div><p style="margin:5px 0 0;font-size:11.5px"><b>Tools:</b> {html.escape(b["tools"])}</p></div>'
            f'<div class="box"><h2>Done when (tick each)</h2>{li(b["done"], "chk")}</div><div class="box"><h2>Hands over to</h2>{html.escape(b["hands"])}</div></div></div></section>')

PER = 3
def npg(k): return 4 + -(-len(og.O[k]) // PER)

def obj_pages(k):
    objs = og.O[k]; out = ''
    for p in range(0, len(objs), PER):
        cards = ''
        for i, (nm, size, mat, reuse, steps) in enumerate(objs[p:p+PER], p + 1):
            bx = og.BOX[k][i-1]; col = mb.rgb(k)
            boxl = (f'<p><b>Box:</b> {tp.ft(bx[0])} W × {tp.ft(bx[1])} D' + (f' × {tp.ft(bx[2])} H' if bx[2] else '') + '</p>' + tp.box_svg(bx, col)) if bx else ''
            cards += (f'<div class="box"><h2>{i}. {html.escape(nm)}</h2>{boxl}<p><b>Size and place:</b> {html.escape(size)}</p><p><b>Materials:</b> {html.escape(mat)}</p>'
                      + (f'<p class="re"><b>Reuse:</b> {html.escape(reuse)}</p>' if reuse != '—' else '')
                      + f'<p><b>How to make it:</b></p><ol>{"".join(f"<li>{html.escape(s)}</li>" for s in steps)}</ol></div>')
        n = 5 + p // PER
        out += f'<section class="pg">{mc.head(k, "Every object, one by one: size, materials, how to make it", f"Page {n} of {npg(k)} · objects")}<div class="ob">{cards}</div></section>'
    return out

def team_cover(lab, ks):
    svg, legend = tp.team_layout_svg(ks)
    rows = ''.join(f'<tr><td><b>{k}</b></td><td>{html.escape(mv.NAMES[k])}</td><td>{mc.fd(*mc.window(k))}</td><td>{len(og.O[k])}</td></tr>' for k in ks)
    mats = ''.join(f'<li><b>{k}</b> · {html.escape(r[0])} ({html.escape(r[1])})</li>' for k in ks for r in mb.B[k]['rows'] if r[0] != 'Total')
    tools = '; '.join(f'{k}: {mb.B[k]["tools"]}' for k in ks)
    extra = '<p class="note">Block M is not assigned yet; it is in this pack as suggested.</p>' if 'M' in ks else ''
    return (f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>{html.escape(lab)} · team pack</h1><p>Crib 2026 · That Night in Bethlehem · your blocks: {", ".join(ks)} · everything your team builds, sizes in feet</p></div></div>'
            f'<div class="cols3" style="margin-top:6px;grid-template-columns:1.45fr 1fr"><div class="box"><h2>Your area on the stage (top view, 1 ft grid; x from the LEFT edge, y from the BACK wall)</h2>{svg}</div>'
            f'<div><div class="box"><h2>Your blocks</h2><table><tr><th>Block</th><th>Name</th><th>Build</th><th>Objects</th></tr>{rows}</table>{extra}</div>'
            f'<div class="box"><h2>How to use this pack</h2><ol><li>The map shows only your objects in colour, numbered, with x, y and height ranges in feet; grey is other teams. Never build on a grey area.</li><li>For each block: page 1 the look, page 2 the blueprint, page 3 every part with size and place, page 4 the steps, then every object one by one with its box size (W × D × H, feet) and a drawing.</li><li>Reuse first; screw, do not glue, anything wooden.</li><li>Tick "done when" on page 4 and hand over.</li></ol></div></div></div></section>'
            f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>{html.escape(lab)} · shopping and tools</h1><p>All materials for your blocks (no prices; ask the owner before buying)</p></div></div>'
            f'<div class="box" style="margin-top:6px"><h2>Materials</h2><ul class="two-col" style="font-size:12px">{mats}</ul></div><div class="box"><h2>Tools</h2><p style="font-size:12px">{html.escape(tools)}</p></div></section>')

def start_pages():
    d = os.path.join(ROOT, '2026', 'share', 'final-blueprint-3-views.png'); shutil.copy(d, os.path.join(OUT, 'img', 'final-blueprint.png'))
    shutil.copy(os.path.join(mc.GENDIR, 'crib-final-3q.jpg'), os.path.join(OUT, 'img', 'final-look.jpg')); shutil.copy(os.path.join(mc.GENDIR, 'crib-final-top.jpg'), os.path.join(OUT, 'img', 'final-top.jpg'))
    thumbs = ''
    for k in mb.ORDER:
        for n in mc.GEN.get(k, []):
            if mc.have(n): shutil.copy(os.path.join(mc.GENDIR, n + '.jpg'), os.path.join(OUT, 'img', n + '.jpg'))
    team = ''.join(f'<tr><td><b>{k}</b></td><td>{html.escape(mv.NAMES[k])}</td><td>{mc.fd(*mc.window(k))}</td><td>{html.escape(mb.B[k]["team"])}</td></tr>' for k in mb.ALL)
    checks = ['The church socket right behind the stage (back-left corner): exact spot and circuit rating', 'Deck height (2 ft assumed), size, level, and whether you may screw into it', 'Ceiling height (about 15 ft assumed) and ceiling type', 'Altar centred on the front wall; crib at its right end', 'Exit and the deck load rating', 'Work-at-height rules for hanging block I', 'How much 2023 plywood still exists']
    p1 = (f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>Crib 2026 · That Night in Bethlehem · crew pack</h1><p>Opens 24 December 2026 · stage 9 ft wide × 16 ft deep · 13 blocks (A, B, C, E to N; there is no D, the rock hill is part of B)</p></div></div>'
          f'<div class="cols" style="margin-top:6px"><div><img src="img/final-look.jpg" style="width:100%;border-radius:6px;border:1px solid #cfc9b8"><div style="display:flex;gap:6px;margin-top:5px;align-items:flex-start"><img src="img/final-top.jpg" style="height:96mm;border-radius:6px;border:1px solid #cfc9b8"><div style="font-size:11.5px;color:#444"><b>The finished crib</b> from the public spot and from directly above. Generated pictures: build to the blueprints on pages 2 and 3 of your block.</div></div></div>'
          f'<div><div class="box"><h2>Who builds what, and when</h2><table><tr><th>Block</th><th>Name</th><th>Build window</th><th>Team</th></tr>{team}</table></div>'
          f'<div class="box"><h2>How to use this pack</h2><ol><li>Find your block letter.</li><li>Page 1: what it looks like and a prompt for a picture of the finished block.</li><li>Page 2: the blueprint drawing. Page 3: every numbered part with its exact size and place, and the cut list. Page 4: the steps, in order. Pages 5 onward: every object one by one, with its size, materials (reuse first) and simple steps anyone can follow alone. Tick "done when" and hand over.</li></ol></div></div></div></section>')
    p2 = (f'<section class="pg"><div class="head" style="background:#2b2a33"><div><h1>The whole crib: front, side and top, plus the view from the public spot</h1><p>Feet. Stage 9 ft wide at the front × 16 ft deep. Letters are the block letters.</p></div></div>'
          f'<div class="box" style="margin-top:6px"><img src="img/final-blueprint.png" style="width:100%;max-height:150mm;object-fit:contain"></div>'
          f'<div class="box"><h2>Check on site first</h2>{"".join("<span style=&quot;margin-right:18px&quot;>☐ " + html.escape(c) + "</span>" for c in checks)}</div></section>').replace('&quot;', '"')
    return p1 + p2

if __name__ == '__main__':
    md = ['# Crew prompts (one per block)', '', 'Attach the final crib photo `2026/images/generated/crib-final-3q.jpg` and the block picture `2026/crew/img/<letter>-pic.png`.', '']
    bodies = []
    for k in mb.ALL:
        b1, prompt = page1(k); body = b1 + page2(k) + page3(k) + page4(k) + obj_pages(k); bodies.append(body)
        md += [f'## Block {k} · {mv.NAMES[k]}', '', '```', prompt, '```', '']
        hp = os.path.join(OUT, f'{k}-crew.html'); open(hp, 'w', encoding='utf8').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{body}')
        mb.pdf(hp, os.path.join(OUT, f'{k}-crew.pdf')); print(k)
    full = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{start_pages()}{"".join(bodies)}'
    open(os.path.join(OUT, 'crew-pack.html'), 'w', encoding='utf8').write(full); mb.pdf(os.path.join(OUT, 'crew-pack.html'), os.path.join(OUT, 'crew-pack.pdf'))
    open(os.path.join(OUT, 'crew-prompts.md'), 'w', encoding='utf8').write('\n'.join(md))
    by = dict(zip(mb.ALL, bodies))
    for lab, ks in tp.teams().items():
        slug = 'stage-team' if lab.startswith('Stage') else 'team-' + lab.split(':')[0].split()[-1]
        open(os.path.join(OUT, f'{slug}.html'), 'w', encoding='utf8').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{team_cover(lab, ks)}{"".join(by[k] for k in ks)}')
        mb.pdf(os.path.join(OUT, f'{slug}.html'), os.path.join(OUT, f'{slug}.pdf')); print(slug)
    print('done')
