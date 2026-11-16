import math, sys
src = open('blueprint.py', encoding='utf-8').read().split("# ---------------- svg")[0].replace("OUT = sys.argv[1]", "")
exec(src)
LABELS = len(sys.argv) > 2 and sys.argv[2] == "lab"
W, IH = 1920, 1080
YAW = math.radians(float(sys.argv[3]) if len(sys.argv) > 3 else 33)
HFOV = math.radians(float(sys.argv[4]) if len(sys.argv) > 4 else 96)
EYE = 5.2; DECK = 2.0
CAMXY = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else V
CAM = (CAMXY[0], CAMXY[1], EYE)
WIDE = CAMXY[1] > 25
F = W / 2 / math.tan(HFOV / 2)
fx, fy = math.sin(YAW), -math.cos(YAW)      # forward (plan): +x right, -y toward back wall
rx, ry = math.cos(YAW), math.sin(YAW)       # right


def proj(x, y, z):
    dx, dy, dz = x - CAM[0], y - CAM[1], z - CAM[2]
    fw = dx * fx + dy * fy
    rt = dx * rx + dy * ry
    if fw < 0.3:
        fw = 0.3
    return (W / 2 + F * rt / fw, IH / 2 - F * dz / fw + 40, fw)


def shade(base, k):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(c * k))) for c in base)


faces = []   # (depth, svg)


def add(poly3, color, k=1.0, stroke="#00000022", sw=1, op=1):
    pp = [proj(*p) for p in poly3]
    depth = max(p[2] for p in pp)
    faces.append((depth, '<polygon points="%s" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="%s"/>' % (
        " ".join("%.1f,%.1f" % (a, b) for a, b, _ in pp), shade(color, k), op, stroke, sw)))


def lab(X, Y, t):
    faces.append((0.01, '<text x="%.0f" y="%.0f" font-size="26" font-family="Arial" font-weight="bold" fill="#c00" text-anchor="middle" stroke="#fff" stroke-width="5" paint-order="stroke">%s</text>' % (X, Y, t)))


def prism(poly, z0, z1, color, label=None):
    n = len(poly)
    cx = sum(p[0] for p in poly) / n
    cy = sum(p[1] for p in poly) / n
    sides = []
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        nxv, nyv = (b[1] - a[1]), -(b[0] - a[0])
        if (mx - cx) * nxv + (my - cy) * nyv < 0:
            nxv, nyv = -nxv, -nyv
        if (CAM[0] - mx) * nxv + (CAM[1] - my) * nyv <= 0:
            continue
        l = math.hypot(nxv, nyv) or 1
        k = 0.62 + 0.38 * max(0, (nxv * -0.5 + nyv * 0.8) / l)
        d = math.hypot(mx - CAM[0], my - CAM[1])
        sides.append((d, [(a[0], a[1], z0), (b[0], b[1], z0), (b[0], b[1], z1), (a[0], a[1], z1)], k))
    for d, f, k in sorted(sides, key=lambda s: -s[0]):
        add(f, color, k)
    add([(x, y, z1) for x, y in poly], color, 1.08)
    if LABELS and label:
        X, Y, _ = proj(cx, cy, z1)
        lab(X, Y, label)


def shrink(poly, k):
    n = len(poly)
    cx = sum(p[0] for p in poly) / n
    cy = sum(p[1] for p in poly) / n
    return [(cx + (x - cx) * k, cy + (y - cy) * k) for x, y in poly]


SAND, STONE, WHITE, GREEN = (214, 196, 160), (190, 178, 150), (238, 234, 224), (150, 175, 120)


def wall(p0, p1, z0, z1, color, op=1):
    add([(p0[0], p0[1], z0), (p1[0], p1[1], z0), (p1[0], p1[1], z1), (p0[0], p0[1], z1)], color, 1.0, "#00000010", 1, op)


def Z(h):
    return DECK + h


wall((-70, 0), (9, 0), 0, 15, (222, 218, 208))
wall((9, 0), (9, 17), 0, 15, (214, 210, 200))
wall((-1, 0), (9, 0), Z(0), Z(5), (205, 180, 130))
wall((9, 0), (9, 16), Z(0), Z(5), (205, 180, 130))
wall((-1, 0), (9, 0), Z(5), 15, (45, 70, 130))
wall((9, 0), (9, 16), Z(5), 15, (36, 60, 118))
add([(-70, 0, 0), (9, 0, 0), (9, 80, 0), (-70, 80, 0)], (205, 195, 180), 1.0, "none")
add([(0, 0, DECK), (9, 0, DECK), (9, 16, DECK), (0, 16, DECK)], (92, 86, 80), 1.0, "none")
add([(0, 16, 0), (0, 16, DECK), (9, 16, DECK), (9, 16, 0)], (20, 20, 24), 1.0, "none")
add([(0, 0, 0), (0, 0, DECK), (0, 16, DECK), (0, 16, 0)], (14, 14, 18), 1.0, "none")
for i, (y0, y1, h) in enumerate(((5.25, 7.0, 0.8), (3.5, 5.25, 1.2), (1.75, 3.5, 1.6), (0.0, 1.75, 2.0))):
    prism(rect(0, y0, 3.4, y1 - y0), DECK, Z(h), GREEN, "12" if i == 0 else None)
