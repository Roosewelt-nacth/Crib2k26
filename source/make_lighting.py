"""Lighting layout (top view): where every light goes, cable trunks from the single distribution box, colours.
Run: python source/make_lighting.py -> 2026/images/lighting-plan.png  (needs make_views.py and Chrome)"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_views as mv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '2026', 'images', 'lighting-plan.png')

WARM = '#F2B84B'      # lamp gold, 2200-2700 K
WWHITE = '#FFF1CF'    # warm white 2700-3000 K
NEUTRAL = '#F5E6B8'   # warm-neutral 3500-4000 K (field flood)
COOL = '#DCEBFA'      # cool white 5000-6500 K
INDIGO = '#1A2A78'    # night-sky wash (blue gel)
VIOLET = '#5B4A9A'    # UV 395 nm
MIST = '#AEBBD9'      # pond / angel cool
TRUNK = '#444450'

# (kind, label, [(x, y), ...])
LIGHTS = [
 ('warm', 'cave glow (2 warm COB, above the arch and behind the manger)', [(3.7, 8.3), (4.7, 7.0)]),
 ('wwhite', 'manger spot (warm white)', [(4.3, 7.6)]),
 ('warm', 'cross-shadow lamp (fixed, behind the Holy Family)', [(5.1, 6.7)]),
 ('warm', 'house room lamps x3', [(4.9, 5.7), (5.4, 6.0), (5.9, 6.3)]),
 ('warm', 'window lamps x15 (A 5, B 6, C 4)', [(7.45, 9.6+0.3*i) for i in range(5)] + [(7.3, 11.5+0.28*i) for i in range(6)] + [(7.45, 13.5+0.3*i) for i in range(4)]),
 ('warm', 'campfire (orange flicker)', [(1.0, 8.3)]),
 ('warm', 'far village + Magi lanterns (40 micro LEDs)', [(8.2, 5.4+0.5*i) for i in range(8)]),
 ('neutral', 'field flood x2 (3500-4000 K)', [(1.6, 6.4), (2.9, 8.6)]),
 ('cool', 'angel lamp (cool white clip lamp)', [(1.6, 2.4)]),
 ('mist', 'pond lights x2 (cool white)', [(0.9, 11.2), (1.4, 12.4)]),
]
PATH = [(1.9, 15.9), (2.2, 13.6), (2.9, 11.2), (3.45, 9.25), (3.73, 8.45)]
STAR = (7.8, 1.2)
WASH = [(2.0, 0.8), (5.0, 0.8), (8.3, 2.0)]     # indigo wash floods on small stands on the upper layer, aimed up at the backdrop
STARBAND = [((0.1, 0.25), (9.0, 0.25)), ((8.85, 0.25), (8.85, 16.0))]   # cool-white star points along the top of both walls
DBOX = (0.7, 0.75)       # hatch A: distribution box, back-left corner of the upper layer, next to the church socket
SOCKET = (0.0, 0.0)
HATCH_C = (0.5, 15.5)    # front-left junction
HATCH_B = (1.5, 4.0)     # field junction (upper layer)
TRUNKS = [
 ('T1 left trunk', [DBOX, (0.3, 4.2), (0.3, 12.0), HATCH_C]),
 ('T1b field branch', [(0.3, 4.1), HATCH_B]),
 ('T2 back trunk', [DBOX, (4.5, 0.4), (8.9, 0.3)]),
 ('T3 right trunk', [(8.9, 0.3), (8.5, 5.4), (8.7, 9.0), (8.7, 13.0), (8.2, 15.5)]),
 ('T4 centre trunk', [DBOX, (3.0, 4.3), (4.4, 7.4)]),
]

def svg():
    S = 52; W, H = 1500, 960; tx, ty = 110, 90
    vw = mv.View('top', S, tx, ty, (0, 9, 0, 16))
    def P(x, y): return vw.pt(x, y)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{mv.DEFS}<rect width="{W}" height="{H}" fill="#fff"/>']
    s.append(mv.T(20, 34, 'Crib 2026 · lighting plan: one plug from the church socket (back-left corner) into one box, everything else 12 V', 24, weight='bold'))
    s.append(mv.T(tx, ty-14, 'TOP VIEW (x from the left edge, y from the back wall, feet)', 15, weight='bold'))
    s.append(f'<rect x="{tx}" y="{ty}" width="{9*S}" height="{16*S}" fill="#fdfdfb" stroke="#2b2a33" stroke-width="2"/>')
    for i in range(10): s.append(f'<line x1="{vw.X(i):.1f}" y1="{ty}" x2="{vw.X(i):.1f}" y2="{ty+16*S}" stroke="#e8ebf2"/>')
    for j in range(17): s.append(f'<line x1="{tx}" y1="{ty+j*S}" x2="{tx+9*S}" y2="{ty+j*S}" stroke="#e8ebf2"/>')
    ctx = [e for e in mv.E if not e.get('dark') and e['name'] != 'selfie mirror']
    s.append(mv.draw_view(vw, ctx, lambda e: '#f2f2f2', lambda e: '#c8c8c8', ghost=lambda e: True))
    # step line
    x1, y1 = P(0, 4.5); x2, _ = P(9, 4.5)
    s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y1:.1f}" stroke="#6b5a36" stroke-width="3" stroke-dasharray="12 6"/>' + mv.T(x2-6, y1-6, 'step +1.5 ft', 12, '#6b5a36', 'end'))
    # star band along the walls
    for (a, b) in STARBAND:
        (xa, ya), (xb, yb) = P(*a), P(*b)
        s.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{COOL}" stroke-width="7"/><line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="#7aa0cf" stroke-width="1.5" stroke-dasharray="2 6"/>')
    # path of light
    pp = ' '.join('%.1f,%.1f' % P(*q) for q in PATH)
    s.append(f'<polyline points="{pp}" fill="none" stroke="{WARM}" stroke-width="9" stroke-linecap="round" opacity=".85"/>')
    # trunks
    for nm, pts in TRUNKS:
        tp = ' '.join('%.1f,%.1f' % P(*q) for q in pts)
        s.append(f'<polyline points="{tp}" fill="none" stroke="{TRUNK}" stroke-width="3" stroke-dasharray="9 5"/>')
        lx, ly = P(*pts[len(pts)//2]); s.append(mv.T(lx+6, ly-6, nm.split(' ')[0], 14, TRUNK, weight='bold'))
    # ceiling feed marker
    cx, cy = P(8.9, 0.3); s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="#fff" stroke="{TRUNK}" stroke-width="2.5"/>' + mv.T(cx-12, cy+18, 'ceiling feed', 11, TRUNK, 'end'))
    # lights
    def dot(x, y, fill, stroke='#7a5a10', r=6):
        X, Y = P(x, y); return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    fills = {'warm': (WARM, '#7a5a10'), 'wwhite': (WWHITE, '#7a5a10'), 'neutral': (NEUTRAL, '#8a7a30'), 'cool': (COOL, '#3d6aa0'), 'mist': (MIST, '#3d4f8f')}
    for kind, lab, pts in LIGHTS:
        f, st = fills[kind]
        for (x, y) in pts: s.append(dot(x, y, f, st, 7 if kind in ('neutral', 'cool') else 5))
    for (x, y) in WASH:
        X, Y = P(x, y); s.append(f'<polygon points="{X:.1f},{Y-9:.1f} {X-9:.1f},{Y+7:.1f} {X+9:.1f},{Y+7:.1f}" fill="{INDIGO}" stroke="#fff" stroke-width="1.5"/>')
    X, Y = P(*STAR)
    st = ' '.join(f'{X+math.cos(math.radians(-90+i*36))*(14 if i%2==0 else 6):.1f},{Y+math.sin(math.radians(-90+i*36))*(14 if i%2==0 else 6):.1f}' for i in range(10))
    s.append(f'<polygon points="{st}" fill="{WARM}" stroke="#7a5a10" stroke-width="1.5"/>')
    # distribution box + junctions
    X, Y = P(*DBOX); s.append(f'<rect x="{X-16:.1f}" y="{Y-12:.1f}" width="32" height="24" fill="#fff2c8" stroke="#a8322c" stroke-width="3"/>' + mv.T(X, Y+5, 'D', 18, '#a8322c', 'middle', 'bold'))
    X0, Y0 = P(*SOCKET); s.append(f'<circle cx="{X0+9:.1f}" cy="{Y0+9:.1f}" r="7" fill="#a8322c"/>' + mv.T(X0+22, Y0+4, 'church socket (wall)', 12, '#a8322c', weight='bold'))
    for nm, pt in (('C', HATCH_C), ('B', HATCH_B)):
        X, Y = P(*pt); s.append(f'<rect x="{X-11:.1f}" y="{Y-11:.1f}" width="22" height="22" fill="#fff" stroke="#a8322c" stroke-width="2.5" stroke-dasharray="4 3"/>' + mv.T(X, Y+5, nm, 14, '#a8322c', 'middle', 'bold'))
    # legend
    lx = 640; ly = 100
    s.append(mv.T(lx, ly, 'WHAT EACH MARK IS (colour = the light colour)', 17, weight='bold'))
    items = [(WARM, '#7a5a10', 'Warm gold 2200-2700 K: cave, lamps, windows, campfire, path, star burst, lanterns'),
             (WWHITE, '#7a5a10', 'Warm white 2700-3000 K: manger spot (the brightest spot in the crib)'),
             (NEUTRAL, '#8a7a30', 'Warm-neutral 3500-4000 K: field floods (Glory moment)'),
             (COOL, '#3d6aa0', 'Cool white 5000-6500 K: angel lamp, star points on the walls'),
             (MIST, '#3d4f8f', 'Mist blue / cool white: pond lights'),
             (INDIGO, '#fff', 'Indigo (night-blue gel on white floods, about #1A2A78): night-sky wash, floods on small stands on the upper layer'),
             ]
    for i, (f, st_, t) in enumerate(items):
        y = ly + 30 + i*30
        s.append(f'<circle cx="{lx+10}" cy="{y-5}" r="8" fill="{f}" stroke="{st_}" stroke-width="1.5"/>' + mv.T(lx+28, y, t, 13.5))
    y = ly + 30 + len(items)*30 + 14
    s.append(f'<rect x="{lx+1}" y="{y-14}" width="24" height="20" fill="#fff2c8" stroke="#a8322c" stroke-width="3"/>' + mv.T(lx+34, y, 'D = distribution box (hatch A, back-left, upper layer): the only 230 V point', 13.5))
    s.append(f'<line x1="{lx}" y1="{y+22}" x2="{lx+26}" y2="{y+22}" stroke="{TRUNK}" stroke-width="3" stroke-dasharray="9 5"/>' + mv.T(lx+34, y+27, 'T1–T4 = 12 V cable trunks; ceiling feed (back right) = star burst and spiral only', 13.5))
    s.append(mv.T(lx, y+54, 'One plug into the church socket right behind the stage. B, C = junction hatches. No mains inside the crib.', 13.5, '#a8322c'))
    s.append(mv.T(lx, y+86, 'NOT ALLOWED: red, bright green, pink, multicolour or flashing fairy lights, RGB colour-cycling.', 13.5, '#a8322c', weight='bold'))
    s.append(mv.T(lx, y+108, 'Fairy lights are steady (not twinkle/flash mode), warm white or cool white only.', 13.5, '#a8322c'))
    s.append('</svg>')
    return '\n'.join(s), W, H

if __name__ == '__main__':
    svg_, w, h = svg(); mv.png(svg_, w, h, OUT); print('ok')
