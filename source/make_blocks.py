"""Builds one blueprint + build-guide sheet per block (A-L) from 2026/pack/index.html.
Run from anywhere: python source/make_blocks.py   (needs Pillow and Chrome or Edge)
Output: 2026/blocks/ (HTML, PDF, img/) and 2026/blocks/all-blocks.pdf
"""
import re, html, os, subprocess, glob, base64
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '2026', 'blocks'); IMG = os.path.join(OUT, 'img')
os.makedirs(IMG, exist_ok=True)
PACK = open(os.path.join(ROOT, '2026', 'pack', 'index.html'), encoding='utf8').read()
PLAN = Image.open(os.path.join(ROOT, '2026', 'images', 'layout-plan-only.png')).convert('RGBA')
S, OX, OY = 1.6, 20, 90

COL = {'A': (120,120,120), 'B': (230,120,20), 'C': (200,50,50), 'E': (40,150,70), 'F': (120,60,200),
       'G': (30,110,220), 'H': (210,170,0), 'I': (0,170,190), 'J': (60,60,160), 'K': (230,60,160), 'L': (110,200,60)}

def rect(x1, y1, x2, y2): return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
SHAPES = {  # displayed-plan coordinates of the 2000px blueprint
 'A': [('p', rect(205,95,655,900))],
 'C': [('p', [(410,305),(578,415),(520,505),(352,395)])],
 'B': [('p', [(358,330),(545,462),(500,545),(308,466)]), ('p', [(350,205),(470,195),(590,330),(580,420),(500,590),(310,490)])],
 'E': [('p', rect(226,178,327,243)), ('p', rect(217,444,300,574)), ('e', (355,145,25)),
       ('p', [(205,95),(375,95),(375,200),(350,205),(305,470),(205,440)])],
 'F': [('p', rect(222,255,342,374))],
 'G': [('p', rect(585,565,655,645)), ('p', rect(585,660,655,750)), ('p', rect(585,765,655,855)), ('p', rect(436,594,496,624)),
       ('e', (490,655,27)), ('p', rect(431,734,501,783)), ('p', rect(516,560,572,893))],
 'H': [('p', [(298,895),(312,895),(405,515),(390,508)]), ('p', rect(208,658,224,684)), ('p', rect(585,853,647,893)),
       ('p', rect(385,100,650,335))],
 'I': [('p', [(585,145),(605,150),(535,350),(500,340)]), ('e', (595,152,16))],
 'K': [('p', rect(597,355,637,545)), ('p', rect(641,365,656,545))],
 'L': [('e', (270,805,33)), ('e', (475,840,25)), ('p', rect(366,870,466,889)), ('e', (55,1045,22))],
 'J': [('p', rect(205,80,680,94)), ('p', rect(656,80,680,1045))],
}
def P(pts): return [(x*S-OX, y*S-OY) for x,y in pts]

def draw_block(k, zoom):
    im = PLAN.copy()
    wash = Image.new('RGBA', im.size, (255,255,255,150)); im = Image.alpha_composite(im, wash)
    ov = Image.new('RGBA', im.size, (0,0,0,0)); d = ImageDraw.Draw(ov); xs, ys = [], []
    for kind, g in SHAPES[k]:
        if kind == 'p':
            pts = P(g); d.polygon(pts, fill=COL[k]+(150,), outline=COL[k]+(255,)); d.line(pts+[pts[0]], fill=COL[k]+(255,), width=5)
            xs += [p[0] for p in pts]; ys += [p[1] for p in pts]
        else:
            cx, cy, r = g; box = [(cx-r)*S-OX,(cy-r)*S-OY,(cx+r)*S-OX,(cy+r)*S-OY]
            d.ellipse(box, fill=COL[k]+(150,), outline=COL[k]+(255,), width=5); xs += [box[0],box[2]]; ys += [box[1],box[3]]
    im = Image.alpha_composite(im, ov).convert('RGB')
    if zoom:
        m = 130; x0, x1 = max(0,min(xs)-m), min(im.width,max(xs)+m); y0, y1 = max(0,min(ys)-m), min(im.height,max(ys)+m)
        im = im.crop((int(x0),int(y0),int(x1),int(y1)))
    return im

