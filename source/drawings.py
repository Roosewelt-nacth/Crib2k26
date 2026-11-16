import math
from drawkit import *

src = open('blueprint.py', encoding='utf-8').read().split("# ---------------- svg")[0].replace("OUT = sys.argv[1]", "")
G = {}
exec(src, G)
O, V, H, C, Lnd, cave, holy, house, mouth, path = (G[k] for k in ("O", "V", "H", "C", "Lnd", "cave", "holy", "house", "mouth", "path"))
HILL = [(3.0, 2.2), (6.0, 1.8), (9.0, 1.7), (9.0, 9.0), (7.1, 9.1), (6.2, 8.9), (5.6, 9.9), (3.4, 9.6), (2.0, 7.6), (2.6, 5.0)]


def shrink(poly, k):
    n = len(poly)
    cx = sum(p[0] for p in poly) / n
    cy = sum(p[1] for p in poly) / n
    return [(cx + (x - cx) * k, cy + (y - cy) * k) for x, y in poly]


def note(d, px, py, lines, size=13, gap=19, fill=INK, head=None):
    if head:
        d.ptxt(px, py, head, size + 1, fill, weight="bold")
        py += gap + 2
    for i, l in enumerate(lines):
        d.ptxt(px, py + i * gap, l, size, fill)


def legh(x, y):
    if 0 <= x <= 3.4 and 0 <= y <= 7.0:
        return 2.0 if y < 1.75 else 1.6 if y < 3.5 else 1.2 if y < 5.25 else 0.8
    if inpoly(x, y, shrink(HILL, 0.62)): return 3.0
    if inpoly(x, y, shrink(HILL, 0.82)): return 2.1
    if inpoly(x, y, HILL): return 1.2
    if 6.2 <= x <= 7.3 and 9.3 <= y <= 16: return 0.55
    return 0.0


def profile(f):
    pts = [(0, 0), (5.5, 0), (6.5, 0.3), (9.0, 3.0), (16, 3.0)]
    for (a, za), (b, zb) in zip(pts, pts[1:]):
        if a <= f <= b: return za + (zb - za) * (f - a) / (b - a)
    return 3.0


# ------------------------------------------------------------------ M0 base frame
def m0():
    d = D(title="PLAN · raked frame on the existing deck (numbers = leg height above deck, ft)", sc=23.5, ox=70, oy=62, h=470)
    d.rect(0, -0.5, 9.5, 0.5, "url(#hatch)", INK, 1.5)
    d.rect(9, -0.5, 0.5, 16.5, "url(#hatch)", INK, 1.5)
    d.rect(0, 0, 9, 16, "#fffef9", INK, 2)
    d.rect(0, 0, 3.4, 7.0, "#e8efd8", "#9fb27f", 1, "6 5")
    d.poly(HILL, "url(#rockp)", "#a8956b", 1.2, "7 5", op=.9)
    d.rect(6.2, 9.3, 1.1, 6.7, "#ece8df", "#b9b2a2", 1)
    for x in (0, 2, 4, 6, 8, 9): d.line(x, 0, x, 16, "#b0a487", .8)
    for y in range(0, 17, 2): d.line(0, y, 9, y, "#b0a487", .8)
    for x in (0, 2, 4, 6, 8):
        for y in range(0, 17, 2):
            h = legh(x + 0.0001, y + 0.0001)
            if h > 0:
                d.rect(x - .09, y - .09, .18, .18, "#8a6a3a", "#5a4020", .8)
                d.txt(x + .15, y - .1, f"{h:.1f}", 9.5, "#5a4020")
    for (x, y, w, h, t_) in ((7.6, 15.2, 1.2, 0.7, "A"), (0.3, 3.2, 2.4, 1.4, "B"), (0.0, 11.3, .5, .5, "C")):
        d.rect(x, y, w, h, "none", RED, 1.8, "4 3"); d.txt(x + w / 2, y + h / 2 + .15, t_, 13, RED, "middle", "bold")
    d.dh(0, 9, 16, "9 ft", 22); d.dv(0, 16, 0, "16 ft", -26)
    d.txt(4.5, -0.62, "church wall (altar wall)", 11, PEN, "middle", "bold")
    d.txt(9.95, 7, "right wall", 12, PEN, "middle", rot=90)
    note(d, 340, 70, ["Frame: 2 × 2 in battens at 2 ft centres, both ways.",
                      "Cross-brace every leg taller than 1.5 ft.",
                      "Skin the tops with 9–12 mm ply; screw, don't glue.",
                      "Green = terrace bands · beige = hill · grey = street.",
                      "Red dashed boxes = service hatches (keep ply loose):",
                      "  A  control box (item 27) under the front-right",
                      "  B  Pepper's-ghost screen + mister (items 9, 10)",
                      "  C  speaker (item 28)",
                      "Black pleated skirting on the open front and left edges."], head="HOW THE FRAME GOES TOGETHER")
    note(d, 340, 320, ["Total frame: ~160 ft of 2 × 2, ~5 ply sheets.",
                       "Max load: hill + cave ≈ 60 kg (thermocol is light).",
                       "Check the deck's own load rating with the church."], head="LOADS")
    d2 = D(title="SECTION · through the cave centre-line, front edge (left) to back wall (right), above the deck", sc=38, ox=70, oy=290, h=470)
    d2.rect(0, 0, 16, 2, "#3b3b42", INK, 1.5)
    d2.ptxt(d2.X(8), d2.Y(1.2), "existing deck 2 ft · black skirting on the open edges", 12, "#eee", "middle")
    d2.line(-0.6, 2, 16.6, 2, INK, 2.5); d2.txt(0, 2.45, "church floor", 12, PEN)
    d2.rect(16, -9, .5, 11, "url(#hatch)", INK, 1.5)
    pts = [(f, -profile(f)) for f in [0, 2, 4, 5.5, 6.5, 8, 9, 12, 16]]
    for f in range(0, 17, 2):
        h = profile(f)
        if h > 0.05: d2.rect(f - .05, -h, .1, h, "#8a6a3a", "#5a4020", .8)
    d2.poly(pts + [(16, -profile(16) - .06), (9, -3.06), (6.5, -.36), (5.5, -.06), (0, -.06)], "#e3c590", "#b58f55", 1, close=True)
    d2.poly([(0, -profile(0)), (5.5, 0), (6.5, -.3), (9, -3), (16, -3)], "none", "#7a5a2a", 2.5, close=False)
    d2.txt(0.3, -0.55, "flat at deck level", 12, PEN)
    d2.txt(6.0, -1.6, "ramp up the rock face", 12, PEN, "end")
    d2.txt(12.5, -3.5, "crest +3.0 ft: hill top, far village, house base", 12, PEN, "middle")
    d2.dh(0, 16, 2, "16 ft", 30)
    d2.txt(6.5, -.75, "+0.3", 11, PEN, "middle")
    note(d2, 722, 90, ["f = distance from front edge", "f 0–5.5 ft : 0.0", "f 6.5 ft : 0.3", "f 8 ft : 1.8", "f 9–16 ft : 3.0", "", "Terraces (left side):", "0.8 / 1.2 / 1.6 / 2.0 ft"], 12, 18, head="LEG HEIGHTS")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M1 cave + hill
