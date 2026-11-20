"""Block data for the 2026 crib (13 blocks A, B, C, E-N; there is no D). Plan of 19 Nov 2026:
two flat layers (deck + a second layer 1.5 ft high across the back 4.5 ft), craft props, one-plug lighting (block H), pond + selfie mirror (block M).
Costs are rough estimates in rupees (reuse / lean / all new), +-25%. Used by make_crew.py (owner guide) and make_crew_pack.py (crew pack)."""
import os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COL = {'A': (120,120,120), 'B': (230,120,20), 'C': (200,50,50), 'E': (40,150,70), 'F': (120,60,200),
       'G': (30,110,220), 'H': (210,170,0), 'I': (0,170,190), 'J': (60,60,160), 'K': (230,60,160), 'L': (110,200,60), 'M': (0,120,110), 'N': (150,110,60)}

TEAMS = {'A': 'Stage team: Vk, Samuel',
         'B': 'Team 4: Janet, Mithul, Yugesh, Stephen, Alvin',
         'C': 'Team 2: Lenin, Runo, Aarthi, Milton, Monus',
         'E': 'Team 1: Rufus, Sanjeetha, Andrew, Samuel',
         'F': 'Team 3: Austin Joel, Richard, Allwyn (with helpers for the craft)',
         'G': 'Team 5: Jino, Shibi, Suja, Adrian, Deric, Vk',
         'H': 'Team 3: Austin Joel, Richard, Allwyn',
         'I': 'Team 3: Austin Joel, Richard, Allwyn',
         'J': 'Team 3: Austin Joel, Richard, Allwyn',
         'K': 'Team 4: Janet, Mithul, Yugesh, Stephen, Alvin',
         'L': 'Stage team: Vk, Samuel',
         'M': 'To be assigned (suggest the Stage team: Vk, Samuel)',
         'N': 'Team 2: Lenin, Runo, Aarthi, Milton, Monus'}

B = {}
def add(k, **kw): B[k] = kw

add('A', name='Two-layer stage', items='12 second layer (the upper level); the rented deck stays as the lower level',
    window='20 Nov → 5 Dec', days='4', phase='20–22 Nov: measure on site and buy wood (week 1). 23 Nov – 5 Dec: build in the workshop and fit on the deck.',
    where='Lower level: the rented deck, flat, 9 ft wide × 16 ft long, 2 ft above the church floor. Upper level: a plywood box 9 ft wide × 4.5 ft deep × 1.5 ft high against the back wall (the step starts 11.5 ft from the front). Black skirting on the front and the left side.',
    rows=[['Plywood 9–12 mm, 8 × 4 ft', '3 sheets', '1,950', '3,900', '5,100'],
          ['Pine battens 2 × 2 in', '~90 ft', '1,800', '2,000', '2,800'],
          ['Screws, brackets, clamps, wood glue', 'lot', '400', '400', '700'],
          ['Black pleated skirting + Velcro', '25 ft run × 2 ft', '0', '1,800', '3,000'],
          ['Fire-retardant spray (all cloth, thermocol, cotton)', '4 L', '1,200', '1,200', '2,000'],
          ['Hatch lids, hinges, floor markers', 'lot', '200', '300', '500']],
    before=['Measure the real deck: height (2 ft assumed), size, level, and whether you may screw into it. If not, clamp and weigh the boxes down.', 'Mark the 9 × 16 ft grid and the step line 11.5 ft from the front with tape.'],
    done=['Both boxes are rigid: two people can stand on any part without flex.', 'Hatch lids A, B and C open easily and are labelled.', 'Skirting hides the open front and left side down to the floor.', 'Every piece passes through the church door.'],
    hands='Everything stands on A. B, C, E, F, G, K, L and M go on after A is placed; H uses the hatches.',
    tools='Saw, drill, screw gun, spirit level, tape measure, staple gun')