def save(k, zoom):
    p = os.path.join(IMG, f'{k}-{"zoom" if zoom else "plan"}.jpg'); draw_block(k, zoom).save(p, quality=90); return f'img/{os.path.basename(p)}'

# ---------- parse pack parts ----------
def part(n):
    a = PACK.find(f'<details id="part{n}"'); b = PACK.find('</details>', a); s = PACK[a:b]
    svgs = re.findall(r'<div class=draw>(<svg.*?</svg>)</div>', s, flags=re.S)
    rows = []
    for r in re.findall(r'<tr>(.*?)</tr>', s, flags=re.S):
        cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, flags=re.S)]
        if len(cells) == 5 and cells[0] != 'Item': rows.append(cells)
    li = [html.unescape(re.sub(r'<[^>]+>', '', x)) for x in re.findall(r'<li>(.*?)</li>', s.split('How to build it')[-1], flags=re.S)]
    warn = re.search(r'Check before cutting</h3>(.*?)</div>', s, flags=re.S)
    return dict(svgs=svgs, rows=rows, steps=li, warn=html.unescape(re.sub(r'<[^>]+>', '', warn.group(1))).strip() if warn else '')
PARTS = {n: part(n) for n in range(12)}

def n(x): return int(x.replace(',', '') or 0)
def fmt(v):
    s = str(v);
    if len(s) <= 3: return s
    h, t = s[:-3], s[-3:]; out = []
    while len(h) > 2: out.insert(0, h[-2:]); h = h[:-2]
    if h: out.insert(0, h)
    return ','.join(out + [t])
def pick(p, keys=None, skip=None):
    out = []
    for r in PARTS[p]['rows']:
        if r[0] == 'Total': continue
        if keys and not any(r[0].startswith(k) for k in keys): continue
        if skip and any(r[0].startswith(k) for k in skip): continue
        out.append(r)
    return out

# ---------- block definitions ----------
B = {}
def add(k, **kw): B[k] = kw

add('A', name='Stage frame and rake', file='A-stage-frame', parts=[0], items='5 base, 12 base (the raked deck every other block sits on)',
    window='20 Nov → 10 Dec', days='6', team='Carpentry crew of 2–3',
    where='Whole stage 9 × 16 ft. Raked from 0 at the front to +3.0 ft at the hill crest; terrace bands +0.8, +1.2, +1.6, +2.0 on the left.',
    rows=pick(0),
    steps=PARTS[0]['steps'],
    before=['Measure the real deck height, size and load rating; the leg heights assume a 2 ft deck.', 'Mark the 9 × 16 ft grid on the deck with tape.', 'Number every 4 × 4 ft frame section so it can be put back in the same place.'],
    done=['Frame is level across and rigid: two people can stand on any panel with no flex.', 'Service hatches A (control box), B (angel and mister) and C (speaker) open freely and are labelled.', 'Skirting on the open front and left edges hides the deck completely.', 'Every section passes through the church door.'],
    hands='Everything stands on A. Blocks B, C, E, G, K go on after A is placed. H uses the hatches.',
    tools='Saw, drill, screw gun, spirit level, measuring tape, staple gun')