def m1():
    d = D(title="PLAN (left) and FRONT ELEVATION (right) · cave and hill, built as one unit, drawn square-on", sc=36, ox=110, oy=75)
    hp = [(-1.3, 5), (-1.5, 3), (-1.0, .8), (1, -.2), (4, -.2), (5.0, .8), (5.5, 3), (5.3, 5)]
    d.poly(hp, "url(#rockp)", "#a8956b", 1.5, "7 5")
    d.rect(0, 2.5, 4, 2.5, "#cdbb92", INK, 2.5)
    d.line(.5, 5, 3.5, 5, "#fffef9", 7)
    d.rect(.5, 3.1, 3, 1.2, "#f3dfb0", GOLD, 1.6, "5 3")
    d.circ(.95, 3.7, .26, "#fff", BLUE, 1.5); d.circ(3.0, 3.6, .22, "#fff", "#8a5a2a", 1.5); d.rect(1.55, 3.35, 1.0, .6, "#e8c98a", "#8a5a2a", 1.4)
    d.txt(.95, 4.22, "Mary", 11, BLUE, "middle"); d.txt(3.0, 4.22, "Joseph", 11, "#8a5a2a", "middle"); d.txt(2.05, 3.75, "manger", 10.5, "#8a5a2a", "middle")
    d.rect(.4, 2.6, .6, .3, "#d7d1c6", PEN, 1); d.rect(1.1, 2.6, .5, .3, "#c8c1b4", PEN, 1); d.txt(.7, 2.85, "ox", 9.5, INK, "middle"); d.txt(1.35, 2.85, "ass", 9.5, INK, "middle")
    d.dh(0, 4, 5, "cave 4 ft", 24); d.dh(-1.5, 5.5, 5, "hill base 7 ft", 56); d.dv(2.5, 5, 4, "2.5 ft deep", 30)
    d.txt(2, -.6, "back of hill: keep 1 ft free for wiring", 11, PEN, "middle")
    # elevation
    d.ox, d.oy = 610, 330
    d.poly([(-1.5, 0), (-1.3, -1.4), (0, -2.6), (1.2, -3), (3.5, -3), (4.8, -2.4), (5.5, 0)], "url(#rockp)", "#a8956b", 1.6)
    arch = [(.5, 0), (.5, -1.8), (.7, -2.2), (1.2, -2.45), (2, -2.5), (2.8, -2.45), (3.3, -2.2), (3.5, -1.8), (3.5, 0)]
    d.poly(arch, "#5a4026", INK, 2)
    d.rect(1.55, -1.1, .9, .35, "#e8c98a", "#8a5a2a", 1)
    d.rect(.8, -1.5, .45, 1.5, "#cfe0f5", BLUE, 1.2); d.circ(1.02, -1.7, .2, "#fff", BLUE, 1.2)
    d.rect(2.8, -2.0, .4, 2.0, "#d9b98a", "#8a5a2a", 1.2); d.circ(3.0, -2.2, .17, "#fff", "#8a5a2a", 1.2)
    d.rect(0, -4.3, 4, 1.5, "none", RED, 1.8, "9 6"); d.txt(2, -3.45, "house (sheet 2) +2.8 → +4.3", 11, RED, "middle")
    d.dv(-2.5, 0, .5, "2.5", -22); d.dv(-3, 0, 5.5, "3.0", 24); d.dh(.5, 3.5, 0, "3 ft", 24)
    d.txt(2, .15 + 1.15, "FRONT VIEW", 12, INK, "middle", "bold")
    d2 = D(title="SECTION through the cave (viewer on the left) · and the layers of the rock skin", sc=62, ox=60, oy=385)
    d2.rect(-.3, 0, 5.8, .1, "url(#ply)", "#8a6a3a", 1.2)
    d2.poly([(-.3, 0), (-.3, -2.9), (.3, -3), (5.2, -3), (5.5, 0)], "url(#rockp)", "#a8956b", 2)
    d2.poly([(0, 0), (0, -2.3), (.3, -2.5), (2.5, -2.5), (2.5, 0)], "#5a4026", INK, 2)
    d2.line(.05, -2.42, .9, -2.42, "#ffd36a", 5); d2.txt(.1, -2.65, "LED strip above lintel", 10.5, GOLD)
    d2.rect(1.1, -.4, .8, .4, "#e8c98a", "#8a5a2a", 1.4); d2.txt(1.5, -.46, "manger", 10, "#8a5a2a", "middle")
    d2.rect(.55, -1.4, .3, 1.4, "#cfe0f5", BLUE, 1.2); d2.circ(.7, -1.6, .17, "#fff", BLUE, 1.2)
    d2.rect(2.0, -1.0, .45, 1.0, "#d9d3c8", PEN, 1.2); d2.txt(2.2, -1.1, "ox/ass", 10, INK, "middle")
    d2.circ(2.35, -.25, .09, "#fff6c0", GOLD, 1.4); d2.txt(2.65, -.15, "cross-shadow lamp (3:00 cue)", 10.5, GOLD)
    d2.dv(-2.5, 0, 0, "2.5", -22); d2.dh(0, 2.5, 0, "2.5 ft deep", 32); d2.dh(-.3, 5.5, 0, "hill ≈ 5.8 ft deep", 62)
    # skin layers
    lay = [("1  ply base 12 mm", "url(#ply)", .5), ("2  thermocol 4 in, glued in layers", "url(#eps)", 1.2), ("3  carve strata with hot knife", "url(#eps)", .5),
           ("4  chicken mesh on arch/overhangs", "#d9dde2", .25), ("5  PoP + PVA coat, 3 mm", "#f2efe6", .3), ("6  sand/grout coat, press pebbles", "#d9c9a0", .3), ("7  dry-brush: sand → ochre → olive", "#c2a46a", .3)]
    y0 = 90
    d2.ptxt(600, 64, "ROCK SKIN, BUILT UP IN ORDER", 13, INK, weight="bold")
    for i, (lb, fill, h) in enumerate(lay):
        yy = y0 + i * 40
        d2.o.append(f'<rect x="600" y="{yy}" width="60" height="{22}" fill="{fill}" stroke="{PEN}" stroke-width="1.2"/>')
        d2.ptxt(672, yy + 16, lb, 12.5, INK)
    d2.ptxt(600, 384, "Cave and hill lift out in two pieces", 12, PEN); d2.ptxt(600, 402, "so they fit through the church door.", 12, PEN)
    d2.ptxt(600, 424, "Seal every layer with PVA; keep LED", 12, PEN); d2.ptxt(600, 442, "wires out of the plaster.", 12, PEN)
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M2 house
def m2():
    d = D(title="FRONT ELEVATION (cut open) and PLAN · upper guest room 'kataluma'", sc=60, ox=70, oy=345)
    d.rect(0, -1.5, 4, 1.5, "#fbf6ea", INK, 2.5)
    d.rect(-.15, -1.65, 4.3, .15, "#e6dcc6", INK, 2)
    d.rect(-.15, -.05, 4.3, .12, "url(#ply)", "#8a6a3a", 1.2)
    d.rect(1.6, -1.2, .5, .6, "#cfe0f5", PEN, 1.2); d.txt(1.85, -.9, "window", 9, PEN, "middle")
    for k, x in enumerate((.25, 1.1, 2.0, 2.9)):
        d.rect(x, -.2, .8, .2, "#d9b98a", "#8a5a2a", 1.2); d.circ(x + .12, -.3, .1, "#fff", "#8a5a2a", 1.2)
    for x in (0.45, 3.2): d.circ(x, -.95, .09, "#ffd36a", GOLD, 1.5)
    d.circ(1.5, -.3, .09, "#ffd36a", GOLD, 1.5); d.txt(1.5, -.45, "lamp", 9, GOLD, "middle")
    d.rect(3.4, -.55, .35, .55, "#cdbb92", PEN, 1); d.rect(.05, -.55, .3, .55, "#cdbb92", PEN, 1); d.txt(.2, -.62, "jars", 9, PEN, "middle")
    d.dh(0, 4, 0, "4 ft", 30); d.dv(-1.5, 0, 0, "1.5 ft room", -26)
    d.txt(2, -1.8, "parapet / roof slab (flat roof, cat on it)", 11, PEN, "middle")
    # stairs
    for k in range(8):
        d.rect(4.2 + k * .26, -0.0 - (k + 1) * .1 * 0, .26, .0, "none", PEN, 0)
    pts = [(4.2, 2.8)]
    for k in range(8):
        pts += [(4.2 + k * .3, 2.8 - (k + 1) * .35 + .35 * 0), (4.2 + (k + 1) * .3, 2.8 - (k + 1) * .35)]
    d.txt(5.0, .9, "stone steps (cut in thermocol)", 11, PEN)
    d.txt(5.0, 1.1, "rise 2.8 ft in 8 steps", 11, PEN)
    d.txt(2, 1.0, "sleeping travellers 1:6 (about 1 ft long)", 12, INK, "middle")
    # plan
    d.ox, d.oy = 640, 150
    d.rect(0, 0, 4, 2, "#fbf6ea", INK, 2.5); d.rect(0, 1.95, 4, .05, "none", RED, 4)
    d.txt(2, 2.35, "open front (cut away)", 11, RED, "middle")
    for k, (x, y) in enumerate(((.3, .3), (1.2, .3), (2.1, .3), (3.0, .3), (.4, 1.1), (1.5, 1.1))):
        d.rect(x, y, .8, .3, "#d9b98a", "#8a5a2a", 1.2)
    d.circ(2.7, 1.2, .1, "#ffd36a", GOLD, 1.5); d.circ(3.5, 1.4, .1, "#ffd36a", GOLD, 1.5); d.circ(.2, .9, .1, "#ffd36a", GOLD, 1.5)
    d.dh(0, 4, 2, "4 ft", 52); d.dv(0, 2, 4, "2 ft", 26)
    d.txt(2, -.25, "PLAN (turned 32° with the cave on site)", 12, INK, "middle", "bold")
    d2 = D(title="SECTION · how the room is held up (no load goes on the cave roof)", sc=70, ox=80, oy=380)
    d2.rect(-.2, 0, 6.2, .08, "url(#ply)", "#8a6a3a", 1.2)
    d2.poly([(-.2, 0), (-.2, -1.6), (.6, -2.8), (5.9, -2.8), (5.9, 0)], "url(#rockp)", "#a8956b", 2)
    d2.poly([(.4, 0), (.4, -2.0), (.9, -2.2), (2.6, -2.2), (2.9, 0)], "#5a4026", INK, 1.8); d2.txt(1.6, -1.0, "cave void", 12, "#fff", "middle")
    d2.rect(.2, -2.9, 2.3, .1, "url(#ply)", "#8a6a3a", 1.6)
    d2.rect(.35, -2.8, .1, .0, "none", PEN, 1)
    d2.rect(.9, -2.82, .1, .62, "#8a6a3a", "#5a4020", 1); d2.rect(2.0, -2.82, .1, .62, "#8a6a3a", "#5a4020", 1)
    d2.txt(.95, -2.1, "2×2 post", 10, PEN, "middle", rot=None)
    d2.rect(.2, -4.4, 2.3, 1.5, "none", RED, 2, "8 5")
    d2.rect(.2, -4.45, 2.3, .08, "#e6dcc6", INK, 1.5)
    d2.rect(2.38, -4.4, .12, 1.5, "#fbf6ea", INK, 1.5); d2.txt(2.5, -3.6, "back wall", 10.5, PEN)
    d2.circ(1.0, -3.2, .06, "#ffd36a", GOLD, 1.2); d2.circ(1.7, -3.2, .06, "#ffd36a", GOLD, 1.2)
    d2.line(1.0, -3.2, 1.0, 0, GOLD, 1, "3 3"); d2.txt(1.05, -.5, "LED wire down to hatch", 10.5, GOLD)
    d2.dv(-4.4, -2.9, .2, "1.5", -20); d2.dv(-2.8, 0, -.2, "2.8", -24)
    note(d2, 560, 110, ["Floor tray: 12 mm ply, 4 × 2 ft.", "Rests on the hill top and two 2 × 2 posts", "standing on the cave's ply base.", "Walls: 2 in thermocol, plastered.", "Whole room weighs under 8 kg.",
                        "Lamps: 3 flicker LEDs on one 3 V line.", "Hidden details: cat on the roof,", "clay oven, sleeping child."], 12.5, 19, head="BUILD NOTES")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M3 path
