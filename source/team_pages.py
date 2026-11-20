"""Per-object dimension drawings and per-team packs for the crew pack.
dims(size) reads the first 'a × b × c' size in an object's text and returns feet; box_svg draws it with its measurements.
team_layout_svg(blocks) draws the 9 × 16 ft stage from above with a 1 ft grid: the team's own objects in colour, numbered, everything else grey."""
import re, html, math
import make_blocks as mb
import make_views as mv

NUM = r'(\d+(?:\.\d+)?|½|¾)'
def _f(s): return {'½': 0.5, '¾': 0.75}.get(s) or float(s)

def dims(size):
    """Return (a, b, c or None) in feet from the first 'a × b [× c]' in the text, or None."""
    m = re.search(NUM + r'\s*(ft|in)?[^×;:.]{0,40}?×\s*' + NUM + r'\s*(ft|in)?(?:[^×;:]{0,40}?×\s*' + NUM + r'\s*(ft|in)?)?', size)
    if not m: return None
    vals = [m.group(1), m.group(3), m.group(5)]; units = [m.group(2), m.group(4), m.group(6)]
    last = next((u for u in reversed(units) if u), 'ft')
    out = []
    for v, u in zip(vals, units):
        if v is None: out.append(None); continue
        x = _f(v); out.append(round(x/12, 2) if (u or last) == 'in' else x)
    return tuple(out)

def ft(x):
    if x is None: return ''
    s = f'{x:.2f}'.rstrip('0').rstrip('.'); return f'{s} ft ({round(x*12)} in)'

def box_svg(d, col):
    """Small isometric box (or flat panel) with labelled sides, 230 × 120 px."""
    a, b, c = d; W, H = 250, 96
    if not c:   # flat piece: a × b
        s = 58 / max(a, b); w, h = a*s, b*s; x0, y0 = 30, 12
        return (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect x="{x0}" y="{y0}" width="{w:.0f}" height="{h:.0f}" fill="{col}" fill-opacity=".35" stroke="#333"/>'
                f'<text x="{x0+w/2:.0f}" y="{y0+h+14:.0f}" font-size="10.5" text-anchor="middle">{html.escape(ft(a))}</text>'
                f'<text x="{x0+w+6:.0f}" y="{y0+h/2+4:.0f}" font-size="10.5">{html.escape(ft(b))}</text></svg>')
    s = 52 / max(a, b, c); ax, bx, cz = max(a*s, 4), max(b*s*0.55, 3), max(c*s, 3)
    x0, y0 = 46, 12 + bx*0.6 + cz
    p = lambda x, y: f'{x:.0f},{y:.0f}'
    A = (x0, y0); B = (x0+ax, y0); Cc = (x0+ax+bx, y0-bx*0.6); Dd = (x0+bx, y0-bx*0.6)
    up = lambda q: (q[0], q[1]-cz)
    face = lambda pts, op: f'<polygon points="{" ".join(p(*q) for q in pts)}" fill="{col}" fill-opacity="{op}" stroke="#333" stroke-width="1"/>'
    svg = (face([A, B, up(B), up(A)], .45) + face([B, Cc, up(Cc), up(B)], .3) + face([up(A), up(B), up(Cc), up(Dd)], .2)
           + f'<text x="{(A[0]+B[0])/2:.0f}" y="{A[1]+13:.0f}" font-size="10.5" text-anchor="middle">W {html.escape(ft(a))}</text>'
           + f'<text x="{(B[0]+Cc[0])/2+6:.0f}" y="{(B[1]+Cc[1])/2+10:.0f}" font-size="10.5">D {html.escape(ft(b))}</text>'
           + f'<text x="{Cc[0]+6:.0f}" y="{(Cc[1]+up(Cc)[1])/2:.0f}" font-size="10.5">H {html.escape(ft(c))}</text>')
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{svg}</svg>'

