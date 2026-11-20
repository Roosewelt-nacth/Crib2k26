"""Backdrop banners for block J: back wall 9 ft wide x 7 ft high, right wall 16 ft wide x 7 ft high.
One continuous Bethlehem night scene across the corner (the back banner's right edge meets the right banner's left edge).
Units: 1 SVG unit = 1 inch. Outputs in 2026/banners/:
  back-banner-9x7ft.svg / .pdf / .png and right-banner-16x7ft.svg / .pdf / .png  (print files; the PDF is vector at full size)
  banners-measured.png  (both banners with dimensions and what stands in front of them)
Run: python source/make_banners.py"""
import os, sys, math, random, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_blocks as mb

ROOT = mb.ROOT; OUT = os.path.join(ROOT, '2026', 'banners'); os.makedirs(OUT, exist_ok=True)
H = 84; BW = 108; RW = 192; PW = BW + RW          # inches

def ridge(y0, amps, x0=0, x1=PW, step=3, seed=0):
    """Closed path of a hill range: ridgeline y0 + sum of sines, filled down to the bottom."""
    pts = []
    for x in range(int(x0), int(x1) + step, step):
        y = y0 + sum(a * math.sin(x / w + p) for a, w, p in amps)
        pts.append((x, y))
    d = f'M{x0},{H+2} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts) + f' L{x1},{H+2} Z'
    return d

def palm(x, base, h, col):
    top = base - h; s = h / 60
    trunk = f'<path d="M{x-1.2*s},{base} Q{x+3*s},{base-h*0.5} {x+1.5*s},{top} L{x+3.3*s},{top} Q{x+5*s},{base-h*0.5} {x+1.2*s},{base} Z" fill="{col}"/>'
    fr = ''
    for ang in (-150, -120, -95, -70, -40, -10, 15, 200):
        a = math.radians(ang); L = 16 * s
        ex, ey = x + 2.4*s + L*math.cos(a), top + L*math.sin(a) + 6*s
        cx, cy = x + 2.4*s + L*0.55*math.cos(a), top + L*0.55*math.sin(a) - 4*s
        fr += f'<path d="M{x+2.4*s},{top} Q{cx:.1f},{cy:.1f} {ex:.1f},{ey:.1f} Q{cx:.1f},{cy+3*s:.1f} {x+2.4*s},{top+1.5*s} Z" fill="{col}"/>'
    return trunk + fr

def olive(x, base, r, col):
    t = f'<path d="M{x-0.8},{base} Q{x+0.6},{base-r} {x},{base-r*1.3} L{x+1.2},{base-r*1.3} Q{x+1.8},{base-r} {x+0.8},{base} Z" fill="{col}"/>'
    blobs = ''.join(f'<ellipse cx="{x+dx:.1f}" cy="{base-r*1.6+dy:.1f}" rx="{r*0.55:.1f}" ry="{r*0.38:.1f}" fill="{col}"/>' for dx, dy in ((-r*0.5, 0), (r*0.5, 0.3), (0, -r*0.35), (r*0.15, r*0.25)))
    return t + blobs

def town(x0, w, rf, col, shade, lit):
    """Houses climbing a hill: each one stands on the ridge line rf(x)."""
    rnd = random.Random(7); s = ''; x = x0
    while x < x0 + w:
        bw = rnd.uniform(1.4, 2.8); bh = rnd.uniform(1.2, 3.0) * (1.25 - abs((x - x0) / w - 0.5)); base = rf(x + bw/2) + 0.6
        y = base - bh
        s += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh+1.2:.1f}" fill="{col}"/><rect x="{x+bw*0.7:.1f}" y="{y:.1f}" width="{bw*0.3:.1f}" height="{bh+1.2:.1f}" fill="{shade}"/>'
        if rnd.random() < 0.5: s += f'<rect x="{x+bw*0.3:.1f}" y="{y+bh*0.35:.1f}" width="0.4" height="0.5" fill="{lit}"/>'
        if rnd.random() < 0.1: s += f'<ellipse cx="{x+bw/2:.1f}" cy="{y:.1f}" rx="{bw*0.32:.1f}" ry="{bw*0.28:.1f}" fill="{col}"/>'
        x += bw * rnd.uniform(0.7, 0.95)
    return s