add('B', name='Cave, rock hill and Holy Family', file='B-cave-hill-holy-family', parts=[1], items='2 cave, 3 Holy Family with ox, donkey and manger, 5 rock hill around them',
    window='23 Nov → 14 Dec', days='14', team='Rock and plaster group + figures and painting group',
    where='One unit about 7 × 6 × 3 ft (hill) with a 4 × 2.5 ft cave in it, turned 33° so the 3 ft wide mouth faces the public spot V. Arch 2.5 ft high. Hill rises to +3.0 ft at the crest on the right wall. Figures 2 ft (hero scale 1:3), ox and donkey about 1 ft. Keep 1 ft free behind for wiring.',
    rows=pick(1),
    steps=['Glue 4 in thermocol into a block (about 7 × 6 × 3 ft); seal every layer with PVA.',
           'Carve strata and cracks with a hot knife; cut the cave 4 × 2.5 ft inside with an arch 3 ft wide × 2.5 ft high.',
           'Mesh the arch and overhangs; coat everything with PoP + PVA, 3 mm; press grout, pebbles and dry grass on while wet.',
           'Dry-brush sand, then ochre, then olive; darker in the cracks. Paint the cave inside near-black so the gold glows; keep the rock around the cave one shade darker.',
           'Hide a warm COB LED above the lintel; keep its wires out of the plaster and run them to hatch A. Leave a 1 ft service gap behind.',
           'Make or repaint the manger (thermocol + plaster) and the clay lamp; lay straw.',
           'Place the figures last: Mary (Mary blue, limestone veil), Joseph (ochre-umber), baby on warm-white straw, ox and donkey beside.',
           'Mark the cross-shadow lamp position for the 3:00 cue, then split the whole unit into numbered pieces that pass through the church door.'],
    before=['Wear a mask for PoP dust; cut thermocol outdoors; fire-retardant spray every cut surface.', 'Decide: buy new 2 ft figures (₹18,000) or reuse and repaint the 2023 set (₹8,000).', 'Cut a cardboard template of the cave arch and check it clears the house floor (block C) at +2.8 ft.'],
    done=['Strata look random, no bright white thermocol shows, and the rock reaches +3.0 ft at the crest.', 'Glow test: dimmer at 2200–2700 K; the cave is the brightest object but does not blow out the baby.', 'From V the manger and baby are visible and not hidden by the arch.', 'Every piece fits through the church door; LED wires reach hatch A with a 1 ft service loop.'],
    hands='C (house) rests on two posts standing on the cave base. E (terraces) abuts the left side and K sits on the crest. H feeds the cave LED and the cross-shadow lamp.',
    tools='Hot-wire cutter, hot knife, trowel, mesh cutters, glue gun, brushes, soldering iron (LED), sculpting clay, dust mask')
add('C', name='House with upper room', file='C-upper-house', parts=[2], items='4 house with the upper guest room (kataluma), cut open',
    window='30 Nov → 14 Dec', days='5', team='Carpentry + small-figure painters',
    where='4 × 2 ft room, floor at +2.8 ft, room height 1.5 ft, over the cave. Open front cut away and turned 33° towards V. Stone steps rise 2.8 ft in 8 steps.',
    rows=pick(2), steps=PARTS[2]['steps'],
    before=['Take the cave arch height (2.5 ft) from block B; the ply floor tray must clear it.', 'Gather six 1:6 sleeping travellers (about 1 ft long) or clay to make them.'],
    done=['Whole room weighs under 8 kg and sits on the posts, not on the cave roof.', 'Three flicker lamps work on one 3 V line.', 'Hidden details placed: cat on the roof, clay oven, sleeping child.', 'Lifts off the cave as one piece.'],
    hands='Sits on B. Lamp wires go down through the hill to hatch A (control box).',
    tools='Hot knife, hobby saw, glue gun, small brushes')
add('E', name="Shepherds' field", file='E-shepherds-field', parts=[4], items='8 shepherds, sheep and campfire; 11 sheepfold; 12 terraces; 13 watchtower',
    window='26 Nov → 16 Dec', days='8', team='Figures and painting group',
    where='Left side of the stage: four terrace boxes 3.4 ft wide over a 7 ft run at +0.8, +1.2, +1.6, +2.0 ft. Shepherds 1.2 ft (1:6), sheep 0.45 ft, fold 1:12, tower 1.5 ft.',
    rows=pick(4), steps=PARTS[4]['steps'],
    before=['Blocks E and F (floating angel) share this zone; agree the ridge position with block F before fixing the boxes.'],
    done=['Four boxes level and screwed to A; treads covered with soil/sand and grass.', 'Campfire LED flickers warm orange and is hidden from the front.', 'Sheep, shepherds and fold are paler and cooler than the village (tier B–C).', 'Boxes lift out singly.'],
    hands='Sits on A. Campfire LED and field flood use H. Ridge and screen (F) sit in the same zone.',
    tools='Hot knife, glue gun, brushes, soldering iron')