add('B', name='Cave, rock hill and Holy Family', items='2 cave, 3 Holy Family with ox, donkey and manger, 5 rock hill',
    window='23 Nov → 14 Dec', days='14',
    where='One unit about 7 × 6 ft, 3.3 ft high, on the lower level with its back against the step. Cave 4 × 2.5 ft at floor level, turned 33° so the 3 ft wide mouth faces the public spot V; arch 2.5 ft high, centre x 4.4, y 7.4. Hill top and house floor at +3.3 ft. Figures 2 ft (hero scale 1:3), ox and donkey about 1 ft.',
    rows=[['Thermocol 4 in, 8 × 4 ft', '9 sheets', '6,750', '10,800', '14,600'],
          ['Plaster of Paris 25 kg', '4 bags', '1,800', '2,400', '3,200'],
          ['Wall putty / tile grout + sand', '3 bags', '700', '900', '1,200'],
          ['PVA glue', '5 L', '1,000', '1,000', '1,200'],
          ['Emulsion / acrylic earth colours + brushes', '8 L', '2,400', '3,200', '4,500'],
          ['Chicken mesh + binding wire', 'lot', '600', '600', '800'],
          ['Straw, dry grass tufts', 'lot', '300', '300', '400'],
          ['Plywood 12 mm base, 8 × 4 ft', '2 sheets', '1,300', '2,600', '3,400'],
          ['Holy Family, 2 ft figures: Mary, Joseph, baby', 'set of 3', '0', '8,000', '18,000'],
          ['Ox and donkey, about 1 ft', '2', '0', '1,500', '3,500'],
          ['Manger (thermocol + plaster) + clay lamp', '1', '400', '400', '800']],
    before=['Wear a mask for plaster dust; cut thermocol outdoors; fire-retardant spray every cut surface.', 'Decide: buy new 2 ft figures (₹18,000) or reuse and repaint the 2023 set (₹8,000).', 'Make a cardboard mock-up of cave + house first (see the stack note).'],
    done=['Rock reaches +3.3 ft and about 10 in of rock sits above the arch.', 'From V the manger and baby are visible and not hidden by the arch.', 'Every piece fits through the church door.', 'Holes and 1 ft cable tails are left for the cave lights (block H fits them).'],
    hands='C (house) rests on the hill top. E (field) and K (far village) sit beside it. H fits the cave and manger lights.',
    tools='Hot-wire cutter, hot knife, trowel, mesh cutters, glue gun, brushes, sculpting clay, dust mask')

add('C', name='House with upper room', items='4 house with the upper guest room (kataluma), cut open',
    window='30 Nov → 14 Dec', days='5',
    where='4 × 2 ft room, floor at +3.3 ft on the hill top, room height 1.5 ft, roof at +4.8 ft. Turned 33° toward V. Outside stair of 8 steps rising 3.3 ft.',
    rows=[['Plywood 4 mm, 8 × 4 ft (walls, roof)', '1 sheet', '700', '900', '1,100'],
          ['Plywood 9 mm floor tray, 4 × 2 ft + 2 × 2 in posts', '1 set', '400', '500', '700'],
          ['Pine strip 1 × 1 in (corners) + screws, wood glue', '~20 ft', '300', '400', '500'],
          ['Wall putty + sand (texture) + whitewash paint', '1 bag + 1 L', '900', '1,000', '1,200'],
          ['Sleeping travellers 1:6 (clay + cloth, or bought)', '6', '0', '600', '2,400'],
          ['Props: jars, baskets, mats, blankets', 'lot', '500', '500', '900'],
          ['Balsa / bamboo for beams, door', 'lot', '250', '250', '400']],
    before=['Take the cave arch height (2.5 ft) and the +3.3 ft hill top from block B.', 'Gather six 1:6 sleeping travellers (about 1 ft long) or clay to make them.'],
    done=['Plywood room, screwed (not glued), weighs under 12 kg and sits on the two posts and the hill top.', 'Hidden details placed: cat on the roof, clay oven, sleeping child.', 'Three small holes with 1 ft cable tails are left for the room lamps (block H fits them).', 'Lifts off the hill as one piece.'],
    hands='Sits on B. H fits the three room lamps through the holes you leave.',
    tools='Jigsaw or hand saw, drill + 3 mm bit, screwdriver, sandpaper, putty knife, brushes')

