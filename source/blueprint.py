import math, sys
from church import church_crop
OUT = sys.argv[1]

# ---------------- geometry (feet). x: 0 (open left edge) -> 9 (right church wall)
#                                   y: 0 (back church wall) -> 16 (open front edge)
PX, OX, OY = 80, 330, 150
def P(x, y): return (OX + PX * x, OY + PX * y)
def pts(poly): return " ".join(f"{P(x,y)[0]:.1f},{P(x,y)[1]:.1f}" for x, y in poly)

V = (-3.0, 19.0)                     # public viewing spot
H = (7.8, 1.2)                       # star hang point (corner, at ceiling)
C = (4.4, 7.4)                       # cave centre
d = (V[0] - C[0], V[1] - C[1]); L_ = math.hypot(*d)
v = (d[0] / L_, d[1] / L_)           # unit vector: cave -> viewer
u = (-v[1], v[0])                    # cave width axis
if u[0] < 0: u = (-u[0], -u[1])
ANG = math.degrees(math.atan2(u[1], u[0]))

def rrect(c, hw, hd):
    return [(c[0] + sx * hw * u[0] + sy * hd * v[0], c[1] + sx * hw * u[1] + sy * hd * v[1])
            for sx, sy in ((-1, 1), (1, 1), (1, -1), (-1, -1))]
def rect(x, y, w, h): return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
def circ(cx, cy, r, n=16): return [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n)) for k in range(n)]
def off(c, k): return (c[0] - k * v[0], c[1] - k * v[1])

cave = rrect(C, 2.0, 1.25)
holy = rrect(off(C, -0.15), 1.5, 0.6)
house = rrect(off(C, 1.5), 2.0, 1.0)
Lnd = off(C, 3.0)                    # cascade landing point (over the crest behind the house)
mouth = off(C, -1.25)

O = {  # solid floor objects for the overlap check
 "cave": cave, "holy": holy, "house": house,
 "shep": rect(0.2, 7.0, 1.7, 2.6), "holo": rect(0.3, 3.2, 2.4, 1.4), "ridge": rect(0.3, 4.6, 2.4, 1.0),
 "fold": rect(0.4, 1.7, 2.0, 1.3), "tower": circ(3.0, 1.0, 0.5), "farvil": rect(7.8, 5.2, 0.8, 3.8),
 "magi": rect(8.7, 5.4, 0.3, 3.0), "hA": rect(7.6, 9.4, 1.4, 1.6), "hB": rect(7.4, 11.3, 1.6, 1.8),
 "hC": rect(7.6, 13.4, 1.4, 1.6), "street": rect(6.2, 9.3, 1.1, 6.7), "well": circ(5.6, 11.2, 0.45),
 "census": rect(4.5, 12.8, 1.4, 1.0), "donk": rect(4.6, 10.0, 1.2, 0.6), "oliveL": circ(1.0, 14.2, 0.6),
 "oliveR": circ(5.4, 14.9, 0.5), "plaque": rect(3.2, 15.5, 2.0, 0.4),
}
ALLOW = {frozenset(p) for p in (("cave", "holy"), ("cave", "house"), ("holy", "house"))}

def sat(a, b):
    for poly in (a, b):
        for i in range(len(poly)):
            x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]
            nx, ny = y1 - y2, x2 - x1
            pa = [nx * x + ny * y for x, y in a]; pb = [nx * x + ny * y for x, y in b]
            if max(pa) <= min(pb) or max(pb) <= min(pa): return False
    return True
keys = list(O)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if frozenset((keys[i], keys[j])) in ALLOW: continue
        assert not sat(O[keys[i]], O[keys[j]]), f"overlap {keys[i]} / {keys[j]}"
for k, poly in O.items():
    assert all(-1e-6 <= x <= 9 + 1e-6 and -1e-6 <= y <= 16 + 1e-6 for x, y in poly), f"out of stage {k}"
# path of light must not cross solid objects (except into cave mouth)
path = [(2.0, 15.9), (2.3, 13.6), (3.0, 11.2), (3.55, 9.25), mouth]
for k, poly in O.items():
    if k in ("cave", "holy", "house"): continue
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        seg = [(x1 - .25, y1), (x2 - .25, y2), (x2 + .25, y2), (x1 + .25, y1)]
        assert not sat(seg, poly), f"path hits {k}"

dist = lambda p: math.hypot(p[0] - V[0], p[1] - V[1])
print("cave angle", round(ANG, 1), "cave dist", round(dist(C), 1))