add('F', name='Floating angel unit', file='F-floating-angel', parts=[5], items='9 floating angel (Pepper\'s ghost), 10 rock ridge with mist tray',
    window='6 Dec → 22 Dec', days='4', team='Electronics lead + one painter',
    where='Black box 2.4 × 1.4 ft behind a 0.8 ft rock ridge in the left field. Acrylic 2.4 × 2 ft at 45°. Mister tray behind the ridge lip, hatch B below.',
    rows=pick(5), steps=PARTS[5]['steps'],
    before=['Decide screen: reuse a tablet you own (free) or buy a monitor plus Pi Zero.', 'Make the 20 second looping angel video: white on pure black, mirrored left to right.'],
    done=['Ghost test at night from V: angel appears to hang in the air, rocks visible through it.', 'Mist rolls forward into the valley and never reaches the screen.', 'Float switch cuts the mister when water is under 3 cm.', 'No fingerprints on the acrylic; microfibre cloth in the kit.'],
    hands='Sits on A in the field next to E. Needs power and the mister relay from H (1:00–3:30), hatch B for service.',
    tools='Jigsaw, black cloth, hot glue, tablet or monitor, spirit level')
add('G', name='Village street', file='G-village-street', parts=[6], items='16–18 three houses, 19 cobbled street, 20 well, 21 census table, 22 donkeys and travellers',
    window='30 Nov → 19 Dec', days='10', team='Rock and plaster + figures groups',
    where='Strip along the right wall, 1.1 × 6.7 ft street sloping +0.8 to +0.3 ft. Houses 2.0 / 2.5 / 1.8 ft tall at 1:6, well 0.9 ft, figures 1.2 ft.',
    rows=pick(6, skip=('Olive', 'Plaque')), steps=[s for s in PARTS[6]['steps'] if 'olive' not in s.lower()] + ['Place census scene and donkeys after the street is dry.'],
    before=['Keep 1 in clear between house tops and the drape bottom (block J).', 'Gather props: jars, baskets, barrels.'],
    done=['Three houses plastered and lit; 15 window lamps work on a 3 V line.', 'Street slopes smoothly, drainage channel cut.', 'Well pool sealed with resin and holds water.', 'Figures at 1:6 stand without glue; wires reach hatch A.'],
    hands='Sits against the right wall on A. Window lamps feed to hatch A (H). Olive trees and plaque are in block L.',
    tools='Hot knife, plaster, cork, resin, glue gun, small brushes')
add('H', name='Lights and control', file='H-lights-control', parts=[3, 10], items='1 path of light, 27 control box, 28 speakers, 29 UV bars, all light channels and the 4-minute show',
    window='23 Nov → 22 Dec (bench build first)', days='9', team='Electronics and show-control group + an electrician for 2 days',
    where='Control box under the deck at hatch A (front right). Path of light 0.5 × 7.7 ft from the front edge to the cave mouth. Speakers at hatch C. UV bars behind the backdrop lip.',
    rows=pick(3) + pick(10), steps=['PATH OF LIGHT'] + PARTS[3]['steps'] + ['SHOW CONTROL'] + PARTS[10]['steps'],
    before=['Wire everything on a bench board first; test every channel for 10 seconds.', 'Confirm the church socket and its circuit rating.'],
    done=['Every channel cues correctly on the 4-minute sheet; the loop restarts at 3:55.', 'Path chase runs front edge to cave mouth in 7 s and never crosses a solid.', 'Audio at 60 dB or less at V.', 'An electrician has checked earthing and the RCCB; no mains voltage inside the crib.'],
    hands='Feeds B, C, E, F, G, I, J and K. Install it last in the church, but build and test it on a bench from week 1.',
    tools='Soldering iron, multimeter, wire strippers, laptop, heat-shrink')
add('I', name='Sky: cloud spiral and star', file='I-sky-cascade', parts=[8], items='6 cloud and angel spiral, 7 star burst with bead strands',
    window='30 Nov → 21 Dec', days='8', team='Rigging lead + 2 helpers (ladder or scaffold, two people at all times)',
    where='Hung from the ceiling over the right-front corner, star 2 ft wide about 1 ft below the ceiling, 60 bead strands 6 ft long, spiral 2.5 ft wide ending 4.5 ft above the deck, 30 mini angels.',
    rows=pick(8), steps=PARTS[8]['steps'],
    before=['Measure the ceiling height and check its type (concrete, beam or plasterboard); this decides the anchors and the line lengths.', 'Ask the church about working at height and scaffold use.'],
    done=['Built and lit at floor level first; hung last.', 'Two lines per hang point, never a single line.', 'Spiral points down towards the manger; star is the highest point from V.', 'Cascade lines stay 2 m clear of any sambrani holder.'],
    hands='Hangs above A and B. Fairy lights and the star LED run on H. Do not hang before the backdrop track (J) is fitted.',
    tools='Ladder or scaffold, plumb line, pliers, wire cutters, fire-retardant spray')