def m3():
    d = D(title="PLAN · path of light, from the front-left of the deck to the cave mouth", sc=45, ox=120, oy=40)
    ps = [(x, y - 7.2) for x, y in path]
    L = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(ps, ps[1:]))
    d.poly([(-.2, 0), (4.2, 0), (4.2, 9.2), (-.2, 9.2)], "#fffef9", "none", 0)
    d.poly(ps, "none", "#f1d58a", 22, close=False)
    d.o[-1] = d.o[-1].replace('stroke-width="22"', 'stroke-width="22" stroke-linecap="round" opacity=".8"')
    d.poly(ps, "none", GOLD, 1.5, "10 7", close=False)
    n = int(L * 18.3 / 6)
    for k in range(n + 1):
        t = k / n * L
        acc = 0
        for a, b in zip(ps, ps[1:]):
            sl = math.hypot(b[0] - a[0], b[1] - a[1])
            if acc + sl >= t:
                u_ = (t - acc) / sl; d.circ(a[0] + (b[0] - a[0]) * u_, a[1] + (b[1] - a[1]) * u_, .05, "#fff6c0", GOLD, 1); break
            acc += sl
    mx, my = mouth[0], mouth[1] - 7.2
    d.rect(mx - 1.5, my - 1.0, 3, 1.0, "#cdbb92", INK, 2); d.txt(mx, my - .35, "cave mouth", 12, INK, "middle")
    d.txt(ps[0][0] + .5, ps[0][1] - .2, "start: front edge", 11.5, INK); d.txt(ps[0][0] + .5, ps[0][1] + .05, "data + 5 V from hatch A", 11.5, INK)
    d.dv(ps[-1][1], ps[0][1], 4.3, f"≈ {L:.1f} ft long", 62)
    d.txt(ps[3][0] + .45, ps[3][1], "0.5 ft wide", 11, GOLD)
    note(d, 470, 70, [f"WS2812B strip, 60 LED/m ≈ {int(L*18.3)} pixels for {L:.1f} ft.", "Order 3 m (spare) · 5 V supply, 5 A.", "Add a 470 Ω resistor on the data line and a",
                      "1000 µF capacitor across the supply.", "", "CHASE CUE (2:30): a bright 8-pixel comet runs", "from the front edge to the cave mouth in 7 s,", "leaving a dim glow behind it.", "",
                      "Keep it clear of the deck-edge skirting and", "plaque (item 25). It must never cross a solid."], 13, 19, head="HOW IT WORKS")
    d2 = D(title="CROSS-SECTION of the path (not to scale vertically)", sc=190, ox=130, oy=250)
    d2.rect(-.8, 0, 2.1, .06, "url(#ply)", "#8a6a3a", 1.2)
    d2.rect(-.8, -.1, .8, .1, "#ddd0a8", PEN, 1); d2.rect(.5, -.1, .8, .1, "#ddd0a8", PEN, 1)
    d2.rect(0, -.16, .5, .16, "#6b6f78", INK, 1.2)
    d2.rect(.02, -.12, .46, .035, "#ffd36a", GOLD, 1)
    d2.rect(0, -.2, .5, .03, "#fff3c8", PEN, 1)
    d2.rect(0, -.26, .5, .06, "#e6d3a0", PEN, 1)
    for x in (-.02, .5): d2.circ(x + .0, -.26, .035, "#b8ad95", PEN, 1)
    d2.dh(0, .5, 0, "0.5 ft", 30)
    for i, (lb, y) in enumerate((("5  fine sand 5 mm, glued; pebbles on the edge", -.24), ("4  diffuser 3 mm (frosted acrylic)", -.19), ("3  WS2812B strip (LEDs face up)", -.125), ("2  aluminium/silicone channel, 10 mm", -.07), ("1  ply base, groove cut 14 mm wide", .03))):
        d2.o.append(f'<line x1="{d2.X(.55):.1f}" y1="{d2.Y(y):.1f}" x2="470" y2="{100+i*34}" stroke="{PEN}" stroke-width=".9"/>')
        d2.ptxt(476, 105 + i * 34, lb, 13, INK)
    d2.ptxt(476, 300, "Wires run in the groove to hatch A; solder + heat-shrink, no tape.", 12.5, PEN)
    d2.ptxt(476, 320, "Test with the strip lying on the deck before gluing sand.", 12.5, PEN)
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M4 shepherds' field
def m4():
    d = D(title="PLAN · shepherds' field (left side of the stage)", sc=38, ox=110, oy=62)
    bands = ((5.25, 7.0, .8), (3.5, 5.25, 1.2), (1.75, 3.5, 1.6), (0, 1.75, 2.0))
    cols = ("#eef3df", "#e3ecd0", "#d8e5c0", "#cddcb0")
    for (y0, y1, h), c in zip(bands, cols):
        d.rect(0, y0, 3.4, y1 - y0, c, "#7f9a60", 1.6); d.txt(3.45, (y0 + y1) / 2 + .1, f"+{h:.1f}", 12, "#4f7a3a")
    d.rect(.2, 7.0, 1.7, 2.6, "#f6f1e3", PEN, 1.5)
    d.rect(.4, 1.7, 2.0, 1.3, "#f1e9d6", INK, 1.6); d.txt(1.4, 2.4, "11 sheepfold", 12, INK, "middle")
    d.circ(3.0, 1.0, .5, "#f1e9d6", INK, 1.8); d.txt(3.0, 1.1, "13", 12, INK, "middle")
    d.rect(.3, 3.2, 2.4, 1.4, "none", BLUE, 1.5, "5 4"); d.txt(1.5, 3.9, "9 (sheet 5)", 11, BLUE, "middle")
    d.rect(.3, 4.6, 2.4, 1.0, "url(#rockp)", "#8d7a52", 1.5); d.txt(1.5, 5.15, "10 ridge", 11, INK, "middle")
    for (x, y) in ((.6, 7.6), (1.4, 7.9), (.7, 8.8), (1.5, 9.1), (1.1, 8.3)): d.circ(x, y, .16, "#fff", PEN, 1.2)
    d.circ(1.0, 8.3, .12, "#f0a03a", "#c05a10", 1.2); d.txt(1.05, 7.45, "8 shepherds", 12, INK, "middle")
    d.txt(1.05, 9.5, "campfire + 6 sheep", 10.5, PEN, "middle")
    d.dv(0, 7, 0, "7 ft", -28); d.dv(7, 9.6, 3.4, "2.6 ft", 34); d.txt(1.7, -.2, "3.4 ft wide", 11.5, INK, "middle")
    note(d, 440, 70, ["Four ply boxes, each 1.75 ft deep, faced with", "2 in thermocol carved as dry-stone walls.", "Real pebbles on the wall fronts; soil/sand on", "the treads; artificial grass patches and moss.", "",
                      "Shepherds (8): two figures 1.2 ft (1:6),", "one old with staff, one young with a lamb.", "Sheepfold (11): ring of pebbles, thorn gate, 1:12.", "Watchtower (13): 1 ft PVC pipe + pebble clay, 1.5 ft.", "",
                      "All of this sits left of the cave and below the", "backdrop's twilight hills print."], 13, 19, head="BUILD NOTES")
    d2 = D(title="SECTION along the field, back wall (left) to front (right)", sc=44, ox=60, oy=330)
    d2.rect(0, 0, 9.6, 2, "#3b3b42", INK, 1.5); d2.txt(4.8, 1.0, "deck", 12, "#eee", "middle")
    stepsx = ((0, 1.75, 2.0), (1.75, 3.5, 1.6), (3.5, 5.25, 1.2), (5.25, 9.6, .8))
    for (a, b, h) in stepsx:
        d2.rect(a, -h, b - a, h, "url(#eps)", PEN, 1.3)
        d2.rect(a, -h - .12, b - a, .12, "#8fae6a", "#5f7f3f", 1)
    for (a, b, h) in stepsx[:3]:
        d2.rect(b - .08, -h, .08, h, "#c9b892", "#8a7a52", 1)
    d2.txt(.9, -2.25, "+2.0", 11, "#4f7a3a", "middle"); d2.txt(2.6, -1.85, "+1.6", 11, "#4f7a3a", "middle"); d2.txt(4.4, -1.45, "+1.2", 11, "#4f7a3a", "middle"); d2.txt(7.4, -1.05, "+0.8", 11, "#4f7a3a", "middle")
    d2.rect(.3, -2.0 - 1.5, .5, 1.5, "#f1e9d6", INK, 1.5, ); d2.txt(.55, -3.7, "tower 1.5", 10.5, INK, "middle")
    d2.rect(1.8, -2.0 - .25, .8, .25, "#f1e9d6", INK, 1.2); d2.txt(2.2, -2.55, "fold 0.25", 10.5, INK, "middle")
    d2.rect(3.7, -1.2 - .8, .3, .8, "url(#rockp)", "#8d7a52", 1.2); d2.txt(3.9, -2.2, "ridge 0.8", 10.5, INK, "middle")
    d2.rect(6.2, -.8 - 1.2, .25, 1.2, "#e2c8a8", PEN, 1.2); d2.rect(6.8, -.8 - 1.2, .25, 1.2, "#bcc8d8", PEN, 1.2); d2.txt(6.5, -2.3, "shepherds 1.2", 10.5, INK, "middle")
    d2.circ(7.4, -.95, .1, "#f0a03a", "#c05a10", 1.2)
    for x in (7.8, 8.3, 8.8): d2.rect(x, -.8 - .45, .35, .45, "#fff", PEN, 1.2)
    d2.dv(-2, 0, 9.6, "2.0 ft above deck", 34)
    d2.txt(4.8, 2.7, "Shepherd scale: figures 1.2 ft (1:6), sheep 0.45 ft, fold at 1:12", 12, PEN, "middle")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M5 floating angel