add('E', name="Shepherds' field", items='8 shepherds, sheep and campfire; 11 sheepfold; 13 watchtower; the dry-stone step wall',
    window='26 Nov → 11 Dec', days='6',
    where='Left side. Lower level: a low terrace wall 1.55 × 0.25 ft, 0.5 ft high (x 0–1.55, y 6.3), 2 standing shepherds 1 ft tall and 1 lying down, 14 sheep spread from y 4.6 to 9.6, a campfire at x 1.0, y 8.3, a black goat-hair tent, boulders, thorn bushes, a stone trough and a fig tree. Upper level behind the step: sheepfold 2 × 1.3 ft (x 0.4–2.4, y 1.75–3.05) and a 1 ft round watchtower 1.5 ft tall at x 3.0, y 1.0. The step face (9 ft × 1.5 ft) is faced as a dry-stone wall.',
    rows=[['Thermocol 2 in, 8 × 4 ft (step wall, sheepfold base)', '2 sheets', '1,600', '3,200', '3,900'],
          ['PoP + grout', '1 bag', '400', '600', '800'],
          ['Soil, sand, artificial grass, moss', 'lot', '900', '900', '1,300'],
          ['Paint + brushes', '3 L', '750', '1,100', '1,500'],
          ['Shepherd figures 1 ft (old man, young man + lamb, one lying down)', '3', '0', '3,000', '6,000'],
          ['Wool sheep (pipe cleaner + wool, made by the team)', '14', '300', '700', '1,800'],
          ['Terrace wall: thermocol 2 in strip + pebbles', '1', '100', '200', '300'],
          ['Goat-hair tent (felt or old blanket), trough, fig tree, boulders, thorn bushes', 'lot', '200', '400', '700'],
          ['Campfire: twigs and pebbles (light fitted by H)', '1', '100', '100', '200'],
          ['Pebbles + glue for the sheepfold', 'lot', '500', '500', '600'],
          ['Watchtower: PVC pipe, clay, pebbles', '1', '500', '500', '700']],
    before=['Check the angel choir place with block F: the choir stands above the sheepfold.', 'Leave holes and 1 ft cable tails for the campfire light and the two field floods (block H).'],
    done=['The step wall is covered in carved dry-stone with real pebbles, 1.5 ft high, full width.', 'Shepherds, sheep and fold are paler and cooler than the village (tier B–C).', 'Ground between the wall and the hill is sand and soil with grass patches.', 'Pieces lift out one at a time.'],
    hands='Sits on A. F (angel choir) stands on the upper level above the sheepfold. H fits the campfire light and the floods.',
    tools='Hot knife, glue gun, brushes')

add('F', name='Pipe-cleaner angel choir', items='9 the angel choir (replaces the floating angel unit)',
    window='1 Dec → 14 Dec', days='2',
    where='On the upper level above the sheepfold at the left (x 0.4–2.8, y 1.0–4.0). One hero angel about 2 ft tall at x 1.6, y 2.4 on a wire pole, and nine small angels 8–10 in tall on wire stakes at different heights. Cool white and silver, no gold.',
    rows=[['White chenille stems (pipe cleaners) 12 mm', '300 pcs', '150', '300', '400'],
          ['Tulle 3 m + coffee filters (wings and robes)', 'lot', '150', '250', '400'],
          ['Wooden beads 1 in (heads)', '12', '100', '150', '250'],
          ['Wire 2–3 mm, 10 m + bamboo sticks (stakes, poles)', 'lot', '150', '250', '400'],
          ['Wire core for the hero angel + silver halo ring', '1 set', '150', '200', '300'],
          ['Glue-gun sticks, white and silver paint', 'lot', '100', '200', '300'],
          ['Battery micro-LED string, cool white (inside the hero)', '2', '150', '250', '400']],
    before=['Make one small angel first as a pattern, then batch the rest. Good job for helpers.', 'Agree the stake holes with block E (sheepfold area).'],
    done=['Hero angel is 2 ft tall, light and stable on its pole.', 'Nine small angels stand firmly on stakes at different heights.', 'All white and silver, no gold, no colour.', 'The clip lamp from block H lights them cool white.'],
    hands='Stands on the upper level beside E. H clips a cool-white angel lamp above them.',
    tools='Wire cutters, pliers, glue gun, scissors')

