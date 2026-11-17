"""Builds 2026/share/block-view-prompts.md and share-pack.pdf (final blueprint + each block's views + 5 image prompts per block).
Run after make_views.py and make_blocks.py: python source/make_prompts.py"""
import os, sys, html, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_blocks as mb
from make_views import NAMES, COL, light, dark

ROOT = mb.ROOT; SH = os.path.join(ROOT, '2026', 'share')

LOOK = {
 'A': ('A raised wooden platform, 9 ft WIDE across the front and 16 ft DEEP from front to back, so it is almost twice as deep as it is wide (ratio 16 to 9). The SHORT 9 ft side is the front (the public side); the LONG 16 ft side is the left side and runs away from the camera toward the back wall. Back and right sides are against church walls; black pleated skirting hangs only on the front and left sides. Plywood top, flat for the first 5.5 ft from the front, then a ramp rising over about 3.5 ft to a back area 3 ft higher. Along the LEFT edge in the back 7 ft there are four wide steps (3.4 ft wide), numbered 1 to 4 from the front, rising toward the back wall to 0.8, 1.2, 1.6 and 2.0 ft.',
       'bare 2x2 pine battens, 9-12 mm plywood skin, black pleated skirting, labelled section numbers in marker, service hatches with loose ply lids'),
 'B': ('A rugged limestone rock hill with horizontal strata, cracks and moss, rising in steps to a crest on the right, with a rough cave in the front: a rounded arch about 3 ft wide and 2.5 ft high, mouth turned 33 degrees toward the viewer, warm gold glow inside. In the cave: a carved stone manger with straw, Mary in blue and cream, Joseph in ochre holding a small lantern, baby Jesus in warm white, an ox and a donkey (2 ft hero figures). Flat top on the hill for the house.',
       'carved thermocol coated in plaster, sand and grout with real pebbles, dry-brushed sand then ochre then olive, near-black cave interior, lamp-gold LED glow, straw, clay, cloth'),
 'C': ('A whitewashed stone guest room with a flat roof and parapet, open front cut away to show sleeping travellers, clay jars and three small oil lamps, a stone outside stair of 8 steps, a cat on the roof.',
       'limestone-coloured plastered thermocol walls, terracotta jars, three warm flicker lamps, woven mats, wool blankets, wooden lintels'),
 'E': ('Four stepped dry-stone terraces with olive-green grass, a ring-shaped stone sheepfold with a thorn gate, a small round stone watchtower, two shepherds in earth-brown cloaks (one old with a staff, one young holding a lamb), six real-wool sheep and a small campfire.',
       'thermocol faced with carved dry-stone walls and real pebbles, soil and sand on the treads, artificial grass and moss, cream wool, clay figures'),
 'F': ("A low rocky ridge hiding a black box; behind it a clear acrylic sheet leaning at 45 degrees with a softly glowing translucent angel floating in mid-air in white-blue light; pale mist rolling over the ridge into the valley.",
       'plaster and thermocol rock, matt-black cloth and plywood housing, clear acrylic, a screen glow, ultrasonic mist'),
 'G': ('A narrow cobbled street rising toward the back between three flat-roofed whitewashed houses (2.0, 2.5 and 1.8 ft tall), a round stone well with a water pool, a Roman soldier and scribe at a census table with scrolls, two donkeys with panniers and two travellers. Warm window lamps.',
       'limestone-coloured plaster, sand-coloured cobbles of cork or clay, ochre wooden doors, tiny terracotta jars, flicker LED window lamps'),
 'H': ('A hidden electronics block: a control box with relay and MOSFET boards, power supplies, a DFPlayer and two small speakers, a thin strip of golden light set in fine sand running from the front edge to the cave mouth, and two violet UV bars.',
       'matt-black project boxes, labelled cables with service loops, aluminium channel with frosted diffuser and fine sand on top, small pebbles along the edge'),
 'I': ('A glowing gold star burst about 2 ft wide hung from the ceiling corner with 60 strands of clear crystal beads falling 6 ft, and a three-turn spiral ribbon of white cotton clouds carrying 30 tiny white angels, curling down toward the hill.',
       'foam-core star with silver tinsel, crystal beads on fishing line, galvanised wire helix skinned in polyfill, paper and feather angels, micro-LED fairy lights'),
 'J': ('A corner backdrop on both walls: the lower 5 ft is a printed twilight Judean hills scene (sand to ochre to dusk violet, a flat-topped fortress, an olive grove), above it deep midnight-blue pleated velvet drape to the ceiling with gold paper stars, hundreds of tiny fibre-optic stars and a choir of 12 UV angels glowing violet-white.',
       'matt fabric print, 1.5x-fullness pleated midnight-blue drape on rings, gold card stars, fibre-optic ends, UV-reactive paint'),
 'K': ('A tiny pale far village of 20 cream houses (3-5 in tall) along the crest, and above it a thin wall shelf painted as a road carrying a miniature caravan of three kings on camels with a servant, each king with a tiny gold lantern.',
       'thermocol and clay houses in limestone tinted with mist blue, micro-LED lanterns, 1:24 painted figures'),
 'L': ('Two gnarled olive trees (2.0 and 1.6 ft), a small wooden plaque with twelve tiny icons for "find 12 details", a jute rope barrier with four brass or wooden posts, and a floor marker for the public viewing spot.',
       'wire and jute trunks wrapped in paper, dried olive leaves, dark and low-saturation olive green, wood and brass posts, printed icons'),
}