add('J', name='Backdrop', file='J-backdrop', parts=[9], items='26 hills print, blue drape, gold stars, fibre-optic stars, UV angel choir',
    window='20 Nov → 20 Dec', days='8', team='Backdrop and rigging group',
    where='Both walls: back wall 9 ft and right wall 16 ft with a rounded corner. Print 5 ft high, blue drape above to the ceiling (about 13 ft above the deck), 250 fibre ends, 12 UV angels 2 ft tall.',
    rows=pick(9), steps=PARTS[9]['steps'],
    before=['Order the print and drape early; they are long-lead items.', 'Measure the real ceiling height; drape cost scales with it (about ₹280 per extra foot of drop).'],
    done=['Track and rope backup are fitted; print joins are flat and tape-free from V.', 'Drape pleats are even at 1.5× fullness and the hem laps the print by 6 in.', 'UV angels are invisible with lights on and glow violet in the dark.', 'Fibre ends twinkle without hotspots.'],
    hands='Hangs on both walls. A blue strip along the walls appears in the plan. Houses (G) leave 1 in below the drape. UV bars and fibre engine are fed by H.',
    tools='Drill, rope, clamps, sewing machine, scissors, UV torch for testing')
add('K', name='Far village and Magi caravan', file='K-far-village-magi', parts=[7], items='14 far village (1:24), 15 Magi caravan on a wall shelf',
    window='10 Dec → 19 Dec', days='4', team='One miniature builder',
    where='Right-wall crest: far village strip 3.8 × 0.8 ft at y 5.2–9.0 and +3.0 ft; Magi shelf 3 × 0.3 ft at +3.6 ft. Both sit at bearings 38–49° from V, clear of the cave house (25–41°).',
    rows=pick(7), steps=PARTS[7]['steps'],
    before=['Re-run the sightline check from V before fixing; the first layout hid both behind the house.'],
    done=['From V both are visible and not covered by the house.', 'Far village is pale cream with blue shadows (tier D: paler, cooler, less saturated).', 'Each king has a micro-LED lantern that glows from 3:30.', 'Strip and shelf are fixed firmly; nothing overhangs the street.'],
    hands='Sits on the crest of B and the right wall. Micro-LEDs wire back to hatch A (H).',
    tools='Craft knife, tweezers, small brushes, micro-LED kit')
add('L', name='Foreground and view spot', file='L-foreground-view-spot', parts=[11], items='23–24 olive trees, 25 "find 12 details" plaque, 30 public view spot and rope',
    window='19 Dec → 23 Dec (olives and plaque can start earlier)', days='4', team='Easy tasks for helpers',
    where='View spot V is 3 ft left and 3 ft in front of the stage corner. Rope barrier curved 5 ft from the stage front, 4 ft clear aisle. Olive 23 at front-left (1.0, 14.2), plaque 2 × 0.4 ft at the front edge.',
    rows=pick(11) + pick(6, keys=('Olive', 'Plaque')),
    steps=PARTS[11]['steps'] + ['Make the two olive trees (wire, jute, paper, dried leaves, umber trunks) and place them as the dark framing in the front corners.', 'Make the plaque with 12 hidden details and place it at the front edge.'],
    before=['Confirm the extinguisher location and the exit with the church.', 'Print the signs (A4, large type).'],
    done=['Six people can stand at V with the full view.', '4 ft clear aisle for wheelchairs at the rope; cables under a ramp or taped flat.', 'Olive trees are darker and less saturated than the field behind.', 'Extinguisher and exit are marked.'],
    hands='Last to place. Plaque and olives are on A at the front; the rope and signs are on the church floor.',
    tools='Rope, posts, floor tape, printer, wire, jute')

ORDER = list('ABCEFGHIJKL')
SEQ = ['Start now (no dependencies): A frame, H bench build, J order and print, figures for B, C, E and G.',
       'After A is framed: B (cave, hill and Holy Family), C, then E, G and K.',
       'Last: I (needs the ceiling height), L, then wiring and aim.']