# ---------------- svg ----------------
INK, PEN, GOLD, BLUE, RED = "#2b2a33", "#4a4a55", "#b07a12", "#2f5aa8", "#a8322c"
HAND = "'Segoe Print','Kalam','Comic Sans MS',cursive"
SANS = "'Segoe UI',Arial,sans-serif"
W, Ht = 3200, 1820
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Ht}" viewBox="0 0 {W} {Ht}">']
s.append('''<defs>
<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#e9e6dc"/><path d="M0 0V10" stroke="#6a6a72" stroke-width="2"/></pattern>
<pattern id="grid" width="80" height="80" patternUnits="userSpaceOnUse" x="330" y="150"><path d="M80 0H0V80" fill="none" stroke="#d6dbe6" stroke-width="1"/></pattern>
<pattern id="rock" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#efe6d2"/><circle cx="4" cy="5" r="1.2" fill="#c9b892"/><circle cx="11" cy="11" r="1" fill="#c9b892"/></pattern>
<pattern id="cob" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#ece8df"/><rect x="1" y="1" width="10" height="10" rx="3" fill="none" stroke="#b9b2a2"/></pattern>
<clipPath id="stage"><rect x="330" y="150" width="720" height="1280"/></clipPath>
<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4a4a55"/></marker>
</defs>''')
s.append(f'<rect width="{W}" height="{Ht}" fill="#fbfaf6"/>')
s.append(f'<rect x="12" y="12" width="{W-24}" height="{Ht-24}" fill="none" stroke="{INK}" stroke-width="3"/>')
s.append(f'<text x="40" y="66" font-family="{HAND}" font-size="34" fill="{INK}">Crib 2026 · "That Night in Bethlehem" · layout blueprint</text>')
s.append(f'<text x="40" y="100" font-family="{SANS}" font-size="17" fill="{PEN}">Stage 9 ft × 16 ft in the church\'s right corner · 1 square = 1 ft · heights are above the stage deck unless marked "floor"</text>')

def T(x, y, t, size=15, fill=INK, anchor="start", font=HAND, rot=None, weight="normal"):
    tr = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{tr}>{t}</text>'
def num(n, x, y):
    X, Y = P(x, y)
    return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="13" fill="#fff" stroke="{INK}" stroke-width="1.6"/>' + T(X, Y + 5, str(n), 14, INK, "middle", SANS, weight="bold")
def poly(p, fill, stroke=PEN, sw=1.6, dash=None, op=1):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polygon points="{pts(p)}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{da}/>'

# --- plan heading
s.append(T(40, 190, "TOP VIEW (PLAN)", 22, INK))
# stage + grid
s.append(f'<rect x="330" y="150" width="720" height="1280" fill="#fffef9"/><rect x="330" y="150" width="720" height="1280" fill="url(#grid)"/>')
# walls
s.append(f'<rect x="40" y="128" width="1050" height="22" fill="url(#hatch)" stroke="{INK}" stroke-width="2"/>')
s.append(f'<rect x="1050" y="128" width="22" height="1540" fill="url(#hatch)" stroke="{INK}" stroke-width="2"/>')
s.append(T(700, 122, "CHURCH WALL (back) · 9 ft of stage", 15, INK, "middle", SANS, weight="bold"))
s.append(T(1095, 790, "CHURCH WALL (right side) · 16 ft of stage", 15, INK, "middle", SANS, rot=90, weight="bold"))
# zones (terraces, hill, rake)
s.append(poly(rect(0, 0, 3.4, 7.0), "#e8efd8", "#9fb27f", 1, "6 5"))
s.append(T(*P(1.7, 6.7), "⑫ terraces +0.8 → +2.0", 13, "#5d7a3e", "middle"))
hill = [(3.0, 2.2), (6.0, 1.8), (9.0, 1.7), (9.0, 9.0), (7.1, 9.1), (6.2, 8.9), (5.6, 9.9), (3.4, 9.6), (2.0, 7.6), (2.6, 5.0)]
s.append(poly(hill, "url(#rock)", "#a8956b", 1.4, "7 5"))
# scale zone arcs (distance from viewer)
for r, lab in ((11, "A | B"), (15, "B | C"), (18, "C | D")):
    X, Y = P(*V)
    s.append(f'<circle cx="{X}" cy="{Y}" r="{r*PX}" fill="none" stroke="#8a9bc2" stroke-width="1.2" stroke-dasharray="3 7" clip-path="url(#stage)"/>')
# backdrop strips along walls
s.append(f'<rect x="330" y="150" width="720" height="10" fill="{BLUE}" opacity=".55"/><rect x="1040" y="150" width="10" height="1280" fill="{BLUE}" opacity=".55"/>')
s.append(T(*P(4.3, 0.08), "", 1))
# far village, tower, fold, magi
s.append(poly(O["farvil"], "#f4efe4", PEN, 1.2)); s.append(T(*P(7.62, 7.1), "⑭ far village 1:24", 11, INK, "middle", rot=-90))
for k in range(6):
    y = 5.4 + k * 0.6
    s.append(poly(rect(7.95, y, 0.35, 0.35), "#fff", PEN, 0.8))