add('G', name='Village street', items='16–18 five houses stepping down toward the back, 19 cobbled street that narrows away from you, 20 well, 21 census table, 22 donkeys and travellers, market stall, palm, chickens',
    window='30 Nov → 17 Dec', days='9',
    where='Right wall side, all on the flat lower level. Five plywood houses along the right wall, tallest at the front: 3.5 / 3.0 / 2.5 / 2.0 / 1.5 ft (1:6, people 1 ft). Street 1.25 ft wide at the front (y 16) narrowing to 0.55 ft at the back (y 9.2). Well, census table, donkeys, a market stall at the front and a palm at the back.',
    rows=[['Plywood 6 mm, 8 × 4 ft (house walls, roofs) + 12 mm offcuts (bases)', '3 sheets', '2,700', '3,600', '4,500'],
          ['Pine strip 1 × 1 in (corners) + screws, wood glue', '~70 ft', '800', '1,100', '1,400'],
          ['Market stall: sticks, cloth awning, tiny baskets', '1', '200', '300', '500'],
          ['Palm tree 3.5 ft: wire, jute, paper or card fronds', '1', '200', '300', '500'],
          ['Washing line, hanging lamps, chickens (clay)', 'lot', '200', '300', '500'],
          ['Lime plaster / PoP + white paint', 'lot', '1,600', '2,400', '3,000'],
          ['Doors, beams, stairs (balsa, bamboo)', 'lot', '700', '700', '1,000'],
          ['Cobbles: cut cork or grooved clay', 'lot', '400', '600', '900'],
          ['Census scene: table, scribe, soldier, 3 villagers', '5 figures', '0', '2,000', '5,500'],
          ['Donkeys with panniers', '2', '0', '800', '2,500'],
          ['Travellers', '2', '0', '800', '2,000'],
          ['Well: PVC ring, pebbles, blue plastic sheet for the water', '1', '500', '500', '800'],
          ['Miniature props: jars, baskets, barrels', 'lot', '600', '600', '1,000']],
    before=['Leave 20 small window holes (houses 1–5: 6, 5, 4, 3, 2) and a 1 ft cable tail inside each house (block H fits the lamps).', 'Keep 1 in clear below the drape bottom (block J).'],
    done=['Five plywood houses, screwed, putty-textured and lime-washed, stepping down 3.5 → 1.5 ft toward the back; plain flat roofs.', 'Street is flat with a cobble pattern.', 'Well has a blue plastic-sheet water surface (no real water).', 'Figures stand without glue; cable tails reach the right-wall trunk.'],
    hands='Sits against the right wall on A. H fits the window lamps. Olive trees and plaque are in L.',
    tools='Jigsaw or hand saw, drill + 3 mm bit, screwdriver, sandpaper, putty knife, glue gun, brushes')