# ---------- html ----------
CSS = """
@page{size:297mm 420mm;margin:9mm}
*{box-sizing:border-box}
body{margin:0;font:12.5px/1.45 'Segoe UI',Arial,sans-serif;color:#1d1d22;background:#fff}
.sheet{page-break-after:always;padding:0}
.sheet:last-child{page-break-after:auto}
.head{display:flex;align-items:center;gap:18px;padding:12px 18px;color:#fff;border-radius:6px}
.letter{font:700 64px/1 'Segoe UI',Arial,sans-serif;width:84px;text-align:center}
.head h1{margin:0;font-size:28px;line-height:1.1}.head p{margin:4px 0 0;font-size:13px;opacity:.95}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
.chips span{background:#efece3;border-radius:999px;padding:3px 10px;font-size:12px}
.row{display:grid;gap:12px;margin-top:10px}
.r2{grid-template-columns:1fr 1fr}.r2i{grid-template-columns:.7fr 1.3fr}
.box{border:1px solid #cfc9b8;border-radius:6px;padding:10px 12px}.box.keep{break-inside:avoid}
.box h2{margin:0 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:#555}
.box img{width:100%;max-height:560px;object-fit:contain;display:block;border:1px solid #cfc9b8;border-radius:4px}
.draw svg{width:100%;max-height:640px;height:auto;display:block;border:1px solid #cfc9b8;border-radius:4px}
.draw{margin-bottom:8px;break-inside:avoid}
table{border-collapse:collapse;width:100%;font-size:12px}
th,td{border-bottom:1px solid #ddd8c8;padding:4px 6px;text-align:left;vertical-align:top}
th{background:#efece3}td.n,th.n{text-align:right;white-space:nowrap}tr.tot td{font-weight:700;border-top:2px solid #888}
ol,ul{margin:4px 0 0;padding-left:20px}.row{break-inside:auto}li{margin-bottom:4px}
.chk li{list-style:none;margin-left:-18px}.chk li:before{content:'\\2610  '}
.warn{background:#fbeeeb;border-color:#a8322c}.warn h2{color:#a8322c}
.sec{font-weight:700;margin:6px 0 0;list-style:none;margin-left:-20px;color:#444}
.cover h1{font-size:34px;margin:0 0 4px}.legend{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;margin:10px 0}
.legend div{display:flex;gap:10px;align-items:center}.legend i{width:26px;height:20px;border:1px solid #000;display:inline-block}
"""

def rgb(k): return 'rgb(%d,%d,%d)' % COL[k]