s.append(poly(O["tower"], "#f1e9d6", INK, 1.6)); s.append(T(*P(3.0, 1.12), "⑬", 13, INK, "middle"))
s.append(poly(O["fold"], "#f1e9d6", PEN, 1.4)); s.append(T(*P(1.4, 2.45), "⑪ sheepfold", 12, INK, "middle"))
s.append(poly(O["magi"], "#fff6e2", GOLD, 1.4)); s.append(T(*P(8.85, 6.95), "⑮", 12, GOLD, "middle", weight="bold"))
# hologram + ridge
s.append(poly(O["holo"], "#eef2fb", BLUE, 1.6))
a1, a2 = P(0.5, 4.4), P(2.6, 3.4)
s.append(f'<path d="M{a1[0]} {a1[1]}L{a2[0]} {a2[1]}" stroke="{BLUE}" stroke-width="4"/>')
s.append(poly(rect(0.9, 3.7, 1.3, 0.6), "#33384a", PEN, 1))
s.append(T(*P(1.55, 3.45), "⑨ floating angel (Pepper's ghost)", 12, BLUE, "middle"))
s.append(poly(O["ridge"], "url(#rock)", "#8d7a52", 1.6)); s.append(T(*P(1.5, 5.2), "⑩ rock ridge + mist tray", 12, INK, "middle"))
# shepherds
s.append(poly(O["shep"], "#f6f1e3", PEN, 1.4))
for (x, y) in ((0.6, 7.6), (1.4, 7.9), (0.7, 8.8), (1.5, 9.1), (1.1, 8.3)):
    s.append(poly(circ(x, y, 0.16, 10), "#fff", PEN, 1))
s.append(poly(circ(1.0, 8.3, 0.12, 8), "#f0a03a", "#c05a10", 1))
s.append(T(*P(1.05, 7.35), "⑧ shepherds", 12, INK, "middle"))
# hill & cave & house
s.append(poly(cave, "#d8c8a4", INK, 2.4))
s.append(poly(holy, "#f3dfb0", GOLD, 1.6))
s.append(poly(house, "none", RED, 2, "9 6"))
cx, cy = P(*C)
s.append(T(cx, cy + 4, "② CAVE", 15, INK, "middle", rot=ANG, weight="bold"))
hx, hy = P(*off(C, -0.15))
s.append(T(hx, hy + 16, "③ Holy Family", 12, GOLD, "middle", rot=ANG))
hcx, hcy = P(*off(C, 1.85))
s.append(T(hcx, hcy, "④ house · UPPER level", 13, RED, "middle", rot=ANG))
# cave dims
e1, e2 = P(*cave[0]), P(*cave[1])
s.append(T((e1[0] + e2[0]) / 2 + 12, (e1[1] + e2[1]) / 2 + 26, "4 ft", 14, INK, "middle", rot=ANG))
e3 = P(*cave[2])
s.append(T((e2[0] + e3[0]) / 2 + 16, (e2[1] + e3[1]) / 2 + 2, "2.5 ft", 13, INK, "middle", rot=ANG - 90))
# mouth arc
mx, my = P(*mouth)
s.append(f'<path d="M{P(*off((mouth[0]-1.5*u[0], mouth[1]-1.5*u[1]),0))[0]:.1f} {P(*off((mouth[0]-1.5*u[0], mouth[1]-1.5*u[1]),0))[1]:.1f} L{P(mouth[0]+1.5*u[0], mouth[1]+1.5*u[1])[0]:.1f} {P(mouth[0]+1.5*u[0], mouth[1]+1.5*u[1])[1]:.1f}" stroke="#fffef9" stroke-width="5"/>')
s.append(T(mx + 120, my + 70, "mouth 3 ft, faces viewer", 12, INK, "middle", rot=ANG))
# cascade (overhead)
H1, L1 = P(*H), P(*Lnd)
s.append(f'<path d="M{H1[0]} {H1[1]} L{L1[0]} {L1[1]}" stroke="#9aa6c9" stroke-width="56" stroke-linecap="round" opacity=".28"/>')
zig = []
n = 9
for k in range(n + 1):
    t = k / n
    x = H[0] + (Lnd[0] - H[0]) * t; y = H[1] + (Lnd[1] - H[1]) * t
    w = 0.9 * math.sin(t * math.pi * 3) * (0.5 + 0.5 * t)
    X, Y = P(x + w * 0.86, y + w * 0.5)
    zig.append(f"{X:.1f},{Y:.1f}")