def team_layout_svg(blocks, scale=34):
    """Top view of the stage, 1 ft grid, x from the left edge, y from the back wall; this team's objects coloured and numbered."""
    S = scale; ox, oy = 46, 30; W = int(ox + 9*S + 300); H = int(oy + 16*S + 40)
    o = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI,Arial">']
    o.append(f'<rect x="{ox}" y="{oy}" width="{9*S}" height="{16*S}" fill="#f4f1e8" stroke="#2b2a33" stroke-width="2"/>')
    for i in range(10): o.append(f'<line x1="{ox+i*S}" y1="{oy}" x2="{ox+i*S}" y2="{oy+16*S}" stroke="#d9d4c6"/><text x="{ox+i*S}" y="{oy-6}" font-size="10" text-anchor="middle">{i}</text>')
    for j in range(17): o.append(f'<line x1="{ox}" y1="{oy+j*S}" x2="{ox+9*S}" y2="{oy+j*S}" stroke="#d9d4c6"/><text x="{ox-6}" y="{oy+j*S+4}" font-size="10" text-anchor="end">{j}</text>')
    o.append(f'<line x1="{ox}" y1="{oy+4.5*S}" x2="{ox+9*S}" y2="{oy+4.5*S}" stroke="#2b2a33" stroke-dasharray="6 4"/><text x="{ox+9*S-4}" y="{oy+4.5*S-4}" font-size="10" text-anchor="end">step +1.5 ft</text>')
    o.append(f'<text x="{ox+4.5*S}" y="{oy+16*S+16}" font-size="11" text-anchor="middle">FRONT (public side, 9 ft) · V is 3 ft left and 3 ft in front of the front-left corner</text>')
    o.append(f'<text x="{ox-30}" y="{oy+8*S}" font-size="11" text-anchor="middle" transform="rotate(-90 {ox-30} {oy+8*S})">LEFT edge (16 ft)</text>')
    skip = {'deck + skirting', 'back-wall drape', 'right-wall drape', 'back-wall print', 'right-wall print', 'selfie mirror'}
    pt = lambda x, y: f'{ox+x*S:.1f},{oy+y*S:.1f}'
    legend = []; n = 0
    for e in mv.E:
        if e['name'] in skip or e['kind'] in ('spiral', 'strands'): continue
        if e['name'] == 'upper layer (second level)' and 'A' not in blocks: continue
        mine = e['b'] in blocks; col = 'rgb(%d,%d,%d)' % mb.COL[e['b']]
        o.append(f'<polygon points="{" ".join(pt(*q) for q in e["poly"])}" fill="{col if mine else "#cfccc4"}" fill-opacity="{.55 if mine else .45}" stroke="{"#222" if mine else "#aaa"}" stroke-width="{1.2 if mine else .6}"/>')
        if mine:
            n += 1; cx = sum(q[0] for q in e['poly'])/len(e['poly']); cy = sum(q[1] for q in e['poly'])/len(e['poly'])
            o.append(f'<circle cx="{ox+cx*S:.1f}" cy="{oy+cy*S:.1f}" r="8" fill="#fff" stroke="#222"/><text x="{ox+cx*S:.1f}" y="{oy+cy*S+3.5:.1f}" font-size="9.5" text-anchor="middle" font-weight="bold">{n}</text>')
            xs = [q[0] for q in e['poly']]; ys = [q[1] for q in e['poly']]
            legend.append(f'{n}. {e["b"]} · {e["name"]}: x {min(xs):.1f}–{max(xs):.1f}, y {min(ys):.1f}–{max(ys):.1f}, {"+" if e["z0"]>=0 else ""}{e["z0"]:.1f} to +{e["z1"]:.1f} ft')
    lx = ox + 9*S + 16
    for i, t in enumerate(legend[:44]):
        o.append(f'<text x="{lx}" y="{oy+10+i*12.2:.0f}" font-size="9.6">{html.escape(t)}</text>')
    o.append('</svg>')
    return '\n'.join(o), legend

def teams():
    """{team label: [blocks]} from make_blocks.TEAMS (M, unassigned, goes with the Stage team as suggested)."""
    out = {}
    for k in mb.ALL:
        t = mb.TEAMS[k]
        lab = 'Stage team: Vk, Samuel' if t.startswith('To be assigned') else t
        lab = lab.split(' (')[0]
        out.setdefault(lab, []).append(k)
    return out