def m5():
    d = D(title="SIDE SECTION · Pepper's-ghost floating angel (viewer is far left, 14 ft away)", sc=120, ox=140, oy=380)
    d.rect(-1.1, 0, 3.4, .06, "url(#ply)", "#8a6a3a", 1.2)
    d.poly([(-1.1, 0), (-1.1, -.55), (-.8, -.8), (-.1, -.8), (.15, -.4), (.2, 0)], "url(#rockp)", "#8d7a52", 2)
    d.txt(-.6, -.9, "ridge (hides screen)", 11.5, INK, "middle")
    d.rect(.2, -.2, 1.6, .2, "#222", INK, 1.5); d.rect(.2, -.1, 1.0, .06, "#8fb8ff", BLUE, 1.5)
    d.txt(.7, .22, "screen face-up", 11.5, BLUE, "middle")
    d.line(0, -1.6, 1.41, -.19, "#8fb8ff", 5); d.o[-1] = d.o[-1].replace('stroke-width="5"', 'stroke-width="5" opacity=".7"')
    d.txt(1.5, -1.0, "clear acrylic 3 mm, 45°", 12, BLUE)
    d.txt(1.5, -.8, "2 ft slant × 2.4 ft wide", 12, BLUE)
    d.line(.5, -.14, .5, -1.1, BLUE, 1.6, "5 3", arrow=True)
    d.line(.5, -1.1, -1.3, -1.1, BLUE, 1.6, "5 3", arrow=True); d.txt(-1.3, -1.2, "to the eye", 11, BLUE)
    d.circ(1.5, -1.1, .26, "#fff", BLUE, 1.6, op=.6); d.line(1.5, -.84, 1.5, -.5, BLUE, 1.4, "3 3")
    d.txt(1.5, -1.5, "angel floats here", 12, BLUE, "middle", "bold")
    d.rect(1.6, -.5, .4, .5, "#33384a", PEN, 1); d.rect(2.0, -.6, .08, .6, "#222", PEN, 1); d.txt(2.1, -.3, "black cloth", 10.5, "#eee")
    d.dv(-1.6, 0, 0, "1.4", -28); d.dh(0, 1.41, 0, "1.4 ft run", 32)
    d.txt(-1.0, .5, "hatch B: lift-out lid", 11, RED)
    note(d, 600, 90, ["How the trick works:", "the screen is lit face-up below the sheet.", "The sheet reflects it toward the viewer, so a", "glowing angel seems to hang in the air behind", "the glass, with real rocks visible through it.", "",
                      "Screen: tablet or monitor, brightness max,", "pure-black background video.", "Angel size on screen ≈ 0.7–1 ft (1:6 scale).", "Fine-tune the glass angle at night from the", "public view spot."], 12.5, 19, head="PEPPER'S GHOST")
    d2 = D(title="PLAN · floating angel unit and valley mist (hatch B)", sc=95, ox=90, oy=62)
    d2.rect(0, 0, 2.4, 1.0, "url(#rockp)", "#8d7a52", 2); d2.txt(1.2, .55, "10 ridge 0.8 ft", 12, INK, "middle")
    d2.rect(.35, .3, 1.7, .4, "#fffef9", PEN, 1.4); d2.txt(1.2, .55, "", 10)
    d2.rect(.35, .35, 1.7, .3, "#bfe0ff", BLUE, 1.2); d2.txt(1.2, .52, "mister tray", 11, BLUE, "middle")
    d2.o.append(f'<circle cx="{d2.X(.8):.1f}" cy="{d2.Y(.5):.1f}" r="5" fill="{BLUE}"/><circle cx="{d2.X(1.6):.1f}" cy="{d2.Y(.5):.1f}" r="5" fill="{BLUE}"/>')
    d2.rect(0, -1.4, 2.4, 1.4, "none", BLUE, 2, "6 4"); d2.txt(1.2, -1.45, "acrylic footprint 2.4 × 1.4", 11.5, BLUE, "middle")
    d2.rect(.3, -1.0, 1.8, .9, "#222", INK, 1.5); d2.rect(.55, -.9, 1.3, .65, "#8fb8ff", BLUE, 1.2); d2.txt(1.2, -.5, "screen", 12, "#222", "middle")
    d2.line(0, -1.4, 2.4, -.05, BLUE, 3)
    d2.dh(0, 2.4, 1.0, "2.4 ft", 30); d2.dv(-1.4, 1.0, 2.4, "2.4 ft total", 28)
    note(d2, 430, 70, ["TOP VIEW: the ridge is the front lip. Behind its", "lip sits a shallow tray with two ultrasonic discs and", "a 5 V fan; mist is pushed forward and rolls into the", "valley. The acrylic and screen sit behind the tray.", "",
                       "Rules:", "• keep 3 cm of water in the tray (float switch)", "• mister on its own relay, 1:00–3:30", "• never let mist reach the screen; place a lip", "• wipe the acrylic with a microfibre cloth before", "  the show; fingerprints show as ghosts"], 12.5, 19, head="MIST + SCREEN ARRANGEMENT")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M6 village
