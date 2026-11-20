"""Layout checks for the final plan: footprint overlaps, things standing on the hill or the path, and sightlines from the public spot V.
Run: python source/check_layout.py  (prints problems; silent lines mean OK)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_views as mv
from PIL import Image, ImageDraw, ImageChops

IGN = {'deck + skirting', 'upper layer (second level)', 'rock hill', 'path of light'}
OK_PAIRS = {('cave', 'Holy Family'), ('olive tree (front left)', 'rock outcrop')}

def mask(poly):
    im = Image.new('1', (900, 1600), 0); ImageDraw.Draw(im).polygon([(x*100, y*100) for x, y in poly], fill=1); return im

def inside(poly, x, y):
    n = len(poly); c = False
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i+1) % n]
        if (y1 > y) != (y2 > y) and x < (x2-x1)*(y-y1)/(y2-y1)+x1: c = not c
    return c

def main():
    els = [e for e in mv.E if e['name'] not in IGN and e['b'] not in 'JI' and 0 <= e['z0'] < 1.6]
    ms = [(e, mask(e['poly'])) for e in els]; bad = 0
    for i in range(len(ms)):
        for j in range(i+1, len(ms)):
            a, b = ms[i][0], ms[j][0]
            if (a['name'], b['name']) in OK_PAIRS or (b['name'], a['name']) in OK_PAIRS: continue
            if a['z1'] <= b['z0'] or b['z1'] <= a['z0']: continue
            o = ImageChops.logical_and(ms[i][1], ms[j][1]).getbbox()
            if o: print('OVERLAP', a['b'], a['name'], '|', b['b'], b['name'], [v/100 for v in o]); bad += 1
    hill = mask([e for e in mv.E if e['name'] == 'rock hill'][0]['poly'])
    for e, m in ms:
        if e['b'] in 'EGLMN' and ImageChops.logical_and(hill, m).getbbox(): print('ON HILL', e['b'], e['name']); bad += 1
    # sightlines from the eye at V to the things that must be seen
    eye = (mv.V[0], mv.V[1], mv.EYE)
    targets = {'baby in the manger': (4.3, 7.6, 1.0), 'Magi caravan': (8.85, 6.9, 3.8), 'far village': (8.2, 7.0, 3.2), 'campfire': (1.07, 8.37, 0.3),
               'angel choir': (1.6, 2.4, 3.5), 'house 3 front': (7.55, 11.6, 1.5), 'census table': (5.1, 12.9, 0.8), 'well': (5.6, 11.2, 0.6)}
    solids = [e for e in mv.E if e['kind'] in ('box', 'cave', 'tree') and e['name'] not in IGN and not e.get('hidden') and e['b'] not in 'J']
    for nm, tp in targets.items():
        for k in range(1, 100):
            s = k/100; x, y, z = (eye[i] + (tp[i]-eye[i])*s for i in range(3))
            for e in solids:
                if e['name'] in ('Holy Family', 'cave') and nm == 'baby in the manger': continue
                if e['z0'] <= z <= e['z1'] and inside(e['poly'], x, y) and not inside(e['poly'], tp[0], tp[1]):
                    print('BLOCKED', nm, 'by', e['b'], e['name'], f'at x {x:.1f}, y {y:.1f}, z {z:.1f}'); bad += 1; break
            else: continue
            break
    print('checks done,', bad, 'problems')

if __name__ == '__main__': main()
