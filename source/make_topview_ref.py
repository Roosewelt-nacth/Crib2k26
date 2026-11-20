"""Top-view reference of the complete crib (two-layer stage, 9 ft wide x 16 ft long) with every block placed.
Run: python source/make_topview_ref.py -> 2026/images/top-view-reference.png (needs make_views.py and Chrome)"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_views as mv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '2026', 'images', 'top-view-reference.png')
INK = '#2b2a33'

def T(x, y, t, size=20, fill=INK, anchor='start', weight='700', rot=None):
    r = f' transform="rotate({rot} {x:.0f} {y:.0f})"' if rot is not None else ''
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="Segoe UI,Arial" font-size="{size}" font-weight="{weight}" fill="{fill}" stroke="#fff" stroke-width="4" paint-order="stroke" text-anchor="{anchor}"{r}>{t}</text>'

DESC = [('A', 'The plywood stage floor itself: flat front 11.5 ft, step, raised back 4.5 ft (1.5 ft high); lids A, B, C'),
        ('B', 'Rock hill with the cave (mouth faces the front-left) and the guest-room house on top'),
        ('C', '(part of B in the picture) house with flat roof, cat on the roof'),
        ('E', "Shepherds' field: terrace wall, tent, 3 shepherds, 14 sheep, campfire, fig tree; sheepfold and watchtower at the back"),
        ('F', 'Pipe-cleaner angel choir above the sheepfold'),
        ('G', 'Narrowing street, 5 flat-roofed houses stepping down, well, census table, donkeys, stall, palm'),
        ('H', 'Path of light (thin gold line) from the front edge to the cave mouth'),
        ('I', 'Star burst (back-right corner), cloud spiral and gold rays to the cave'),
        ('J', 'Backdrop: banners 9 × 7 ft (back) and 16 × 7 ft (right), drape above'),
        ('K', 'Far village on a rock ridge and the Magi shelf along the right wall'),
        ('L', 'Two olive trees and the plaque'),
        ('N', 'Front rocks, pond set into the field, shepherd boy, front wall')]

def svg():
    S = 56; W, H = 1700, 1080; px, py = 110, 120
    vw = mv.View('top', S, px, py, (0, 9, 0, 16))
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{mv.DEFS}<rect width="{W}" height="{H}" fill="#f6f4ee"/>']
    s.append(T(30, 42, 'TOP VIEW of the complete crib: stage 9 ft WIDE × 16 ft LONG (back wall at the top, public at the bottom)', 28))
    s.append(f'<rect x="{px}" y="{py-12}" width="{9*S}" height="12" fill="url(#hatch)" stroke="{INK}"/><rect x="{px+9*S}" y="{py-12}" width="12" height="{16*S+12}" fill="url(#hatch)" stroke="{INK}"/>')
    s.append(f'<rect x="{px}" y="{py}" width="{9*S}" height="{16*S}" fill="#ead2a0" stroke="{INK}" stroke-width="2"/>')
    s.append(f'<rect x="{px}" y="{py}" width="{9*S}" height="{4.5*S}" fill="#d3b273" stroke="#6b5a36" stroke-width="2"/>')
    els = [e for e in mv.E if not e.get('dark') and e['name'] != 'selfie mirror' and e['name'] != 'upper layer (second level)' and e['kind'] not in ('strands',) and not e.get('drape') and not e['name'].endswith('print')]
    s.append(mv.draw_view(vw, els, lambda e: '#fff2c8' if e.get('gold') else mv.light(mv.COL[e['b']]), lambda e: mv.dark(mv.COL[e['b']])))
    x1, y1 = vw.pt(0, 4.5); x2, _ = vw.pt(9, 4.5)
    s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y1:.0f}" stroke="#6b5a36" stroke-width="5" stroke-dasharray="14 6"/>')
    s.append(f'<line x1="{px-4}" y1="{py+16*S}" x2="{px+9*S}" y2="{py+16*S}" stroke="#111" stroke-width="9"/><line x1="{px-4}" y1="{py}" x2="{px-4}" y2="{py+16*S}" stroke="#111" stroke-width="9"/>')
    # letters
    for b in 'BEFGHIJKLM':
        sel = [e for e in els if e['b'] == b and e['kind'] not in ('spiral', 'flat')]
        pts = []
        for e in sel:
            xs = [q[0] for q in e['poly']]; ys = [q[1] for q in e['poly']]; pts.append(((min(xs)+max(xs))/2, (min(ys)+max(ys))/2))
        if b == 'H': pts = [(2.9, 11.2)]
        if b == 'I': pts = [mv.HANG]
        if b == 'J': pts = [(4.5, 0.15)]
        if b == 'A': pts = [(4.5, 13.0)]
        if not pts: continue
        cx = sum(p[0] for p in pts)/len(pts); cy = sum(p[1] for p in pts)/len(pts)
        if b == 'B': cx, cy = mv.C
        X, Y = vw.pt(cx, cy); s.append(T(X, Y+9, b, 30, INK, 'middle'))
    for nm, (x, y, w, h) in (('A', (0, 0.2, 1.2, 0.8)), ('C', (0, 15, 1, 1))):
        X, Y = vw.pt(x, y); s.append(f'<rect x="{X:.0f}" y="{Y:.0f}" width="{w*S:.0f}" height="{h*S:.0f}" fill="none" stroke="#006e66" stroke-width="2.5" stroke-dasharray="6 3"/>')
    ax, ay = vw.pt(9, 16)
    s.append(f'<line x1="{px}" y1="{py+16*S+34}" x2="{px+9*S}" y2="{py+16*S+34}" stroke="#a8322c" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(px+4.5*S, py+16*S+28, '9 ft wide', 22, '#a8322c', 'middle'))
    s.append(f'<line x1="{px-60}" y1="{py}" x2="{px-60}" y2="{py+16*S}" stroke="#a8322c" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>' + T(px-72, py+8*S, '16 ft long', 22, '#a8322c', 'middle', rot=-90))
    lx = 760
    s.append(T(lx, 130, 'WHAT EACH BLOCK IS (seen from above)', 22))
    for i, (k, t) in enumerate(DESC):
        y = 172 + i*34
        c = mv.COL.get(k, (120, 120, 120))
        s.append(f'<rect x="{lx}" y="{y-18}" width="26" height="22" fill="{mv.light(c)}" stroke="{mv.dark(c)}" stroke-width="2"/>' + T(lx+38, y, f'{k}  {t}', 17, INK, weight='400'))
    s.append(T(lx, 172+len(DESC)*34+20, 'Pale boxes = props seen from above. Gold line = path of light. Dashed brown line = the step.', 16, '#555', weight='400'))
    s.append('</svg>')
    return '\n'.join(s), W, H

if __name__ == '__main__':
    svg_, w, h = svg(); mv.png(svg_, w, h, OUT); print('ok')
