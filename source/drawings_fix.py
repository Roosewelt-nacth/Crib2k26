import math
from drawings import *
from drawings import m0, m1, m3, m4  # re-export


def m2():
    d = D(title="FRONT ELEVATION (cut open) and PLAN · upper guest room 'kataluma'", sc=72, ox=100, oy=215)
    d.rect(0, -1.5, 4, 1.5, "#fbf6ea", INK, 2.5)
    d.rect(-.15, -1.65, 4.3, .15, "#e6dcc6", INK, 2)
    d.rect(-.15, 0, 4.3, .12, "url(#ply)", "#8a6a3a", 1.2)
    d.rect(1.6, -1.2, .5, .6, "#cfe0f5", PEN, 1.2); d.txt(1.85, -.9, "window", 9, PEN, "middle")
    for x in (.25, 1.1, 2.0, 2.9):
        d.rect(x, -.2, .8, .2, "#d9b98a", "#8a5a2a", 1.2); d.circ(x + .12, -.3, .1, "#fff", "#8a5a2a", 1.2)
    for x in (0.45, 3.2): d.circ(x, -.95, .09, "#ffd36a", GOLD, 1.5)
    d.circ(1.5, -.3, .09, "#ffd36a", GOLD, 1.5)
    d.rect(3.4, -.55, .35, .55, "#cdbb92", PEN, 1); d.rect(.05, -.55, .3, .55, "#cdbb92", PEN, 1); d.txt(.2, -.62, "jars", 9, PEN, "middle")
    d.dh(0, 4, 0.12, "4 ft", 24); d.dv(-1.5, 0, 0, "1.5 ft room", -22)
    d.txt(2, -1.8, "flat roof slab + parapet (cat on it)", 11.5, PEN, "middle")
    pts = [(4.15, .12)]
    for k in range(8):
        pts += [(4.15 + k * .3, .12 + (k + 1) * .35), (4.15 + (k + 1) * .3, .12 + (k + 1) * .35)]
    pts += [(4.15, .12 + 8 * .35)]
    d.poly(pts, "url(#rockp)", "#8a7a52", 1.4)
    d.txt(5.8, 1.2, "stone steps cut in thermocol,", 11.5, PEN); d.txt(5.8, 1.4, "rise 2.8 ft in 8 steps", 11.5, PEN)
    d.txt(1.0, 1.75, "sleeping travellers 1:6 (about 1 ft long)", 12, INK)
    d.ox, d.oy = 650, 70
    d.sc = 62
    d.rect(0, 0, 4, 2, "#fbf6ea", INK, 2.5); d.rect(0, 1.95, 4, .05, "none", RED, 4)
    d.txt(2, 2.4, "open front (cut away)", 11, RED, "middle")
    for (x, y) in ((.3, .3), (1.2, .3), (2.1, .3), (3.0, .3), (.4, 1.1), (1.5, 1.1)):
        d.rect(x, y, .8, .3, "#d9b98a", "#8a5a2a", 1.2)
    for (x, y) in ((2.7, 1.2), (3.5, 1.4), (.2, .9)): d.circ(x, y, .1, "#ffd36a", GOLD, 1.5)
    d.dh(0, 4, 2, "4 ft", 46); d.dv(0, 2, 4, "2 ft", 24)
    d.txt(2, -.2, "PLAN", 12, INK, "middle", "bold")
    d2 = D(title="SECTION · how the room is held up (no load goes on the cave roof)", sc=70, ox=80, oy=380)
    d2.rect(-.2, 0, 6.2, .08, "url(#ply)", "#8a6a3a", 1.2)
    d2.poly([(-.2, 0), (-.2, -1.6), (.6, -2.8), (5.9, -2.8), (5.9, 0)], "url(#rockp)", "#a8956b", 2)
    d2.poly([(.4, 0), (.4, -2.0), (.9, -2.2), (2.6, -2.2), (2.9, 0)], "#5a4026", INK, 1.8); d2.txt(1.6, -1.0, "cave void", 12, "#fff", "middle")
    d2.rect(.2, -2.9, 2.3, .1, "url(#ply)", "#8a6a3a", 1.6)
    d2.rect(.9, -2.82, .1, .62, "#8a6a3a", "#5a4020", 1); d2.rect(2.0, -2.82, .1, .62, "#8a6a3a", "#5a4020", 1)
    d2.txt(.95, -2.1, "post", 10, "#fff")
    d2.rect(.2, -4.4, 2.3, 1.5, "none", RED, 2, "8 5")
    d2.rect(.2, -4.45, 2.3, .08, "#e6dcc6", INK, 1.5)
    d2.rect(2.38, -4.4, .12, 1.5, "#fbf6ea", INK, 1.5); d2.txt(2.6, -3.6, "back wall", 10.5, PEN)
    d2.circ(1.0, -3.2, .06, "#ffd36a", GOLD, 1.2); d2.circ(1.7, -3.2, .06, "#ffd36a", GOLD, 1.2)
    d2.line(1.0, -3.2, 1.0, -2.9, GOLD, 1, "3 3"); d2.txt(3.1, -1.3, "LED wires run down through the", 10.5, GOLD); d2.txt(3.1, -1.1, "hill to hatch A (item 27)", 10.5, GOLD)
    d2.dv(-4.4, -2.9, .2, "1.5", -20); d2.dv(-2.8, 0, -.2, "2.8", -24)
    note(d2, 560, 110, ["Floor tray: 12 mm ply, 4 × 2 ft.", "Rests on the hill top and two 2 × 2 posts", "standing on the cave's ply base.", "Walls: 2 in thermocol, plastered.", "Whole room weighs under 8 kg.",
                        "Lamps: 3 flicker LEDs on one 3 V line.", "Hidden details: cat on the roof,", "clay oven, sleeping child."], 12.5, 19, head="BUILD NOTES")
    return [d.svg(), d2.svg()]