def scene(photo=False, rf_photo=None):
    rnd = random.Random(2026)
    o = ['<defs>'
         '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#141f4d"/><stop offset=".38" stop-color="#1F2F66"/>'
         '<stop offset=".62" stop-color="#3b3a7e"/><stop offset=".78" stop-color="#5B4A9A"/><stop offset=".9" stop-color="#8a78b4"/><stop offset="1" stop-color="#AEBBD9"/></linearGradient>'
         '<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF1CF" stop-opacity=".55"/><stop offset=".35" stop-color="#F2B84B" stop-opacity=".18"/><stop offset="1" stop-color="#F2B84B" stop-opacity="0"/></radialGradient>'
         '</defs>']
    if not photo: o.append(f'<rect x="0" y="0" width="{PW}" height="{H}" fill="url(#sky)"/>')
    # the real star hangs at x 7.8 ft on the back wall: a soft glow behind it
    o.append(f'<ellipse cx="94" cy="8" rx="26" ry="20" fill="url(#glow)"/>')
    for _ in range(0 if photo else 420):
        x = rnd.uniform(0, PW); y = rnd.uniform(0, 46) ** 1.08
        r = rnd.choice((0.18, 0.22, 0.28, 0.35, 0.5)); c = '#F2B84B' if rnd.random() < 0.12 else '#FFF1CF'
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" opacity="{rnd.uniform(.45, .95):.2f}"/>')
    # hill ranges, far to near
    if not photo: o.append(f'<path d="{ridge(44, [(3.5, 23, 0.4), (2.2, 9, 1.3), (1.0, 4, 0.2)])}" fill="#AEBBD9" opacity=".55"/>')
    amps = [(4.5, 31, 2.0), (2.0, 11, 0.7), (0.8, 5, 1.9)]
    if not photo: o.append(f'<path d="{ridge(49, amps)}" fill="#7d72ad"/>')
    # Bethlehem on the far hill of the right banner (wall y 1-5 ft from the back corner), seated on the ridge
    rf = rf_photo or (lambda x: 49 + sum(a * math.sin(x / w + p) for a, w, p in amps))
    o.append(town(BW + 128, 44, rf, '#6f6688', '#524a6c', '#F2B84B') if photo else town(BW + 10, 46, rf, '#c8bedb', '#9d93bf', '#F2B84B'))
    if not photo: o.append(f'<path d="{ridge(56, [(4.0, 19, 0.9), (2.4, 8, 2.6), (0.9, 3.5, 0.4)])}" fill="#5B4A9A"/>')
    C1, C2, C3 = ('#2f2836', '#2b2733', '#3a3326') if photo else ('#463f7a', '#4d4a5e', '#5c5641')
    o.append(f'<path d="{ridge(63, [(3.2, 27, 1.7), (1.6, 7, 0.3)])}" fill="{C1}" opacity="{.72 if photo else 1}"/>')
    # near terraces: dusk-darkened olive and sand
    o.append(f'<path d="{ridge(70, [(2.6, 22, 0.2), (1.2, 6, 1.1)])}" fill="{C2}" opacity="{.72 if photo else 1}"/>')
    o.append(f'<path d="{ridge(76, [(2.0, 17, 2.4), (1.0, 5, 0.6)])}" fill="{C3}" opacity="{.72 if photo else 1}"/>')
    for k in range(0, PW, 6):
        y = 72 + 2.0*math.sin(k/22 + 0.2)
        if rnd.random() < 0.55: o.append(olive(k + rnd.uniform(0, 4), y + rnd.uniform(1, 4), rnd.uniform(1.6, 2.6), '#24281d' if photo else '#3c4230'))
    # palms (painted, replacing the plywood cut-outs): two on the back banner, one on the right banner
    for x, h in ((14, 52), (36, 46), (BW + 156, 56)):
        o.append(palm(x, 80, h, '#141a3a'))
    return '\n'.join(o)

def svg_for(x0, w, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}in" height="{H}in" viewBox="{x0} 0 {w} {H}">'
            f'<clipPath id="c"><rect x="{x0}" y="0" width="{w}" height="{H}"/></clipPath><g clip-path="url(#c)">{inner}</g></svg>')

def chrome(): return mb.chrome()

