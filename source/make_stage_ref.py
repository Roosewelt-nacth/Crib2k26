"""Bare-stage reference for the team: plan view (9 ft wide x 16 ft long) + an elevated 3/4 view where the long side reads long.
Run: python source/make_stage_ref.py -> 2026/images/stage-only-reference.png (needs make_views.py and Chrome)"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_views as mv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '2026', 'images', 'stage-only-reference.png')
INK = '#2b2a33'; RED = '#a8322c'; TEAL = '#006e66'; BROWN = '#6b5a36'

def T(x, y, t, size=20, fill=INK, anchor='start', weight='700', rot=None):
    r = f' transform="rotate({rot} {x:.0f} {y:.0f})"' if rot is not None else ''
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="Segoe UI,Arial" font-size="{size}" font-weight="{weight}" fill="{fill}" stroke="#fff" stroke-width="4" paint-order="stroke" text-anchor="{anchor}"{r}>{t}</text>'

def svg():
    W, H = 1700, 1000
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{mv.DEFS}<rect width="{W}" height="{H}" fill="#f6f4ee"/>']
    s.append(T(30, 44, 'BARE STAGE reference (no props): 9 ft WIDE × 16 ft LONG, almost twice as long as it is wide', 30))
    s.append(T(30, 76, 'Front (public side) = the SHORT 9 ft side. Left side = the LONG 16 ft side. Back and right sides touch the church walls.', 19, '#444', weight='400'))
    # ---- plan (left)
    S = 48; px, py = 130, 150
    s.append(T(px-100, py-50, 'PLAN (looking down)', 20))
    s.append(f'<rect x="{px}" y="{py-14}" width="{9*S}" height="14" fill="url(#hatch)" stroke="{INK}"/><rect x="{px+9*S}" y="{py-14}" width="14" height="{16*S+14}" fill="url(#hatch)" stroke="{INK}"/>')
    s.append(f'<rect x="{px}" y="{py}" width="{9*S}" height="{16*S}" fill="#e8cf9d" stroke="{INK}" stroke-width="2"/>')
    s.append(f'<rect x="{px}" y="{py}" width="{9*S}" height="{4.5*S}" fill="#cfa96a" stroke="{BROWN}" stroke-width="2"/>')
    s.append(f'<line x1="{px}" y1="{py+4.5*S}" x2="{px+9*S}" y2="{py+4.5*S}" stroke="{BROWN}" stroke-width="5" stroke-dasharray="14 6"/>')
    s.append(f'<line x1="{px-4}" y1="{py+16*S}" x2="{px+9*S}" y2="{py+16*S}" stroke="#111" stroke-width="9"/><line x1="{px-4}" y1="{py}" x2="{px-4}" y2="{py+16*S}" stroke="#111" stroke-width="9"/>')
    s.append(T(px+4.5*S, py+2.3*S, 'BACK 4.5 ft', 22, BROWN, 'middle')); s.append(T(px+4.5*S, py+2.3*S+24, 'raised 1.5 ft', 20, BROWN, 'middle'))
    s.append(T(px+4.5*S, py+4.5*S+26, 'STEP, 1.5 ft high, full width', 17, BROWN, 'middle'))
    s.append(T(px+4.5*S, py+10.5*S, 'FRONT 11.5 ft', 22, INK, 'middle')); s.append(T(px+4.5*S, py+10.5*S+24, 'flat, deck height', 20, INK, 'middle'))
    for nm, (x, y, w, h) in (('A', (0, 0.2, 1.2, 0.8)), ('C', (0, 15, 1, 1))):
        s.append(f'<rect x="{px+x*S}" y="{py+y*S}" width="{w*S}" height="{h*S}" fill="#fff2c8" stroke="{TEAL}" stroke-width="2.5" stroke-dasharray="6 3"/>' + T(px+(x+w/2)*S, py+(y+h/2)*S+7, nm, 18, TEAL, 'middle'))
    bx, by = px+1.5*S, py+4.0*S
    s.append(f'<rect x="{bx-10}" y="{by-10}" width="20" height="20" fill="#fff2c8" stroke="{TEAL}" stroke-width="2.5" stroke-dasharray="6 3"/>' + T(bx, by+6, 'B', 16, TEAL, 'middle'))
    s.append(T(px+9*S/2, py-22, 'BACK WALL (church) 9 ft', 17, INK, 'middle')); s.append(T(px+9*S+44, py+8*S, 'RIGHT WALL (church) 16 ft', 17, INK, 'middle', rot=90))
    s.append(T(px+4.5*S, py+16*S+62, 'FRONT, black skirting (public side)', 17, '#111', 'middle'))
    s.append(T(px-30, py+8*S, 'LEFT, black skirting', 17, '#111', 'middle', rot=-90))
    s.append(f'<line x1="{px}" y1="{py+16*S+30}" x2="{px+9*S}" y2="{py+16*S+30}" stroke="{RED}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(px+4.5*S, py+16*S+24, '9 ft = WIDTH', 24, RED, 'middle'))
    s.append(f'<line x1="{px-70}" y1="{py}" x2="{px-70}" y2="{py+16*S}" stroke="{RED}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(px-82, py+8*S, '16 ft = LENGTH', 24, RED, 'middle', rot=-90))
    # ---- elevated 3/4 view (right)
    ox, oy, PW, PH = 700, 110, 960, 850
    s.append(T(ox, oy-12, 'THREE-QUARTER VIEW from the front-left, about 28 ft away and 14 ft up (the 16 ft length is fully visible)', 18))
    s.append(f'<rect x="{ox}" y="{oy}" width="{PW}" height="{PH}" fill="#fbfaf6" stroke="{INK}"/>')
    keep = ('deck + skirting', 'upper layer (second level)', 'back-wall print', 'right-wall print', 'back-wall drape', 'right-wall drape')
    elems = [e for e in mv.E if e['name'] in keep]
    def fill(e):
        if e.get('dark'): return '#4a4a54'
        if e['name'].startswith('upper'): return '#cfa96a'
        return '#e4e2da'
    cam = (-14.0, 30.0, 16.0); yaw = math.atan2(18.5, 22.0); hfov = math.radians(38)
    s.append(mv.persp_panel(elems, fill, lambda e: '#6a6a72', W=PW, H=PH, letters=False, x0=ox, y0=oy, cam=cam, yaw=yaw, hfov=hfov, vshift=-640))
    F = PW/2/math.tan(hfov/2); fx, fy = math.sin(yaw), -math.cos(yaw); rx, ry = math.cos(yaw), math.sin(yaw)
    def pr(x, y, z):
        dx, dy, dz = x-cam[0], y-cam[1], (z+2.0)-cam[2]
        fw = max(dx*fx+dy*fy, 0.3); rt = dx*rx+dy*ry
        return (ox+PW/2+F*rt/fw, oy+PH/2-F*dz/fw+PH*0.04-640)
    def lab(x, y, z, t, col=RED, size=22, dx=0, dy=0, anchor='middle'):
        X, Y = pr(x, y, z); return T(X+dx, Y+dy, t, size, col, anchor)
    s.append(lab(4.5, 10.5, 0, 'FRONT 11.5 ft flat', INK))
    s.append(lab(4.5, 2.3, 1.5, 'BACK 4.5 ft, raised 1.5 ft', BROWN, dy=-6))
    s.append(lab(4.5, 16, -1.0, '9 ft wide (short)', RED, dy=34))
    s.append(lab(0, 8, -1.0, '16 ft long', RED, dx=-70, dy=50))
    s.append('</svg>')
    return '\n'.join(s), W, H

if __name__ == '__main__':
    svg_, w, h = svg(); mv.png(svg_, w, h, OUT); print('ok')