def sheet(k):
    b = B[k]; rows = b['rows']
    tot = [sum(n(r[i]) for r in rows) for i in (2, 3, 4)]
    zoom_img = None
    xs = [p for kind, g in SHAPES[k] for p in ([x*S-OX for x, y in g] if kind == 'p' else [(g[0]-g[2])*S-OX, (g[0]+g[2])*S-OX])]
    ys = [p for kind, g in SHAPES[k] for p in ([y*S-OY for x, y in g] if kind == 'p' else [(g[1]-g[2])*S-OY, (g[1]+g[2])*S-OY])]
    area = (max(xs)-min(xs))*(max(ys)-min(ys)) / (PLAN.width*PLAN.height)
    full = save(k, False)
    imgs = f'<div class="box"><h2>Where it sits on the layout</h2><img src="{full}"></div>'
    if area < 0.35:
        zoom_img = save(k, True)
        imgs = f'<div class="row r2i"><div class="box"><h2>Where it sits</h2><img src="{full}"></div><div class="box"><h2>Close-up</h2><img src="{zoom_img}"></div></div>'
    draws = ''.join(f'<div class="draw">{s}</div>' for p in b['parts'] for s in PARTS[p]['svgs'])
    trs = ''.join('<tr><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % tuple(html.escape(c) for c in r) for r in rows)
    trs += '<tr class="tot"><td colspan="2">Total for this block</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % tuple(fmt(t) for t in tot)
    steps = ''
    c = 0
    for s in b['steps']:
        if s.isupper(): steps += f'<li class="sec">{s.title()}</li>'; c = 0
        else: c += 1; steps += f'<li value="{c}">{html.escape(s)}</li>'
    li = lambda xs, cls='': f'<ul class="{cls}">' + ''.join(f'<li>{html.escape(x)}</li>' for x in xs) + '</ul>'
    warns = [PARTS[p]['warn'] for p in b['parts'] if PARTS[p]['warn']]
    return f"""<section class="sheet">
<div class="head" style="background:{rgb(k)}"><div class="letter">{k}</div><div><h1>{html.escape(b['name'])}</h1><p>{html.escape(b['items'])}</p></div></div>
<div class="chips"><span>Build window: {b['window']}</span><span>About {b['days']} person-days</span><span>{html.escape(b['team'])}</span><span>Cost: Prop-only &#8377;{fmt(tot[0])} · Lean &#8377;{fmt(tot[1])} · Full &#8377;{fmt(tot[2])}</span></div>
<div class="box"><h2>Position and size</h2>{html.escape(b['where'])}</div>
{imgs}
<div class="row"><div class="box"><h2>Blueprint drawings (dimensioned)</h2>{draws}</div></div>
<div class="row r2"><div class="box"><h2>Materials (&#8377;)</h2><table><tr><th>Item</th><th>Qty</th><th class="n">Prop-only</th><th class="n">Lean</th><th class="n">Full</th></tr>{trs}</table><p style="margin:6px 0 0"><b>Tools:</b> {html.escape(b['tools'])}</p></div>
<div class="box"><h2>How to build it, in order</h2><ol>{steps}</ol></div></div>
<div class="row r2"><div class="box"><h2>Before you start</h2>{li(b['before'])}{''.join(f'<div class="box warn" style="margin-top:8px"><h2>Check before cutting</h2>{html.escape(w)}</div>' for w in warns)}</div>
<div class="box"><h2>Done when (tick each)</h2>{li(b['done'], 'chk')}<h2 style="margin-top:10px">Hands over to</h2>{html.escape(b['hands'])}</div></div>
</section>"""

def cover():
    leg = ''.join(f'<div><i style="background:{rgb(k)}"></i><b>{k}</b> {B[k]["name"]} <span style="color:#777">· {B[k]["window"]}</span></div>' for k in ORDER)
    return f"""<section class="sheet cover"><h1>Crib 2026 · That Night in Bethlehem</h1><p>Eleven independent build blocks (there is no D: the rock hill is part of B). Each sheet has its own plan, drawings, materials, steps and a done-when checklist.</p>
<div class="box"><img src="{ 'img/overview.jpg' }"></div><div class="legend">{leg}</div>
<div class="box"><h2>Order of work</h2><ol>{''.join(f'<li>{html.escape(s)}</li>' for s in SEQ)}</ol></div></section>"""

def wrap(body): return f'<!doctype html><html><head><meta charset="utf-8"><title>Crib 2026 build blocks</title><style>{CSS}</style></head><body>{body}</body></html>'

def chrome():
    for p in ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe']:
        if os.path.exists(p): return p

def pdf(htmlpath, pdfpath):
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--user-data-dir=' + os.path.join(os.environ.get('TEMP', '.'), 'crib_chrome_profile'), '--virtual-time-budget=5000', '--no-pdf-header-footer', f'--print-to-pdf={pdfpath}', 'file:///' + htmlpath.replace('\\', '/')], check=True, capture_output=True, timeout=90)

if __name__ == '__main__':
    Image.open(os.path.join(ROOT, '2026', 'images', 'layout-plan-blocks.png')).convert('RGB').save(os.path.join(IMG, 'overview.jpg'), quality=90)
    allbody = cover()
    open(os.path.join(OUT, '00-overview.html'), 'w', encoding='utf8').write(wrap(cover()))
    pdf(os.path.join(OUT, '00-overview.html'), os.path.join(OUT, '00-overview.pdf'))
    for k in ORDER:
        s = sheet(k); allbody += s
        hp = os.path.join(OUT, B[k]['file'] + '.html'); open(hp, 'w', encoding='utf8').write(wrap(s))
        pdf(hp, os.path.join(OUT, B[k]['file'] + '.pdf')); print(k, 'ok')
    ap = os.path.join(OUT, 'all-blocks.html'); open(ap, 'w', encoding='utf8').write(wrap(allbody)); pdf(ap, os.path.join(OUT, 'all-blocks.pdf'))
    print('done')