def shot(svg_text, wpx, hpx, path):
    sp = path[:-4] + '.tmp.html'
    open(sp, 'w', encoding='utf8').write(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#fff}}svg{{display:block;width:{wpx}px;height:{hpx}px}}</style>{svg_text}')
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--user-data-dir=' + os.path.join(os.environ.get('TEMP', '.'), 'crib_chrome_profile'),
                    f'--window-size={wpx},{hpx}', '--force-device-scale-factor=1', f'--screenshot={path}', 'file:///' + sp.replace('\\', '/')], check=True, capture_output=True, timeout=120)
    os.remove(sp)

def to_pdf(svg_text, w_in, path):
    hp = path[:-4] + '.tmp.html'
    open(hp, 'w', encoding='utf8').write(f'<!doctype html><style>@page{{size:{w_in}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block}}</style>{svg_text}')
    mb.pdf(hp, path); os.remove(hp)

def measured(inner):
    """Both banners side by side (as unfolded from the corner) with sizes and what stands in front of them."""
    S = 5.0; pad = 60; Wpx = int(PW*S + 2*pad + 30); Hpx = int(H*S + 300)
    X = lambda x: pad + x*S + (30 if x >= BW else 0); Y = lambda y: 90 + y*S
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wpx}" height="{Hpx}" viewBox="0 0 {Wpx} {Hpx}" font-family="Segoe UI,Arial">',
         f'<rect width="{Wpx}" height="{Hpx}" fill="#faf8f2"/>',
         f'<text x="{pad}" y="34" font-size="22" font-weight="bold" fill="#2b2a33">Block J backdrop banners: one night scene across the corner (feet; drawn as if the corner were unfolded)</text>',
         f'<text x="{pad}" y="60" font-size="14" fill="#555">Print on matt flex or fabric. Bottom edge sits on the stage deck. Above the banners, from 7 ft up to the ceiling (about 13 ft above the deck), hangs the blue drape with gold stars.</text>']
    for x0, w, lab in ((0, BW, 'BACK WALL BANNER · 9 ft wide × 7 ft high (108 × 84 in)'), (BW, RW, 'RIGHT WALL BANNER · 16 ft wide × 7 ft high (192 × 84 in)')):
        o.append(f'<svg x="{X(x0)}" y="{Y(0)}" width="{w*S}" height="{H*S}" viewBox="{x0} 0 {w} {H}" preserveAspectRatio="none"><g>{inner}</g></svg>')
        o.append(f'<rect x="{X(x0)}" y="{Y(0)}" width="{w*S}" height="{H*S}" fill="none" stroke="#2b2a33" stroke-width="2"/>')
        o.append(f'<text x="{X(x0)+w*S/2}" y="{Y(H)+70}" font-size="16" font-weight="bold" text-anchor="middle" fill="#2b2a33">{lab}</text>')
        # width dimension
        yy = Y(H) + 40
        o.append(f'<line x1="{X(x0)}" y1="{yy}" x2="{X(x0+w)}" y2="{yy}" stroke="#444" stroke-width="1.5"/><line x1="{X(x0)}" y1="{yy-8}" x2="{X(x0)}" y2="{yy+8}" stroke="#444"/><line x1="{X(x0+w)}" y1="{yy-8}" x2="{X(x0+w)}" y2="{yy+8}" stroke="#444"/>')
        o.append(f'<text x="{X(x0)+w*S/2}" y="{yy-6}" font-size="14" text-anchor="middle">{w//12} ft ({w} in)</text>')
        for f in range(0, w//12 + 1):
            o.append(f'<line x1="{X(x0+f*12)}" y1="{Y(H)}" x2="{X(x0+f*12)}" y2="{Y(H)+10}" stroke="#444"/><text x="{X(x0+f*12)}" y="{Y(H)+24}" font-size="11" text-anchor="middle">{f}</text>')
    # height dimension
    o.append(f'<line x1="{pad-20}" y1="{Y(0)}" x2="{pad-20}" y2="{Y(H)}" stroke="#444" stroke-width="1.5"/>')
    for f in range(0, 8):
        o.append(f'<line x1="{pad-26}" y1="{Y(H-f*12)}" x2="{pad-14}" y2="{Y(H-f*12)}" stroke="#444"/><text x="{pad-30}" y="{Y(H-f*12)+4}" font-size="11" text-anchor="end">{f}</text>')
    o.append(f'<text x="{pad-44}" y="{Y(H/2)}" font-size="13" text-anchor="middle" transform="rotate(-90 {pad-44} {Y(H/2)})">7 ft (84 in) high, from the deck</text>')
    # what stands in front (dashed outlines)
    def zone(x0, x1, h, txt, col='#c0392b'):
        o.append(f'<rect x="{X(x0)}" y="{Y(H-h)}" width="{(x1-x0)*S}" height="{h*S}" fill="{col}" fill-opacity=".10" stroke="{col}" stroke-dasharray="7 5" stroke-width="2"/>')
        o.append(f'<text x="{X(x0)+6}" y="{Y(H-h)+16}" font-size="12" fill="{col}" font-weight="bold">{txt}</text>')
    zone(0, BW, 18, 'raised level 1.5 ft: bottom 18 in hidden')
    zone(BW, BW+54, 18, 'raised level 1.5 ft (first 4.5 ft)')
    zone(BW+62, BW+108, 36, 'far-village ridge 3 ft (K)', '#8e44ad')
    o.append(f'<rect x="{X(BW+65)}" y="{Y(H-47)}" width="{36*S}" height="{4*S}" fill="#8e44ad" fill-opacity=".35" stroke="#8e44ad" stroke-width="2"/>')
    o.append(f'<text x="{X(BW+65)+4}" y="{Y(H-47)-6}" font-size="11" fill="#8e44ad" font-weight="bold">Magi shelf, 3 ft long, at 3.6 ft</text>')
    zone(BW+110, BW+192, 42, 'five houses up to 3.5 ft (G)', '#1f6fb2')
    o.append(f'<text x="{X(94/1)}" y="{Y(4)}" font-size="12" fill="#b07d10" text-anchor="middle">real star hangs here (in front)</text>')
    o.append(f'<text x="{X(BW)-15}" y="{Y(0)-8}" font-size="12" text-anchor="middle" fill="#2b2a33">corner</text>')
    o.append('</svg>')
    return '\n'.join(o), Wpx, Hpx

PPI = 100
ZOOM_X0 = 2370
PHOTO = os.path.join(OUT, 'source', 'pexels-photo-9181823.jpeg')

def photo_base():
    """Panorama 300 x 84 in at PPI from the starry-desert photo: scaled 1.3x, ridge at about 4 ft above the deck, mirrored copies across the width, graded to the crib palette."""
    from PIL import Image, ImageOps, ImageEnhance
    W, Hh = PW*PPI, H*PPI
    ph = Image.open(PHOTO).convert('RGB'); s = 1.3 * Hh / 3360
    ph = ph.resize((int(ph.width*s), int(ph.height*s)), Image.LANCZOS)
    top = int(3070*s - 0.52*Hh)
    pano = Image.new('RGB', (W, Hh), (21, 31, 77))
    band = ph.crop((0, max(top, 0), ph.width, min(top+Hh, ph.height)))
    right = band.resize((RW*PPI, band.height), Image.LANCZOS)           # one photo across the 16 ft banner
    pano.paste(right, (BW*PPI, max(-top, 0)))
    pano.paste(ImageOps.mirror(right.crop((0, 0, BW*PPI, band.height))), (0, max(-top, 0)))   # its mirror on the 9 ft banner: the fold is the wall corner
    # grade: cool the sky, turn the warm sand into dusk violet-brown, darken slightly
    r, g, b = pano.split()
    r = r.point(lambda v: int(v*0.72)); g = g.point(lambda v: int(v*0.70)); b = b.point(lambda v: min(255, int(v*1.05+18)))
    pano = Image.merge('RGB', (r, g, b)); pano = ImageEnhance.Contrast(pano).enhance(1.08)
    return pano

def plain_photo():
    """The photo alone, zoomed in so the hills fill the lower 60% (hilltops about 4 ft up), upscaled to PPI with light sharpening.
    One copy across the 16 ft banner, its mirror on the 9 ft banner so the hills meet at the corner."""
    from PIL import Image, ImageOps, ImageFilter
    ph = Image.open(PHOTO).convert('RGB'); Hh = H*PPI
    ridge, x0 = 2950, ZOOM_X0                           # hilltop row in the photo; left edge of the zoomed window
    rows = int((ph.height - ridge) / 0.6); cols = int(rows * RW / H)
    band = ph.crop((x0, ph.height - rows, x0 + cols, ph.height)).resize((RW*PPI, Hh), Image.LANCZOS)
    band = band.filter(ImageFilter.UnsharpMask(radius=3, percent=60, threshold=2))
    pano = Image.new('RGB', (PW*PPI, Hh)); pano.paste(band, (BW*PPI, 0))
    pano.paste(ImageOps.mirror(band.crop((0, 0, BW*PPI, Hh))), (0, 0)); return pano

def ridge_of(img):
    """Skyline of the photo hills, in inches from the top, one value per inch across: first warm (sand) pixel below the sky."""
    sm = img.resize((PW, H)).load(); out = []
    for x in range(PW):
        y = next((y for y in range(10, H) if sm[x, y][0] > sm[x, y][2] - 18), H - 10); out.append(y)
    return [sum(out[max(0, i-3):i+4]) / len(out[max(0, i-3):i+4]) for i in range(PW)]

def build_photo(inner_overlay, base):
    from PIL import Image
    W, Hh = base.size
    ov = os.path.join(OUT, 'overlay.png'); sp = ov[:-4] + '.html'
    open(sp, 'w', encoding='utf8').write(f'<!doctype html><style>html,body{{margin:0;background:transparent}}svg{{display:block}}</style><svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" viewBox="0 0 {PW} {H}">{inner_overlay}</svg>')
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--default-background-color=00000000', '--user-data-dir=' + os.path.join(os.environ.get('TEMP', '.'), 'crib_chrome_profile'),
                    f'--window-size={W},{Hh}', '--force-device-scale-factor=1', f'--screenshot={ov}', 'file:///' + sp.replace(os.sep, '/')], check=True, capture_output=True, timeout=300)
    os.remove(sp); top = Image.open(ov).convert('RGBA'); os.remove(ov)
    base = base.convert('RGBA'); base.alpha_composite(top); return base.convert('RGB')

