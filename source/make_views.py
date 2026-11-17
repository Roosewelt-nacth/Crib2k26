"""Front / side / top orthographic views of the 2026 crib from the blueprint coordinates.
Outputs (2026/share/): final-blueprint-3-views.png, block-views/<letter>-views.png
Run: python source/make_views.py   (needs Chrome or Edge for the PNG render)
Feet. x: 0 (open left edge) -> 9 (right wall). y: 0 (back wall) -> 16 (open front). z: 0 = deck top (deck is 2 ft above the church floor).
Heights are the pack's figures; the rake and terraces are the leg heights from sheet 0. Ceiling assumed 15 ft above the floor (+13 above deck).
"""
import math, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '2026', 'share'); BV = os.path.join(OUT, 'block-views'); os.makedirs(BV, exist_ok=True)
COL = {'A': (120,120,120), 'B': (230,120,20), 'C': (200,50,50), 'E': (40,150,70), 'F': (120,60,200),
       'G': (30,110,220), 'H': (210,170,0), 'I': (0,170,190), 'J': (60,60,160), 'K': (230,60,160), 'L': (110,200,60)}
NAMES = {'A':'Stage frame and rake','B':'Cave, rock hill and Holy Family','C':'House with upper room','E':"Shepherds' field",'F':'Floating angel unit','G':'Village street','H':'Lights and control','I':'Sky: cloud spiral and star','J':'Backdrop','K':'Far village and Magi shelf','L':'Foreground and view spot'}
CEIL = 13.0; EYE = 3.2
V = (-3.0, 19.0); HANG = (7.8, 1.2); C = (4.4, 7.4)
d = (V[0]-C[0], V[1]-C[1]); L_ = math.hypot(*d); v = (d[0]/L_, d[1]/L_); u = (-v[1], v[0])
if u[0] < 0: u = (-u[0], -u[1])
def rrect(c, hw, hd): return [(c[0]+sx*hw*u[0]+sy*hd*v[0], c[1]+sx*hw*u[1]+sy*hd*v[1]) for sx, sy in ((-1,1),(1,1),(1,-1),(-1,-1))]
def off(c, k): return (c[0]-k*v[0], c[1]-k*v[1])
def rect(x, y, w, h): return [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
def circ(cx, cy, r, n=20): return [(cx+r*math.cos(2*math.pi*k/n), cy+r*math.sin(2*math.pi*k/n)) for k in range(n)]
LND = off(C, 3.0); MOUTH = off(C, -1.25)

E = []  # (block, name, kind, poly, z0, z1, extra)
def add(b, name, kind, poly, z0, z1, **kw): E.append(dict(b=b, name=name, kind=kind, poly=poly, z0=z0, z1=z1, **kw))

add('A', 'deck + skirting', 'box', rect(0,0,9,16), -2.0, 0.0, dark=True)
hill = [(3.0,2.2),(6.0,1.8),(9.0,1.7),(9.0,9.0),(7.1,9.1),(6.2,8.9),(5.6,9.9),(3.4,9.6),(2.0,7.6),(2.6,5.0)]
add('B', 'rock hill', 'box', hill, 0.0, 3.0)
for y0, y1, lv in ((0,1.75,2.0),(1.75,3.5,1.6),(3.5,5.25,1.2),(5.25,7.0,0.8)):
    add('E', f'terrace +{lv}', 'box', rect(0,y0,3.4,y1-y0), 0.0, lv)
add('E', 'shepherd ledge', 'box', rect(0.2,7.0,1.7,2.6), 0.0, 0.8)
add('E', 'sheepfold', 'box', rect(0.4,1.75,2.0,1.3), 1.6, 1.85)
add('E', 'watchtower', 'box', circ(3.0,1.0,0.5), 2.0, 3.5)
for (x, y) in ((0.5,7.5),(1.3,8.0)): add('E', 'shepherd', 'box', rect(x,y,0.3,0.3), 0.8, 2.0)
for (x, y) in ((0.6,8.7),(1.4,9.0),(0.9,9.2),(0.3,8.3),(1.6,8.2),(0.4,9.25)): add('E', 'sheep', 'box', rect(x,y,0.35,0.3), 0.8, 1.25)
add('E', 'campfire', 'box', circ(1.0,8.3,0.15,8), 0.8, 1.1, gold=True)
add('F', 'ridge', 'box', rect(0.3,4.6,2.4,1.0), 1.2, 2.0)
add('F', 'angel unit (acrylic at 45 deg)', 'box', rect(0.3,3.2,2.4,1.4), 1.2, 2.6, glass=True)
add('B', 'cave', 'cave', rrect(C, 2.0, 1.25), 0.5, 3.0)
add('B', 'Holy Family', 'box', rrect(off(C,-0.15), 1.5, 0.6), 0.5, 2.5, small=True)
add('C', 'guest room', 'box', rrect(off(C,1.5), 2.0, 1.0), 2.8, 4.3, glass=True)
add('G', 'street', 'box', rect(6.2,9.3,1.1,6.7), 0.0, 0.5)
add('G', 'house A', 'box', rect(7.6,9.4,1.4,1.6), 0.7, 2.7)
add('G', 'house B', 'box', rect(7.4,11.3,1.6,1.8), 0.6, 3.1)
add('G', 'house C', 'box', rect(7.6,13.4,1.4,1.6), 0.4, 2.2)
add('G', 'well', 'box', circ(5.6,11.2,0.45), 0.0, 0.6)
add('G', 'census table + soldier', 'box', rect(4.5,12.8,1.4,1.0), 0.0, 1.9)
add('G', 'donkeys', 'box', rect(4.6,10.0,1.2,0.6), 0.0, 1.1)
add('K', 'far village', 'box', rect(7.8,5.2,0.8,3.8), 3.0, 3.35)
add('K', 'Magi shelf + caravan', 'box', rect(8.7,5.4,0.3,3.0), 3.6, 3.95)
add('H', 'path of light', 'flat', [(1.75,15.9),(2.05,15.9),(2.55,13.6),(3.25,11.2),(3.8,9.25),(MOUTH[0]+0.25,MOUTH[1]),(MOUTH[0]-0.25,MOUTH[1]),(3.3,9.25),(2.75,11.2),(2.05,13.6)], 0.0, 0.03, gold=True)
add('H', 'speaker', 'box', rect(0.0,11.3,0.3,0.4), 0.0, 0.5)
add('H', 'control box (under deck)', 'box', rect(7.6,15.2,1.2,0.8), -1.5, -0.1, hidden=True)
add('H', 'UV bar (back wall)', 'box', rect(1.0,0.0,3.3,0.12), 4.8, 5.0)
add('H', 'UV bar (right wall)', 'box', rect(8.88,6.0,0.12,3.3), 4.8, 5.0)
add('I', 'star burst', 'star', circ(HANG[0],HANG[1],1.0), 10.5, 12.5)
add('I', 'bead strands', 'strands', circ(HANG[0],HANG[1],0.9), 4.5, 10.5)
add('I', 'cloud and angel spiral', 'spiral', [HANG, LND], 4.5, 10.5)
add('J', 'back-wall print', 'box', rect(0,-0.12,9,0.12), 0.0, 5.0)
add('J', 'back-wall drape', 'box', rect(0,-0.12,9,0.12), 5.0, CEIL, drape=True)
add('J', 'right-wall print', 'box', rect(9.0,0,0.12,16), 0.0, 5.0)
add('J', 'right-wall drape', 'box', rect(9.0,0,0.12,16), 5.0, CEIL, drape=True)
add('L', 'olive tree (front left)', 'tree', circ(1.0,14.2,0.6), 0.0, 2.0)
add('L', 'olive tree (front right)', 'tree', circ(5.4,14.9,0.5), 0.0, 1.6)
add('L', 'plaque', 'box', rect(3.2,15.5,2.0,0.4), 0.0, 0.8)

def light(c, k=0.55): return '#%02x%02x%02x' % tuple(int(255-(255-x)*k) for x in c)
def dark(c): return '#%02x%02x%02x' % tuple(int(x*0.55) for x in c)
def bounds(poly, i): return min(p[i] for p in poly), max(p[i] for p in poly)

class View:
    def __init__(s, kind, S, x0, y0, ext):  # ext = (hmin,hmax,vmin,vmax) in feet of this view's own axes
        s.kind, s.S, s.ox, s.oy, s.ext = kind, S, x0, y0, ext
    def X(s, h): return s.ox + (h - s.ext[0]) * s.S
    def Y(s, w): return s.oy + (s.ext[3] - w) * s.S    # w = vertical axis (z for elevations, y for top) top = ext[3]
    # front: h = x, v = z. side: h = y, v = z. top: h = x, v = y (back at top)
    def pt(s, h, w): return (s.X(h), s.Y(w) if s.kind != 'top' else s.oy + (w - s.ext[2]) * s.S)

def proj(view, e):
    p = e['poly']
    if view == 'front': return bounds(p, 0), (e['z0'], e['z1'])
    if view == 'side': return bounds(p, 1), (e['z0'], e['z1'])
    return bounds(p, 0), bounds(p, 1)

def draw_view(vw, elems, fillfn, strokefn, label=None, ghost=lambda e: False):
    out = []; S = vw.S
    def Pt(h, w): return vw.pt(h, w)
    order = sorted(elems, key=lambda e: ((sum(q[1] for q in e['poly'])/len(e['poly'])) if vw.kind == 'front' else (-sum(q[0] for q in e['poly'])/len(e['poly'])) if vw.kind == 'side' else e['z1']))
    order = [e for e in order if e.get('dark')] + [e for e in order if not e.get('dark')]
    for e in order:
        if vw.kind == 'top' and e.get('dark'): continue
        (h0, h1), (w0, w1) = proj(vw.kind, e)
        if vw.kind == 'top' and e['kind'] in ('strands',): continue
        if vw.kind != 'top' and e.get('floor') and False: continue
        g = ghost(e); fill = '#f1f1f1' if g else fillfn(e); stroke = '#c4c4c4' if g else strokefn(e)
        sw = 1.2 if g else 2
        op = 0.55 if (e.get('glass') or e['kind'] == 'cave' or e['b'] == 'J') and not g else 1
        dash = ' stroke-dasharray="8 6"' if e.get('hidden') else ''
        k = e['kind']
        if vw.kind == 'top':
            if k == 'spiral':
                a, b = e['poly']; n = 60
                for i in range(n+1):
                    t = i/n; px = a[0]+(b[0]-a[0])*t; py = a[1]+(b[1]-a[1])*t
                    dx, dy = b[0]-a[0], b[1]-a[1]; ln = math.hypot(dx, dy); nx, ny = -dy/ln, dx/ln
                    sw_ = 1.25*math.sin(2*math.pi*3*t); x_, y_ = Pt(px+nx*sw_, py+ny*sw_)
                    out.append(f'<circle cx="{x_:.1f}" cy="{y_:.1f}" r="{0.28*S:.1f}" fill="{fill}" fill-opacity=".55" stroke="{stroke}" stroke-width="1"/>')
                continue
            pts = ' '.join('%.1f,%.1f' % Pt(x, y) for x, y in e['poly'])
            out.append(f'<polygon points="{pts}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
            if k == 'tree':
                cx, cy = Pt(sum(q[0] for q in e['poly'])/len(e['poly']), sum(q[1] for q in e['poly'])/len(e['poly']))
                out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{0.12*S:.1f}" fill="{dark(COL[e["b"]]) if not g else "#bbb"}"/>')
            continue
        if k == 'spiral':
            a, b = e['poly']; n = 60
            for i in range(n+1):
                t = i/n; px = a[0]+(b[0]-a[0])*t; py = a[1]+(b[1]-a[1])*t
                dx, dy = b[0]-a[0], b[1]-a[1]; ln = math.hypot(dx, dy); nx, ny = -dy/ln, dx/ln
                sw_ = 1.25*math.sin(2*math.pi*3*t); z = e['z1']-(e['z1']-e['z0'])*t
                h = (px+nx*sw_) if vw.kind == 'front' else (py+ny*sw_)
                x_, y_ = Pt(h, z)
                out.append(f'<circle cx="{x_:.1f}" cy="{y_:.1f}" r="{0.28*S:.1f}" fill="{fill}" fill-opacity=".6" stroke="{stroke}" stroke-width="1"/>')
            continue
        if k == 'strands':
            c0 = sum(q[0] for q in e['poly'])/len(e['poly']) if vw.kind == 'front' else sum(q[1] for q in e['poly'])/len(e['poly'])
            for i in range(13):
                hh = c0 - 0.9 + i*0.15
                x1, y1 = Pt(hh, e['z1']); x2, y2 = Pt(hh, e['z0'])
                out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="1.3"/>')
            continue
        x1, y1 = Pt(h0, w1); x2, y2 = Pt(h1, w0)
        if k == 'star':
            cx, cy = (x1+x2)/2, (y1+y2)/2; r = (x2-x1)/2*1.1; pts = []
            for i in range(10):
                rr = r if i % 2 == 0 else r*0.45; a = -math.pi/2 + i*math.pi/5
                pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
            out.append(f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'); continue
        if k == 'tree':
            tw = (x2-x1)*0.18; cx = (x1+x2)/2; ch = (y2-y1)
            out.append(f'<rect x="{cx-tw/2:.1f}" y="{y1+ch*0.45:.1f}" width="{tw:.1f}" height="{ch*0.55:.1f}" fill="{dark(COL[e["b"]]) if not g else "#bbb"}"/>')
            out.append(f'<ellipse cx="{cx:.1f}" cy="{y1+ch*0.3:.1f}" rx="{(x2-x1)/2*1.25:.1f}" ry="{ch*0.32:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'); continue
        if k == 'cave':
            wd = x2-x1; ht = y2-y1
            path = f'M{x1:.1f},{y2:.1f} L{x1:.1f},{y1+wd*0.4:.1f} Q{x1:.1f},{y1:.1f} {(x1+x2)/2:.1f},{y1:.1f} Q{x2:.1f},{y1:.1f} {x2:.1f},{y1+wd*0.4:.1f} L{x2:.1f},{y2:.1f} Z'
            out.append(f'<path d="{path}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>'); continue
        out.append(f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{max(x2-x1,1.5):.1f}" height="{max(y2-y1,1.5):.1f}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
    return ''.join(out)

FONT = "font-family=\"'Segoe UI',Arial,sans-serif\""
def T(x, y, t, size=18, fill='#2b2a33', anchor='start', weight='normal', rot=None):
    r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{r}>{t}</text>'

def dim_h(x1, x2, y, label, col='#4a4a55'):
    return (f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>'
            + T((x1+x2)/2, y-6, label, 16, col, 'middle'))
def dim_v(x, y1, y2, label, col='#4a4a55'):
    return (f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>'
            + T(x-8, (y1+y2)/2, label, 16, col, 'middle', rot=-90))
DEFS = '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4a4a55"/></marker><pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="#ecebe4"/><path d="M0 0V9" stroke="#7a7a82" stroke-width="2"/></pattern></defs>'

YAW = math.radians(33); HFOV = math.radians(96); CAMV = (-3.0, 19.0, 5.2)
def _shade(h, k):
    h = h.lstrip('#'); r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(c*k))) for c in (r, g, b))

def persp_panel(elems, fillfn, strokefn, W=1200, H=680, ghost=lambda e: False, letters=True, x0=0, y0=0):
    """True perspective from V (same camera as the grey block-out: yaw 33 deg, 96 deg lens, eye 5.2 ft above the floor)."""
    F = W/2/math.tan(HFOV/2); fx, fy = math.sin(YAW), -math.cos(YAW); rx, ry = math.cos(YAW), math.sin(YAW)
    def pr(x, y, z):
        dx, dy, dz = x-CAMV[0], y-CAMV[1], (z+2.0)-CAMV[2]
        fw = max(dx*fx+dy*fy, 0.3); rt = dx*rx+dy*ry
        return (x0+W/2+F*rt/fw, y0+H/2-F*dz/fw+H*0.04, fw)
    faces = []
    def addf(pts3, fill, k, stroke, sw=1.4, op=1):
        pp = [pr(*q) for q in pts3]
        faces.append((max(q[2] for q in pp), '<polygon points="%s" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="%s"/>' % (' '.join('%.1f,%.1f' % (a, b) for a, b, _ in pp), _shade(fill, k), op, stroke, sw)))
    for e in elems:
        g = ghost(e); fill = '#e6e6e6' if g else fillfn(e); stroke = '#bdbdbd' if g else strokefn(e); k = e['kind']; poly = e['poly']
        op = 0.6 if (e.get('glass') or k == 'cave' or e['b'] == 'J') and not g else 1
        if g: op = 0.3
        if e.get('hidden'): continue
        if k == 'spiral':
            a, b = poly
            for i in range(61):
                t = i/60; px = a[0]+(b[0]-a[0])*t; py = a[1]+(b[1]-a[1])*t
                dx, dy = b[0]-a[0], b[1]-a[1]; ln = math.hypot(dx, dy); nx, ny = -dy/ln, dx/ln
                o = 1.25*math.sin(2*math.pi*3*t); X, Y, fw = pr(px+nx*o, py+ny*o, e['z1']-(e['z1']-e['z0'])*t)
                faces.append((fw, f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{0.28*F/fw:.1f}" fill="{fill}" fill-opacity=".6" stroke="{stroke}"/>'))
            continue
        if k == 'strands':
            cx = sum(q[0] for q in poly)/len(poly); cy = sum(q[1] for q in poly)/len(poly)
            for i in range(14):
                an = 2*math.pi*i/14; X1, Y1, fw = pr(cx+0.9*math.cos(an), cy+0.9*math.sin(an), e['z1']); X2, Y2, _ = pr(cx+0.9*math.cos(an), cy+0.9*math.sin(an), e['z0'])
                faces.append((fw, f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{stroke}" stroke-width="1.2"/>'))
            continue
        if k == 'star':
            cx = sum(q[0] for q in poly)/len(poly); cy = sum(q[1] for q in poly)/len(poly); X, Y, fw = pr(cx, cy, (e['z0']+e['z1'])/2); r = 1.0*F/fw
            pts = []
            for i in range(10):
                rr = r if i % 2 == 0 else r*0.45; a_ = -math.pi/2+i*math.pi/5; pts.append(f'{X+rr*math.cos(a_):.1f},{Y+rr*math.sin(a_):.1f}')
            faces.append((fw, f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')); continue
        if k == 'flat':
            addf([(x, y, 0.03) for x, y in poly], '#fff2c8' if not g else fill, 1, stroke); continue
        n = len(poly); cx = sum(q[0] for q in poly)/n; cy = sum(q[1] for q in poly)/n
        z0, z1 = e['z0'], e['z1']
        for i in range(n):
            a_, b_ = poly[i], poly[(i+1) % n]; mx, my = (a_[0]+b_[0])/2, (a_[1]+b_[1])/2; nx_, ny_ = b_[1]-a_[1], -(b_[0]-a_[0])
            if (mx-cx)*nx_+(my-cy)*ny_ < 0: nx_, ny_ = -nx_, -ny_
            if (CAMV[0]-mx)*nx_+(CAMV[1]-my)*ny_ <= 0: continue
            l = math.hypot(nx_, ny_) or 1; kk = 0.62+0.38*max(0, (nx_*-0.5+ny_*0.8)/l)
            addf([(a_[0], a_[1], z0), (b_[0], b_[1], z0), (b_[0], b_[1], z1), (a_[0], a_[1], z1)], fill, kk, stroke, 1.2, op)
        addf([(x, y, z1) for x, y in poly], fill, 1.1, stroke, 1.6, op)
        if k == 'tree' and not g:
            X, Y, fw = pr(cx, cy, z1); faces.append((fw-0.01, f'<ellipse cx="{X:.1f}" cy="{Y:.1f}" rx="{0.75*F/fw:.1f}" ry="{0.5*F/fw:.1f}" fill="{fill}" stroke="{stroke}"/>'))
    out = ''.join(f for _, f in sorted(faces, key=lambda t: -t[0]))
    if letters:
        for b in COL:
            if b == 'A': continue
            sel = [e for e in elems if e['b'] == b and e['kind'] not in ('flat', 'spiral', 'strands') and not e.get('hidden')]
            if b == 'H': sel = [e for e in elems if e['b'] == 'H' and e['name'] == 'speaker']
            pts = [pr(sum(q[0] for q in e['poly'])/len(e['poly']), sum(q[1] for q in e['poly'])/len(e['poly']), e['z1']) for e in sel]
            if b == 'I': pts = [pr(HANG[0], HANG[1], 11.5)]
            if b == 'J': pts = [pr(1.0, 0.0, 9.0)]
            if not pts: continue
            X = sum(q[0] for q in pts)/len(pts); Y = sum(q[1] for q in pts)/len(pts)
            out += f'<text x="{X:.1f}" y="{Y+9:.1f}" {FONT} font-size="28" font-weight="700" fill="#111" stroke="#fff" stroke-width="5" paint-order="stroke" text-anchor="middle">{b}</text>'
    cid = f'pc{int(x0)}_{int(y0)}'
    return f'<clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{W}" height="{H}"/></clipPath><g clip-path="url(#{cid})">{out}</g>'

def master():
    S = 66; ZMIN, ZMAX = -2.2, 13.8
    W = 3000; H = 2330
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}<rect width="{W}" height="{H}" fill="#fbfaf6"/><rect x="10" y="10" width="{W-20}" height="{H-20}" fill="none" stroke="#2b2a33" stroke-width="3"/>']
    s.append(T(40, 62, 'Crib 2026 · "That Night in Bethlehem" · final blueprint: front, side and top views', 34, weight='bold'))
    s.append(T(40, 96, 'Stage 9 ft × 16 ft · feet · one scale for all three views · heights above the stage deck (deck is 2 ft above the church floor) · block letters match the build guide', 17, '#5d5b66'))
    top0 = 190
    vf = View('front', S, 80, top0, (0, 9, ZMIN, ZMAX)); vs = View('side', S, 80+9*S+170, top0, (0, 16, ZMIN, ZMAX)); vt = View('top', S, 80+9*S+170+16*S+170, top0, (0, 9, 0, 16))
    fill = lambda e: '#33333a' if e.get('dark') else '#fff2c8' if e.get('gold') else '#e8f0fb' if e.get('drape') else light(COL[e['b']])
    fill2 = lambda e: '#33333a' if e.get('dark') else '#fff2c8' if e.get('gold') else ('#cbd5f2' if e.get('drape') else light(COL[e['b']]))
    strk = lambda e: dark(COL[e['b']])
    for vw, ttl, sub in ((vf, 'FRONT VIEW', 'looking from the public side toward the altar wall'), (vs, 'SIDE VIEW (from the open left edge)', 'back wall on the left, front on the right'), (vt, 'TOP VIEW', 'back wall at the top, public in front')):
        s.append(T(vw.ox, top0-34, ttl, 22, weight='bold')); s.append(T(vw.ox, top0-12, sub, 15, '#5d5b66'))
        if vw.kind == 'top':
            s.append(f'<rect x="{vw.X(0):.1f}" y="{vw.oy:.1f}" width="{9*S}" height="{16*S}" fill="#fffef9" stroke="#2b2a33" stroke-width="2"/>')
            gx = ''.join(f'<line x1="{vw.X(i):.1f}" y1="{vw.oy:.1f}" x2="{vw.X(i):.1f}" y2="{vw.oy+16*S:.1f}" stroke="#dde1ea"/>' for i in range(10))
            gy = ''.join(f'<line x1="{vw.X(0):.1f}" y1="{vw.oy+i*S:.1f}" x2="{vw.X(9):.1f}" y2="{vw.oy+i*S:.1f}" stroke="#dde1ea"/>' for i in range(17))
            s.append(gx+gy)
        else:
            gy_floor = vw.Y(-2); gy_deck = vw.Y(0); gy_ceil = vw.Y(CEIL); hw = (9 if vw.kind == 'front' else 16)*S
            s.append(f'<rect x="{vw.X(0):.1f}" y="{gy_ceil-20:.1f}" width="{hw}" height="20" fill="url(#hatch)" stroke="#2b2a33"/>')
            s.append(f'<line x1="{vw.X(0)-30:.1f}" y1="{gy_floor:.1f}" x2="{vw.X(0)+hw+30:.1f}" y2="{gy_floor:.1f}" stroke="#2b2a33" stroke-width="3"/>')
            s.append(f'<line x1="{vw.X(0):.1f}" y1="{gy_deck:.1f}" x2="{vw.X(0)+hw:.1f}" y2="{gy_deck:.1f}" stroke="#8a8a92" stroke-dasharray="4 4"/>')
        els = [e for e in E if not (vw.kind != 'top' and e['b'] == 'H' and e['kind'] == 'flat')]
        s.append(draw_view(vw, els, fill2, strk))
        # block letters
        for b in COL:
            if b in ('A',): continue
            sel = [e for e in E if e['b'] == b and not (vw.kind != 'top' and e['kind'] == 'flat')]
            if b == 'H': sel = [e for e in sel if (e['name'] == 'path of light' if vw.kind == 'top' else e['name'] == 'speaker')]
            pe = [proj(vw.kind, e) for e in sel]
            if not pe: continue
            hs = [h for (hh, _) in pe for h in hh]; ws = [w for (_, ww) in pe for w in ww]
            cx = (min(hs)+max(hs))/2; cw = (min(ws)+max(ws))/2
            x_, y_ = vw.pt(cx, cw)
            if b == 'J': x_, y_ = vw.pt(1.0 if vw.kind != 'side' else 1.0, 9.5 if vw.kind != 'top' else 0.0)
            if b == 'J' and vw.kind == 'top': x_, y_ = vw.pt(0.4, 0.45)
            s.append(f'<text x="{x_:.1f}" y="{y_+8:.1f}" {FONT} font-size="26" font-weight="700" fill="#111" stroke="#fff" stroke-width="5" paint-order="stroke" text-anchor="middle">{b}</text>')
        # height ruler
        if vw.kind != 'top':
            hw = (9 if vw.kind == 'front' else 16)*S; xr = vw.X(0)+hw+16
            for z, lab in ((0,'deck'),(3.0,'+3.0 hill crest'),(4.3,'+4.3 house roof'),(CEIL,'+13 ceiling (assumed)')):
                s.append(f'<line x1="{vw.X(0)-6:.1f}" y1="{vw.Y(z):.1f}" x2="{xr-8:.1f}" y2="{vw.Y(z):.1f}" stroke="#a9a9b3" stroke-dasharray="2 5"/>')
                s.append(T(xr, vw.Y(z)+5, lab, 14, '#5d5b66'))
            ey = vw.Y(EYE)
            s.append(f'<line x1="{vw.X(0)-6:.1f}" y1="{ey:.1f}" x2="{xr-8:.1f}" y2="{ey:.1f}" stroke="#a8322c" stroke-dasharray="6 5"/>'); s.append(T(xr, ey+5, 'eye 5.2 ft above floor', 14, '#a8322c'))
            s.append(dim_v(vw.X(0)-28, vw.Y(0), vw.Y(-2), '2 ft deck'))
            s.append(dim_h(vw.X(0), vw.X(0)+hw, vw.Y(-2)+34, '9 ft' if vw.kind == 'front' else '16 ft'))
        else:
            s.append(dim_h(vw.X(0), vw.X(9), vw.oy+16*S+30, '9 ft')); s.append(dim_v(vw.X(0)-24, vw.oy, vw.oy+16*S, '16 ft'))
            s.append(T(vw.X(0), vw.oy+16*S+62, 'Public view spot V: 3 ft left and 3 ft in front of the front-left corner, eye 5.2 ft above the floor.', 15, '#a8322c'))
    py0 = top0 + (ZMAX-ZMIN)*S + 150
    s.append(T(40, py0-20, 'TILTED VIEW FROM THE PUBLIC SPOT V: the stage is turned 33 degrees, 9 ft wall on the left, 16 ft wall running away to the right', 20, weight='bold'))
    s.append(f'<rect x="40" y="{py0}" width="1500" height="850" fill="#f3f1ea" stroke="#2b2a33" stroke-width="2"/>')
    s.append(persp_panel(E, fill2, strk, W=1500, H=850, x0=40, y0=py0))
    ly = py0 + 40; lx0 = 1620
    s.append(T(lx0, ly, 'BLOCKS', 20, weight='bold'))
    for i, b in enumerate('ABCEFGHIJKL'):
        x = lx0 + (i % 2)*680; y = ly + 40 + (i//2)*44
        s.append(f'<rect x="{x}" y="{y-16}" width="34" height="22" fill="{light(COL[b])}" stroke="{dark(COL[b])}" stroke-width="2"/>' + T(x+46, y+2, f'{b}  {NAMES[b]}', 18))
    s.append('</svg>')
    return '\n'.join(s), W, H

def block_sheet(b):
    mine = [e for e in E if e['b'] == b]
    ext = {}
    for kind in ('front', 'side', 'top'):
        hs = []; ws = []
        for e in mine:
            if kind != 'top' and e['kind'] == 'flat': continue
            (h0, h1), (w0, w1) = proj(kind, e); hs += [h0, h1]; ws += [w0, w1]
        if not hs: hs, ws = [0, 1], [0, 1]
        ext[kind] = (min(hs), max(hs), min(ws), max(ws))
    m = 0.6
    def box(k): hmin, hmax, wmin, wmax = ext[k]; return (hmin-m, hmax+m, wmin-m, wmax+m)
    E3 = {k: box(k) for k in ext}
    big = max(max(e[1]-e[0], e[3]-e[2]) for e in E3.values())
    S = min(120, 760/big)
    W = 80; panels = []; pw = []
    for k in ('front', 'side', 'top'):
        hmin, hmax, wmin, wmax = E3[k]; pw.append(((hmax-hmin)*S, (wmax-wmin)*S))
    Wt = 80*4 + sum(p[0] for p in pw); PH = 700; Ht = int(max(p[1] for p in pw) + 330 + PH + 90)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(Wt)}" height="{Ht}" viewBox="0 0 {int(Wt)} {Ht}">{DEFS}<rect width="{int(Wt)}" height="{Ht}" fill="#ffffff"/>']
    s.append(T(40, 56, f'BLOCK {b} · {NAMES[b]} · front, side and top view', 30, weight='bold'))
    s.append(T(40, 88, 'Coloured = this block. Pale grey = neighbouring blocks for position. Feet. Same orientation as the master blueprint.', 16, '#5d5b66'))
    x = 80
    for k, ttl in (('front', 'FRONT (from the public side)'), ('side', 'SIDE (from the left edge)'), ('top', 'TOP')):
        hmin, hmax, wmin, wmax = E3[k]; pwid = (hmax-hmin)*S; phgt = (wmax-wmin)*S
        vw = View(k, S, x, 170, (hmin, hmax, wmin, wmax))
        s.append(T(x, 150, ttl, 20, weight='bold'))
        s.append(f'<rect x="{x:.1f}" y="170" width="{pwid:.1f}" height="{phgt:.1f}" fill="#fcfcfa" stroke="#dcdcdc"/>')
        ctx = [e for e in E if e['b'] != b and not (k != 'top' and e['kind'] == 'flat') and not (e['b'] == 'A' and False)]
        s.append(f'<g clip-path="url(#c{k})"><clipPath id="c{k}"><rect x="{x:.1f}" y="170" width="{pwid:.1f}" height="{phgt:.1f}"/></clipPath>')
        s.append(draw_view(vw, ctx, lambda e: '#f1f1f1', lambda e: '#c4c4c4', ghost=lambda e: True))
        s.append(draw_view(vw, [e for e in mine if not (k != 'top' and e['kind'] == 'flat')], lambda e: '#fff2c8' if e.get('gold') else ('#cbd5f2' if e.get('drape') else light(COL[b])), lambda e: dark(COL[b])))
        s.append('</g>')
        mh = ext[k]
        s.append(dim_h(vw.X(mh[0]), vw.X(mh[1]), 170+phgt+34, f'{mh[1]-mh[0]:.1f} ft'))
        if k == 'top': s.append(dim_v(vw.X(mh[0])-14, vw.pt(0, mh[2])[1], vw.pt(0, mh[3])[1], f'{mh[3]-mh[2]:.1f} ft'))
        else: s.append(dim_v(vw.X(mh[0])-14, vw.Y(mh[3]), vw.Y(mh[2]), f'{mh[3]-mh[2]:.1f} ft high ({mh[2]:+.1f} to {mh[3]:+.1f})'))
        x += pwid + 80
    py = int(max(p[1] for p in pw) + 280)
    s.append(T(80, py-12, 'TILTED VIEW FROM THE PUBLIC SPOT V: stage turned 33 degrees, 9 ft wall on the left, 16 ft wall running away to the right', 20, weight='bold'))
    s.append(f'<rect x="80" y="{py}" width="1240" height="{PH}" fill="#f3f1ea" stroke="#2b2a33"/>')
    s.append(persp_panel(E, lambda e: '#fff2c8' if e.get('gold') else light(COL[b]), lambda e: dark(COL[b]), W=1240, H=PH, ghost=lambda e: e['b'] != b, letters=False, x0=80, y0=py))
    s.append('</svg>')
    return '\n'.join(s), int(Wt), Ht

def fi(x):
    if x < 1: return f'{round(x*12)} in'
    t = f'{x:.2f}'.rstrip('0').rstrip('.')
    return f'{t} ft ({round(x*12)} in)'

def part_groups(b):
    """Group identical parts of block b. Returns list of dict(no, name, size, where, base, members=[element indexes])."""
    mine = [e for e in E if e['b'] == b]; groups = {}
    for idx, e in enumerate(mine):
        p = e['poly']; nm = e['name']; z = e['z1'] - e['z0']; xs = [q[0] for q in p]; ys = [q[1] for q in p]
        if e['kind'] == 'strands': size = '60 strands, each 6 ft long, hung from a 1.8 ft ring'
        elif e['kind'] == 'spiral': size = '2.5 ft wide, 3 turns, from 10.5 ft down to 4.5 ft above the deck; 30 small angels (4-6 in)'
        elif e['kind'] == 'star': size = '2 ft wide, hung about 1 ft below the ceiling'
        elif e['kind'] == 'flat': size = '0.5 ft (6 in) wide × 7.7 ft long, set flush in the deck'
        elif nm == 'shepherd': size = 'figure 1.2 ft (14 in) tall, scale 1:6; stands on a base about 4 in across'
        elif nm == 'sheep': size = 'about 0.45 ft (5 in) long, 0.4 ft (5 in) tall; real wool'
        elif nm == 'campfire': size = 'about 4 in across, 4 in tall, orange flicker LED inside'
        elif nm == 'rock hill': size = 'about 7 ft × 6 ft base (irregular, see top view), up to 3 ft high; keep 1 ft free behind for wiring'
        elif e['kind'] == 'tree':
            dia = math.hypot(p[0][0]-p[len(p)//2][0], p[0][1]-p[len(p)//2][1])*1.25
            size = f'canopy about {fi(dia)} across, {fi(z)} tall'
        elif nm == 'deck + skirting': size = '9 ft wide at the front × 16 ft deep; skirting 2 ft'
        elif nm.endswith('print'): size = '5 ft high; wall length ' + ('16 ft' if 'right' in nm else '9 ft')
        elif nm.endswith('drape'): size = 'from 5 ft up to the ceiling (about 13 ft above the deck); wall length ' + ('16 ft' if 'right' in nm else '9 ft')
        else:
            if len(p) == 4:
                w = math.hypot(p[1][0]-p[0][0], p[1][1]-p[0][1]); d = math.hypot(p[2][0]-p[1][0], p[2][1]-p[1][1])
            elif len(p) >= 8: w = d = math.hypot(p[0][0]-p[len(p)//2][0], p[0][1]-p[len(p)//2][1])
            else: w = max(xs)-min(xs); d = max(ys)-min(ys)
            big, small = max(w, d), min(w, d)
            size = f'{fi(big)} × {fi(small)}' + (f' × {fi(z)} high' if z > 0.05 else '')
            if e['kind'] == 'cave': size += ', arch 2.5 ft high'
        if e['kind'] in ('cave',) or nm in ('Holy Family', 'guest room'): size += '; turned 33° toward V'
        if e['kind'] in ('spiral', 'strands', 'star', 'flat'): where = f'centre x {sum(xs)/len(xs):.1f} ft from the left edge, y {sum(ys)/len(ys):.1f} ft from the back wall' if e['kind'] in ('star', 'strands') else 'see top view'
        else: where = f'{min(xs):.1f}–{max(xs):.1f} ft from the left edge; {min(ys):.1f}–{max(ys):.1f} ft from the back wall'
        if e['kind'] == 'spiral': where = f'from the star at x {HANG[0]} ft, y {HANG[1]} ft, curling down to x {LND[0]:.1f} ft, y {LND[1]:.1f} ft'
        if e['kind'] == 'flat': where = 'front edge x 1.9 ft, y 15.9 ft, to the cave mouth x 3.7 ft, y 8.5 ft'
        base = 'on the deck' if e['z0'] == 0 else f'{e["z0"]:.1f} ft above the deck'
        if e['z0'] < 0: base = 'under the deck'
        if nm in ('cave', 'Holy Family', 'guest room', 'rock hill'): base = 'see stack note'
        key = (nm, size)
        g = groups.setdefault(key, dict(name=nm, size=size, wheres=[], base=base, members=[]))
        g['wheres'].append(where); g['members'].append(idx)
    out = []
    for i, g in enumerate(groups.values(), 1):
        g['no'] = i; g['count'] = len(g['members']); out.append(g)
    return out

def blueprint_svg(b):
    mine = [e for e in E if e['b'] == b]; groups = part_groups(b)
    owner = {m: g['no'] for g in groups for m in g['members']}
    ext = {}
    for kind in ('front', 'side', 'top'):
        hs = []; ws = []
        for e in mine:
            if kind != 'top' and e['kind'] == 'flat': continue
            (h0, h1), (w0, w1) = proj(kind, e); hs += [h0, h1]; ws += [w0, w1]
        if not hs: hs, ws = [0, 1], [0, 1]
        ext[kind] = (min(hs), max(hs), min(ws), max(ws))
    wide = b in ('A', 'J', 'I', 'H', 'L')
    m = 0.5
    E3 = {}
    for k, (a, c, d, f) in ext.items():
        E3[k] = (-0.3, 9.3, -0.3, 16.3) if (k == 'top' and wide) else (a-m, c+m, d-m, f+m)
        if wide and k != 'top': E3[k] = (min(a, 0)-0.3, max(c, 16 if k == 'side' else 9)+0.3, min(d, -2)-0.3, max(f, 0)+0.3)
    spanw = sum(e[1]-e[0] for e in E3.values()); spanh = max(e[3]-e[2] for e in E3.values())
    S = min(100, (1650-3*70)/spanw, 640/spanh)
    X0 = 100; gap = 90; top = 120
    Wt = int(X0 + spanw*S + gap*3 + 60); Ht = int(top + spanh*S + 130)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wt}" height="{Ht}" viewBox="0 0 {Wt} {Ht}">{DEFS}<rect width="{Wt}" height="{Ht}" fill="#ffffff"/>']
    s.append(T(20, 36, f'BLOCK {b} · {NAMES[b]}: blueprint with measurements (feet). Numbers match the parts table.', 24, weight='bold'))
    x = X0
    for k, ttl in (('front', 'FRONT (from the public side)'), ('side', 'SIDE (from the open left edge, back wall on the left)'), ('top', 'TOP (x from left edge, y from back wall)')):
        hmin, hmax, wmin, wmax = E3[k]; pwid = (hmax-hmin)*S; phgt = (wmax-wmin)*S
        vw = View(k, S, x, top, (hmin, hmax, wmin, wmax))
        s.append(T(x, top-18, ttl, 15, weight='bold'))
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{pwid:.1f}" height="{phgt:.1f}" fill="#fdfdfb" stroke="#bbb"/>')
        cid = f'bp{k}'
        s.append(f'<clipPath id="{cid}"><rect x="{x:.1f}" y="{top}" width="{pwid:.1f}" height="{phgt:.1f}"/></clipPath><g clip-path="url(#{cid})">')
        if k == 'top':
            for i in range(int(math.floor(hmin)), int(math.ceil(hmax))+1): s.append(f'<line x1="{vw.X(i):.1f}" y1="{top}" x2="{vw.X(i):.1f}" y2="{top+phgt:.1f}" stroke="#e1e5ee"/>')
            for j in range(int(math.floor(wmin)), int(math.ceil(wmax))+1): s.append(f'<line x1="{x:.1f}" y1="{top+(j-wmin)*S:.1f}" x2="{x+pwid:.1f}" y2="{top+(j-wmin)*S:.1f}" stroke="#e1e5ee"/>')
        else:
            gy = vw.Y(0); s.append(f'<line x1="{x:.1f}" y1="{gy:.1f}" x2="{x+pwid:.1f}" y2="{gy:.1f}" stroke="#8a8a92" stroke-dasharray="5 4"/>')
            for z in range(int(math.floor(wmin)), int(math.ceil(wmax))+1): s.append(f'<line x1="{x:.1f}" y1="{vw.Y(z):.1f}" x2="{x+pwid:.1f}" y2="{vw.Y(z):.1f}" stroke="#eef0f5"/>')
            for hh in range(int(math.floor(hmin)), int(math.ceil(hmax))+1): s.append(f'<line x1="{vw.X(hh):.1f}" y1="{top}" x2="{vw.X(hh):.1f}" y2="{top+phgt:.1f}" stroke="#eef0f5"/>')
        ctx = [e for e in E if e['b'] != b and not (k != 'top' and e['kind'] == 'flat') and not (e.get('dark') and k == 'top')]
        s.append(draw_view(vw, ctx, lambda e: '#f3f3f3', lambda e: '#d0d0d0', ghost=lambda e: True))
        shown = [e for e in mine if not (k != 'top' and e['kind'] == 'flat') and not (e.get('dark') and k == 'top')]
        s.append(draw_view(vw, shown, lambda e: '#fff2c8' if e.get('gold') else ('#cbd5f2' if e.get('drape') else light(COL[b])), lambda e: dark(COL[b])))
        for idx, e in enumerate(mine):
            if e not in shown: continue
            (h0, h1), (w0, w1) = proj(k, e); cx, cy = vw.pt((h0+h1)/2, (w0+w1)/2)
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="11" fill="#fff" stroke="#111" stroke-width="1.6"/>' + T(cx, cy+5, str(owner[idx]), 13, '#111', 'middle', 'bold'))
        s.append('</g>')
        mh = ext[k]
        if not (wide and k != 'top'):
            s.append(dim_h(vw.X(mh[0]), vw.X(mh[1]), top+phgt+26, f'{mh[1]-mh[0]:.1f} ft ({mh[0]:.1f} to {mh[1]:.1f})'))
            if k == 'top': s.append(dim_v(vw.X(hmin)-16, vw.pt(0, mh[2])[1], vw.pt(0, mh[3])[1], f'{mh[3]-mh[2]:.1f} ft ({mh[2]:.1f} to {mh[3]:.1f})'))
            else: s.append(dim_v(vw.X(hmin)-16, vw.Y(mh[3]), vw.Y(mh[2]), f'{mh[3]-mh[2]:.1f} ft high ({mh[2]:+.1f} to {mh[3]:+.1f} above the deck)'))
        else:
            s.append(dim_h(vw.X(0), vw.X(9 if k != 'side' else 16), top+phgt+26, '9 ft' if k != 'side' else '16 ft'))
        if k == 'top':
            for i in range(int(math.ceil(hmin)), int(math.floor(hmax))+1): s.append(T(vw.X(i), top-4, str(i), 11, '#666', 'middle'))
            for j in range(int(math.ceil(wmin)), int(math.floor(wmax))+1): s.append(T(x-5, top+(j-wmin)*S+4, str(j), 11, '#666', 'end'))
        x += pwid + gap
    s.append('</svg>')
    return '\n'.join(s), Wt, Ht

RAMP = [(16, 0.0), (10.5, 0.0), (9.5, 0.3), (8, 1.8), (7, 3.0), (0, 3.0)]   # (y from back wall, leg height above deck); f = 16 - y

def frame_groups():
    secs = [f'S{r*2+c+1}: x {c*4}–{c*4+4}, y {r*4}–{r*4+4}' for r in range(4) for c in range(2)]
    return [dict(no=1, name='Frame sections S1–S8', size='each 4 ft × 4 ft; 2×2 in battens, 4 sides + 1 cross batten each way at the 2 ft centre', wheres=['; '.join(secs)], count=1, base='on the deck'),
            dict(no=2, name='Edge strips R1–R4', size='each 1 ft × 4 ft, along the right wall', wheres=['x 8–9, y 0–16, in four 4 ft pieces'], count=1, base='on the deck'),
            dict(no=3, name='Leg heights (by distance f from the front edge)', size='f 0–5.5 ft: no legs · f 6.5 ft: 0.3 ft (4 in) · f 8 ft: 1.8 ft (22 in) · f 9–16 ft: 3.0 ft (36 in); ramp straight between', wheres=['y = 16 − f from the back wall'], count=1, base='on the deck'),
            dict(no=4, name='Left terrace boxes (made in block E)', size='3.4 ft wide, 1.75 ft deep each, tops +2.0 / +1.6 / +1.2 / +0.8 ft', wheres=['x 0–3.4; y 0–1.75, 1.75–3.5, 3.5–5.25, 5.25–7.0'], count=1, base='on the deck'),
            dict(no=5, name='Hatch lid A (control box)', size='1.2 ft × 0.8 ft, loose plywood', wheres=['x 7.6–8.8, y 15.2–16.0'], count=1, base='flush with the deck'),
            dict(no=6, name='Hatch lid B (angel screen + mister)', size='1.3 ft × 0.6 ft, loose plywood', wheres=['x 0.9–2.2, y 3.7–4.3'], count=1, base='flush with the deck'),
            dict(no=7, name='Hatch lid C (speaker)', size='1 ft × 1 ft, loose plywood', wheres=['x 0–1, y 11.2–12.2'], count=1, base='flush with the deck'),
            dict(no=8, name='Skirting, black pleated', size='25 ft run, 2 ft drop, Velcro', wheres=['front edge (9 ft) and left edge (16 ft)'], count=1, base='hangs to the floor')]

def frame_svg():
    S = 44; W = 1500; H = 960
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}<rect width="{W}" height="{H}" fill="#fff"/>']
    s.append(T(20, 34, 'BLOCK A · Stage frame and rake: blueprint with measurements (feet). Numbers match the parts table.', 24, weight='bold'))
    # top view
    tx, ty = 70, 110
    s.append(T(tx, ty-16, 'TOP: sections and hatches (x from the left edge, y from the back wall)', 15, weight='bold'))
    s.append(f'<rect x="{tx}" y="{ty}" width="{9*S}" height="{16*S}" fill="#fdfdfb" stroke="#2b2a33" stroke-width="2"/>')
    for r in range(4):
        for c in range(2):
            n = r*2+c+1; x0, y0 = tx+c*4*S, ty+r*4*S
            s.append(f'<rect x="{x0}" y="{y0}" width="{4*S}" height="{4*S}" fill="#eceff4" fill-opacity=".7" stroke="#6a7a96" stroke-width="1.6"/>' + T(x0+4*S/2, y0+4*S/2+6, f'S{n}', 20, '#33415f', 'middle', 'bold'))
            s.append(f'<line x1="{x0+2*S}" y1="{y0}" x2="{x0+2*S}" y2="{y0+4*S}" stroke="#aab4c8" stroke-dasharray="4 4"/><line x1="{x0}" y1="{y0+2*S}" x2="{x0+4*S}" y2="{y0+2*S}" stroke="#aab4c8" stroke-dasharray="4 4"/>')
    for r in range(4): s.append(f'<rect x="{tx+8*S}" y="{ty+r*4*S}" width="{S}" height="{4*S}" fill="#dfe6d8" stroke="#6b8a5a" stroke-width="1.6"/>' + T(tx+8.5*S, ty+r*4*S+2*S+5, f'R{r+1}', 14, '#3e5a30', 'middle', 'bold'))
    for (y0, y1, lv) in ((0, 1.75, 2.0), (1.75, 3.5, 1.6), (3.5, 5.25, 1.2), (5.25, 7.0, 0.8)):
        s.append(f'<rect x="{tx}" y="{ty+y0*S}" width="{3.4*S}" height="{(y1-y0)*S}" fill="none" stroke="#2f8a4a" stroke-width="2.2" stroke-dasharray="7 4"/>' + T(tx+1.7*S, ty+(y0+y1)/2*S+5, f'+{lv}', 14, '#2f8a4a', 'middle', 'bold'))
    for no, (x0, y0, w, h) in ((5, (7.6, 15.2, 1.2, 0.8)), (6, (0.9, 3.7, 1.3, 0.6)), (7, (0, 11.2, 1, 1))):
        s.append(f'<rect x="{tx+x0*S}" y="{ty+y0*S}" width="{w*S}" height="{h*S}" fill="#fff2c8" stroke="#a8322c" stroke-width="2" stroke-dasharray="6 3"/><circle cx="{tx+(x0+w/2)*S}" cy="{ty+(y0+h/2)*S}" r="11" fill="#fff" stroke="#111"/>' + T(tx+(x0+w/2)*S, ty+(y0+h/2)*S+5, str(no), 13, '#111', 'middle', 'bold'))
    for f in (5.5, 6.5, 8, 9):
        yy = ty+(16-f)*S; s.append(f'<line x1="{tx}" y1="{yy}" x2="{tx+9*S}" y2="{yy}" stroke="#a8322c" stroke-width="1.5" stroke-dasharray="10 5"/>' + T(tx+9*S+8, yy+5, f'f = {f}', 13, '#a8322c'))
    for i in range(10): s.append(T(tx+i*S, ty-3, str(i), 11, '#666', 'middle'))
    for j in range(17): s.append(T(tx-6, ty+j*S+4, str(j), 11, '#666', 'end'))
    s.append(dim_h(tx, tx+9*S, ty+16*S+28, '9 ft (front, public side)')); s.append(dim_v(tx-30, ty, ty+16*S, '16 ft (left side)'))
    s.append(T(tx, ty+16*S+60, 'f = distance from the front edge. Red dashed lines mark where the leg height changes.', 12, '#a8322c'))
    # side profile
    sx, sy = 700, 150; SS = 44; base = sy+3.6*SS
    s.append(T(sx, sy-40, 'SIDE: ramp profile and leg heights (back wall on the left, front on the right)', 15, weight='bold'))
    pts = [(sx+y*SS, base-h*SS) for y, h in RAMP]
    poly = [(sx, base), *[(x, y) for x, y in pts], (sx+16*SS, base)]
    poly = [(sx, base-3.0*SS)] + [(sx+y*SS, base-h*SS) for y, h in sorted(RAMP)] + [(sx+16*SS, base)]
    s.append('<polygon points="%s" fill="#e3c590" stroke="#8a5a12" stroke-width="2"/>' % ' '.join('%.1f,%.1f' % q for q in [(sx, base)] + [(sx+y*SS, base-h*SS) for y, h in sorted(RAMP)] + [(sx+16*SS, base)]))
    s.append(f'<rect x="{sx}" y="{base}" width="{16*SS}" height="{2*SS}" fill="#33333a"/>' + T(sx+8*SS, base+SS+6, 'existing deck 2 ft (black skirting on the front and left)', 14, '#fff', 'middle'))
    for y, h in sorted(RAMP):
        s.append(f'<line x1="{sx+y*SS}" y1="{base}" x2="{sx+y*SS}" y2="{base-max(h,0.05)*SS}" stroke="#8a5a12" stroke-dasharray="3 3"/>' + T(sx+y*SS, base-h*SS-8, f'{h} ft', 14, '#8a5a12', 'middle', 'bold'))
        s.append(T(sx+y*SS, base+2*SS+18, f'f {16-y:g}', 12, '#666', 'middle'))
    s.append(dim_h(sx, sx+16*SS, base+2*SS+44, '16 ft'))
    s.append(dim_v(sx-20, base-3.0*SS, base, '3.0 ft crest'))
    s.append(T(sx, base+2*SS+80, 'Profile for the area right of the left terraces (x 3.4–9 ft). Between the marked points the ramp is a straight line. The rock hill and house sit on this ramp.', 12, '#555'))
    # front elevation
    fx, fy = 700, 560; FS = 44
    s.append(T(fx, fy-14, 'FRONT: width and heights across the back (9 ft wide; left terrace boxes up to +2.0 ft)', 15, weight='bold'))
    s.append(f'<rect x="{fx}" y="{fy+3.2*FS}" width="{9*FS}" height="{2*FS}" fill="#33333a"/>')
    s.append(f'<rect x="{fx+3.4*FS}" y="{fy+0.2*FS}" width="{5.6*FS}" height="{3.0*FS}" fill="#e3c590" stroke="#8a5a12" stroke-width="2"/>')
    for (lv, x0, x1) in ((2.0, 0, 3.4),):
        s.append(f'<rect x="{fx}" y="{fy+(3.2-lv)*FS}" width="{3.4*FS}" height="{lv*FS}" fill="#e8efd8" stroke="#2f8a4a" stroke-width="2.2"/>' + T(fx+1.7*FS, fy+(3.2-lv)*FS-6, 'terraces to +2.0', 13, '#2f8a4a', 'middle', 'bold'))
    s.append(T(fx+6.2*FS, fy+0.2*FS-6, '+3.0 ft back area (right of the terraces)', 13, '#8a5a12', 'middle', 'bold'))
    s.append(dim_h(fx, fx+9*FS, fy+5.2*FS+26, '9 ft'))
    s.append('</svg>')
    return '\n'.join(s), W, H

def chrome():
    for p in ('C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'):
        if os.path.exists(p): return p
def png(svg, w, h, path):
    sp = path[:-4] + '.svg'; open(sp, 'w', encoding='utf8').write(svg)
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--user-data-dir=' + os.path.join(os.environ.get('TEMP', '.'), 'crib_chrome_profile'),
                    f'--window-size={w},{h}', '--force-device-scale-factor=1', f'--screenshot={path}', 'file:///' + sp.replace('\\', '/')], check=True, capture_output=True, timeout=90)
    os.remove(sp)

if __name__ == '__main__':
    svg, w, h = master(); png(svg, w, h, os.path.join(OUT, 'final-blueprint-3-views.png')); print('master')
    for b in 'ABCEFGHIJKL':
        svg, w, h = block_sheet(b); png(svg, w, h, os.path.join(BV, f'{b}-views.png')); print(b)
