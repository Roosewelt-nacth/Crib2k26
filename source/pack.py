import sys, html
import drawings_fix as DR
from church import church_svg

E = html.escape
MODS = [
 dict(id="0", name="Raked base frame + skirting", covers="all items stand on it (new sheet, not in 1–30)", zone="whole stage",
  days=6, when=(4, 24), fn="m0", lines=[
   ("Pine/casuarina battens 2 × 2 in", "~160 ft", 3500, 5000), ("Plywood 9–12 mm, 8 × 4 ft", "5 sheets", 6500, 8500), ("Screws, nails, brackets, wood glue", "lot", 600, 1000),
   ("Black pleated skirting + Velcro", "25 ft run × 2 ft", 1800, 3000), ("Fire-retardant spray (all cloth, thermocol, cotton)", "4 L", 1200, 2000)],
  steps=["Confirm deck height, size and load rating on site; mark the 9 × 16 ft grid.", "Prefab the frame in 4 × 4 ft sections at the workshop; label each section.", "Cut legs to the heights on the plan; screw to the battens at 2 ft centres.", "Cross-brace every leg taller than 1.5 ft, both ways.",
         "Skin the tops with ply; leave hatches A, B, C loose.", "Skirting on the open front and left edges with Velcro (removable)."],
  check="Deck height 2 ft and a free 9 × 16 ft are assumed. Re-cut the leg heights if the deck is different."),
 dict(id="1", name="Cave, hill and Holy Family set", covers="2 cave · 3 Holy Family, ox, donkey, manger · 5 rock hill", zone="Tier A (hero), 1:3",
  days=14, when=(7, 28), fn="m1", lines=[
   ("Thermocol 4 in, 8 × 4 ft", "8 sheets", 9600, 13000), ("Plaster of Paris 25 kg", "4 bags", 2400, 3200), ("Wall putty / tile grout + sand", "3 bags", 900, 1200), ("PVA glue", "5 L", 1000, 1200),
   ("Emulsion/acrylic earth colours + brushes", "8 L", 3200, 4500), ("Chicken mesh + binding wire", "lot", 600, 800), ("Straw, dry grass tufts", "lot", 300, 400), ("Warm COB LEDs 12 V + dimmer (cave glow)", "2 + 1", 700, 1000),
   ("Holy Family, 2 ft figures: Mary, Joseph, baby", "set of 3", 8000, 18000), ("Ox and donkey, about 1 ft", "2", 1500, 3500), ("Manger (thermocol + plaster) + clay lamp", "1", 400, 800)],
  steps=["Glue 4 in thermocol into a block (hill ≈ 7 × 6 × 3 ft); cut the 4 × 2.5 ft cave inside it.", "Carve strata and cracks with a hot knife; cut the arch 3 ft wide × 2.5 ft high.", "Mesh the arch and overhangs; coat with PoP + PVA, 3 mm.",
         "Sand/grout coat while wet; press in real pebbles and dry grass.", "Dry-brush sand, then ochre, then olive; darker in cracks.", "Fit manger, straw, animals and figures last; hide the LED above the lintel.", "Split into cave and hill pieces that pass through the church door."],
  check="Swing item: buy new 2 ft figures (₹18,000) or reuse the 2023 set (₹8,000 incl. repaint)."),
 dict(id="2", name="Upper house (guest room)", covers="4 house with guest room, cut open", zone="Tier A–B, 1:6",
  days=5, when=(14, 28), fn="m2", lines=[
   ("Thermocol 2 in, 8 × 4 ft", "2 sheets", 2400, 3200), ("PoP + whitewash paint", "1 bag + 1 L", 1100, 1300), ("Sleeping travellers 1:6 (DIY clay + cloth, or bought)", "6", 600, 2400),
   ("Props: jars, baskets, mats, blankets", "lot", 500, 900), ("Flicker LED lamps + wiring", "3", 400, 600), ("Balsa / bamboo for beams, door", "lot", 250, 400)],
  steps=["Cut walls from 2 in thermocol on a 4 × 2 ft base; remove the front wall (cut open).", "Make the floor tray from 12 mm ply, resting on two posts and the hill.", "Plaster and whitewash; cut stone steps down one side.",
         "Dress the room: mats, blankets, jars, six sleepers, three flicker lamps.", "Add hidden details: cat on the roof, clay oven, sleeping child."],
  check="Floor at +2.8 ft must clear the cave arch (2.5 ft) with the ply tray."),
 dict(id="3", name="Path of light", covers="1 path of light (pixel strip under sand)", zone="front to cave mouth",
  days=2, when=(24, 36), fn="m3", lines=[
   ("WS2812B 60 LED/m strip, 5 V", "3 m", 1000, 1300), ("Aluminium/silicone channel + diffuser", "3 m", 400, 700), ("Fine sand, pebbles, glue", "lot", 600, 800), ("5 V 5 A supply + connectors, 470 Ω, 1000 µF", "1 set", 750, 1000)],
  steps=["Cut a 14 mm groove along the path; fit the channel flush.", "Solder the strip (5 V, GND, data) and seal with heat-shrink.", "Fix the diffuser strip over the LEDs.", "Glue fine sand on top and pebbles at the edges.", "Run data to hatch A; test the chase at 20 px/s."],
  check="The path must never cross a solid object; it is checked on the master plan."),
 dict(id="4", name="Shepherds' field", covers="8 shepherds, sheep, campfire · 11 sheepfold · 12 terraces · 13 watchtower", zone="Tier B–C, 1:6 to 1:12",
  days=8, when=(10, 30), fn="m4", lines=[
   ("Thermocol 4 in ×3 + 2 in ×1, 8 × 4 ft", "4 sheets", 6400, 7800), ("PoP + grout", "2 bags", 1200, 1600), ("Soil, sand, artificial grass, moss", "lot", 1200, 1800), ("Paint + brushes", "4 L", 1500, 2000),
   ("Shepherd figures 1.2 ft (old man, young man + lamb)", "2", 2400, 5000), ("Wool sheep", "6", 600, 1800), ("Campfire: twigs + orange flicker LED", "1", 300, 500), ("Pebbles + glue for the sheepfold", "lot", 500, 600), ("Watchtower: PVC pipe, clay, pebbles", "1", 500, 700)],
  steps=["Build four ply boxes 1.75 ft deep at +0.8, +1.2, +1.6 and +2.0 ft.", "Face with 2 in thermocol carved as dry-stone walls; glue real pebbles on the fronts.", "Soil/sand on the treads; grass patches and moss.", "Sheepfold: pebble ring with a thorn gate. Watchtower: 1 ft PVC + pebble clay.",
         "Place the shepherds, campfire and sheep last."],
  check="Items 9 and 10 (sheet 5) sit inside this zone; build them together."),
 dict(id="5", name="Floating angel + valley mist", covers="9 floating angel (Pepper's ghost) · 10 rock ridge with mist tray", zone="left field",
  days=4, when=(20, 36), fn="m5", lines=[
   ("Clear acrylic 3 mm, 2.4 × 2 ft sheet", "1", 2000, 3000), ("Screen: reuse an old tablet, or 10–13 in monitor + Pi Zero 2 W", "1", 0, 7000), ("Black cloth, plywood housing, black paint", "lot", 800, 1200),
   ("Ultrasonic mister discs ×2 + tray + 5 V fan + float", "1 set", 1500, 2200), ("Ridge: thermocol + PoP + paint", "1 sheet", 2700, 3200)],
  steps=["Build a black box 2.4 × 1.4 ft behind the ridge; put the screen in face-up.", "Mount the acrylic at 45°, leaning toward the viewer at the top.", "Cover everything except the acrylic with black cloth; the ridge hides the screen.",
         "Make a 20 s looping angel video: white on pure black, mirrored left-right.", "Test at night from the view spot; tune the angle and brightness.", "Mister tray behind the ridge lip, 3 cm water, on its own relay."],
  check="Swing item: a tablet you already own makes the screen free; a monitor needs a power source."),
 dict(id="6", name="Village street and houses", covers="16–18 houses · 19 street · 20 well · 21 census · 22 donkeys · 23–24 olives · 25 plaque", zone="Tier B, 1:6",
  days=12, when=(14, 33), fn="m6", lines=[
   ("Thermocol 2 in, 8 × 4 ft", "4 sheets", 4800, 6000), ("Lime plaster / PoP + white paint", "lot", 2400, 3000), ("Doors, beams, stairs (balsa, bamboo)", "lot", 700, 1000),
   ("Census scene: table, scribe, soldier, 3 villagers", "5 figures", 2000, 5500), ("Donkeys with panniers", "2", 800, 2500), ("Travellers", "2", 800, 2000),
   ("Well: PVC ring, pebbles, resin pool", "1", 800, 1200), ("Olive trees (wire, jute, paper, dried leaves)", "2", 800, 1200), ("Plaque: wood + printed icons", "1", 900, 1500),
   ("Flicker LEDs + wire for windows", "15", 1000, 1400), ("Miniature props: jars, baskets, barrels", "lot", 600, 1000)],
  steps=["Cut house blocks (heights 2.0, 2.5, 1.8 ft); cut windows and doors.", "Add wood lintels and the outside stair on the tallest house.", "Plaster, lime-wash, stain with a thin brown glaze.",
         "Pave the street with cut cork or grooved clay; add a drainage channel.", "Build the well with a sealed resin pool; make the olive trees.", "Fit lamps in the windows; run wires through the base to hatch A."],
  check="Houses sit against the right wall; keep 1 in clear for the drape bottom."),
 dict(id="7", name="Far village and Magi caravan", covers="14 far village (1:24) · 15 Magi caravan on a wall shelf", zone="Tier D, 1:24",
  days=4, when=(24, 33), fn="m7", lines=[
   ("Thermocol 1 in + clay for 20 houses", "1 sheet", 800, 1200), ("Pale cream/blue paint", "lot", 500, 600), ("1:24 caravan: 3 kings, camels, servant", "set", 1500, 3500), ("Wall shelf (ply, 3 ft) + 40 micro LEDs 3 mm", "1", 800, 1000)],
  steps=["Cut a 3.8 × 0.8 ft strip; make 20 houses 3–5 in tall; paint pale with blue shadows.", "Place the strip at y 5.2–9.0 on the right-wall crest at +3.0 ft.", "Fix a 3 × 0.3 ft ply shelf at +3.6 ft; paint a road line on it.",
         "Mount the caravan; fit micro LED lanterns on the kings.", "Check from the view spot that both are visible (bearings 38–49°)."],
  check="Positions changed after the sight check: the first layout hid both behind the house."),
 dict(id="8", name="Overhead cascade", covers="6 cloud and angel spiral · 7 star burst with bead strands", zone="ceiling corner",
  days=8, when=(14, 35), fn="m8", lines=[
   ("Polyfill / cotton wool", "3 kg", 900, 1200), ("Galvanised wire 3 mm + florist wire", "20 m", 800, 1000), ("Star base: foam core, silver tinsel/sheet", "1", 600, 900),
   ("Crystal bead strands, 60 × 6 ft", "110 m", 2500, 5000), ("Warm-white 12 V 10 W LED centre", "1", 600, 900), ("Mini angels 4–6 in, paper/feather", "30", 1500, 4500),
   ("Micro LED fairy strings", "5 × 3 m", 1200, 1800), ("Fishing line, swivels, anchors, hooks", "lot", 900, 1200), ("Ladder / scaffold hire", "2 days", 1500, 3000)],
  steps=["Mark hang points with a plumb line; confirm the ceiling type and anchors.", "Build the 2 ft star on a foam core with tinsel and a 10 W LED.", "Hang 60 bead strands (6 ft) from a 1.8 ft ring.",
         "Wind the wire helix 2.5 ft wide; skin it with polyfill; spray fire retardant.", "Attach 30 angels and micro-LED strings; hang from 7 points.", "Test at floor level first; hang last; trim after lighting."],
  check="Ceiling ≈ 15 ft is an assumption. If higher, strands and lines get longer; if plasterboard, use toggle anchors."),
 dict(id="9", name="Backdrop: print, drape, stars, UV angels", covers="26 hills print · blue drape · fibre-optic stars · UV angel choir", zone="both walls",
  days=8, when=(4, 34), fn="m9", lines=[
   ("Hills print on matt fabric/flex, 5 × 25 ft", "125 sq ft", 1750, 4400), ("Blue drape, 8.5 ft drop × 25 ft (poly vs velvet)", "~28 m", 2600, 5200), ("Gold stars: card + glitter + glue", "120", 600, 1000),
   ("Fibre-optic star kit with twinkle engine", "250 ends", 2500, 3800), ("UV LED bars 395 nm, 1 m", "2", 1600, 2600), ("UV-reactive paint + brushes", "12 angels", 1200, 1700),
   ("Curtain track, rope, hooks, clamps", "25 ft", 1500, 2500), ("Stitching + pleat tape", "lot", 1000, 1600)],
  steps=["Fit the ceiling track and a rope backup along both walls.", "Hang the five print panels; tape the joins flat.", "Sew and pleat the drape (1.5× fullness); hang on rings.",
         "Push 250 fibre ends through the top band; tape and route to the engine.", "Glue gold stars in irregular clusters.", "Paint 12 angels with UV paint; fit UV bars behind the print lip and test in the dark."],
  check="Swing item: drape cost scales with ceiling height (add about ₹280 per extra foot of drop)."),
 dict(id="10", name="Electrics and show control", covers="27 control box · 28 speakers · 29 UV bars · all lighting channels", zone="under deck, hidden",
  days=7, when=(7, 36), fn="m10", lines=[
   ("ESP32 boards ×2 (one spare)", "2", 1200, 1400), ("8-ch relay + 4 MOSFET modules", "set", 900, 1200), ("DFPlayer mini + SD + amp", "1", 500, 700), ("Speakers 5 W", "2", 600, 1200),
   ("PSUs: 12 V 10 A, 5 V 10 A, 24 V 2 A, 12 V 3 A", "4", 2600, 3200), ("RGBW wash bars", "3", 4500, 6000), ("Warm COB spots", "3", 1800, 2400), ("Flicker tea-lights / lamps", "35", 600, 900),
   ("Wire, terminals, fuses, connectors, ties", "lot", 2000, 2800), ("Extension boards, MCB, earthing check", "lot", 1200, 1500), ("Start button / timer", "1", 300, 500), ("Electrician, 2 days", "2", 1500, 3000)],
  steps=["Wire everything on a bench board first; test each channel for 10 s.", "Separate 12 V and 5 V rails, one fuse each, one common ground.", "Label every cable at both ends; leave a 1 ft service loop at each hatch.",
         "Program the 4-minute cue sheet; add a start button and manual override.", "Set the audio to 60 dB or less at the view spot.", "An electrician checks earthing and the RCCB before the first full run."],
  check="No mains voltage inside the crib. The church socket and its circuit rating must be confirmed."),
 dict(id="11", name="Public area and safety", covers="30 view spot + rope · signage · extinguisher", zone="front-left corner",
  days=2, when=(33, 37), fn="m11", lines=[
   ("Jute rope 15 m + 4 brass or wood posts", "1 set", 1200, 2200), ("Floor marker, signage and printing", "lot", 400, 800), ("CO₂ extinguisher (if the church has none)", "1", 0, 3000), ("Sambrani brass holder (closed)", "1", 300, 800)],
  steps=["Mark V on the floor: 3 ft left and 3 ft in front of the stage corner.", "Curve the rope barrier 5 ft from the stage front; keep a 4 ft clear aisle.", "Place the signs and the 'find 12 details' plaque.",
         "Confirm the extinguisher location and the exit with the church.", "Walk through with six people at V to confirm the sightlines."],
  check="Capacity at V is six people; the queue forms single file along the right-hand aisle."),
]