ORIENT = ('STAGE ORIENTATION (do not swap): the stage is 9 ft wide across the FRONT and 16 ft DEEP. The front, public edge is the SHORT 9 ft side. The LEFT side is the LONG 16 ft side running away from the viewer to the back wall. The back wall is 9 ft, the right wall is 16 ft. ')
PRE = (ORIENT + 'Attached is a three-view line drawing (front, side, top) of ONE build block of a handmade Christmas crib, to scale. '
       'Keep the exact proportions, positions and the number of parts. Real physical handmade model, not CGI, not an illustration. '
       'No Christmas tree, no snow, no text, no people other than the figures described. Palette: lamp gold, warm white, Mary blue, midnight blue, dusk violet, mist blue, limestone, sand, ochre, olive; no red, bright green or pink.')

def prompts(k):
    b = mb.B[k]; look, mat = LOOK[k]
    what = f'BLOCK {k}, {NAMES[k]}: {look}'
    size = b['where']
    common = f'{PRE}\n\n{what}\nSize and place: {size}\nMaterials: {mat}.'
    return [
     ('Front view', f'{common}\n\nCreate ONE studio photograph of this block seen straight from the FRONT (public side), camera level with the middle of the block, no perspective distortion, centred, plain light-grey seamless background, soft even light, sharp focus, 16:9.'),
     ('Side view', f'{common}\n\nCreate ONE studio photograph of this block seen straight from the LEFT SIDE (back wall on the left of the picture, front on the right), camera level with the middle of the block, no perspective distortion, plain light-grey seamless background, soft even light, 16:9.'),
     ('Top view', f'{common}\n\nCreate ONE studio photograph of this block seen straight DOWN from directly above (back wall at the top of the picture, public side at the bottom), no perspective distortion, plain light-grey background, soft even light, 1:1.'),
     ('Three-quarter hero view', f'{common}\n\nCreate ONE hero photograph of this block from the front-left at a three-quarter angle and slightly above, turned about 33 degrees exactly as in the fourth (tilted) panel of the attached drawing, as it will be seen by the public, soft warm studio light with a gentle shadow, plain neutral background, shallow depth of field, 16:9.'),
     ('Detail close-up', f'{common}\n\nCreate ONE macro close-up photograph of the most important detail of this block (the figures, texture or lighting), showing real handmade surface texture, slightly imperfect, warm light, shallow depth of field, 4:3.'),
    ]

def md():
    o = ['# Crib 2026: view prompts for every block (to share with the group)', '',
         '**How to use:** for each block, attach its three-view drawing from `2026/share/block-views/<letter>-views.png` (and, for the hero view, the master `final-blueprint-3-views.png`) to your image model, then paste the prompt. The three-view drawing is the exact layout; the prompt supplies materials and look. If a result drifts, add: "keep the exact proportions from the attached drawing".', '',
         '**Master drawing:** `2026/share/final-blueprint-3-views.png`', '']
    for k in mb.ORDER:
        o += [f'## Block {k} · {NAMES[k]}', '', f'Attach: `2026/share/block-views/{k}-views.png`', '']
        for t, p in prompts(k):
            o += [f'### {k} · {t}', '', '```', p, '```', '']
    return '\n'.join(o)

def pack():
    css = mb.CSS + 'pre{white-space:pre-wrap;font:11.5px/1.4 Consolas,monospace;background:#f6f4ee;border:1px solid #d9d4c6;border-radius:5px;padding:7px;margin:4px 0 8px}h3{margin:6px 0 0;font-size:13px}.im{width:100%;border:1px solid #cfc9b8;border-radius:4px}'
    body = [f'<section class="sheet"><div class="head" style="background:#2b2a33"><div><h1>Crib 2026 · That Night in Bethlehem</h1><p>Final blueprint: front, side and top views. Share pack for the group.</p></div></div><div class="box" style="margin-top:10px"><img class="im" src="final-blueprint-3-views.png"></div><div class="box" style="margin-top:10px"><h2>How to use</h2><ol><li>Pick your block (A to L) on the next pages.</li><li>Attach its three-view drawing to the image model.</li><li>Paste one of the five prompts (front, side, top, three-quarter, detail).</li><li>Send the result to the group lead to check against the drawing.</li></ol></div></section>']
    for k in mb.ORDER:
        ps = ''.join(f'<h3>{k} · {t}</h3><pre>{html.escape(p)}</pre>' for t, p in prompts(k))
        body.append(f'<section class="sheet"><div class="head" style="background:{mb.rgb(k)}"><div class="letter">{k}</div><div><h1>{html.escape(NAMES[k])}</h1><p>{html.escape(mb.B[k]["items"])}</p></div></div><div class="box" style="margin-top:10px"><img class="im" src="block-views/{k}-views.png"></div><div class="box" style="margin-top:10px"><h2>Image prompts</h2>{ps}</div></section>')
    page = f'<!doctype html><html><head><meta charset="utf-8"><title>Crib 2026 share pack</title><style>{css}</style></head><body>{"".join(body)}</body></html>'
    hp = os.path.join(SH, 'share-pack.html'); open(hp, 'w', encoding='utf8').write(page)
    mb.pdf(hp, os.path.join(SH, 'share-pack.pdf'))

if __name__ == '__main__':
    open(os.path.join(SH, 'block-view-prompts.md'), 'w', encoding='utf8').write(md())
    pack(); print('done')