if __name__ == '__main__' and os.path.exists(PHOTO):
    from PIL import Image
    pano = plain_photo(); W, Hh = pano.size     # the photo alone: no tint, no painted extras (owner's choice, 20 Nov)
    for name, x0, w in (('back-banner-9x7ft', 0, BW), ('right-banner-16x7ft', BW, RW)):
        im = pano.crop((x0*PPI, 0, (x0+w)*PPI, Hh))
        im.save(os.path.join(OUT, name + '.jpg'), quality=92, dpi=(PPI, PPI))
        im.save(os.path.join(OUT, name + '.pdf'), resolution=PPI)
        im.resize((w*12, H*12), Image.LANCZOS).save(os.path.join(OUT, name + '.png')); print(name, im.size)
    for n in ('back-banner-9x7ft.svg', 'right-banner-16x7ft.svg'):
        p = os.path.join(OUT, n)
        if os.path.exists(p): os.remove(p)
    pano.resize((PW*5, H*5), Image.LANCZOS).save(os.path.join(OUT, 'pano-preview.png'))
    import base64
    b64 = base64.b64encode(open(os.path.join(OUT, 'pano-preview.png'), 'rb').read()).decode()
    m, wpx, hpx = measured(f'<image href="data:image/png;base64,{b64}" x="0" y="0" width="{PW}" height="{H}" preserveAspectRatio="none"/>')
    shot(m, wpx, hpx, os.path.join(OUT, 'banners-measured.png')); os.remove(os.path.join(OUT, 'pano-preview.png')); print('measured')
elif __name__ == '__main__':
    inner = scene()
    for name, x0, w in (('back-banner-9x7ft', 0, BW), ('right-banner-16x7ft', BW, RW)):
        s = svg_for(x0, w, inner)
        open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf8').write(s)
        shot(s.replace(f'width="{w}in" height="{H}in"', f'width="{w*12}" height="{H*12}"'), w*12, H*12, os.path.join(OUT, name + '.png'))
        to_pdf(s, w, os.path.join(OUT, name + '.pdf')); print(name)
    m, wpx, hpx = measured(inner)
    shot(m, wpx, hpx, os.path.join(OUT, 'banners-measured.png')); print('measured')