PALETTE = [
 ("Hero · complementary", "Lamp gold", "#F2B84B", "Cave glow, star burst, path of light, lamp flames, Magi lanterns"),
 ("Hero · highlight", "Warm white", "#FFF1CF", "Baby, manger straw: the brightest spot in the crib"),
 ("Hero · cool accent", "Mary blue", "#3A5BA8", "Mary's robe only"),
 ("Cool family", "Midnight blue", "#1F2F66", "Drape, night sky, shadows"),
 ("Cool family", "Dusk violet", "#5B4A9A", "UV angels, far hills, show wash"),
 ("Cool family", "Mist blue", "#AEBBD9", "Mist, clouds, far village, angel hologram"),
 ("Earth family", "Limestone", "#EDE3CB", "House walls, village, rock highlights, wool"),
 ("Earth family", "Sand", "#D2BC8C", "Paths, ground, hills print"),
 ("Earth family", "Ochre", "#B98A3E", "Rock mid-tones, doors, beams; Joseph (darken with #8A5A2B)"),
 ("Earth family", "Olive", "#7D8A4A", "Terraces, olive trees, moss"),
 ("Tiny accent", "Terracotta", "#A5583A", "Jars and a few roof tiles; nothing larger than a hand"),
 ("Neutral", "Near-black", "#15151A", "Skirting, deepest shadows"),
]
PIECES = [
 ("Cave and hill", "Ochre base, sand then limestone dry-brush, midnight-tinted shadows; inside near-black so the gold glows"),
 ("Holy Family", "Mary blue and limestone veil, Joseph ochre-umber, baby and straw warm white, manger sand"),
 ("Guest room house", "Limestone walls, terracotta jars, three lamp-gold flames"),
 ("Shepherds' field", "Olive treads, sand paths, limestone walls, earth-brown cloaks, cream wool"),
 ("Floating angel", "Mist blue fading to white; no gold, so it stays cool against the warm cave"),
 ("Village", "Limestone houses, sand street, ochre doors, tiny terracotta, warm window lamps (dimmer than the cave)"),
 ("Far village and Magi", "Limestone tinted with mist blue, tiny gold points; kings in dusk violet, mist blue and ochre"),
 ("Backdrop", "Hills print sand to ochre to dusk violet; drape midnight blue; gold stars in clusters; cool-white fibre stars"),
 ("Cascade", "Clouds mist blue and white, angels warm white, star lamp gold, clear bead strands"),
 ("Frame and trees", "Skirting near-black; olive trees olive with umber trunks, darker than the field behind them"),
]
RULES = [
 "Focal point dead centre: the cave and star. Keep the rock around the cave one shade darker so the gold glows.",
 "Leading lines: the path of light and the cascade spiral both point at the manger.",
 "Balance: cool white-blue angel and field on the left, many small warm lamps on the right, each dimmer than the cave.",
 "Atmospheric depth: pieces get paler, cooler and less saturated with distance (tiers A to D).",
 "Frame: dark, low-saturation olive trees in the two front corners.",
 "Repeat in threes: three lamps, three kings, three terrace steps.",
 "Gold in five places only: cave, star, path, lamps, Magi lanterns. A sixth glowing gold thing comes out.",
 "Proportion: about 60% cool blue, 30% earth, 10% gold.",
 "Not allowed: Christmas red, bright green, pink, primaries, colour-cycling or strobing lights.",
]
LIGHTS = [("Cave and lamps", "Warm 2200–2700 K"), ("Field flood", "Warm-neutral 3500–4000 K"), ("Fibre-optic stars", "Cool white with a few warm"), ("Sky wash", "Indigo (about #1A2A78), dusk amber for the first 30 s"), ("UV angels", "395 nm violet-white"), ("Mist", "Pale blue, lit by the cool wash")]