add('H', name='Lights (one plug, one box)', items='1 path of light, 27 box, 28 speaker; every light in the crib',
    window='23 Nov → 22 Dec (bench build first)', days='9',
    where='One plug from the church socket (right behind the stage, back-left corner) into one box at the back-left of the upper level (hatch A, x 0–1.2, y 0.2–1.0). 12 V and 5 V inside the crib. Four trunks: left, back (with the ceiling feed at the back-right corner), right, centre. Three hand switches.',
    rows=[['Distribution box: metal box, 6 A MCB, 30 mA RCCB, 3 switches, fuse block, inlet lead + plug', '1', '1,500', '2,500', '4,000'],
          ['12 V 10 A power supplies', '2', '1,000', '1,400', '2,200'],
          ['5 V 5 A power supply (USB lights, speaker)', '1', '300', '400', '600'],
          ['Cave: 2 warm COB LEDs 12 V (2700 K) + dimmer knob', '2+1', '400', '950', '1,500'],
          ['Manger spot (warm white) + cross-shadow lamp (warm, fixed)', '2', '300', '600', '1,000'],
          ['House room lamps, warm flicker', '3', '150', '400', '600'],
          ['Window lamps, warm flicker 2200–2400 K', '15', '500', '1,000', '1,500'],
          ['Campfire, orange flicker', '1', '100', '300', '500'],
          ['Path of light: 3 m warm LED strip (2200–2700 K) + channel + diffuser', '1', '800', '1,500', '2,200'],
          ['Field floods 10 W 12 V (3500–4000 K) + small stands', '2', '600', '1,200', '2,000'],
          ['Angel lamp 10 W cool white (5000 K), clip type', '1', '300', '600', '1,000'],
          ['Night-sky wash: 3 × 10 W 12 V cool-white floods + deep night-blue gel + small stands', '3', '1,200', '2,300', '3,500'],
          ['Star points: 5 strings × 3 m steady cool white (6000 K), a few warm', '5', '800', '1,500', '2,500'],
          ['Star burst: 10 W warm LED (2700–3000 K)', '1', '300', '600', '900'],
          ['Cloud spiral: 5 strings × 3 m micro-LED, steady warm white', '5', '600', '1,200', '1,800'],
          ['Far village + Magi lanterns: 40 micro LEDs, warm', '40', '400', '800', '1,200'],
          ['Pond: 2 small cool-white LEDs under the clear sheet', '2', '300', '600', '900'],
          ['Speaker, Bluetooth 10 W (60 dB or less at the public spot)', '1', '0', '1,200', '2,000'],
          ['Cable (trunks 1.5 mm², branches 0.75 mm²), connectors, fuses, heat-shrink, ties, labels', 'lot', '1,500', '2,500', '3,500'],
          ['Electrician: 1 day, a required safety check of the box, earthing and RCCB', '1', '500', '1,000', '1,500']],
    before=['Confirm the church socket behind the stage: its exact spot and circuit rating.', 'Collect the light-point list from every block (hole + 1 ft cable tail at each).', 'Colour rule: gold only in the cave, star, path, lamps and Magi lanterns. No red, bright green, pink, multicolour, flashing or UV lights.'],
    done=['Bench test passed: every light works for 10 s on its own switch.', 'Only one 230 V plug; no mains voltage anywhere inside the crib.', 'An electrician has checked the box, earthing and RCCB.', 'Run-through of the 3 switches (Lamps, Night sky, Glory) looks right from the public spot.'],
    hands='Feeds every block. Install after the other blocks are placed (14–17 Dec), then aim and rehearse (18–23 Dec).',
    tools='Soldering iron, multimeter, wire strippers, screwdrivers, heat-shrink, ladder')