s.append(f'<polyline points="{" ".join(zig)}" fill="none" stroke="#5c6ea8" stroke-width="2" stroke-dasharray="6 4"/>')
sx_, sy_ = H1
star = " ".join(f"{sx_+math.cos(math.radians(-90+i*36))*(20 if i%2==0 else 8):.1f},{sy_+math.sin(math.radians(-90+i*36))*(20 if i%2==0 else 8):.1f}" for i in range(10))
s.append(f'<polygon points="{star}" fill="#f3c34c" stroke="{GOLD}" stroke-width="1.5"/>')
s.append(T(H1[0] - 30, H1[1] + 44, "⑦ star hang point", 13, GOLD, "end", weight="bold"))
s.append(T(H1[0] - 30, H1[1] + 62, "(at ceiling, height: confirm)", 12, GOLD, "end"))
s.append(T(*P(7.55, 3.95), "⑥ cloud + angel spiral", 13, "#3d4f8f", "middle", rot=-58))
s.append(T(*P(7.95, 4.3), "(overhead, lands +4.5 ft)", 11, "#3d4f8f", "middle", rot=-58))
# village
s.append(poly(O["street"], "url(#cob)", PEN, 1.2))
s.append(T(*P(6.75, 14.6), "⑲ street 1.1 ft", 12, INK, "middle", rot=-90))
for k, lab, n_ in (("hA", "⑯", "h 2 ft"), ("hB", "⑰", "h 2.5 ft"), ("hC", "⑱", "h 1.8 ft")):
    p = O[k]; s.append(poly(p, "#f7f3ea", INK, 1.8))
    cxh = sum(q[0] for q in p) / 4; cyh = sum(q[1] for q in p) / 4
    s.append(T(*P(cxh, cyh - 0.05), lab + " house", 13, INK, "middle"))
    s.append(T(*P(cxh, cyh + 0.3), n_, 12, PEN, "middle"))
s.append(poly(O["well"], "#d9e8f5", BLUE, 1.6)); s.append(T(*P(5.6, 11.95), "⑳ well", 12, INK, "middle"))
s.append(poly(O["census"], "#f6efe0", RED, 1.4)); s.append(T(*P(5.2, 13.38), "㉑ census + soldier", 12, RED, "middle"))
s.append(poly(O["donk"], "#f6efe0", PEN, 1.2)); s.append(T(*P(5.2, 10.42), "㉒ donkeys", 11, INK, "middle"))
# olives, plaque
for k, lab in (("oliveL", "㉓ olive h 2 ft"), ("oliveR", "㉔ olive")):
    s.append(poly(O[k], "#cfdcb8", "#5d7a3e", 1.6))
    cxo = sum(q[0] for q in O[k]) / len(O[k]); cyo = sum(q[1] for q in O[k]) / len(O[k])
    s.append(T(*P(cxo, cyo + 0.07), lab, 11, "#3d5a26", "middle"))
s.append(poly(O["plaque"], "#fff", INK, 1.6)); s.append(T(*P(4.2, 15.8), "㉕ plaque", 12, INK, "middle"))
# path of light
pp = " ".join(f"{P(x,y)[0]:.1f},{P(x,y)[1]:.1f}" for x, y in path)
s.append(f'<polyline points="{pp}" fill="none" stroke="#f1d58a" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>')
s.append(f'<polyline points="{pp}" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 7"/>')
s.append(T(*P(2.95, 13.9), "① path of light 0.5 ft", 13, GOLD, "middle", rot=-74, weight="bold"))
# under-deck & hidden
s.append(poly(rect(7.6, 15.2, 1.2, 0.7), "none", PEN, 1.4, "4 4")); s.append(T(*P(8.2, 15.65), "㉗ control", 11, PEN, "middle"))
for (x, y) in ((0.05, 11.3), (8.65, 8.7)):
    s.append(poly(rect(x, y, 0.3, 0.5), "#444", PEN, 1))
s.append(T(*P(0.45, 11.65), "㉘ spkr", 11, PEN))
s.append(f'<path d="M{P(3.6,0.18)[0]} {P(3.6,0.18)[1]}H{P(8.8,0.18)[0]}M{P(8.82,0.2)[0]} {P(8.82,0.2)[1]}V{P(8.82,4.9)[1]}" stroke="#7d3fbf" stroke-width="5" stroke-dasharray="14 6"/>')
s.append(T(*P(8.6, 2.6), "㉙ UV bars (hidden)", 12, "#7d3fbf", "middle", rot=90))
# spot levels
for (x, y, t) in ((0.25, 15.75, "±0.0"), (2.6, 9.9, "+0.8"), (0.35, 6.25, "+1.5"), (2.45, 0.35, "+2.0"),
                  (6.0, 8.5, "+0.3"), (7.2, 4.6, "+3.0 crest"), (6.4, 15.6, "+0.3"), (6.4, 9.75, "+0.8")):
    X, Y = P(x, y)
    s.append(f'<path d="M{X-6} {Y-12}h12l-6 9z" fill="{INK}"/>' + T(X + 9, Y - 2, t, 12, INK, font=SANS))