MISC = [("Tools and consumables (hot-wire cutter, blades, glue guns)", 1500, 3000, 800), ("Transport and delivery", 1500, 3000, 800)]
EXCL = ["skirting", "Holy Family", "Ox and donkey", "Sleeping travellers", "Shepherd figures", "Wool sheep", "Census scene", "Donkeys with", "Travellers", "1:24 caravan", "Ladder", "UV LED bars", "RGBW wash", "Warm COB spots", "Speakers", "Electrician", "Extension boards", "CO₂"]
CUT = {("0", "Plywood"): 3250, ("1", "Thermocol"): 6000, ("1", "Plaster of Paris"): 1800, ("1", "Wall putty"): 700, ("1", "Emulsion"): 2400, ("4", "Thermocol"): 3200, ("4", "PoP"): 800, ("4", "Paint"): 1000,
       ("6", "Thermocol"): 2400, ("6", "Lime plaster"): 1600, ("6", "Plaque"): 300, ("6", "Flicker LEDs"): 500, ("9", "Hills print"): 800, ("9", "Blue drape"): 1800, ("9", "UV-reactive"): 600, ("9", "Curtain track"): 700, ("9", "Stitching"): 0,
       ("8", "Crystal bead"): 1000, ("8", "Mini angels"): 500, ("8", "Micro LED"): 600, ("10", "ESP32"): 600, ("10", "PSUs"): 1000, ("10", "Wire, terminals"): 1200, ("11", "Jute rope"): 1000, ("11", "Floor marker"): 300}


