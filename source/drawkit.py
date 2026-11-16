import math
INK, PEN, GOLD, BLUE, RED, GREEN, VIOLET = "#2b2a33", "#4a4a55", "#b07a12", "#2f5aa8", "#a8322c", "#4f7a3a", "#7d3fbf"
SANS = "'Segoe UI',Arial,sans-serif"
HAND = "'Segoe Print','Kalam','Comic Sans MS',cursive"
ROCK, ROCKD, CREAM = "#e8dcc0", "#cdbb92", "#f6f1e3"


class D:
    def __init__(s, w=900, h=460, sc=30, ox=40, oy=40, title=""):
        s.w, s.h, s.sc, s.ox, s.oy = w, h, sc, ox, oy
        s.o = [f'<rect width="{w}" height="{h}" fill="#fffef9" stroke="{INK}" stroke-width="1.5"/>']
        if title:
            s.o.append(f'<text x="14" y="24" font-family="{SANS}" font-size="15" font-weight="bold" fill="{INK}">{title}</text>')

    def X(s, x): return s.ox + s.sc * x
    def Y(s, y): return s.oy + s.sc * y

    def rect(s, x, y, w, h, fill="#fff", stroke=PEN, sw=1.4, dash=None, op=1, rx=0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.o.append(f'<rect x="{s.X(x):.1f}" y="{s.Y(y):.1f}" width="{s.sc*w:.1f}" height="{s.sc*h:.1f}" rx="{rx}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def poly(s, pts, fill="#fff", stroke=PEN, sw=1.4, dash=None, op=1, close=True):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        tag = "polygon" if close else "polyline"
        s.o.append(f'<{tag} points="{" ".join("%.1f,%.1f" % (s.X(x), s.Y(y)) for x, y in pts)}" fill="{fill if close else "none"}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linejoin="round"/>')

    def line(s, x1, y1, x2, y2, stroke=PEN, sw=1.4, dash=None, arrow=False):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#ar)"' if arrow else ""
        s.o.append(f'<line x1="{s.X(x1):.1f}" y1="{s.Y(y1):.1f}" x2="{s.X(x2):.1f}" y2="{s.Y(y2):.1f}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>')

    def circ(s, x, y, r, fill="#fff", stroke=PEN, sw=1.4, op=1):
        s.o.append(f'<circle cx="{s.X(x):.1f}" cy="{s.Y(y):.1f}" r="{s.sc*r:.1f}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>')

    def txt(s, x, y, t, size=13, fill=INK, anchor="start", weight="normal", rot=None, font=SANS):
        s.ptxt(s.X(x), s.Y(y), t, size, fill, anchor, weight, rot, font)

    def ptxt(s, px, py, t, size=13, fill=INK, anchor="start", weight="normal", rot=None, font=SANS):
        tr = f' transform="rotate({rot} {px:.1f} {py:.1f})"' if rot is not None else ""
        t = t.replace("&", "&amp;")
        halo = '' if fill.lower() in ("#fff", "#eee", "#f0f0f0", "#e7d5ff", "#ffffff") else ' stroke="#fffef9" stroke-width="3.5" paint-order="stroke"'
        s.o.append(f'<text x="{px:.1f}" y="{py:.1f}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{halo}{tr}>{t}</text>')

    def dh(s, x1, x2, y, label, gap=24, size=13):
        py = s.Y(y) + gap
        a, b = s.X(x1), s.X(x2)
        s.o.append(f'<line x1="{a:.1f}" y1="{s.Y(y):.1f}" x2="{a:.1f}" y2="{py+6:.1f}" stroke="{PEN}" stroke-width=".8"/><line x1="{b:.1f}" y1="{s.Y(y):.1f}" x2="{b:.1f}" y2="{py+6:.1f}" stroke="{PEN}" stroke-width=".8"/>')
        s.o.append(f'<line x1="{a:.1f}" y1="{py:.1f}" x2="{b:.1f}" y2="{py:.1f}" stroke="{PEN}" stroke-width="1.2" marker-start="url(#ar)" marker-end="url(#ar)"/>')
        s.ptxt((a + b) / 2, py - 5, label, size, INK, "middle")

    def dv(s, y1, y2, x, label, gap=-24, size=13):
        px = s.X(x) + gap
        a, b = s.Y(y1), s.Y(y2)
        s.o.append(f'<line x1="{s.X(x):.1f}" y1="{a:.1f}" x2="{px-6 if gap<0 else px+6:.1f}" y2="{a:.1f}" stroke="{PEN}" stroke-width=".8"/><line x1="{s.X(x):.1f}" y1="{b:.1f}" x2="{px-6 if gap<0 else px+6:.1f}" y2="{b:.1f}" stroke="{PEN}" stroke-width=".8"/>')
        s.o.append(f'<line x1="{px:.1f}" y1="{a:.1f}" x2="{px:.1f}" y2="{b:.1f}" stroke="{PEN}" stroke-width="1.2" marker-start="url(#ar)" marker-end="url(#ar)"/>')
        s.ptxt(px - 6 if gap < 0 else px + 6, (a + b) / 2 + 4, label, size, INK, "end" if gap < 0 else "start", rot=None)

    def svg(s):
        defs = (f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{PEN}"/></marker>'
                '<pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="#e9e6dc"/><path d="M0 0V9" stroke="#6a6a72" stroke-width="2"/></pattern>'
                '<pattern id="rockp" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#efe6d2"/><circle cx="3" cy="4" r="1.1" fill="#c9b892"/><circle cx="9" cy="9" r="1" fill="#c9b892"/></pattern>'
                '<pattern id="eps" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#f4f6f8"/><circle cx="4" cy="4" r="2.2" fill="none" stroke="#b9c2cc" stroke-width=".8"/></pattern>'
                '<pattern id="ply" width="14" height="6" patternUnits="userSpaceOnUse"><rect width="14" height="6" fill="#e3c590"/><path d="M0 3H14" stroke="#b58f55" stroke-width="1"/></pattern></defs>')
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.w}" height="{s.h}" viewBox="0 0 {s.w} {s.h}">{defs}{"".join(s.o)}</svg>'


def inpoly(x, y, poly):
    c = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c