add('I', name='Star and cloud spiral', items='6 cloud and angel spiral, 7 star burst with bead strands',
    window='30 Nov → 21 Dec', days='6',
    where='Hangs from the ceiling over the right-back corner: star 2 ft wide about 1 ft below the ceiling at x 7.8, y 1.2; 30 strands of plastic crystal beads 6 ft long on a 1.8 ft ring; spiral 2.5 ft wide, 3 turns, ending 4.5 ft above the deck near x 6.0, y 4.9. Five gold threads run from the star down to the cave roof as rays. Three hang points only.',
    rows=[['Polyfill / cotton wool', '3 kg', '900', '900', '1,200'],
          ['Galvanised wire 3 mm + florist wire', '20 m', '800', '800', '1,000'],
          ['Star base: foil, card or foam core + silver', '1', '600', '600', '900'],
          ['Plastic crystal-bead strands, 6 ft each', '30', '500', '1,250', '2,500'],
          ['Small pipe-cleaner angels for the spiral (same method as F)', '30', '300', '500', '900'],
          ['Fishing line 20 kg, swivels, anchors, hooks (3 hang points)', 'lot', '600', '600', '900'],
          ['Ladder / scaffold hire', '2 days', '0', '1,500', '3,000'],
          ['Gold metallic thread for the star rays', '5 × 10 ft', '100', '150', '250']],
    before=['Measure the ceiling height and type; plasterboard needs toggle anchors or a rope over a beam. Mark the 3 hang points with a plumb line.', 'Ask the church about working at height; two people at all times.'],
    done=['Built and lit at floor level first; hung last.', 'Two lines per hang point, never a single line.', 'Light cables from block H are tied along the lines to the ceiling feed.', 'Cascade lines stay 2 m clear of any sambrani holder.'],
    hands='Hangs above the hill. H fits the star light, the spiral strings and the ceiling feed. Hang after the drape track (J) is fitted.',
    tools='Ladder or scaffold, plumb line, pliers, wire cutters, fire-retardant spray')

add('J', name='Backdrop', items='26 hills print, blue drape, gold stars, painted angel choir',
    window='20 Nov → 17 Dec', days='7',
    where='Both walls: back wall 9 ft and right wall 16 ft, rounded corner. Print 5 ft high; blue drape from 5 ft up to the ceiling (about 13 ft above the deck); about 120 gold stars; 12 angels 2 ft tall painted white and silver. A plywood far-hill silhouette 5.4 ft long (x 3.6–9.0) stands on the upper level 2.5 ft high in front of the print; three palm cut-outs 1.2 × 4 ft are fixed to the drape (two on the back wall, one on the right wall). Star lights are fitted behind the drape by block H.',
    rows=[['Hills print on matt fabric / flex, 5 × 25 ft', '125 sq ft', '800', '1,750', '4,400'],
          ['Blue drape, 8.5 ft drop × 25 ft (poly vs velvet)', '~28 m', '1,800', '2,600', '5,200'],
          ['Gold stars: card + glitter + glue', '120', '600', '600', '1,000'],
          ['Curtain track, rope, hooks, clamps', '25 ft', '700', '1,500', '2,500'],
          ['Stitching + pleat tape', 'lot', '0', '1,000', '1,600'],
          ['Choir angels 2 ft, card or foam, white and silver paint', '12', '300', '600', '900'],
          ['Far-hill silhouette: 4 mm plywood 5.4 × 2.5 ft + 2 feet', '1', '400', '700', '900'],
          ['Palm cut-outs 1.2 × 4 ft: card or 4 mm plywood, dark paint', '3', '300', '500', '800']],
    before=['Order the print and drape early; they are long-lead items.', 'Measure the real ceiling height; drape cost scales with it (about ₹280 per extra foot of drop).', 'Leave a pocket along the top of the print for the star lights (block H).'],
    done=['Track and rope backup fitted; print joins flat from V.', 'Drape pleats even at 1.5× fullness; the hem laps the print by 6 in.', 'Twelve painted angels in white and silver, no glow paint.', 'Gold stars in irregular clusters; no colour other than the palette.'],
    hands='Hangs on both walls. H fits the star points and the night-sky wash. Houses (G) leave 1 in below the drape.',
    tools='Drill, rope, clamps, sewing machine, scissors')