def propcost(mid, a, c):
    if any(e in a for e in EXCL): return 0
    for (m_, k), v in CUT.items():
        if m_ == mid and a.startswith(k): return v
    return c
for m in MODS:
    m["lines"] = [(a, b, c, d, propcost(m["id"], a, c)) for a, b, c, d in m["lines"]]
    m["lean"] = sum(l[2] for l in m["lines"]); m["full"] = sum(l[3] for l in m["lines"]); m["prop"] = sum(l[4] for l in m["lines"])
LEAN = sum(m["lean"] for m in MODS) + sum(x[1] for x in MISC); FULL = sum(m["full"] for m in MODS) + sum(x[2] for x in MISC); PROP = sum(m["prop"] for m in MODS) + sum(x[3] for x in MISC)
CL, CF = round(LEAN * 0.10), round(FULL * 0.10)
CP = round(PROP * 0.10)
TL, TF = LEAN + CL, FULL + CF
TP = PROP + CP
DAYS = sum(m["days"] for m in MODS)
def ind(n):
    s_ = str(int(n))
    if len(s_) <= 3: return s_
    head, tail = s_[:-3], s_[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return ",".join(parts) + "," + tail
fmt = lambda n: "₹ " + ind(n)
print("lean", LEAN, "full", FULL, "prop", PROP, "total", TL, TF, TP, "person-days", DAYS)

CSS = """
@page { size: 1587px 1122px; margin: 0 }
*{box-sizing:border-box}
body{margin:0;font-family:'Segoe UI',Arial,sans-serif;color:#2b2a33;background:#fff}
.page{width:1587px;height:1122px;overflow:hidden;position:relative;page-break-after:always;padding:20px 28px 0;background:#fbfaf6}
.hdr{display:flex;align-items:flex-end;justify-content:space-between;border-bottom:3px solid #2b2a33;padding-bottom:8px;margin-bottom:10px}
.hdr h1{margin:0;font-family:'Segoe Print','Kalam',cursive;font-size:29px;font-weight:600}
.hdr .sub{font-size:14px;color:#4a4a55;margin-top:2px}
.chips{display:flex;gap:10px}
.chip{border:1.5px solid #2b2a33;border-radius:8px;padding:4px 12px;font-size:14px;background:#fff;text-align:center;line-height:1.25}
.chip b{display:block;font-size:17px}
.ftr{position:absolute;left:28px;right:28px;bottom:8px;font-size:11.5px;color:#4a4a55;display:flex;justify-content:space-between;border-top:1px solid #c9c5b8;padding-top:4px}
.body{display:flex;gap:18px}
.left{width:900px;display:flex;flex-direction:column;gap:8px}
.left svg{display:block}
.right{width:600px;font-size:13px}
.right h3{margin:0 0 4px;font-size:14px;letter-spacing:.04em;border-bottom:1.5px solid #2b2a33;padding-bottom:2px}
table{border-collapse:collapse;width:100%;font-size:12.5px;background:#fff}
td,th{border:1px solid #c9c5b8;padding:3px 6px;vertical-align:top}
th{background:#ece8dc;text-align:left}
td.n,th.n{text-align:right;white-space:nowrap}
tr.tot td{font-weight:700;background:#f3efe3}
ol{margin:4px 0 0;padding-left:20px}
ol li{margin-bottom:4px;line-height:1.28}
.box{border:1.5px solid #2b2a33;border-radius:8px;background:#fff;padding:8px 12px;margin-top:10px}
.box.warn{border-color:#a8322c;background:#fff6f4}
.warn b{color:#a8322c}
.sec{margin-top:12px}
.big{font-size:40px;font-weight:700;line-height:1}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.bar{height:15px;background:#b07a12;border-radius:3px}
.bar.l{background:#7d9a5c}
.gantt{position:relative;margin-top:6px}
.gr{display:flex;align-items:center;height:34px;border-bottom:1px solid #e0dccf}
.gl{width:330px;font-size:13.5px;font-weight:600;padding-right:10px}
.gt{position:relative;flex:1;height:100%}
.gb{position:absolute;top:9px;height:16px;border-radius:4px;background:#b07a12}
.wk{display:flex;margin-left:330px;font-size:12px;color:#4a4a55}
.wk div{flex:1;border-left:1px solid #c9c5b8;padding-left:5px}
"""


def pageframe(inner, n, tot, title, sub="", chips=""):
    return (f'<section class="page"><div class="hdr"><div><h1>{E(title)}</h1><div class="sub">{sub}</div></div><div class="chips">{chips}</div></div>{inner}'
            f'<div class="ftr"><span>Crib 2026 · "That Night in Bethlehem" · build pack · rough estimate, ±25%, confirm with local quotes</span><span>Sheet {n} of {tot}</span></div></section>')


def module_page(m, n, tot):
    svgs = getattr(DR, m["fn"])()
    rows = "".join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td class="n">{ind(p)}</td><td class="n">{ind(c)}</td><td class="n">{ind(d)}</td></tr>' for a, b, c, d, p in m["lines"])
    tbl = (f'<table><tr><th>Item</th><th>Qty / spec</th><th class="n">Prop-only ₹</th><th class="n">Lean ₹</th><th class="n">Full ₹</th></tr>{rows}'
           f'<tr class="tot"><td colspan="2">Sheet total</td><td class="n">{ind(m["prop"])}</td><td class="n">{ind(m["lean"])}</td><td class="n">{ind(m["full"])}</td></tr></table>')
    steps = "".join(f"<li>{E(s)}</li>" for s in m["steps"])
    d0, d1 = m["when"]
    import datetime
    base = datetime.date(2026, 11, 16)
    wd = lambda k: (base + datetime.timedelta(days=k)).strftime("%d %b")
    right = (f'<div class="right"><h3>ITEMS REQUIRED</h3>{tbl}<div class="sec"><h3>HOW TO BUILD IT</h3><ol>{steps}</ol></div>'
             f'<div class="box"><b>Time:</b> about {m["days"]} person-days · build window {wd(d0)} → {wd(d1)}<br><b>Covers:</b> {E(m["covers"])}<br><b>Scale zone:</b> {E(m["zone"])}</div>'
             f'<div class="box warn"><b>Check / swing:</b> {E(m["check"])}</div></div>')
    left = '<div class="left">' + "".join(svgs) + "</div>"
    chips = f'<div class="chip">Prop-only<b>{fmt(m["prop"])}</b></div><div class="chip">Lean<b>{fmt(m["lean"])}</b></div><div class="chip">Full<b>{fmt(m["full"])}</b></div><div class="chip">Effort<b>{m["days"]} p-days</b></div>'
    return pageframe(f'<div class="body">{left}{right}</div>', n, tot, f'Part {m["id"]} · {m["name"]}', f'Individual blueprint · items {E(m["covers"])}', chips)


def glance():
    mx = max(m["full"] for m in MODS)
    rows = "".join(f'<div style="display:flex;align-items:center;height:19px;font-size:12px"><div style="width:250px">{m["id"]} · {E(m["name"])}</div><div class="bar l" style="height:8px;width:{m["lean"]/mx*300:.0f}px"></div><div style="width:6px"></div><div class="bar" style="height:8px;width:{(m["full"]-m["lean"])/mx*300:.0f}px"></div><div style="margin-left:8px">{fmt(m["prop"])} · {fmt(m["lean"])} · {fmt(m["full"])}</div></div>' for m in MODS)
    return '<div class="box"><b>Cost at a glance</b> (prop-only · lean · full)<div style="margin-top:6px">' + rows + '</div></div>'


def cover(n, tot):
    chips = f'<div class="chip">Prop-only<b>{fmt(TP)}</b></div><div class="chip">Lean build<b>{fmt(TL)}</b></div><div class="chip">Full build<b>{fmt(TF)}</b></div><div class="chip">Crew<b>6–8 people</b></div><div class="chip">Opens<b>24 Dec 2026</b></div>'
    left = (f'<div style="width:900px"><img src="persp_blank.png" style="width:900px;border:1.5px solid #2b2a33"><div style="font-size:13px;color:#4a4a55;margin:4px 0 12px">Block-out of what visitors see from the public view spot (grey boxes = real positions and heights; no textures). The finished crib fills this frame.</div>'
            f'<div class="grid2"><div class="box" style="margin-top:0"><b>The idea</b><br>The Nativity as it most likely happened: a cave beneath a crowded guest room, a Roman census, shepherds in terraced fields, a far-off Magi caravan. '
            f'Forced perspective makes 9 × 16 ft read like a valley. By day it is a museum-quality diorama; in the dark, a 4-minute show.</div>'
            f'<div class="box" style="margin-top:0"><b>The 4-minute show</b><br>Dusk → lamps and fire → stars and mist → angel floats over the shepherds → hidden angel choir glows → light runs down the path to the cave → cave glows, cross-shadow, everything warm.</div></div>'
            + glance() + '</div>')
    right = ('<div style="width:620px;font-size:13.5px"><h3 style="margin:0 0 6px;font-size:15px;border-bottom:1.5px solid #2b2a33">WHAT IS IN THIS PACK</h3>'
             '<table><tr><th>Sheet</th><th>Contents</th></tr><tr><td>2</td><td>Master blueprint (plan, section, schedule of 30 items)</td></tr><tr><td>3</td><td>Church context, two view block-outs for the image prompts</td></tr>'
             '<tr><td>4</td><td>Colour and composition</td></tr><tr><td>5–16</td><td>Part sheets 0–11: individual blueprint, items required, build steps, cost</td></tr><tr><td>17</td><td>Cost summary for the presentation</td></tr><tr><td>18</td><td>Schedule 16 Nov → 24 Dec, on-site checks, risks</td></tr></table>'
             f'<div class="sec"><div class="big">{fmt(TP)} · {fmt(TL)} · {fmt(TF)}</div><div style="margin-top:4px;color:#4a4a55">Prop-only (figures, stage, lights not counted) · Lean · Full. All include 10% contingency.</div></div>'
             '<div class="box warn"><b>Assumed, to confirm on site</b><br>• Deck height 2 ft and a free 9 × 16 ft<br>• Ceiling about 15 ft; ceiling type for the star hook<br>• Altar centred on the front wall; crib at the right end<br>• Public stands 3 ft left and 3 ft in front of the stage corner</div>'
             '<div class="box"><b>Changed after the sight check</b><br>The Magi caravan and far village were hidden behind the cave house from the view spot. They now sit on the right-wall crest and a wall shelf (bearings 38–49°).</div>'
             '<div class="box"><b>How to use the image prompts</b><br>Attach the two block-out images and the church key plan to the image model so it keeps the layout; the prompt file is crib-2026-image-prompts.md.</div>'
             '<div style="margin-top:10px;text-align:center">' + church_svg(300, 385) + '<div style="font-size:12px;color:#4a4a55">Where the crib sits in the church (assumed)</div></div></div>')
    return pageframe(f'<div class="body">{left}{right}</div>', n, tot, 'Crib 2026 · "That Night in Bethlehem"', 'Build pack for presentation: layout, parts, materials, cost and schedule', chips)


def master(n, tot):
    inner = ('<img src="bp.png" style="width:1531px;border:1.5px solid #2b2a33;display:block">'
             '<div style="display:flex;gap:16px;margin-top:8px;font-size:13px"><div class="box" style="margin:0;flex:1"><b>Read it like this</b> · top view on the left (1 square = 1 ft), section along the sightline in the middle, schedule of items on the right. Items 1–30 are numbered the same on every part sheet.</div>'
             '<div class="box warn" style="margin:0;flex:1"><b>Changed since the first version</b> · Magi caravan (15) and far village (14) moved to the right-wall crest; acrylic for the floating angel (9) is 2.4 × 2 ft; church key plan added.</div></div>')
    return pageframe(inner, n, tot, 'Master blueprint · whole layout', 'Stage 9 × 16 ft in the right corner of the church · plan, section, 30-item schedule')


def context(n, tot):
    left = (f'<div style="width:620px">{church_svg(600, 770)}</div>')
    mid = ('<div style="width:830px"><div style="font-size:14px;font-weight:700;margin-bottom:4px">VIEW 1 · standing at the public spot (front-left corner of the stage)</div>'
           '<img src="persp_blank.png" style="width:800px;border:1.5px solid #2b2a33"><div style="font-size:14px;font-weight:700;margin:10px 0 4px">VIEW 2 · wide shot from the centre aisle (altar centre-left, crib at the right end)</div>'
           '<img src="persp2_blank.png" style="width:800px;border:1.5px solid #2b2a33"></div>')
    inner = (f'<div class="body">{left}{mid}</div>')
    return pageframe(inner, n, tot, 'Church context and the two views', 'Key plan (left) and grey block-outs generated from the blueprint coordinates; attach them to the image model')



def colour(n, tot):
    sw = "".join(f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:5px"><div style="width:46px;height:30px;border-radius:5px;background:{h};border:1px solid #8886"></div><div style="font-size:12.5px;line-height:1.25"><b>{E(nm)}</b> <span style="color:#4a4a55">{h} · {E(role)}</span><br>{E(use)}</div></div>' for role, nm, h, use in PALETTE)
    pcs = "".join(f"<tr><td style='white-space:nowrap'><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in PIECES)
    rls = "".join(f"<li>{E(r)}</li>" for r in RULES)
    lts = "".join(f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in LIGHTS)
    bar = "".join(f'<div style="flex:{w};background:{c};height:26px"></div>' for w, c in ((60, "#1F2F66"), (30, "#D2BC8C"), (10, "#F2B84B")))
    left = (f'<div style="width:560px"><h3 style="margin:0 0 6px;font-size:15px;border-bottom:1.5px solid #2b2a33">PALETTE: TWELVE COLOURS, NO MORE</h3>{sw}'
            f'<div style="display:flex;border:1px solid #2b2a33;margin-top:8px">{bar}</div><div style="display:flex;font-size:11.5px"><div style="flex:60">60% cool</div><div style="flex:30">30% earth</div><div style="flex:10">10% gold</div></div></div>')
    mid = (f'<div style="width:470px;font-size:13px"><h3 style="margin:0 0 6px;font-size:15px;border-bottom:1.5px solid #2b2a33">COMPOSITION RULES</h3><ol style="margin:0;padding-left:18px">{rls}</ol>'
           f'<h3 style="margin:14px 0 6px;font-size:15px;border-bottom:1.5px solid #2b2a33">LIGHT COLOURS</h3><table>{lts}</table></div>')
    right = (f'<div style="width:420px;font-size:12.5px"><h3 style="margin:0 0 6px;font-size:15px;border-bottom:1.5px solid #2b2a33">PIECE BY PIECE</h3><table>{pcs}</table></div>')
    return pageframe(f'<div class="body">{left}{mid}{right}</div>', n, tot, "Colour and composition", "Gold is the one complementary colour against blue night; everything else stays in related blues and earth tones")


def summary(n, tot):
    mx = max(m["full"] for m in MODS)
    rows = "".join(f'<tr><td>{m["id"]}</td><td>{E(m["name"])}</td><td class="n">{m["days"]}</td><td class="n">{ind(m["prop"])}</td><td class="n">{ind(m["lean"])}</td><td class="n">{ind(m["full"])}</td>'
                   f'<td style="width:260px"><div class="bar l" style="width:{m["lean"]/mx*240:.0f}px"></div><div class="bar" style="width:{m["full"]/mx*240:.0f}px;margin-top:2px"></div></td></tr>' for m in MODS)
    misc = "".join(f'<tr><td></td><td>{E(a)}</td><td class="n"></td><td class="n">{ind(p)}</td><td class="n">{ind(b)}</td><td class="n">{ind(c)}</td><td></td></tr>' for a, b, c, p in MISC)
    tbl = (f'<table><tr><th>#</th><th>Part</th><th class="n">Person-days</th><th class="n">Prop-only ₹</th><th class="n">Lean ₹</th><th class="n">Full ₹</th><th>Lean (green) vs Full (gold)</th></tr>{rows}{misc}'
           f'<tr class="tot"><td></td><td>Subtotal</td><td class="n">{DAYS}</td><td class="n">{ind(PROP)}</td><td class="n">{ind(LEAN)}</td><td class="n">{ind(FULL)}</td><td></td></tr>'
           f'<tr><td></td><td>Contingency 10%</td><td></td><td class="n">{ind(CP)}</td><td class="n">{ind(CL)}</td><td class="n">{ind(CF)}</td><td></td></tr>'
           f'<tr class="tot"><td></td><td>TOTAL, rough estimate</td><td></td><td class="n">{ind(TP)}</td><td class="n">{ind(TL)}</td><td class="n">{ind(TF)}</td><td></td></tr></table>')
    top3 = sorted(MODS, key=lambda m: -m["full"])[:3]
    right = ('<div style="width:520px;font-size:13.5px">'
             f'<div class="box" style="margin-top:0"><div class="big">{fmt(TP)}</div><div>Prop-only (figures, stage, lights not counted)</div><div class="big" style="margin-top:10px">{fmt(TL)}</div><div>Lean build, all-in</div><div class="big" style="margin-top:10px">{fmt(TF)}</div><div>Full build, all-in</div></div>'
             '<div class="box"><b>Where the money goes (full build)</b><br>' + "<br>".join(f'{m["name"]}: {fmt(m["full"])}' for m in top3) + '</div>'
             '<div class="box warn"><b>Biggest swings</b><br>• 2 ft Holy Family figures: ₹8,000 if repainted from 2023, ₹18,000 new<br>• Drape: depends on ceiling height (about ₹280 per foot of drop), polyester vs velvet<br>'
             '• Floating-angel screen: free with an old tablet, ₹7,000 with a new monitor and player<br>• Crystal strands and mini angels: ₹4,000 if you make them, ₹9,500 if bought</div>'
             '<div class="box"><b>Prop-only tier</b><br>Counts prop materials only. Not counted: figures (reused from 2023), the rented stage and skirting, rented lights, speakers, electrician, extinguisher, ladder hire. Half the plywood is reused from 2023. Smaller rock, painted hills, a simpler backdrop and cascade, 10% contingency.</div><div class="box"><b>Ways to lower it further</b><br>• Reuse 2023 plywood, frames, skirting, figures: up to about ₹ 10,000–15,000 if you still have them<br>• Borrow wash lights and spots from the church or a hirer: up to ₹ 6,300<br>• Make the Magi caravan from clay instead of buying: about ₹ 2,000</div>'
             '<div class="box"><b>How to read this</b><br>Prices are rough Indian market rates for 2026, ±25%. Collect two quotes for plywood, thermocol, print and figures. '
             'This replaces the earlier ₹40,000–70,000 first guess, which was top-down; this one adds up every line.</div></div>')
    return pageframe(f'<div class="body"><div style="width:960px">{tbl}</div>{right}</div>', n, tot, 'Cost summary', 'Rough estimate in rupees · Lean (reuse and DIY) versus Full (buy new)',
                     f'<div class="chip">Prop-only<b>{fmt(TP)}</b></div><div class="chip">Lean<b>{fmt(TL)}</b></div><div class="chip">Full<b>{fmt(TF)}</b></div><div class="chip">Effort<b>{DAYS} person-days</b></div>')


def schedule(n, tot):
    import datetime
    base = datetime.date(2026, 11, 16)
    N = 39.0
    wks = [("16–22 Nov", "Measure, order, start"), ("23–29 Nov", "Carve, frame"), ("30 Nov–6 Dec", "Plaster, paint, sew"), ("7–13 Dec", "Detail, wire, test"), ("14–20 Dec", "Install in church"), ("21–24 Dec", "Rehearse, open")]
    wk = '<div class="wk">' + "".join(f'<div style="flex:{w}"><b>{a}</b><br>{b}</div>' for (a, b), w in zip(wks, (7, 7, 7, 7, 7, 4))) + "</div>"
    rows = ""
    for m in MODS:
        a, b = m["when"]
        rows += (f'<div class="gr"><div class="gl">{m["id"]} · {E(m["name"])}</div><div class="gt"><div class="gb" style="left:{a/N*100:.1f}%;width:{(b-a)/N*100:.1f}%"></div></div></div>')
    rows += ('<div class="gr"><div class="gl" style="color:#a8322c">Install in church (14–17 Dec)</div><div class="gt"><div class="gb" style="background:#a8322c;left:%.1f%%;width:%.1f%%"></div></div></div>' % (28 / N * 100, 4 / N * 100))
    rows += ('<div class="gr"><div class="gl" style="color:#2f5aa8">Wire, aim, test, rehearse (18–23 Dec)</div><div class="gt"><div class="gb" style="background:#2f5aa8;left:%.1f%%;width:%.1f%%"></div></div></div>' % (32 / N * 100, 6 / N * 100))
    ms = [("22 Nov", "Site measurements done; long-lead items ordered"), ("30 Nov", "Frame sections finished; rock carved"), ("7 Dec", "Plaster and paint finished; figures placed in the workshop"), ("13 Dec", "Electronics and show tested on the bench"),
          ("14 Dec", "Install starts in the church"), ("18 Dec", "Lights on, aim and sightline check from V"), ("21 Dec", "First full run of the show"), ("23 Dec", "Final rehearsal and safety walk-through"), ("24 Dec", "Crib opens")]
    mt = "".join(f"<tr><td style='white-space:nowrap'><b>{a}</b></td><td>{E(b)}</td></tr>" for a, b in ms)
    left = f'<div style="width:1000px"><div class="gantt">{wk}{rows}</div><div class="sec"><h3 style="margin:14px 0 4px;font-size:14px;border-bottom:1.5px solid #2b2a33">KEY DATES</h3><table style="width:640px"><tr><th>Date</th><th>Milestone</th></tr>{mt}</table></div></div>'
    right = ('<div style="width:520px;font-size:13.5px"><div class="box" style="margin-top:0"><b>Crew</b><br>6–8 volunteers, about 3 workdays a week: carving and plaster (2), figures and painting (2), electrics and show control (1–2, one with an electrician), backdrop and rigging (1–2). '
             f'Total effort about {DAYS} person-days.</div>'
             '<div class="box warn"><b>Do these first, in week 1</b><br>1. Measure deck height, ceiling height, ceiling type and the star hook points<br>2. Confirm the altar position and the power point<br>3. Order the long-lead items: fibre-optic kit, UV bars, acrylic, 2 ft figures, backdrop print<br>4. Ask the church about working at height and the deck load rating</div>'
             '<div class="box"><b>Main risks</b><br>• Ceiling higher than 15 ft: longer strands, more drape<br>• Print or figures arrive late: order by 22 Nov<br>• Thermocol and cotton: fire retardant on everything; no open flames<br>• Mist or water near electrics: keep trays sealed with a float switch<br>• Door width: build the hill in pieces that pass the door</div>'
             '<div class="box"><b>Dress rehearsal checklist</b><br>Run the show three times; stand at V and check the angel, the UV choir, the path, the cave glow and the cross-shadow from the rope; check the sound level; test the manual override.</div></div>')
    return pageframe(f'<div class="body">{left}{right}</div>', n, tot, 'Schedule: 16 Nov → 24 Dec 2026', 'Build in the workshop, install in the church from 14 Dec, rehearse 21–23 Dec, open 24 Dec')


def main(out):
    tot = 5 + len(MODS) + 1
    pages = [cover(1, tot), master(2, tot), context(3, tot), colour(4, tot)]
    n = 5
    for m in MODS:
        pages.append(module_page(m, n, tot)); n += 1
    pages.append(summary(n, tot)); n += 1
    pages.append(schedule(n, tot))
    open(out, "w", encoding="utf-8").write(f"<!doctype html><html><head><meta charset='utf-8'><title>Crib 2026 build pack</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>")


if __name__ == "__main__":
    main(sys.argv[1])