# open edges skirting
for k in range(0, 1280, 16):
    s.append(f'<path d="M322 {150+k} q-6 8 0 16" fill="none" stroke="{INK}" stroke-width="1.2"/>')
for k in range(0, 720, 16):
    s.append(f'<path d="M{330+k} 1438 q8 6 16 0" fill="none" stroke="{INK}" stroke-width="1.2"/>')
s.append(T(305, 900, "open side · black skirting", 13, PEN, "middle", SANS, rot=-90))
s.append(T(690, 1462, "open front · black skirting", 13, PEN, "middle", SANS))
# overall dims
s.append(f'<path d="M330 1500H1050" stroke="{PEN}" stroke-width="1.4" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(690, 1494, "9 feet", 18, INK, "middle"))
s.append(f'<path d="M262 150V1430" stroke="{PEN}" stroke-width="1.4" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(252, 790, "16 feet", 18, INK, "middle", rot=-90))
# viewer
VX, VY = P(*V)
s.append(f'<circle cx="{VX}" cy="{VY}" r="15" fill="{INK}"/><path d="M{VX-30} {VY+28}q30 -22 60 0" stroke="{INK}" stroke-width="4" fill="none"/>')
s.append(T(VX + 44, VY + 6, "㉚ PUBLIC VIEW SPOT", 16, INK, weight="bold"))
s.append(T(VX + 44, VY + 28, "3 ft left + 3 ft in front of the stage corner", 13, PEN, font=SANS))
s.append(f'<path d="M{P(-1.1,15.4)[0]} {P(-1.1,15.4)[1]} Q{P(-1.3,17.3)[0]} {P(-1.3,17.3)[1]} {P(0.6,17.1)[0]} {P(0.6,17.1)[1]}" stroke="{RED}" stroke-width="3" stroke-dasharray="2 6" fill="none"/>')
s.append(T(120, 1556, "rope barrier", 12, RED, font=SANS))
s.append(f'<path d="M{VX} {VY} L{H1[0]} {H1[1]}" stroke="{RED}" stroke-width="1.6" stroke-dasharray="14 6 3 6"/>')
s.append(T(*P(-0.9, 15.2), "main sightline → path → cave → star", 13, RED, rot=-58.8))
for r, lab in ((11, "A|B"), (15, "B|C"), (18, "C|D")):
    ang = math.radians(-35)
    X, Y = VX + r * PX * math.cos(ang), VY + r * PX * math.sin(ang)
    if 330 < X < 1050 and 150 < Y < 1430:
        s.append(T(X, Y, f"zone {lab}", 12, "#5c6ea8", "middle", SANS))
s.append(T(330, 1560, "Scale zones measured from the view spot: A < 11 ft · B 11–15 ft · C 15–18 ft · D > 18 ft", 14, "#5c6ea8", font=SANS))
s.append(T(330, 1582, "Blue strip on both walls = backdrop: lower 5 ft twilight-hills print, above it blue drape with gold stars up to the ceiling.", 14, BLUE, font=SANS))
s.append(T(330, 1604, f"Cave and house are turned {ANG:.0f}° so their open fronts face the view spot, like the 2023 church at 45°.", 14, INK, font=SANS))

# ---------------- SECTION along main sightline ----------------
SX0, SFL, SS = 1250, 830, 45
dirv = ((H[0] - V[0]), (H[1] - V[1])); dl = math.hypot(*dirv); dirv = (dirv[0] / dl, dirv[1] / dl)
def proj(p): return (p[0] - V[0]) * dirv[0] + (p[1] - V[1]) * dirv[1]
DECK = 2.0
def sx(sv): return SX0 + SS * sv
def sy(hfloor): return SFL - SS * hfloor
s_edge = 3 / 10.8 * dl  # enters stage at x=0
s_wall = proj((9, 0)) + 0.3
s_cave, s_mouth, s_land, s_star = proj(C), proj(mouth), proj(Lnd), proj(H)
s.append(T(1250, 132, "SECTION along the main sightline (view spot → star corner)", 22, INK))
s.append(f'<path d="M{sx(-1)} {SFL}H{sx(s_wall)+30}" stroke="{INK}" stroke-width="3"/>' + T(sx(-0.8), SFL + 22, "church floor", 13, PEN, font=SANS))
s.append(f'<rect x="{sx(s_wall)}" y="{sy(16)}" width="22" height="{SS*16}" fill="url(#hatch)" stroke="{INK}" stroke-width="2"/>')
s.append(f'<path d="M{sx(-1)} {sy(15)}H{sx(s_wall)}" stroke="{PEN}" stroke-dasharray="10 8"/>' + T(sx(-0.8), sy(15) - 8, "ceiling ≈ 15 ft? — measure on site", 14, RED, font=SANS))
# deck
s.append(f'<rect x="{sx(s_edge)}" y="{sy(DECK)}" width="{sx(s_wall)-sx(s_edge)}" height="{SS*DECK}" fill="#3b3b42"/>')
s.append(T(sx(s_edge) + 8, sy(DECK) + 50, "deck 2 ft (confirm) · black skirting", 13, "#f0f0f0", font=SANS))
# terrain
prof = [(s_edge, 0), (s_mouth - 1.5, 0.15), (s_mouth, 0.3), (s_mouth + 2.4, 0.3), (s_mouth + 2.6, 2.8), (s_land, 3.0), (s_wall, 3.0)]
tp = [f"{sx(a):.1f},{sy(DECK+b):.1f}" for a, b in prof]
s.append(f'<polygon points="{sx(s_edge):.1f},{sy(DECK):.1f} {" ".join(tp)} {sx(s_wall):.1f},{sy(DECK):.1f}" fill="url(#rock)" stroke="#8d7a52" stroke-width="2"/>')
# cave arch cut
s.append(f'<path d="M{sx(s_mouth)} {sy(DECK+0.3)} V{sy(DECK+2.5)} Q{sx(s_mouth+1.2)} {sy(DECK+3.0)} {sx(s_mouth+2.5)} {sy(DECK+2.5)} V{sy(DECK+0.3)}Z" fill="#5a4026"/>')
s.append(f'<rect x="{sx(s_cave)-26}" y="{sy(DECK+2.3)}" width="40" height="{SS*2.0}" fill="#f3dfb0" stroke="{GOLD}" stroke-width="2"/>')
s.append(T(sx(s_cave) - 6, sy(DECK + 0.3) + 32, "Holy Family 2 ft", 13, GOLD, "middle", weight="bold"))
s.append(T(sx(s_mouth) - 14, sy(DECK + 3.0), "cave arch 2.5 ft", 13, INK, "end"))
# house
hs0 = s_mouth + 1.9
s.append(f'<rect x="{sx(hs0)}" y="{sy(DECK+4.3)}" width="{SS*2.3}" height="{SS*1.5}" fill="#f7f3ea" stroke="{RED}" stroke-width="2"/>')
s.append(T(sx(hs0) + SS * 2.3 + 10, sy(DECK + 4.3) + 14, "house upper room", 13, RED))
s.append(T(sx(hs0) + SS * 2.3 + 10, sy(DECK + 4.3) + 32, "floor +2.8 → +4.3", 13, RED))
# backdrop
s.append(f'<rect x="{sx(s_wall)-10}" y="{sy(DECK+5)}" width="10" height="{SS*5}" fill="#9a8f78"/>')
s.append(f'<rect x="{sx(s_wall)-10}" y="{sy(15)}" width="10" height="{sy(DECK+5)-sy(15)}" fill="{BLUE}"/>')
s.append(T(sx(s_wall) + 40, sy(DECK + 2.5), "hills print 5 ft", 13, PEN, font=SANS))
s.append(T(sx(s_wall) + 40, sy(11), "blue drape + gold stars", 13, BLUE, font=SANS))
s.append(T(sx(s_wall) + 40, sy(10.5), "fibre stars + UV angels", 13, "#7d3fbf", font=SANS))
# cascade helix
hz = []
for k in range(61):
    t = k / 60
    a = s_star + (s_land - s_star) * t
    hh = 14.0 + (DECK + 4.5 - 14.0) * t
    a += 0.9 * math.sin(t * math.pi * 6)
    hz.append(f"{sx(a):.1f},{sy(hh):.1f}")
s.append(f'<polyline points="{" ".join(hz)}" fill="none" stroke="#9aa6c9" stroke-width="12" opacity=".7" stroke-linecap="round"/>')
s.append(f'<polyline points="{" ".join(hz)}" fill="none" stroke="#3d4f8f" stroke-width="2" stroke-dasharray="6 4"/>')
for k in range(7):
    xx = sx(s_star - 0.9 + k * 0.3)
    s.append(f'<path d="M{xx} {sy(14)} V{sy(14 - 2 - (k % 3))}" stroke="#a7b4d6" stroke-width="1.4"/>')
stx, sty = sx(s_star), sy(14)
star2 = " ".join(f"{stx+math.cos(math.radians(-90+i*36))*(22 if i%2==0 else 9):.1f},{sty+math.sin(math.radians(-90+i*36))*(22 if i%2==0 else 9):.1f}" for i in range(10))
s.append(f'<polygon points="{star2}" fill="#f3c34c" stroke="{GOLD}" stroke-width="1.5"/>')
s.append(T(stx - 30, sty - 6, "⑦ star + bead strands, hung ~1 ft below ceiling", 13, GOLD, "end", weight="bold"))
s.append(T(sx(s_land) - 70, sy(9.5), "⑥ cloud + angel spiral", 14, "#3d4f8f", "end", weight="bold"))
s.append(T(sx(s_land) - 70, sy(9.5) + 18, "≈ 2.5 ft wide, ends 4.5 ft above deck", 13, "#3d4f8f", "end", font=SANS))
# viewer + sightlines
ex, ey = sx(0), sy(5.2)
s.append(f'<circle cx="{ex}" cy="{sy(5.55)}" r="10" fill="{INK}"/><path d="M{ex} {sy(5.3)} V{sy(2.6)} M{ex} {sy(2.6)} L{ex-12} {SFL} M{ex} {sy(2.6)} L{ex+12} {SFL} M{ex-16} {sy(4.4)} H{ex+16}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
s.append(T(ex + 18, sy(6.0), "eye 5.2 ft (floor)", 13, INK, font=SANS))
for (a, h) in ((s_cave, DECK + 1.3), (s_star, 14)):
    s.append(f'<path d="M{ex} {ey} L{sx(a)} {sy(h)}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="14 6 3 6"/>')
# distance ticks
for a, lab in ((0, "0"), (s_edge, f"{s_edge:.1f}"), (s_cave, f"{s_cave:.1f}"), (s_star, f"{s_star:.1f}"), (s_wall, f"{s_wall:.1f} ft")):
    s.append(f'<path d="M{sx(a)} {SFL+4} V{SFL+16}" stroke="{PEN}" stroke-width="1.4"/>' + T(sx(a), SFL + 34, lab, 13, PEN, "middle", SANS))
s.append(T(sx(11), SFL + 58, "distance from view spot along the sightline", 13, PEN, "middle", SANS))

# ---------------- SCHEDULE ----------------
rows = [
 ("1", "Path of light", "0.5 ft wide, ~7.5 ft long", "0 → +0.3", "—", "Addressable LED strip under sand"),
 ("2", "Cave (grotto)", f"4 × 2.5 ft, turned {ANG:.0f}°", "arch 2.5 ft", "—", "Mouth 3 ft wide faces view spot"),
 ("3", "Holy Family + stone manger", "3 × 1.2 ft group", "figures 2 ft", "1:3 (hero)", "Ox and donkey inside the cave"),
 ("4", "House, upper guest room", "4 × 2 ft over cave back", "floor +2.8, room 1.5", "1:6", "Cut open; travellers + lamps"),
 ("5", "Rock hill mass", "around cave & house", "up to +3.0", "—", "Thermocol + plaster + grout"),
 ("6", "Cloud + angel spiral", "≈ 2.5 ft wide helix", "ceiling → +4.5", "angels 4–6 in", "Flame-retardant fibre, LED only"),
 ("7", "Star + bead strands", "star 2 ft dia", "~1 ft below ceiling", "—", "Hang from corner; confirm height"),
 ("8", "Shepherds, sheep, campfire", "1.7 × 2.6 ft", "+0.8", "1:6 (1.2 ft)", "Real wool sheep"),
 ("9", "Floating angel unit", "2.4 × 1.4 ft", "acrylic 2.4 × 2 ft at 45°", "—", "Pepper's ghost, screen hidden"),
 ("10", "Rock ridge + mist tray", "2.4 × 1.0 ft", "ridge 0.8 ft", "—", "Hides screen; ultrasonic mister"),
 ("11", "Sheepfold", "2 × 1.3 ft", "walls 0.25 ft", "1:12", "Dry-stone pebbles"),
 ("12", "Terraces", "3.4 × 7 ft zone", "+0.8 → +2.0", "—", "4 steps, real soil + grass"),
 ("13", "Watchtower", "1 ft dia", "1.5 ft on +2.0", "1:12", "Round stone"),
 ("14", "Far village", "3.8 × 0.8 ft, right-wall crest", "houses 3–5 in", "1:24", "Pale, cool; clear of cave house"),
 ("15", "Magi caravan", "3 × 0.3 ft wall shelf", "shelf +3.6, figs 2.5 in", "1:24", "Above far village; tiny lamps"),
 ("16–18", "Village houses A, B, C", "1.4–1.6 × 1.6–1.8 ft", "2.0 / 2.5 / 1.8 ft", "1:6", "Against right wall; lit windows"),
 ("19", "Cobbled street", "1.1 × 6.7 ft", "+0.3 → +0.8", "—", "Rises toward the back"),
 ("20", "Well", "0.9 ft dia", "0.6 ft", "1:6", "Real water"),
 ("21", "Census table, soldier, scribe", "1.4 × 1.0 ft", "figures 1.2 ft", "1:6", "Scrolls with names"),
 ("22", "Donkeys + travellers", "1.2 × 0.6 ft", "0.6 ft", "1:6", "Near the cave steps"),
 ("23–24", "Olive trees", "1.2 / 1.0 ft canopy", "2.0 / 1.6 ft", "—", "Wire + bark + real leaves"),
 ("25", '"Find 12 details" plaque', "2 × 0.4 ft", "0.8 ft", "—", "At the front edge"),
 ("26", "Backdrop (both walls)", "9 ft + 16 ft, curved corner", "print 5 ft, drape to ceiling", "—", "Hills print + blue drape + gold stars"),
 ("27–29", "Control box, speakers, UV bars", "under deck / hidden", "—", "—", "ESP32, DFPlayer, 395 nm UV"),
 ("30", "Public view spot + rope", "3 ft + 3 ft from corner", "eye 5.2 ft (floor)", "—", "All scale zones measured from here"),
]
TX, TY, RH = 1250, 920, 25
cols = [(0, "#"), (62, "Item"), (390, "Footprint"), (650, "Height"), (870, "Scale"), (1010, "Notes")]
s.append(T(TX, TY - 18, "SCHEDULE OF ITEMS", 22, INK))
s.append(f'<rect x="{TX-8}" y="{TY}" width="1412" height="{RH*(len(rows)+1)+8}" fill="#fff" stroke="{INK}" stroke-width="1.6"/>')
for cx_, h in cols:
    s.append(T(TX + cx_, TY + 20, h, 14, INK, font=SANS, weight="bold"))
s.append(f'<path d="M{TX-8} {TY+28}H{TX+1404}" stroke="{INK}"/>')
for i, r in enumerate(rows):
    y = TY + 28 + RH * (i + 1) - 7
    if i % 2 == 0:
        s.append(f'<rect x="{TX-7}" y="{y-17}" width="1410" height="{RH}" fill="#f3f1ea"/>')
    for (cx_, _), val in zip(cols, r):
        s.append(T(TX + cx_, y, val.replace("&", "&amp;"), 13.5, INK, font=SANS, weight="bold" if cx_ == 0 else "normal"))
# title block
by = TY + RH * (len(rows) + 1) + 30
s.append(f'<rect x="{TX-8}" y="{by}" width="1412" height="{Ht-40-by}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
s.append(T(TX + 10, by + 34, "CRIB 2026 · THAT NIGHT IN BETHLEHEM", 22, INK))
s.append(T(TX + 10, by + 62, "Assumed as in the 2023 layout: back wall 9 ft, right wall 16 ft, people view from the front-left corner. Check on site before cutting: deck height, ceiling height, star hook.", 13.5, PEN, font=SANS))
s.append(T(TX + 1394, by + 34, "Master sheet · 16 Nov 2026", 14, PEN, "end", SANS))

# ---------------- church key plan inset (right column)
KX, KY = 2740, 150
s.append(T(KX, KY - 22, "CRIB POSITION IN THE CHURCH", 20, INK))
s.append(f'<rect x="{KX-6}" y="{KY-6}" width="472" height="332" fill="#fff" stroke="{INK}" stroke-width="1.6"/>')
s.append(church_crop(KX, KY, 460, 320, "150 30 460 320"))
notes = ["Assumed from your description (please correct me if wrong):",
         "1. The altar is at the centre of the church's front wall.",
         "2. The crib stage is in the right-hand corner, at the end of",
         "    that wall: 9 ft along the altar wall, 16 ft along the right wall.",
         "3. The public walks up the right side and stands at VIEW 1",
         "    (front-left corner of the stage). The altar is then behind",
         "    their left shoulder and out of frame.",
         "4. A wide shot from the centre aisle (VIEW 2) shows the altar",
         "    centre-left and the crib at the far right end.",
         "Block-out views from both spots: see the build pack, sheet 3"]
for i, n_ in enumerate(notes):
    s.append(T(KX, KY + 366 + i * 24, n_, 14.5, INK if i else RED, font=SANS, weight="bold" if i == 0 else "normal"))
s.append('</svg>')
html = '<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#fff}svg{display:block}</style></head><body>' + "".join(s) + '</body></html>'
open(OUT, "w", encoding="utf-8").write(html)
print("ok")