add('K', name='Far village and Magi caravan', items='14 far village (1:24), 15 Magi caravan on a wall shelf',
    window='10 Dec → 17 Dec', days='4',
    where='Right-wall crest: a rock ridge 3.8 × 0.8 ft and 3 ft high (x 7.8–8.6, y 5.2–9.0) carrying 20 tiny houses; Magi shelf 3 × 0.3 ft at +3.6 ft on the right wall (x 8.7–9.0, y 5.4–8.4). Both at bearings 38–49° from V, clear of the cave house.',
    rows=[['Rock ridge base 3.8 × 0.8 × 3 ft: thermocol 4 in + plaster', '1', '1,050', '1,400', '1,800'],
          ['Thermocol 1 in + clay for 20 houses', '1 sheet', '800', '800', '1,200'],
          ['Pale cream / blue paint', 'lot', '500', '500', '600'],
          ['1:24 caravan: 3 kings, camels, servant', 'set', '0', '1,500', '3,500'],
          ['Wall shelf (ply, 3 ft)', '1', '300', '300', '400']],
    before=['Re-run the sightline check from V before fixing; the first layout hid both behind the house.', 'Leave 40 micro-LED points and a 1 ft cable tail (block H fits them).'],
    done=['From V both are visible and not hidden by the house.', 'Houses are pale cream with blue shadows (tier D).', 'Ridge and shelf are fixed firmly.', 'Cable tails reach the right-wall trunk.'],
    hands='Sits on the right wall beside B. H fits the micro LEDs and the lanterns.',
    tools='Craft knife, tweezers, small brushes')

add('L', name='Foreground and view spot', items='23–24 olive trees, 25 "find 12 details" plaque, 30 public view spot and rope',
    window='19 Dec → 23 Dec (olives and plaque can start earlier)', days='4',
    where='V is 3 ft left and 3 ft in front of the stage corner, eye 5.2 ft above the floor. Rope barrier curved 5 ft from the stage front, 4 ft clear aisle. Olive 23 grows from the front-left rocks at x 0.7, y 14.3 (2.6 ft tall); olive 24 at x 3.7, y 12.3 (1.8 ft); plaque 2 × 0.4 ft at x 3.2–5.2, y 15.5–15.9.',
    rows=[['Jute rope 15 m + 4 brass or wood posts', '1 set', '1,000', '1,200', '2,200'],
          ['Floor marker, signage, printing', 'lot', '300', '400', '800'],
          ['CO2 extinguisher (if the church has none)', '1', '0', '0', '3,000'],
          ['Sambrani brass holder (closed)', '1', '300', '300', '800'],
          ['Olive trees (wire, jute, paper, dried leaves)', '2', '800', '800', '1,200'],
          ['Plaque: wood + printed icons', '1', '300', '900', '1,500']],
    before=['Confirm the extinguisher location and the exit with the church.', 'Print the signs (A4, large type).'],
    done=['Six people can stand at V with the full view.', '4 ft clear aisle for wheelchairs; cables under a ramp or taped flat.', 'Olive trees are darker and less saturated than the field behind.', 'Extinguisher and exit are marked.'],
    hands='Last to place. Plaque and olives stand on A at the front; the rope and signs are on the church floor.',
    tools='Rope, posts, floor tape, printer, wire, jute')