def m6():
    ox, oy, s_ = 60, 40, 55
    d = D(title="PLAN · village strip along the right wall (items 16–25)", sc=s_, ox=ox, oy=oy)
    dx, dy = 4.2, 9.0
    d.o.append(f'<rect x="{d.X(0)}" y="{d.Y(0)}" width="{s_*4.8}" height="{s_*7}" fill="#fffef9" stroke="{INK}" stroke-width="2"/>')
    def sh(poly): return [(x - dx, y - dy) for x, y in poly]
    d.o.append(f'<rect x="{d.X(4.8)}" y="{d.Y(0)}" width="14" height="{s_*7}" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.poly(sh(O["street"]), "#ece8df", "#b9b2a2", 1.4)
    for k, lab in (("hA", "16"), ("hB", "17"), ("hC", "18")):
        d.poly(sh(O[k]), "#f7f3ea", INK, 1.8); p = O[k]; d.txt(sum(q[0] for q in p) / 4 - dx, sum(q[1] for q in p) / 4 - dy + .1, lab, 13, INK, "middle", "bold")
    d.poly(sh(O["well"]), "#d9e8f5", BLUE, 1.6); d.txt(5.6 - dx, 11.2 - dy + .08, "20", 11, INK, "middle")
    d.poly(sh(O["census"]), "#f6efe0", RED, 1.4); d.txt(5.2 - dx, 13.3 - dy, "21", 11, RED, "middle")
    d.poly(sh(O["donk"]), "#f6efe0", PEN, 1.2); d.txt(5.2 - dx, 10.4 - dy, "22", 11, INK, "middle")
    d.poly(sh(O["oliveR"]), "#cfdcb8", "#5d7a3e", 1.6); d.txt(5.4 - dx, 14.95 - dy, "24", 11, "#3d5a26", "middle")
    d.poly(sh(O["plaque"]), "#fff", INK, 1.6); d.txt(4.2 - dx, 15.8 - dy, "25", 11, INK, "middle")
    d.dv(0, 7, 0, "7 ft", -24)
    d.txt(.1, -.2, "view from above · back of the stage is at the top", 11, PEN)
    rows = ["16  house A  1.4 × 1.6 ft  h 2.0 ft", "17  house B  1.6 × 1.8 ft  h 2.5 ft (tallest, stair)", "18  house C  1.4 × 1.6 ft  h 1.8 ft", "19  street 1.1 × 6.7 ft, rises 0.3 → 0.8", "20  well  0.9 ft dia  h 0.6",
            "21  census table + soldier + scribe", "22  two donkeys + two travellers", "23–24  olive trees  2.0 / 1.6 ft", "25  'find 12 details' plaque 2 × 0.4 ft"]
    d.ptxt(400, 72, "ITEMS ON THIS SHEET", 13.5, INK, weight="bold")
    for i, r in enumerate(rows): d.ptxt(400, 98 + i * 21, r, 12.5, INK)
    d.ptxt(400, 308, "All at 1:6: figures 1.2 ft, doors 0.9 ft. Tier B (11–15 ft).", 12.5, PEN)
    d.ptxt(400, 329, "Lamps in windows: 15 flicker LEDs on a 3 V line.", 12.5, PEN)
    d.ptxt(400, 350, "Olive 23 (left, front) is on the master plan at (1.0, 14.2).", 12.5, PEN)
    d2 = D(title="ELEVATION along the right wall (front of stage on the right) · heights above the deck", sc=47, ox=50, oy=345)
    def zs(y): return 0.8 - (y - 9.3) * (0.5 / 6.7)
    d2.poly([(y - 9.0, -zs(y) if y > 9.3 else -0.8) for y in [9.0, 9.3, 12, 16]] + [(7.0, 0), (0, 0)], "#ece8df", "#b9b2a2", 1.4)
    for k, lab, h in (("hA", "16", 2.0), ("hB", "17", 2.5), ("hC", "18", 1.8)):
        ys = [q[1] for q in O[k]]; y0, y1 = min(ys) - 9.0, max(ys) - 9.0
        z0 = zs((min(ys) + max(ys)) / 2)
        d2.rect(y0, -(z0 + h), y1 - y0, h, "#f7f3ea", INK, 2)
        d2.rect(y0 + .45 * (y1 - y0), -(z0 + .9), .35, .6, "#cdbb92", PEN, 1); d2.rect(y0 + .1, -(z0 + h * .6), .3, .3, "#9fb0c8", PEN, 1)
        d2.txt((y0 + y1) / 2, -(z0 + h) - .1, f"{lab}  h {h}", 11.5, INK, "middle")
    d2.rect(2.0, -1.8, .15, 1.0, "#e2c8a8", PEN, 1.2); d2.rect(2.35, -1.8, .15, 1.0, "#bcc8d8", PEN, 1.2); d2.txt(2.3, -1.9, "soldier 1.2", 10.5, INK, "middle")
    d2.dv(-3.3, 0, 7.1, "street rises 0.8 → 0.3 toward the front", 24)
    d2.txt(0, 1.0, "back of stage", 11.5, PEN); d2.txt(7.0, 1.0, "front edge", 11.5, PEN, "end")
    d2.dh(0, 1.6, 0, "", 0)
    d2.ptxt(520, 80, "Scale guide at 1:6 (hero 1:3)", 13, INK, weight="bold")
    d2.ptxt(520, 102, "adult 6 ft  →  1.0 ft", 12.5, INK); d2.ptxt(520, 122, "child 3 ft  →  0.5 ft", 12.5, INK); d2.ptxt(520, 142, "door 6 ft  →  1.0 ft", 12.5, INK)
    d2.ptxt(520, 170, "Keep house walls 2 in thick: plaster + paint", 12.5, PEN); d2.ptxt(520, 190, "the cut edges to look like lime-washed stone.", 12.5, PEN)
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M7 far village + Magi + sight check
def bearings(poly):
    b = [math.degrees(math.atan2(x - V[0], -(y - V[1]))) for x, y in poly]
    return min(b), max(b)


def m7():
    d = D(title="ELEVATION of the right-wall crest · far village (14) and Magi shelf (15), drawn large", sc=105, ox=70, oy=340)
    d.rect(-.3, -2.6, 4.6, 1.3, "url(#hatch)", INK, 1.2, op=.35)
    d.poly([(0, 0), (0, -.8), (4.0, -.8), (4.0, 0)], "url(#rockp)", "#a8956b", 2)
    d.txt(2.0, -.35, "hill crest +3.0 ft (rock face)", 12, INK, "middle")
    import random
    random.seed(4)
    x = .1
    while x < 3.7:
        w, hh = random.choice((.12, .15, .18)), random.choice((.25, .3, .36, .42))
        d.rect(x, -.8 - hh, w, hh, "#f3ede0", PEN, .8); x += w + .04
    d.txt(2.0, -1.35, "14  far village: 20 houses, 3–5 in tall, pale cream", 12, INK, "middle")
    d.rect(.1, -2.25, 3.8, .06, "url(#ply)", "#8a6a3a", 1.2)
    for k in range(3):
        x0 = .3 + k * .75
        d.rect(x0, -2.25 - .26, .42, .18, "#c79a4b", "#7a5a2a", 1); d.rect(x0 + .12, -2.25 - .44, .12, .18, "#7b4fa0", PEN, .8)
        d.circ(x0 + .26, -2.25 - .3, .02, "#ffd36a", GOLD, 1)
    for k in range(3):
        x0 = 2.5 + k * .35
        d.rect(x0, -2.25 - .22, .25, .14, "#c79a4b", "#7a5a2a", 1)
    d.txt(2.0, -2.8, "15  Magi caravan on a wall shelf: 3 kings + servant + pack camels, 1:24", 12, INK, "middle")
    d.dv(-2.25, 0, 4.0, "shelf +3.6 ft", 26)
    d.dv(-.8, 0, -.1, "+3.0", -24)
    d.dh(0, 3.8, 0, "3.8 ft strip (y 5.2 → 9.0)", 28)
    d.txt(2.0, .85, "Shelf: 3 × 0.3 ft, ply, painted as a road. Micro-LED lantern on each king.", 11.5, PEN, "middle")
    d2 = D(title="SIGHT CHECK from the public view spot (plan, bearings measured from V)", sc=22, ox=70, oy=18, h=470)
    d2.rect(0, 0, 9, 16, "#fffef9", INK, 1.8)
    d2.rect(9, -.4, .4, 17, "url(#hatch)", INK, 1.4); d2.rect(0, -.4, 9.4, .4, "url(#hatch)", INK, 1.4)
    hb = bearings(house); fb = bearings(O["farvil"]); mb = bearings(O["magi"])
    far = 30
    def ray(b, col, dash=None, w=1.4):
        r = math.radians(b); ex, ey = V[0] + far * math.sin(r), V[1] - far * math.cos(r)
        d2.line(V[0], V[1], ex, ey, col, w, dash)
    # shadow wedge
    r1, r2 = math.radians(hb[0]), math.radians(hb[1])
    d2.o.append(f'<clipPath id="stg7"><rect x="{d2.X(-3.5)}" y="{d2.Y(0)}" width="{22*(3.5+9.4)}" height="{22*20}"/></clipPath>')
    d2.o.append(f'<polygon clip-path="url(#stg7)" points="{d2.X(V[0]):.1f},{d2.Y(V[1]):.1f} {d2.X(V[0]+far*math.sin(r1)):.1f},{d2.Y(V[1]-far*math.cos(r1)):.1f} {d2.X(V[0]+far*math.sin(r2)):.1f},{d2.Y(V[1]-far*math.cos(r2)):.1f}" fill="{RED}" fill-opacity=".15"/>')
    ray(hb[0], RED, "6 4"); ray(hb[1], RED, "6 4"); ray(fb[0], GREEN); ray(mb[1], GOLD)
    d2.poly(cave, "#d8c8a4", INK, 1.5); d2.poly(house, "#f7f3ea", RED, 1.8, "6 4")
    d2.rect(7.8, 5.2, .8, 3.8, "#f4efe4", PEN, 1.2); d2.rect(8.7, 5.4, .3, 3.0, "#fff6e2", GOLD, 1.4)
    for k in ("hA", "hB", "hC"): d2.poly(O[k], "#f7f3ea", PEN, 1)
    d2.o.append(f'<circle cx="{d2.X(V[0]):.1f}" cy="{d2.Y(V[1]):.1f}" r="8" fill="{INK}"/>')
    d2.txt(V[0] + .4, V[1] + .5, "V · public view spot", 12, INK, weight="bold")
    d2.txt(2.0, 2.0, "", 10)
    note(d2, 470, 70, [f"Cave house blocks bearings {hb[0]:.0f}° – {hb[1]:.0f}° (red wedge).", f"Far village (14) now sits at {fb[0]:.0f}° – {fb[1]:.0f}°: visible.", f"Magi shelf (15) now sits at {mb[0]:.0f}° – {mb[1]:.0f}°: visible.", "",
                       "In the first layout both sat at 21–36°,", "directly behind the house, so the Magi were", "completely hidden from the view spot.", "",
                       "The change moves them onto the right-wall crest", "and a wall shelf, where the house cannot cover them."], 13, 20, head="WHY THEY MOVED")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M8 cascade
def m8():
    d = D(title="ELEVATION along the main sightline · star burst, strands and cloud-and-angel spiral", sc=30, ox=110, oy=410, h=470)
    # heights above church floor: z up. y coordinate = -z
    dirv = ((H[0] - V[0]), (H[1] - V[1])); dl = math.hypot(*dirv); dirv = (dirv[0] / dl, dirv[1] / dl)
    pr = lambda p: (p[0] - V[0]) * dirv[0] + (p[1] - V[1]) * dirv[1]
    s0, s1 = pr(H), pr(Lnd)
    d.rect(-3.5, 0, 12, .2, "#3b3b42", INK, 1.2); d.txt(-3.4, .5, "church floor", 11, PEN)
    d.rect(-3.5, -2.0, 6.0, 2.0, "#3b3b42", INK, 1.2); d.txt(-3.4, -1.0, "deck 2 ft", 11, "#eee")
    d.line(-3.5, -15, 8.5, -15, RED, 2, "10 6"); d.txt(-3.4, -15.3, "ceiling ≈ 15 ft (measure on site)", 12, RED, weight="bold")
    d.rect(7.6, -15, .4, 15, "url(#hatch)", INK, 1.5)
    pts = []
    for k in range(61):
        t = k / 60; a = (s0 - s0) + (s1 - s0) * t * (-1) + .9 * math.sin(t * math.pi * 6) * 0
        a = -(s1 - s0) * 0 + (s0 - s0)
    pts = []
    span = abs(s1 - s0)
    for k in range(61):
        t = k / 60
        a = 6.2 - span * t + 0.9 * math.sin(t * math.pi * 6)
        z = 14.0 + (6.5 - 14.0) * t
        pts.append((a, -z))
    d.poly(pts, "none", "#cfd6ea", 16, close=False); d.o[-1] = d.o[-1].replace('stroke-width="16"', 'stroke-width="16" stroke-linecap="round" opacity=".8"')
    d.poly(pts, "none", "#3d4f8f", 1.6, "6 4", close=False)
    for k in range(0, 61, 8):
        a, z = pts[k]; d.line(a, z, a, -15, "#7a86b0", .9, "2 3")
    for k in range(8):
        d.line(6.2 - .9 + k * .26, -14, 6.2 - .9 + k * .26, -8.0 - (k % 3) * .6, "#a7b4d6", 1.4)
    d.poly([(6.2 + math.cos(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42), -14 + math.sin(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42)) for i in range(10)], "#f3c34c", GOLD, 1.6)
    d.txt(6.9, -14.4, "7  star burst 2 ft wide", 12, GOLD, weight="bold"); d.txt(6.9, -14.0, "hung 1 ft below ceiling", 11.5, GOLD)
    d.txt(7.0, -7.6, "bead strands, 6 ft", 11.5, "#5c6ea8")
    d.txt(-1.2, -11.0, "6  cloud + angel spiral", 13, "#3d4f8f", "end", "bold"); d.txt(-1.2, -10.6, "2.5 ft wide, 30 angels", 11.5, "#3d4f8f", "end")
    d.dv(-6.5, 0, -1.8, "ends 6.5 ft", -22)
    d.dv(-14, -2, 3.0, "", 0)
    d.dv(-15, -14, 8.0, "1 ft", 26)
    ex = -3.0
    d.circ(ex, -5.5, .2, INK, INK, 1); d.line(ex, -5.3, ex, -2.5, INK, 4)
    d.txt(ex - .3, -5.9, "eye 5.2 ft", 11, INK, "end")
    d.line(ex, -5.2, 6.2, -14, RED, 1.3, "14 6 3 6"); d.txt(0.5, -9.6, "sightline to the star", 11.5, RED, rot=-47)
    d.o.append(f'<text x="{d.X(0)}" y="{d.Y(0)}" font-size="1"/>')
    note(d, 640, 110, ["7 hang points (A–G) on the ceiling:", "A  star ring, 4 lines to the hub", "B–G  six anchors on a 1.8 ft spiral line;", "     each drops to a loop in the wire frame.", "",
                       "Use 20 kg fishing line or 0.5 mm wire,", "two lines per point, never a single line.", "", "Hang plan assumes a ceiling you can screw", "into. Plasterboard needs toggle anchors or", "a rope over a beam. Check before buying."], 12.5, 19, head="RIGGING")
    d2 = D(title="STAR BURST DETAIL (top view and side view) · cascade plan", sc=100, ox=140, oy=140, h=470)
    star = [(math.cos(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42), math.sin(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42)) for i in range(10)]
    d2.poly(star, "#f6df9c", GOLD, 2)
    d2.circ(0, 0, .2, "#fff6c0", GOLD, 2); d2.circ(0, 0, .9, "none", PEN, 1, op=1)
    for k in range(60):
        a = math.radians(k * 6); d2.circ(.9 * math.cos(a), .9 * math.sin(a), .018, "#9aa6c9", PEN, .5)
    d2.dh(-1, 1, 1, "2 ft star, ring 1.8 ft", 30)
    d2.txt(0, -1.15, "TOP VIEW", 12, INK, "middle", "bold")
    d2.ptxt(300, 70, "60 strands, one every 6°", 12.5, INK); d2.ptxt(300, 90, "each strand 6 ft of crystal beads", 12.5, INK)
    d2.ptxt(300, 110, "fixed to eyelets on a 1.8 ft ring", 12.5, INK)
    # side view
    d2.ox, d2.oy = 620, 140
    d2.rect(-.2, -.9, .4, .12, "#555", INK, 1.2); d2.line(0, -.9, 0, -1.4, PEN, 2); d2.txt(0, -1.5, "ceiling hook", 11, PEN, "middle")
    d2.poly([(-1, 0), (0, -.55), (1, 0), (0, .35)], "#f6df9c", GOLD, 2)
    d2.rect(-.15, -.12, .3, .3, "#fff6c0", GOLD, 1.5)
    for k in range(-6, 7):
        d2.line(k * .15, .15, k * .15, 1.3 + abs(k) * .02, "#a7b4d6", 1.2)
    d2.txt(0, 1.7, "SIDE VIEW", 12, INK, "middle", "bold"); d2.txt(1.25, -.05, "foam core 25 mm + cotton + tinsel", 10.5, PEN)
    d2.txt(1.25, .15, "10 W warm LED centre", 10.5, GOLD)
    d2.ptxt(40, 350, "SPIRAL CONSTRUCTION", 13.5, INK, weight="bold")
    for i, tx in enumerate(["Frame: galvanised wire 3 mm, a 2.5 ft wide ribbon wound as a 3-turn helix, braced with cross-wires.",
                            "Skin: polyfill (cotton wool) teased thin and sprayed with fire retardant.",
                            "Angels: 30 × 4–6 in paper/feather, each on a 4 in loop; 5 micro-LED strings tucked in the clouds.",
                            "Test at floor level first; hang last; trim only when everything is lit."]):
        d2.ptxt(40, 374 + i * 22, tx, 12.5, INK)
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M9 backdrop
def m9():
    d = D(title="DEVELOPED ELEVATION of both walls (back wall on the left, right wall to its right) · heights above the deck", sc=31, ox=60, oy=432, h=470)
    Wd = 25
    d.rect(0, -13, 25, 13, "#e6e0d2", INK, 1.5)
    d.rect(0, -8.5, 25, 8.5, "#35508f", PEN, 1, op=1)
    d.rect(0, -13, 25, 4.5, "#27407a", PEN, 0, op=.0)
    d.rect(0, -5, 25, 5, "#d9c08a", PEN, 1.2)
    for x in range(0, 26, 5): d.line(x, -5, x, 0, "#8a7a52", 1.2)
    d.txt(12.5, -2.3, "5 panels of hills print, 5 ft × 5 ft each, twilight Judean hills", 12.5, "#4a3a18", "middle", "bold")
    d.poly([(0, -3), (2, -3.8), (4.5, -3.2), (7, -4.2), (9, -3.5)], "none", "#8a7a52", 1.6, close=False)
    d.poly([(9, -3.5), (12, -4.0), (15, -3.1), (18, -4.3), (21, -3.4), (25, -3.9)], "none", "#8a7a52", 1.6, close=False)
    d.line(9, -13, 9, 0, INK, 2, "10 5"); d.txt(9.15, -12.4, "corner (round it, 1.5 ft radius)", 11.5, INK)
    d.txt(4.5, .85, "BACK WALL 9 ft", 12, INK, "middle", "bold"); d.txt(17, .85, "RIGHT WALL 16 ft", 12, INK, "middle", "bold")
    import random
    random.seed(7)
    for k in range(90):
        x = random.uniform(.3, 24.7); z = random.uniform(9.0, 12.7)
        d.circ(x, -z, random.choice((.04, .05, .06)), "#fff", "none", 0)
    d.txt(12.5, -11.6, "fibre-optic stars: 250 ends in the top band, with a thicker band (Milky Way)", 12, "#fff", "middle")
    for x in (2.5, 5.5, 13.5, 20.5, 23.2):
        d.poly([(x, -9), (x + .3, -9.4), (x + .8, -9), (x + .3, -9.8)], "#e5b84a", "none", 0)
    for k in range(12):
        x = 1.2 + k * 1.95
        d.circ(x, -8.0, .13, "none", VIOLET, 1.5)
        d.poly([(x - .6, -7.6), (x - .15, -7.9), (x, -6.4), (x + .15, -7.9), (x + .6, -7.6), (x + .2, -7.0), (x, -6.4), (x - .2, -7.0)], "none", VIOLET, 1.2, "3 3")
    d.txt(12.5, -6.15, "12 UV angels (about 2 ft tall): invisible by day, glow violet under UV", 12, "#e7d5ff", "middle")
    d.line(3.6, -5, 8.8, -5, VIOLET, 5, "14 6"); d.line(9.2, -5, 13.9, -5, VIOLET, 5, "14 6"); d.txt(6.2, -4.55, "UV bar", 10.5, VIOLET, "middle")
    d.rect(14.2, -3.6, 3.8, .4, "none", PEN, 1, "3 3"); d.txt(16.1, -3.9, "14 far village strip", 10.5, PEN, "middle")
    d.rect(14.4, -3.62, 3.0, .08, "#8a5a2a", "#8a5a2a", 1.5); d.txt(15.9, -3.7, "", 9)
    d.txt(15.9, -4.15, "15 Magi shelf", 10.5, GOLD, "middle")
    d.poly([(7.8 + math.cos(math.radians(-90 + i * 36)) * (.45 if i % 2 == 0 else .2), -12.0 + math.sin(math.radians(-90 + i * 36)) * (.45 if i % 2 == 0 else .2)) for i in range(10)], "#f3c34c", GOLD, 1.5)
    d.txt(7.5, -12.45, "7 star", 10.5, GOLD, "end")
    d.line(0, -13.0, 25, -13.0, "#b03030", 3, "8 5"); d.txt(.2, -13.15, "ceiling track (deck + 13 ft = floor + 15 ft)", 11, "#b03030")
    d.dv(-13, 0, 25, "13 ft", 22); d.dv(-5, 0, 0, "5 ft", -22); d.dv(-13, -5, 0, "8 ft drape", -34)
    d.dh(0, 9, 0, "9 ft", 38); d.dh(9, 25, 0, "16 ft", 38)
    d2 = D(title="DETAIL · section through the wall (side view): how the pieces hang", sc=33, ox=110, oy=435, h=470)
    d2.rect(-.7, -13, .7, 13.5, "url(#hatch)", INK, 1.5)
    d2.rect(-.7, -13.5, 3, .5, "url(#hatch)", INK, 1.5); d2.txt(.7, -13.75, "ceiling (confirm height)", 11, RED)
    d2.rect(0, 0, 8, 2, "#3b3b42", INK, 1.2); d2.txt(4, 1, "deck + skirting", 11, "#eee", "middle")
    d2.rect(.05, -5, .25, 5, "#e0c690", "#8a7a52", 1.4); d2.txt(.6, -2.6, "print panel on 1 × 2 in frame (5 ft)", 11, PEN)
    d2.rect(.3, -5.4, .5, .4, "#2a2a30", INK, 1.4); d2.txt(.95, -5.15, "UV bar behind a 4 in lip", 11, VIOLET)
    d2.line(.7, -5.45, 1.3, -8.0, VIOLET, 1.6, "5 3", arrow=True)
    d2.poly([(.55, -12.8), (.75, -9), (.4, -5.4), (.8, -5.0), (.4, -4.6)], "none", "#2f4f9a", 5, close=False)
    d2.txt(1.3, -10.5, "blue drape: 1.5× pleat, rings on the track,", 11, "#2f4f9a"); d2.txt(1.3, -10.1, "bottom hem laps the print by 6 in", 11, "#2f4f9a")
    d2.rect(.3, -13.0, .4, .22, "#b03030", INK, 1.2); d2.txt(.95, -12.7, "track + rope backup", 11, "#b03030")
    d2.rect(1.9, -1.2, .8, 1.2, "#2a2a30", INK, 1.4); d2.txt(2.0, -1.45, "fibre-optic engine + hatch", 11, PEN)
    d2.line(1.95, -1.2, .5, -9.2, "#7f8fb5", 1, "2 3")
    d2.dv(-13, 0, 7.8, "13 ft above deck", 28)
    note(d2, 560, 80, ["BACKDROP BUILD ORDER", "1  fit track and rope backup first", "2  hang print panels, tape joins flat", "3  hang the drape, adjust pleats", "4  push fibre ends through, tape behind", "5  glue gold stars", "6  paint UV angels (matt, thin coats)", "7  fit UV bars and test in the dark",
                        "", "Fibre ends: 250 in the top band;", "bundles tie to one 1 ft-long bundle", "behind the drape at the corner."], 12.5, 19, head="")
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M10 electrical
def m10():
    d = D(title="BLOCK DIAGRAM · power, controller and loads (everything inside the crib is low voltage)", sc=1, ox=0, oy=0, h=470)
    def box(x, y, w, h, t1, t2="", fill="#fff", stroke=INK):
        d.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
        d.ptxt(x + w / 2, y + 22, t1, 13, INK, "middle", "bold")
        if t2: d.ptxt(x + w / 2, y + 40, t2, 11, PEN, "middle")
    def arr(x1, y1, x2, y2): d.o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{PEN}" stroke-width="1.6" marker-end="url(#ar)"/>')
    box(8, 190, 160, 60, "Church mains", "230 V · 6 A MCB + RCCB", "#fff3f0", RED)
    box(180, 90, 130, 56, "12 V 10 A PSU", "wash, spots, UV, fibre")
    box(180, 170, 130, 56, "5 V 10 A PSU", "pixels, ESP32, audio")
    box(180, 250, 130, 56, "24 V 2 A PSU", "ultrasonic mister")
    box(180, 330, 130, 56, "12 V 3 A PSU", "LED lamps, tea-lights")
    for yy in (118, 198, 278, 358): arr(168, 220, 180, yy)
    box(350, 140, 140, 150, "ESP32 controller", "4-minute cue sheet", "#eef5ff", BLUE)
    d.ptxt(420, 232, "start button", 11, PEN, "middle"); d.ptxt(420, 250, "manual override", 11, PEN, "middle"); d.ptxt(420, 268, "SD: sounds", 11, PEN, "middle")
    arr(310, 198, 350, 198); arr(310, 118, 350, 160)
    box(540, 60, 150, 80, "8-ch relay board", "12 V loads + mister")
    box(540, 160, 150, 70, "4 MOSFET dimmers", "wash, cave, field")
    box(540, 250, 150, 60, "Pixel data", "path of light")
    box(540, 330, 150, 60, "DFPlayer + amp", "2 speakers")
    for (yy, ty) in ((100, 175), (195, 205), (280, 240), (360, 270)): arr(490, ty, 540, yy)
    loads = ["Fibre · UV bars · mister · fan", "RGBW wash · cave · field · cross lamp", "WS2812 path · star LED · spiral LEDs", "Bells · crickets · angel voice · choir",
             "Lamps · campfire · Magi lanterns"]
    for i, l in enumerate(loads): d.ptxt(706, 100 + i * 70, l, 12, INK)
    d.ptxt(710, 78, "LOADS", 13, INK, weight="bold")
    d.ptxt(20, 420, "Rules: separate fuse per rail · one common ground point · label both cable ends · 1 ft service loop at every hatch ·", 12, PEN)
    d.ptxt(20, 440, "no mains voltage behind the rock · earthing and RCCB checked by an electrician before the first full run.", 12, PEN)
    d2 = D(title="CUE SHEET · 4-minute show (0:00 – 3:55 then loop)", sc=1, ox=0, oy=0, h=470)
    rows = [("RGBW sky wash", [(0, .5, "#f0b060"), (.5, 3.5, "#3a4a9a"), (3.5, 3.92, "#f0b060")]),
            ("Oil lamps (flicker)", [(.5, 3.92, "#f4c04a")]), ("Campfire", [(.5, 3.92, "#f08a3a")]), ("Fibre-optic stars", [(1, 3.92, "#9ab4e8")]),
            ("Mist", [(1, 3.5, "#b9d6ee")]), ("Ambient sound", [(1, 3.92, "#8fa98a")]), ("Field flood (white-gold)", [(1.67, 2.5, "#fff2b0")]),
            ("Floating angel (video)", [(1.67, 2.5, "#8fb8ff")]), ("UV angel choir", [(1.83, 3.5, "#b07fe0")]), ("Path of light chase", [(2.5, 3.0, "#ffd36a")]),
            ("Star + cascade LEDs", [(2.5, 3.92, "#e6c85a")]), ("Cave glow", [(3.0, 3.92, "#f1b24a")]), ("Cross-shadow lamp", [(3.0, 3.13, "#e08a3a")]), ("Magi lanterns", [(3.5, 3.92, "#e6c85a")])]
    X0, X1, Y0, RH = 230, 880, 52, 26
    d2.o.append(f'<line x1="{X0}" y1="{Y0-6}" x2="{X1}" y2="{Y0-6}" stroke="{INK}" stroke-width="1.5"/>') if False else None
    px = lambda m: X0 + (X1 - X0) * m / 4.0
    for m in range(5):
        d2.o.append(f'<line x1="{px(m)}" y1="{Y0-4}" x2="{px(m)}" y2="{Y0+RH*len(rows)}" stroke="#d0d0d0" stroke-width="1"/>')
        d2.ptxt(px(m), Y0 - 10, f"{m}:00", 12, INK, "middle")
    for i, (nm, segs) in enumerate(rows):
        yy = Y0 + i * RH
        d2.ptxt(16, yy + 17, nm, 12.5, INK)
        for a, b, c in segs:
            d2.o.append(f'<rect x="{px(a):.1f}" y="{yy+4}" width="{px(b)-px(a):.1f}" height="{RH-9}" rx="3" fill="{c}" stroke="{PEN}" stroke-width=".8"/>')
    marks = [(0, "dusk"), (.5, "night, lamps"), (1.0, "stars, mist"), (1.67, "'Glory to God'"), (1.83, "UV choir"), (2.5, "path"), (3.0, "cave + cross"), (3.5, "all warm")]
    for m, tx in marks:
        d2.ptxt(px(m) + 3, Y0 + RH * len(rows) + 16 + (14 if marks.index((m, tx)) % 2 else 0), tx, 11, PEN)
    d2.ptxt(16, 464, "Loop: fade to dusk at 3:55 and restart. A short sign says 'the crib shows every 10 minutes'.", 11.5, PEN)
    return [d.svg(), d2.svg()]


# ------------------------------------------------------------------ M11 public area
def m11():
    d = D(title="PLAN · public viewing area at the front-left corner of the stage", sc=24, ox=40, oy=40, h=470)
    # shift so V at (-3,19) is at approx x=? ; plot x from -14 to 9
    sx = lambda x: x + 14
    o_ = []
    d.o.append(f'<rect x="{d.X(sx(0))}" y="{d.Y(0)}" width="{24*9}" height="{24*16}" fill="#f3dfb0" fill-opacity=".5" stroke="{INK}" stroke-width="2"/>')
    d.o.append(f'<rect x="{d.X(sx(9))}" y="{d.Y(0)-10}" width="12" height="{24*21}" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.o.append(f'<rect x="{d.X(sx(-14))}" y="{d.Y(0)-10}" width="{24*23.4}" height="10" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.txt(sx(4.5), 8, "CRIB STAGE 9 × 16 ft", 13, INK, "middle", "bold")
    d.txt(sx(-7), -.6, "altar wall", 11, PEN, "middle")
    d.circ(sx(V[0]), V[1], 3.0, "#e8f0fb", BLUE, 1.5, op=.4)
    d.o.append(f'<circle cx="{d.X(sx(V[0])):.1f}" cy="{d.Y(V[1]):.1f}" r="9" fill="{INK}"/>')
    d.txt(sx(V[0]) + .5, V[1] + .15, "V · standing spot, 6 people at a time", 12, INK, weight="bold")
    d.line(sx(V[0]), V[1], sx(4.4), 7.4, RED, 1.3, "14 6 3 6")
    arc = [(sx(-3.3), 15.2), (sx(-4.5), 16.8), (sx(-5.0), 19.0), (sx(-4.6), 21.2), (sx(-3.2), 22.8), (sx(-1.0), 23.2), (sx(1.0), 22.4), (sx(2.0), 20.6)]
    d.poly(arc, "none", RED, 3, "2 7", close=False)
    for (x, y) in arc[::2]: d.circ(x, y, .14, "#b08a2a", INK, 1.2)
    d.txt(sx(-4.9), 23.8, "rope barrier + 4 brass posts, 5 ft from the stage front", 11.5, RED)
    d.line(sx(-12), 22, sx(-5.2), 20, PEN, 2, "3 6", arrow=True); d.txt(sx(-12), 22.8, "queue comes from the right-hand aisle", 11.5, PEN)
    d.line(sx(-1.2), 18.4, sx(-6.6), 12.8, "#3a7a3a", 2, "5 5", arrow=True); d.txt(sx(-12.6), 12.2, "exit past the altar side, 4 ft clear aisle", 11.5, "#3a7a3a")
    d.rect(sx(-9), 4.0, .6, .6, "#fff", RED, 2); d.txt(sx(-8.2), 4.5, "fire extinguisher (check church has one)", 11.5, RED)
    d.rect(sx(3.2), 15.5, 2.0, .4, "#fff", INK, 1.6); d.txt(sx(4.2), 15.3, "25 plaque", 10.5, INK, "middle")
    d.dh(sx(-3), sx(0), 19, "3 ft", 16); d.dv(16, 19, sx(-3), "3 ft", 16)
    note(d, 560, 120, ["CAPACITY: 6 people at V at once;", "queue in single file behind the rope.", "", "SIGNAGE (A4, large type):", "• 'Please stand here · the best view'", "• 'The crib shows every 10 minutes'", "• 'Find 12 details' near the plaque", "",
                       "SAFETY:", "• thermocol, cotton, fabric: fire-retardant", "• no candles; real flames only if sambrani is", "  in a closed brass holder, off by 2 m", "• cables under ramp or taped flat", "• 4 ft clear for wheelchairs at the rope"], 12.5, 19, head="")
    d2 = D(title="KEY PLAN · where this sits in the church (assumed: altar centre, crib at the right end)", sc=1, ox=0, oy=0, h=470)
    from church import church_crop
    d2.o.append(church_crop(20, 20, 560, 430, "30 30 580 440"))
    d2.ptxt(600, 80, "VIEW 1 · public spot", 13, RED, weight="bold"); d2.ptxt(600, 100, "stand here, look diagonally at the corner", 12, INK)
    d2.ptxt(600, 130, "VIEW 2 · wide shot from the aisle", 13, BLUE, weight="bold"); d2.ptxt(600, 150, "shows altar centre-left, crib at the far end", 12, INK)
    d2.ptxt(600, 190, "Check on site:", 13, INK, weight="bold")
    for i, tx in enumerate(["• is the altar really centred on this wall?", "• how far is the stage edge from the nearest pew?", "• is the right wall shared with the church wall?", "• where is the nearest power point and exit?"]):
        d2.ptxt(600, 214 + i * 22, tx, 12, INK)
    return [d.svg(), d2.svg()]
