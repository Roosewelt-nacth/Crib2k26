import math
# Church key plan in a 640 x 820 design space (church size is a guess; the stage is drawn to scale: 8 px = 1 ft)
INK, PEN, GOLD, BLUE, RED = "#2b2a33", "#4a4a55", "#b07a12", "#2f5aa8", "#a8322c"
SANS = "'Segoe UI',Arial,sans-serif"
S = 8.0
CX0, CX1, CY0, CY1 = 40, 600, 40, 790   # church inner walls
SW, SD = 9 * S, 16 * S                  # stage 9 ft along the altar wall, 16 ft along the right wall
SX0, SY0 = CX1 - SW, CY0                # stage top-left


def t(x, y, s, size=14, fill=INK, anchor="start", weight="normal", rot=None):
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" stroke="#fbfaf6" stroke-width="4" paint-order="stroke"{tr}>{s}</text>'


def church_inner(extra=True):
    o = []
    o.append(f'<rect x="{CX0}" y="{CY0}" width="{CX1-CX0}" height="{CY1-CY0}" fill="#fbfaf6" stroke="{INK}" stroke-width="10"/>')
    # sanctuary step
    o.append(f'<rect x="{CX0+5}" y="{CY0+5}" width="{CX1-CX0-10}" height="170" fill="#efe9da"/>')
    o.append(f'<path d="M{CX0+5} {CY0+175}H{CX1-5}" stroke="{PEN}" stroke-width="2" stroke-dasharray="8 5"/>')
    o.append(t(CX0 + 16, CY0 + 192, "sanctuary step", 12, PEN))
    # altar (centre of the church)
    ax = (CX0 + CX1) / 2
    o.append(f'<rect x="{ax-45}" y="{CY0+30}" width="90" height="46" fill="#fff" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<rect x="{ax-45}" y="{CY0+30}" width="90" height="12" fill="#d9c27a" stroke="{INK}" stroke-width="1.5"/>')
    o.append(t(ax, CY0 + 64, "ALTAR", 15, INK, "middle", "bold"))
    o.append(t(ax, CY0 + 16, "ALTAR WALL (front of church)", 12, PEN, "middle", "bold"))
    # pews + aisle
    for side in (0, 1):
        x0 = CX0 + 30 if side == 0 else ax + 34
        wdt = ax - 34 - (CX0 + 30) if side == 0 else CX1 - 40 - (ax + 34)
        for k in range(11):
            y = CY0 + 250 + k * 40
            o.append(f'<rect x="{x0}" y="{y}" width="{wdt}" height="16" rx="3" fill="#e6dcc6" stroke="{PEN}" stroke-width="1"/>')
    o.append(t(ax, CY0 + 420, "centre aisle", 13, PEN, "middle", rot=-90))
    o.append(t(CX0 + 110, CY0 + 235, "pews (congregation faces the altar)", 12, PEN, "middle"))
    o.append(f'<path d="M{ax-60} {CY1-6}H{ax+60}" stroke="{INK}" stroke-width="12"/>' + t(ax, CY1 - 14, "main door", 12, PEN, "middle"))
    # stage (right corner, at the end of the altar wall)
    o.append(f'<rect x="{SX0}" y="{SY0}" width="{SW}" height="{SD}" fill="#f3dfb0" stroke="{GOLD}" stroke-width="3"/>')
    o.append(t(SX0 + SW / 2, SY0 + SD / 2 - 6, "CRIB", 17, INK, "middle", "bold"))
    o.append(t(SX0 + SW / 2, SY0 + SD / 2 + 14, "STAGE", 13, INK, "middle"))
    o.append(t(SX0 + SW / 2, SY0 + SD / 2 + 32, "9 × 16 ft", 12, INK, "middle"))
    # viewer spot: 3 ft left + 3 ft in front of the stage front-left corner
    vx, vy = SX0 - 3 * S, SY0 + SD + 3 * S
    # cone toward cave direction (stage plan bearing 33 deg from the "toward altar wall" axis, rotated toward the right)
    hdg = math.radians(33)
    fx, fy = math.sin(hdg), -math.cos(hdg)
    half = math.radians(48)
    Lc = 300
    a1 = (vx + Lc * math.sin(hdg - half), vy - Lc * math.cos(hdg - half))
    a2 = (vx + Lc * math.sin(hdg + half), vy - Lc * math.cos(hdg + half))
    o.append(f'<path d="M{vx} {vy} L{a1[0]:.1f} {a1[1]:.1f} L{a2[0]:.1f} {a2[1]:.1f} Z" fill="{RED}" fill-opacity=".10" stroke="{RED}" stroke-width="1.5" stroke-dasharray="7 5" clip-path="url(#chclip)"/>')
    o.append(f'<circle cx="{vx}" cy="{vy}" r="9" fill="{INK}"/>')
    o.append(t(vx - 16, vy - 8, "VIEW 1 · public spot", 13, RED, "end", "bold"))
    o.append(t(vx - 16, vy + 8, "3 ft left + 3 ft in front", 11, PEN, "end"))
    # visitor queue arrows
    o.append(f'<path d="M{vx-120} {vy+120} Q{vx-60} {vy+70} {vx-18} {vy+22}" stroke="{PEN}" stroke-width="2.5" fill="none" stroke-dasharray="3 6" marker-end="url(#arch)"/>')
    o.append(t(vx - 130, vy + 142, "queue comes up the right-hand side", 11, PEN, "end"))
    # view 2 : from the centre aisle (wide shot)
    wx, wy = ax, 600
    tx, ty = SX0 + SW / 2, SY0 + SD / 2
    ang = math.atan2(tx - wx, -(ty - wy))
    half2 = math.radians(32)
    L2 = 520
    b1 = (wx + L2 * math.sin(ang - half2), wy - L2 * math.cos(ang - half2))
    b2 = (wx + L2 * math.sin(ang + half2), wy - L2 * math.cos(ang + half2))
    o.append(f'<path d="M{wx} {wy} L{b1[0]:.1f} {b1[1]:.1f} L{b2[0]:.1f} {b2[1]:.1f} Z" fill="{BLUE}" fill-opacity=".07" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="3 6" clip-path="url(#chclip)"/>')
    o.append(f'<circle cx="{wx}" cy="{wy}" r="9" fill="{BLUE}"/>')
    o.append(t(wx + 14, wy + 5, "VIEW 2 · from the aisle", 13, BLUE, "start", "bold"))
    o.append(t(wx + 14, wy + 21, "altar centre-left, crib at the right end", 11, PEN, "start"))
    o.append(t(CX0 + 20, CY1 - 40, "Key plan · church size is a guess; only the stage is to scale", 11, PEN))
    return "".join(o)


def church_svg(width, height, title=True, extra_notes=True):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 640 {height*640/width:.0f}">']
    s.append('<defs><clipPath id="chclip"><rect x="40" y="40" width="560" height="750"/></clipPath>'
             f'<marker id="arch" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{PEN}"/></marker></defs>')
    s.append(f'<rect width="640" height="{height*640/width:.0f}" fill="#fbfaf6"/>')
    s.append(church_inner())
    s.append("</svg>")
    return "".join(s)


if __name__ == "__main__":
    import sys
    html = '<!doctype html><html><body style="margin:0;background:#fbfaf6">' + church_svg(1000, 1280) + '</body></html>'
    open(sys.argv[1], "w", encoding="utf-8").write(html)


def church_crop(x, y, w, h, vb):
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vb}">'
            '<defs><clipPath id="chclip"><rect x="40" y="40" width="560" height="750"/></clipPath>'
            f'<marker id="arch" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{PEN}"/></marker></defs>'
            + church_inner() + '</svg>')