add('M', name='Photo corner: pond and selfie mirror', items='31 pond, 32 selfie mirror (photo spot at the front-left start of the stage)',
    window='11 Dec → 20 Dec', days='4',
    where='Pond 1.6 × 3 ft, long side front to back along the left edge (x 0.35–1.95, y 10.3–13.3). Selfie mirror 2 ft wide × 5 ft tall on the church floor, centre 6 ft left of the stage edge and 3 ft left of V (x −6, y 19), faces the queue, turned about 23° toward the crib so a visitor at V sees the crib behind them.',
    rows=[['Acrylic mirror sheet 2 × 5 ft (shatter-safe, not glass)', '1', '0', '3,500', '6,000'],
          ['Mirror frame (2 × 2 in + 12 mm ply back) and weighted base', '1 set', '800', '1,200', '2,000'],
          ['Pond tray (12 mm ply 1.6 × 3 ft), blue cloth, clear 3 mm sheet', '1', '400', '700', '1,200'],
          ['Pebbles, sand, artificial reeds', 'lot', '300', '500', '900'],
          ['Sign "Take a photo, share it" + floor marker', 'lot', '100', '200', '400']],
    before=['Check with the church that a floor mirror is allowed.', 'Costs are estimates; get quotes before buying the mirror sheet.'],
    done=['Pond is a safe flat tray, no water on the deck; pond lights are fitted by H.', 'Mirror is anchored on its weighted base and cannot tip; all edges covered.', 'A person at V sees the crib behind them in the mirror.', 'The mirror and its queue do not block the view from V; 4 ft aisle clear.'],
    hands='Pond sits on A at the front-left (H fits its lights). The mirror stands on the church floor beside V and the rope barrier (L).',
    tools='Saw, drill, staple gun, spirit level, phone for the angle test')

add('N', name='Foreground: rocks, shepherd boy, front wall', items='33 rock outcrop, 34 shepherd boy with lamb, 35 front dry-stone wall, 36 dog, water jar, herbs and reeds',
    window='7 Dec → 20 Dec', days='5',
    where='The front 2.5 ft of the stage, nearest the visitors (largest and darkest things in the crib). Rock outcrop 1.7 × 2.4 ft, 1 ft high, in the front-left corner (x 0–1.7, y 13.6–16, leaving hatch C free) with olive 23 growing from it. Shepherd boy 1.3 ft (sitting, 1:3) with a lamb at x 2.5–3.1, y 14.9–15.4, facing the cave. Front dry-stone wall 1.85 × 0.3 ft, 0.6 ft high (x 3.4–5.25, y 14.6). Dog, water jar, herbs and reeds.',
    rows=[['Real rocks and pebbles (collected), thermocol 4 in core', 'lot + 1 sheet', '300', '800', '1,200'],
          ['PoP + grout + earth paint', '1 bag', '400', '500', '700'],
          ['Shepherd boy 1.3 ft sitting, with a lamb (reuse 2023 or clay)', '1', '0', '1,500', '3,500'],
          ['Sleeping dog (clay) and a terracotta water jar', '2', '100', '300', '600'],
          ['Herbs, reeds, dry grass, moss', 'lot', '100', '200', '400']],
    before=['Leave hatch C (x 0–1, y 15–16) free: the rocks stop at x 1.05 there.', 'Agree the olive 23 hole with block L: the tree grows out of the rocks.'],
    done=['From V the rocks, boy and wall frame the scene but hide nothing (check from V).', 'Everything here is darker and larger than the field behind.', 'Hatch C opens without moving a rock.', 'Each piece lifts out on its own.'],
    hands='Sits on A at the front. L plants olive 23 in the rocks; H runs the path of light between them.',
    tools='Hot knife, trowel, glue gun, brushes, gloves')
for _k, _t in TEAMS.items(): B[_k]['team'] = _t

ORDER = list('ABCEFGHIJKLMN')
ALL = ORDER
ADDITIONAL = []

def rgb(k): return 'rgb(%d,%d,%d)' % COL[k]

def chrome():
    for p in ('C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'):
        if os.path.exists(p): return p

def pdf(htmlpath, pdfpath):
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--user-data-dir=' + os.path.join(os.environ.get('TEMP', '.'), 'crib_chrome_profile'), '--virtual-time-budget=5000',
                    '--no-pdf-header-footer', f'--print-to-pdf={pdfpath}', 'file:///' + htmlpath.replace('\\', '/')], check=True, capture_output=True, timeout=90)

import crew_steps as _cs
for _k in B:
    B[_k]['steps'] = _cs.X[_k]['steps']