prism(O["street"], DECK, Z(0.55), (170, 165, 155), "19")
hillp = [(3.0, 2.2), (6.0, 1.8), (9.0, 1.7), (9.0, 9.0), (7.1, 9.1), (6.2, 8.9), (5.6, 9.9), (3.4, 9.6), (2.0, 7.6), (2.6, 5.0)]
prism(hillp, DECK, Z(1.2), STONE, "5")
prism(shrink(hillp, 0.82), Z(1.2), Z(2.1), STONE)
prism(shrink(hillp, 0.62), Z(2.1), Z(3.0), STONE)
prism(cave, DECK, Z(2.5), (150, 130, 100), "2")
prism(holy, Z(0.3), Z(2.3), (235, 210, 150), "3")
prism(house, Z(2.8), Z(4.3), WHITE, "4")
prism(O["shep"], DECK, Z(0.8), SAND)
prism(rect(0.3, 7.2, 1.5, 2.2), Z(0.8), Z(1.2), (240, 230, 200), "8")
prism(O["ridge"], Z(1.0), Z(1.8), STONE, "10")
prism(rect(0.5, 3.6, 2.0, 0.15), Z(1.4), Z(3.4), (120, 160, 255), "9")
prism(O["fold"], Z(2.0), Z(2.25), (200, 190, 165), "11")
prism(O["tower"], Z(2.0), Z(3.5), (200, 190, 165), "13")
prism(O["farvil"], Z(3.0), Z(3.4), (240, 236, 226), "14")
prism(O["magi"], Z(3.6), Z(3.85), (230, 180, 70), "15")
for k, lb, h in (("hA", "16", 2.0), ("hB", "17", 2.5), ("hC", "18", 1.8)):
    prism(O[k], Z(0.55), Z(0.55 + h), WHITE, lb)
prism(O["well"], DECK, Z(0.6), (190, 205, 225), "20")
prism(O["census"], DECK, Z(1.2), (220, 180, 160), "21")
prism(O["donk"], DECK, Z(0.6), (170, 150, 130), "22")
prism(O["oliveL"], DECK, Z(2.0), (110, 150, 90), "23")
prism(O["oliveR"], DECK, Z(1.6), (110, 150, 90), "24")
prism(O["plaque"], DECK, Z(0.8), (255, 255, 255), "25")
if WIDE:
    wall((9, 0), (9, 80), 0, 15, (214, 210, 200))
    prism(rect(-29, 3.5, 6, 2.5), 0, 3.2, (235, 235, 240), "ALTAR")
    for r in range(7):
        for (xa, xb) in ((-52, -29.5), (-22.5, -4)):
            prism(rect(xa, 18 + r * 3.2, xb - xa, 1.2), 0, 2.8, (150, 115, 80))
pp3 = [proj(x, y, Z(0.03)) for x, y in path]
faces.append((0.05, '<polyline points="%s" fill="none" stroke="#ffd36a" stroke-width="10" stroke-linecap="round"/>' % " ".join("%.1f,%.1f" % (a, b) for a, b, _ in pp3)))
for t in [k / 40 for k in range(41)]:
    x = H[0] + (Lnd[0] - H[0]) * t
    y = H[1] + (Lnd[1] - H[1]) * t
    z = 14.0 + (DECK + 4.5 - 14.0) * t
    a = 0.9 * math.sin(t * math.pi * 6)
    X, Y, d = proj(x + a * 0.86, y + a * 0.5, z)
    faces.append((0.02, '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" fill-opacity=".8"/>' % (X, Y, 120 / d + 4)))
sx_, sy_, sd = proj(H[0], H[1], 14.0)
faces.append((0.02, '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffd45a"/>' % (sx_, sy_, 260 / sd)))
if LABELS:
    lab(sx_, sy_ - 40, "6/7")
body = "".join(f for d, f in sorted(faces, key=lambda f: -f[0]))
svg = '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"><rect width="%d" height="%d" fill="#e9e4da"/>%s</svg>' % (W, IH, W, IH, body)
open(sys.argv[1], "w", encoding="utf-8").write('<!doctype html><html><body style="margin:0">' + svg + '</body></html>')
for nm, p in (("cave", C), ("house", off(C, 1.5)), ("farvil", (8.2, 7.1)), ("magi", (8.85, 6.9)), ("tower", (3.0, 1.0)),
              ("street", (6.75, 12)), ("path start", path[0]), ("far corner", (9, 0)), ("stage FL", (0, 16))):
    dx, dy = p[0] - V[0], p[1] - V[1]
    print(nm, "bearing %.1f" % math.degrees(math.atan2(dx, -dy)), "dist %.1f" % math.hypot(dx, dy))