def m5():
    d = D(title="SIDE SECTION · Pepper's-ghost floating angel (viewer is far left, 14 ft away)", sc=120, ox=250, oy=390)
    d.rect(-1.1, 0, 3.4, .06, "url(#ply)", "#8a6a3a", 1.2)
    d.poly([(-1.1, 0), (-1.1, -.55), (-.8, -.8), (-.1, -.8), (.15, -.4), (.2, 0)], "url(#rockp)", "#8d7a52", 2)
    d.txt(-.6, -.9, "ridge (hides screen)", 11.5, INK, "middle")
    d.rect(.2, -.2, 1.6, .2, "#222", INK, 1.5); d.rect(.2, -.1, 1.0, .06, "#8fb8ff", BLUE, 1.5)
    d.txt(.7, .3, "screen face-up", 11.5, BLUE, "middle")
    d.line(0, -1.6, 1.41, -.19, "#8fb8ff", 5); d.o[-1] = d.o[-1].replace('stroke-width="5"', 'stroke-width="5" opacity=".7"')
    d.txt(.1, -2.1, "clear acrylic 3 mm at 45°:", 12, BLUE); d.txt(.1, -1.93, "2 ft slant × 2.4 ft wide", 12, BLUE)
    d.line(.5, -.14, .5, -1.1, BLUE, 1.6, "5 3", arrow=True)
    d.line(.5, -1.1, -1.9, -1.1, BLUE, 1.6, "5 3", arrow=True); d.txt(-1.9, -1.2, "to the viewer's eye", 11, BLUE)
    d.circ(1.5, -1.1, .26, "#fff", BLUE, 1.6, op=.6)
    d.txt(1.9, -1.35, "angel appears to float here", 12, BLUE, weight="bold")
    d.rect(1.6, -.5, .4, .5, "#33384a", PEN, 1); d.rect(2.0, -.6, .08, .6, "#222", PEN, 1)
    d.dh(0, 1.41, 0, "1.4 ft run", 74)
    d.txt(-1.1, .55, "hatch B: lift-out lid", 11, RED)
    note(d, 640, 90, ["How the trick works:", "the screen is lit face-up below the sheet.", "The sheet reflects it toward the viewer, so", "a glowing angel seems to hang in the air", "behind the glass, with real rocks visible", "through it.", "",
                      "Screen: tablet or monitor, brightness max,", "pure-black background video.", "Angel on screen ≈ 0.7–1 ft (1:6 scale).", "Fine-tune the glass angle at night from", "the public view spot."], 12.5, 19, head="PEPPER'S GHOST")
    d2 = D(title="PLAN · floating angel unit and valley mist (hatch B)", sc=85, ox=90, oy=170)
    d2.rect(0, 0, 2.4, 1.0, "url(#rockp)", "#8d7a52", 2); d2.txt(1.2, .9, "10 ridge 0.8 ft", 11.5, INK, "middle")
    d2.rect(.35, .15, 1.7, .5, "#bfe0ff", BLUE, 1.2); d2.txt(1.2, .43, "mister tray", 11, BLUE, "middle")
    d2.o.append(f'<circle cx="{d2.X(.7):.1f}" cy="{d2.Y(.55):.1f}" r="4" fill="{BLUE}"/><circle cx="{d2.X(1.7):.1f}" cy="{d2.Y(.55):.1f}" r="4" fill="{BLUE}"/>')
    d2.rect(0, -1.4, 2.4, 1.4, "none", BLUE, 2, "6 4")
    d2.rect(.3, -1.0, 1.8, .9, "#222", INK, 1.5); d2.rect(.55, -.9, 1.3, .65, "#8fb8ff", BLUE, 1.2); d2.txt(1.2, -.5, "screen", 12, "#222", "middle")
    d2.line(0, -1.4, 2.4, -.05, BLUE, 3)
    d2.txt(1.2, -1.5, "acrylic footprint 2.4 × 1.4 ft", 11.5, BLUE, "middle")
    d2.dh(0, 2.4, 1.0, "2.4 ft", 28)
    note(d2, 430, 70, ["TOP VIEW: the ridge is the front lip. Behind its", "lip sits a shallow tray with two ultrasonic discs and", "a 5 V fan; mist is pushed forward and rolls into the", "valley. The acrylic and screen sit behind the tray.", "",
                       "Rules:", "• keep 3 cm of water in the tray (float switch)", "• mister on its own relay, 1:00–3:30", "• never let mist reach the screen; keep a lip", "• wipe the acrylic with a microfibre cloth before", "  the show; fingerprints show as ghosts"], 12.5, 19, head="MIST + SCREEN ARRANGEMENT")
    return [d.svg(), d2.svg()]


def m6():
    s_ = 55
    dx, dy = 3.0, 9.0
    d = D(title="PLAN · village strip along the right wall (items 16–25)", sc=s_, ox=60, oy=62)
    d.o.append(f'<rect x="{d.X(0)}" y="{d.Y(0)}" width="{s_*6}" height="{s_*7}" fill="#fffef9" stroke="{INK}" stroke-width="2"/>')
    def sh(poly): return [(x - dx, y - dy) for x, y in poly]
    d.o.append(f'<rect x="{d.X(6)}" y="{d.Y(0)}" width="14" height="{s_*7}" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.poly(sh(O["street"]), "#ece8df", "#b9b2a2", 1.4)
    for k, lab in (("hA", "16"), ("hB", "17"), ("hC", "18")):
        d.poly(sh(O[k]), "#f7f3ea", INK, 1.8); p = O[k]; d.txt(sum(q[0] for q in p) / 4 - dx, sum(q[1] for q in p) / 4 - dy + .1, lab, 13, INK, "middle", "bold")
    d.poly(sh(O["well"]), "#d9e8f5", BLUE, 1.6); d.txt(5.6 - dx, 11.2 - dy + .08, "20", 11, INK, "middle")
    d.poly(sh(O["census"]), "#f6efe0", RED, 1.4); d.txt(5.2 - dx, 13.3 - dy, "21", 11, RED, "middle")
    d.poly(sh(O["donk"]), "#f6efe0", PEN, 1.2); d.txt(5.2 - dx, 10.4 - dy, "22", 11, INK, "middle")
    d.poly(sh(O["oliveR"]), "#cfdcb8", "#5d7a3e", 1.6); d.txt(5.4 - dx, 14.95 - dy, "24", 11, "#3d5a26", "middle")
    d.poly(sh(O["plaque"]), "#fff", INK, 1.6); d.txt(4.2 - dx, 15.8 - dy, "25", 11, INK, "middle")
    d.dv(0, 7, 0, "7 ft", -10)
    d.txt(3.0, 7.45, "back of the stage is at the top", 11, PEN, "middle")
    rows = ["16  house A  1.4 × 1.6 ft  h 2.0 ft", "17  house B  1.6 × 1.8 ft  h 2.5 ft (stair)", "18  house C  1.4 × 1.6 ft  h 1.8 ft", "19  street 1.1 × 6.7 ft, 0.8 → 0.3", "20  well  0.9 ft dia  h 0.6",
            "21  census table + soldier + scribe", "22  two donkeys + two travellers", "23–24  olive trees 2.0 / 1.6 ft", "25  'find 12 details' plaque 2 × 0.4 ft"]
    d.ptxt(480, 82, "ITEMS ON THIS SHEET", 13.5, INK, weight="bold")
    for i, r in enumerate(rows): d.ptxt(480, 108 + i * 21, r, 12.5, INK)
    d.ptxt(480, 322, "All at 1:6: figures 1.2 ft, doors 0.9 ft.", 12.5, PEN)
    d.ptxt(480, 343, "Window lamps: 15 flicker LEDs on a 3 V line.", 12.5, PEN)
    d.ptxt(480, 364, "Olive 23 sits front-left at (1.0, 14.2).", 12.5, PEN)
    d2 = D(title="ELEVATION along the right wall (front of stage on the right) · heights above the deck", sc=58, ox=50, oy=370)
    def zs(y): return 0.8 - (y - 9.3) * (0.5 / 6.7)
    d2.poly([(0, -0.8), (.3, -0.8), (7.0, -0.3), (7.0, 0), (0, 0)], "#ece8df", "#b9b2a2", 1.4)
    for k, lab, h in (("hA", "16", 2.0), ("hB", "17", 2.5), ("hC", "18", 1.8)):
        ys = [q[1] for q in O[k]]; y0, y1 = min(ys) - 9.0, max(ys) - 9.0
        z0 = zs((min(ys) + max(ys)) / 2)
        d2.rect(y0, -(z0 + h), y1 - y0, h, "#f7f3ea", INK, 2)
        d2.rect(y0 + .45 * (y1 - y0), -(z0 + .9), .35, .6, "#cdbb92", PEN, 1); d2.rect(y0 + .1, -(z0 + h * .6), .3, .3, "#9fb0c8", PEN, 1)
        d2.txt((y0 + y1) / 2, -(z0 + h) - .1, f"{lab}  h {h}", 11.5, INK, "middle")
    d2.txt(0, .55, "back of stage", 11.5, PEN); d2.txt(7.0, .55, "front edge", 11.5, PEN, "end")
    d2.txt(3.5, .55, "street slopes 0.8 → 0.3 ft", 11.5, PEN, "middle")
    d2.ptxt(520, 90, "Scale guide at 1:6 (hero 1:3)", 13, INK, weight="bold")
    d2.ptxt(520, 112, "adult 6 ft  →  1.0 ft", 12.5, INK); d2.ptxt(520, 132, "child 3 ft  →  0.5 ft", 12.5, INK); d2.ptxt(520, 152, "door 6 ft  →  1.0 ft", 12.5, INK)
    d2.ptxt(520, 190, "Keep house walls 2 in thick: plaster + paint", 12.5, PEN); d2.ptxt(520, 210, "the cut edges to look like lime-washed stone.", 12.5, PEN)
    return [d.svg(), d2.svg()]


def m7():
    d = D(title="ELEVATION of the right-wall crest · far village (14) and Magi shelf (15), drawn large", sc=105, ox=70, oy=345)
    d.rect(-.3, -3.0, 4.6, 2.2, "#e9eef7", PEN, 1)
    d.poly([(0, 0), (0, -.8), (4.0, -.8), (4.0, 0)], "url(#rockp)", "#a8956b", 2)
    d.txt(2.0, -.35, "hill crest +3.0 ft (rock face)", 12, INK, "middle")
    import random
    random.seed(4)
    x = .1
    while x < 3.7:
        w, hh = random.choice((.12, .15, .18)), random.choice((.25, .3, .36, .42))
        d.rect(x, -.8 - hh, w, hh, "#f3ede0", PEN, .8); x += w + .04
    d.txt(2.0, -1.4, "14  far village: 20 houses, 3–5 in tall, pale cream", 12, INK, "middle")
    d.rect(.1, -2.25, 3.8, .06, "url(#ply)", "#8a6a3a", 1.2)
    for k in range(3):
        x0 = .3 + k * .75
        d.rect(x0, -2.25 - .26, .42, .18, "#c79a4b", "#7a5a2a", 1); d.rect(x0 + .12, -2.25 - .44, .12, .18, "#7b4fa0", PEN, .8)
        d.circ(x0 + .26, -2.25 - .3, .02, "#ffd36a", GOLD, 1)
    for k in range(3):
        d.rect(2.5 + k * .35, -2.25 - .22, .25, .14, "#c79a4b", "#7a5a2a", 1)
    d.txt(2.0, -2.85, "15  Magi caravan on a wall shelf: 3 kings, servant, pack camels, 1:24", 12, INK, "middle")
    d.dv(-2.25, 0, 4.0, "shelf +3.6 ft", 26)
    d.dv(-.8, 0, -.1, "+3.0", -24)
    d.dh(0, 3.8, 0, "3.8 ft strip (y 5.2 → 9.0)", 28)
    d.txt(2.0, .85, "Shelf: 3 × 0.3 ft, ply, painted as a road. Micro-LED lantern on each king.", 11.5, PEN, "middle")
    d2 = D(title="SIGHT CHECK from the public view spot (plan, bearings measured from V)", sc=19, ox=100, oy=52, h=470)
    d2.rect(0, 0, 9, 16, "#fffef9", INK, 1.8)
    d2.rect(9, -.4, .4, 17, "url(#hatch)", INK, 1.4); d2.rect(0, -.4, 9.4, .4, "url(#hatch)", INK, 1.4)
    hb = bearings(house); fb = bearings(O["farvil"]); mb = bearings(O["magi"])
    def endp(b):
        r = math.radians(b); far = (V[1] + 0.5) / math.cos(r)
        return V[0] + far * math.sin(r), V[1] - far * math.cos(r)
    e1, e2 = endp(hb[0]), endp(hb[1])
    d2.o.append(f'<polygon points="{d2.X(V[0]):.1f},{d2.Y(V[1]):.1f} {d2.X(e1[0]):.1f},{d2.Y(e1[1]):.1f} {d2.X(e2[0]):.1f},{d2.Y(e2[1]):.1f}" fill="{RED}" fill-opacity=".15"/>')
    for b, col, dash in ((hb[0], RED, "6 4"), (hb[1], RED, "6 4"), (fb[0], GREEN, None), (mb[1], GOLD, None)):
        e = endp(b); d2.line(V[0], V[1], e[0], e[1], col, 1.4, dash)
    d2.poly(cave, "#d8c8a4", INK, 1.5); d2.poly(house, "#f7f3ea", RED, 1.8, "6 4")
    d2.rect(7.8, 5.2, .8, 3.8, "#f4efe4", PEN, 1.2); d2.rect(8.7, 5.4, .3, 3.0, "#fff6e2", GOLD, 1.4)
    for k in ("hA", "hB", "hC"): d2.poly(O[k], "#f7f3ea", PEN, 1)
    d2.o.append(f'<circle cx="{d2.X(V[0]):.1f}" cy="{d2.Y(V[1]):.1f}" r="8" fill="{INK}"/>')
    d2.txt(V[0] + .5, V[1] + .1, "V · public view spot", 12, INK, weight="bold")
    d2.txt(4.0, 9.8, "cave house", 11, RED, "middle")
    note(d2, 470, 80, [f"Cave house blocks bearings {hb[0]:.0f}° – {hb[1]:.0f}° (red wedge).", f"Far village (14) now sits at {fb[0]:.0f}° – {fb[1]:.0f}°: visible.", f"Magi shelf (15) now sits at {mb[0]:.0f}° – {mb[1]:.0f}°: visible.", "",
                       "In the first layout both sat at 21–36°,", "directly behind the house, so the Magi were", "completely hidden from the view spot.", "",
                       "The change moves them onto the right-wall crest", "and a wall shelf, where the house cannot cover them."], 13, 20, head="WHY THEY MOVED")
    return [d.svg(), d2.svg()]


def m8():
    d = D(title="ELEVATION at the star corner · star burst, strands and cloud-and-angel spiral (heights above the church floor)", sc=24, ox=210, oy=432, h=470)
    span = 4.0
    xl = 6.2 - span
    d.rect(-6, 0, 14.4, .15, "#3b3b42", INK, 1.2); d.txt(-5.9, .65, "church floor", 11, PEN)
    d.rect(-6, -2.0, 5.5, 2.0, "#3b3b42", INK, 1.2); d.txt(-5.8, -1.0, "deck 2 ft", 11, "#eee")
    d.line(-6, -15, 7.6, -15, RED, 2, "10 6"); d.txt(-5.9, -15.25, "ceiling ≈ 15 ft (measure on site)", 12, RED, weight="bold")
    d.rect(7.6, -15, .5, 15, "url(#hatch)", INK, 1.5)
    pts = []
    for k in range(61):
        t = k / 60
        pts.append((6.2 - span * t + 0.9 * math.sin(t * math.pi * 6), -(14.0 + (6.5 - 14.0) * t)))
    d.poly(pts, "none", "#cfd6ea", 16, close=False); d.o[-1] = d.o[-1].replace('stroke-width="16"', 'stroke-width="16" stroke-linecap="round" opacity=".8"')
    d.poly(pts, "none", "#3d4f8f", 1.6, "6 4", close=False)
    for k in range(0, 61, 10):
        a, z = pts[k]; d.line(a, z, a, -15, "#7a86b0", .9, "2 3")
    for k in range(8):
        d.line(6.2 - .9 + k * .26, -14, 6.2 - .9 + k * .26, -8.0 - (k % 3) * .6, "#a7b4d6", 1.4)
    d.poly([(6.2 + math.cos(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42), -14 + math.sin(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42)) for i in range(10)], "#f3c34c", GOLD, 1.6)
    d.txt(5.0, -13.7, "7  star burst, 2 ft wide, hung 1 ft", 12, GOLD, "end", "bold"); d.txt(5.0, -13.3, "below the ceiling", 12, GOLD, "end")
    d.txt(7.0, -9.5, "strands 6 ft", 11.5, "#5c6ea8", "end")
    d.txt(xl - .9, -10.5, "6  cloud + angel spiral,", 12.5, "#3d4f8f", "end", "bold"); d.txt(xl - .9, -10.1, "2.5 ft wide, 30 angels", 12, "#3d4f8f", "end")
    d.dv(-6.5, 0, xl - 1.4, "6.5 ft", -10)
    d.line(-5.8, -6.4, -1.2, -9.8, RED, 1.3, "14 6 3 6", arrow=True); d.txt(-5.9, -6.9, "sightline from the viewer", 11.5, RED); d.txt(-5.9, -6.5, "eye 5.2 ft, 20.8 ft away", 11.5, RED)
    note(d, 640, 110, ["7 hang points (A–G) on the ceiling:", "A  star ring, 4 lines to the hub", "B–G  six anchors on a 1.8 ft spiral line;", "     each drops to a loop in the wire frame.", "",
                       "Use 20 kg fishing line or 0.5 mm wire,", "two lines per point, never a single line.", "", "Hang plan assumes a ceiling you can screw", "into. Plasterboard needs toggle anchors or", "a rope over a beam. Check before buying."], 12.5, 19, head="RIGGING")
    d2 = D(title="STAR BURST DETAIL (top view and side view)", sc=100, ox=150, oy=185, h=470)
    star = [(math.cos(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42), math.sin(math.radians(-90 + i * 36)) * (1.0 if i % 2 == 0 else .42)) for i in range(10)]
    d2.poly(star, "#f6df9c", GOLD, 2)
    d2.circ(0, 0, .2, "#fff6c0", GOLD, 2); d2.circ(0, 0, .9, "none", PEN, 1)
    for k in range(60):
        a = math.radians(k * 6); d2.circ(.9 * math.cos(a), .9 * math.sin(a), .018, "#9aa6c9", PEN, .5)
    d2.dh(-1, 1, 1, "2 ft star, ring 1.8 ft", 30)
    d2.txt(0, -1.25, "TOP VIEW", 12, INK, "middle", "bold")
    d2.ptxt(330, 80, "30 strands, one every 12°", 12.5, INK); d2.ptxt(330, 100, "each strand 6 ft of crystal beads", 12.5, INK); d2.ptxt(330, 120, "fixed to eyelets on a 1.8 ft ring", 12.5, INK)
    d2.ox, d2.oy = 700, 160
    d2.rect(-.2, -.9, .4, .12, "#555", INK, 1.2); d2.line(0, -.9, 0, -1.3, PEN, 2); d2.txt(0, -1.4, "ceiling hook", 11, PEN, "middle")
    d2.poly([(-1, 0), (0, -.55), (1, 0), (0, .35)], "#f6df9c", GOLD, 2)
    d2.rect(-.15, -.12, .3, .3, "#fff6c0", GOLD, 1.5)
    for k in range(-6, 7): d2.line(k * .15, .15, k * .15, 1.3 + abs(k) * .02, "#a7b4d6", 1.2)
    d2.txt(0, 1.75, "SIDE VIEW", 12, INK, "middle", "bold")
    d2.txt(0, 2.0, "foam core 25 mm + cotton + tinsel", 10.5, PEN, "middle"); d2.txt(0, 2.2, "10 W warm LED centre", 10.5, GOLD, "middle")
    d2.ptxt(40, 372, "SPIRAL CONSTRUCTION", 13.5, INK, weight="bold")
    for i, tx in enumerate(["Frame: galvanised wire 3 mm, a 2.5 ft wide ribbon wound as a 3-turn helix, braced with cross-wires.",
                            "Skin: polyfill (cotton wool) teased thin and sprayed with fire retardant.",
                            "Angels: 30 × 4–6 in paper/feather, each on a 4 in loop; 5 micro-LED strings tucked in the clouds.",
                            "Test at floor level first; hang last; trim only when everything is lit."]):
        d2.ptxt(40, 396 + i * 21, tx, 12.5, INK)
    return [d.svg(), d2.svg()]


def m9():
    d = D(title="DEVELOPED ELEVATION of both walls (back wall left, right wall to its right) · heights above the deck", sc=28, ox=100, oy=410, h=470)
    d.rect(0, -13, 25, 13, "#e6e0d2", INK, 1.5)
    d.rect(0, -13, 25, 8, "#2b4585", PEN, 1)
    d.rect(0, -5, 25, 5, "#d9c08a", PEN, 1.2)
    for x in range(0, 26, 5): d.line(x, -5, x, 0, "#8a7a52", 1.2)
    d.txt(12.5, -2.3, "5 panels of hills print, 5 ft × 5 ft each, twilight Judean hills", 12.5, "#4a3a18", "middle", "bold")
    d.poly([(0, -3), (2, -3.8), (4.5, -3.2), (7, -4.2), (9, -3.5)], "none", "#8a7a52", 1.6, close=False)
    d.poly([(9, -3.5), (12, -4.0), (15, -3.1), (18, -4.3), (21, -3.4), (25, -3.9)], "none", "#8a7a52", 1.6, close=False)
    d.line(9, -13, 9, 0, INK, 2, "10 5"); d.txt(9.2, -.35, "corner, rounded 1.5 ft radius", 11, INK)
    import random
    random.seed(7)
    for k in range(110):
        d.circ(random.uniform(.3, 24.7), -random.uniform(9.4, 12.7), random.choice((.04, .05, .06)), "#fff", "none", 0)
    d.txt(12.5, -12.3, "fibre-optic stars: 250 ends in the top band, a denser Milky Way streak", 12, "#fff", "middle")
    for x in (2.5, 5.5, 13.5, 20.5, 23.2):
        d.poly([(x, -9.7), (x + .3, -10.2), (x + .8, -9.7), (x + .3, -10.6)], "#e5b84a", "none", 0)
    for k in range(12):
        x = 1.2 + k * 1.95
        d.circ(x, -8.2, .15, "none", "#caa8ff", 1.5)
        d.poly([(x - .6, -7.8), (x - .15, -8.1), (x, -6.5), (x + .15, -8.1), (x + .6, -7.8), (x + .2, -7.2), (x, -6.5), (x - .2, -7.2)], "none", "#caa8ff", 1.2, "3 3")
    d.txt(12.5, -5.6, "12 UV angels, 2 ft tall: invisible by day, glow violet under UV", 12, "#e7d5ff", "middle")
    d.line(3.6, -5.1, 8.8, -5.1, VIOLET, 4, "14 6"); d.line(9.2, -5.1, 13.9, -5.1, VIOLET, 4, "14 6"); d.txt(6.2, -4.65, "UV bar", 10.5, VIOLET, "middle")
    d.rect(14.2, -3.5, 3.8, .35, "none", PEN, 1.4, "3 3"); d.txt(16.1, -3.7, "14", 10.5, PEN, "middle")
    d.rect(14.4, -3.62, 3.0, .08, "#8a5a2a", "#8a5a2a", 1.5); d.txt(15.9, -4.0, "15 Magi shelf", 10.5, GOLD, "middle")
    d.poly([(7.8 + math.cos(math.radians(-90 + i * 36)) * (.45 if i % 2 == 0 else .2), -11.4 + math.sin(math.radians(-90 + i * 36)) * (.45 if i % 2 == 0 else .2)) for i in range(10)], "#f3c34c", GOLD, 1.5)
    d.txt(7.4, -10.8, "7 star", 10.5, "#f3c34c", "end")
    d.line(0, -13.0, 25, -13.0, "#b03030", 3, "8 5"); d.txt(.2, -13.25, "ceiling track (deck + 13 ft = floor + 15 ft)", 11, "#b03030")
    d.dv(-13, 0, 25, "13 ft", 22); d.dv(-13, -5, 0, "8 ft drape", -10); d.dv(-5, 0, 0, "5 ft print", -10)
    d.dh(0, 9, 0, "back wall 9 ft", 22); d.dh(9, 25, 0, "right wall 16 ft", 22)
    d2 = D(title="DETAIL · section through the wall (side view): how the pieces hang", sc=26, ox=110, oy=400, h=470)
    d2.rect(-.7, -13, .7, 13.5, "url(#hatch)", INK, 1.5)
    d2.rect(-.7, -13.5, 3, .5, "url(#hatch)", INK, 1.5); d2.txt(2.5, -13.2, "ceiling (confirm height)", 11, RED)
    d2.rect(0, 0, 8, 2, "#3b3b42", INK, 1.2); d2.txt(4, 1, "deck + skirting", 11, "#eee", "middle")
    d2.rect(.05, -5, .25, 5, "#e0c690", "#8a7a52", 1.4); d2.txt(.9, -2.6, "print panel on 1 × 2 in frame (5 ft)", 11, PEN)
    d2.rect(.3, -5.4, .5, .4, "#2a2a30", INK, 1.4); d2.txt(1.0, -5.1, "UV bar behind a 4 in lip", 11, VIOLET)
    d2.line(.7, -5.45, 1.5, -8.0, VIOLET, 1.6, "5 3", arrow=True)
    d2.poly([(.55, -12.8), (.75, -9), (.4, -5.4), (.8, -5.0), (.4, -4.6)], "none", "#2f4f9a", 5, close=False)
    d2.txt(1.3, -10.6, "blue drape: 1.5× pleat, rings on the track,", 11, "#2f4f9a"); d2.txt(1.3, -10.2, "bottom hem laps the print by 6 in", 11, "#2f4f9a")
    d2.rect(.3, -13.0, .4, .22, "#b03030", INK, 1.2); d2.txt(1.0, -12.5, "track + rope backup", 11, "#b03030")
    d2.rect(1.9, -1.2, .8, 1.2, "#2a2a30", INK, 1.4); d2.txt(2.9, -.5, "fibre-optic engine in hatch", 11, PEN)
    d2.dv(-13, 0, 7.8, "13 ft above deck", 28)
    note(d2, 560, 80, ["BACKDROP BUILD ORDER", "1  fit track and rope backup first", "2  hang print panels, tape joins flat", "3  hang the drape, adjust pleats", "4  push fibre ends through, tape behind", "5  glue gold stars", "6  paint UV angels (matt, thin coats)", "7  fit UV bars and test in the dark",
                        "", "Fibre ends: 250 in the top band;", "bundle them to one 1 ft-long bundle", "behind the drape at the corner."], 12.5, 19)
    return [d.svg(), d2.svg()]


def m10():
    a, b = _m10_orig()
    return [a, b]


import drawings as _dr
_m10_orig = _dr.m10


def m11():
    d = D(title="PLAN · public viewing area at the front-left corner of the stage", sc=17.5, ox=40, oy=52, h=470)
    sx = lambda x: x + 14
    d.o.append(f'<rect x="{d.X(sx(0))}" y="{d.Y(0)}" width="{17.5*9}" height="{17.5*16}" fill="#f3dfb0" fill-opacity=".5" stroke="{INK}" stroke-width="2"/>')
    d.o.append(f'<rect x="{d.X(sx(9))}" y="{d.Y(0)-8}" width="12" height="{17.5*21}" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.o.append(f'<rect x="{d.X(sx(-14))}" y="{d.Y(0)-8}" width="{17.5*23.4}" height="8" fill="url(#hatch)" stroke="{INK}" stroke-width="1.5"/>')
    d.txt(sx(4.5), 8, "CRIB STAGE 9 × 16 ft", 12.5, INK, "middle", "bold")
    d.txt(sx(-7), -.7, "altar wall", 11, PEN, "middle")
    d.circ(sx(V[0]), V[1], 3.0, "#e8f0fb", BLUE, 1.5, op=.4)
    d.o.append(f'<circle cx="{d.X(sx(V[0])):.1f}" cy="{d.Y(V[1]):.1f}" r="8" fill="{INK}"/>')
    d.txt(sx(V[0]) + .4, V[1] - .3, "V", 13, INK, weight="bold")
    d.line(sx(V[0]), V[1], sx(4.4), 7.4, RED, 1.3, "14 6 3 6")
    arc = [(sx(-3.3), 15.2), (sx(-4.5), 16.8), (sx(-5.0), 19.0), (sx(-4.6), 21.2), (sx(-3.2), 22.8), (sx(-1.0), 23.2), (sx(1.0), 22.4), (sx(2.0), 20.6)]
    d.poly(arc, "none", RED, 3, "2 7", close=False)
    for (x, y) in arc[::2]: d.circ(x, y, .16, "#b08a2a", INK, 1.2)
    d.txt(sx(-10.2), 17.8, "rope barrier + 4 posts", 11.5, RED)
    d.line(sx(-13), 21.5, sx(-5.6), 20.0, PEN, 2, "3 6", arrow=True); d.txt(sx(-13.7), 23.2, "queue from the right-hand aisle", 11.5, PEN)
    d.line(sx(-3.4), 17.2, sx(-8), 11.0, "#3a7a3a", 2, "5 5", arrow=True); d.txt(sx(-13.7), 10.3, "exit toward the altar side, 4 ft clear", 11.5, "#3a7a3a")
    d.rect(sx(-9), 3.6, .7, .7, "#fff", RED, 2); d.txt(sx(-8.0), 4.35, "fire extinguisher", 11.5, RED)
    d.rect(sx(3.2), 15.5, 2.0, .45, "#fff", INK, 1.6); d.txt(sx(4.2), 15.3, "25 plaque", 10.5, INK, "middle")
    d.dh(sx(-3), sx(0), 19, "3 ft", 14)
    note(d, 500, 90, ["V = standing spot, 3 ft left and 3 ft in front", "of the stage corner. 6 people at a time;", "single file behind the rope.", "", "SIGNAGE (A4, large type):", "• 'Please stand here · the best view'", "• 'The crib shows every 10 minutes'", "• 'Find 12 details' near the plaque", "",
                      "SAFETY:", "• thermocol, cotton, fabric: fire-retardant", "• no candles; sambrani only in a closed", "  brass holder, 2 m from the cascade", "• cables under a ramp or taped flat", "• 4 ft clear for wheelchairs at the rope"], 12.5, 19)
    d2 = D(title="KEY PLAN · where this sits in the church (assumed: altar centre, crib at the right end)", sc=1, ox=0, oy=0, h=470)
    from church import church_crop
    d2.o.append(church_crop(20, 36, 560, 424, "30 30 580 440"))
    d2.ptxt(600, 80, "VIEW 1 · public spot", 13, RED, weight="bold"); d2.ptxt(600, 100, "stand here, look diagonally at the corner", 12, INK)
    d2.ptxt(600, 130, "VIEW 2 · wide shot from the aisle", 13, BLUE, weight="bold"); d2.ptxt(600, 150, "shows altar centre-left, crib at the far end", 12, INK)
    d2.ptxt(600, 190, "Check on site:", 13, INK, weight="bold")
    for i, tx in enumerate(["• is the altar really centred on this wall?", "• how far is the stage edge from the pews?", "• is the right wall the church wall?", "• where are the power point and the exit?"]):
        d2.ptxt(600, 214 + i * 22, tx, 12, INK)
    return [d.svg(), d2.svg()]
