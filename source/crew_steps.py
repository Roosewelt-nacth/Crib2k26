"""Exact build data per block for the crew pack: cut/make list and numbered steps with measurements.
Sizes are the pack's figures (feet, inches). Positions are measured from the LEFT edge (x) and the BACK wall (y) of the 9 x 16 ft stage.
Things marked 'about' are working sizes: confirm on the first mock-up."""

STACK_NOTE = ('STACK NOTE (cave, hill, house): the pack gives the house floor 2.8 ft above the cave floor and the room 1.5 ft high, so the room top is 4.3 ft above the cave floor. '
              'Make a cardboard mock-up of cave + house first, stand it on the frame ramp and look at it from the public spot before cutting thermocol.')

X = {}

X['A'] = dict(
 cut=[('Frame sections', '8 sections, each 4 × 4 ft (2 across × 4 deep), plus 4 strips 1 ft × 4 ft along the right wall = 9 × 16 ft'),
      ('Batten 2 × 2 in', 'about 160 ft in total: 4 sides + 2 cross battens (at 2 ft centres) per section, plus legs'),
      ('Legs (2 × 2 in) by distance f from the front edge', 'f 0–5.5 ft: none (flat on the deck) · f 6.5 ft: 0.3 ft (4 in) · f 8 ft: 1.8 ft (22 in) · f 9–16 ft: 3.0 ft (36 in); ramp straight between these'),
      ('Plywood 9–12 mm', '5 sheets of 8 × 4 ft, cut to cover 9 × 16 ft (144 sq ft)'),
      ('Hatch lids (loose plywood)', 'A: 1.2 × 0.8 ft at x 7.6, y 15.2 (front right) · B: 1.3 × 0.6 ft at x 0.9, y 3.7 (angel screen) · C: 1 × 1 ft at x 0, y 11.2 (speaker)'),
      ('Skirting, black pleated', '25 ft run (9 ft front + 16 ft left), 2 ft drop, fixed with Velcro')],
 steps=['On site: measure the real deck. The plan assumes it is 2 ft high and a free 9 × 16 ft. Mark the 9 × 16 ft rectangle with tape and tick every 4 ft along the front and the left side.',
        'Workshop: lay out 2 × 2 in battens in 4 × 4 ft squares. Fix the 4 sides with screws (not glue), then add one cross batten each way at the 2 ft centre. Make 8 squares and 4 strips of 1 × 4 ft. Number each section in marker.',
        'Cut legs to the heights in the cut list (front part flat, then the ramp, then 3.0 ft at the back). Screw legs to the section corners and mid-points under the ramp and back area.',
        'Cross-brace every leg taller than 1.5 ft with diagonal battens in both directions.',
        'Skin the tops with 9–12 mm plywood, screws about every 6 in at the edges and 12 in inside. Cut and leave the three hatch lids loose (sizes and places in the cut list).',
        'Fix the black skirting with Velcro along the front edge (9 ft) and the left edge (16 ft), 2 ft drop, so the open sides are hidden to the floor.',
        'Spray all cloth and any thermocol with fire retardant (4 L in total).',
        'Dry-fit the whole 9 × 16 ft frame in the workshop on a taped outline. Stand two people on each section: it must not flex. Check every section passes through the church door.'],
 )

X['B'] = dict(
 cut=[('Thermocol 4 in', '8 sheets of 8 × 4 ft, glued in layers up to about 3 ft high (9 layers at the highest point)'),
      ('Cave inside', '4 ft long × 2.5 ft deep, arch 3 ft wide × 2.5 ft high; centre at x 4.4 ft, y 7.4 ft; turned 33° so the mouth faces the public spot V'),
      ('Plywood base 12 mm', 'one base under the hill, 7 × 6 ft in pieces no wider than 4 ft; keep 1 ft free behind for wiring'),
      ('Figures (hero scale 1:3)', 'Mary, Joseph and baby about 2 ft tall for a standing figure; Holy Family group 3 ft × 1.2 ft; ox and donkey about 1 ft'),
      ('Manger', 'thermocol + plaster, about 1 ft long, with clay lamp'),
      ('Lights', '2 warm COB LEDs 12 V (2200–2700 K) on one dimmer, hidden above the lintel')],
 steps=['Make a cardboard mock-up of the arch (3 ft wide × 2.5 ft high) and the cave plan (4 × 2.5 ft). ' + STACK_NOTE,
        'Cut 4 in thermocol to the hill outline (see top view) and glue the layers with PVA up to about 3 ft. Seal every layer with PVA. Keep 1 ft free behind.',
        'Mark the cave on the top layer with its centre at x 4.4 ft, y 7.4 ft, turned 33°. Cut the 4 × 2.5 ft inside with the hot knife and cut the arch to the template.',
        'Carve horizontal strata and cracks on the outside with the hot knife; step the rock face up toward the right-wall crest (+3.0 ft).',
        'Fit chicken mesh over the arch and overhangs. Coat everything with plaster of Paris + PVA, 3 mm thick. While wet, press on sand/grout and real pebbles and dry grass.',
        'Dry-brush sand, then ochre, then olive; darker in the cracks. Paint the cave inside near-black. Keep the rock around the cave one shade darker than the rest so the gold glows.',
        'Hide the COB LED above the lintel; run the wires through the back to hatch A with a 1 ft service loop. Mark the cross-shadow lamp position for the 3:00 cue.',
        'Make the manger and clay lamp, lay straw, then place Mary, Joseph, baby, ox and donkey last (group about 3 × 1.2 ft, in the cave).',
        'Split the whole unit into numbered pieces, none wider than 4 ft, and check each passes the church door.'],
 )

X['C'] = dict(
 cut=[('Floor tray, plywood 12 mm', '4 ft × 2 ft'),
      ('Walls, thermocol 2 in thick', 'back wall 4 ft × 1.5 ft high; two side walls 2 ft × 1.5 ft high; the front is cut open'),
      ('Roof slab', '4 ft × 2 ft, with a parapet about 3 in high around it'),
      ('Posts 2 × 2 in', '2 posts, length 2.8 ft (34 in) minus the plywood thickness, standing on the cave base (not on the cave roof)'),
      ('Outside stair', '8 steps, total rise 2.8 ft (34 in), so each step rises about 4.2 in; tread about 6 in'),
      ('Dressing', '6 sleeping travellers 1:6 (about 1 ft long), 3 flicker lamps on one 3 V line, jars, mats, blankets; cat on the roof, clay oven, sleeping child')],
 steps=['Check the cave arch (2.5 ft) with the mock-up (see block B). ' + STACK_NOTE,
        'Cut the 12 mm plywood floor tray 4 × 2 ft. It rests on the hill top and on two 2 × 2 in posts that stand on the cave base. Cut the posts so the floor is 2.8 ft above the cave floor.',
        'Cut the walls from 2 in thermocol: back wall 4 ft × 1.5 ft, side walls 2 ft × 1.5 ft. Glue them to the tray. Leave the front open (cut away).',
        'Make the flat roof slab 4 × 2 ft with a 3 in parapet; fit it on top. Whole room must weigh under 8 kg.',
        'Plaster and whitewash. Cut stone steps down one side: 8 steps, each about 4.2 in high, about 6 in deep.',
        'Dress the room: mats, blankets, jars, six sleepers, three flicker lamps wired together on one 3 V line.',
        'Add the hidden details: cat on the roof, clay oven, sleeping child.',
        'Run the lamp wires down through the hill to hatch A. Check the room lifts off the cave as one piece.'],
 )

X['E'] = dict(
 cut=[('Terrace boxes (plywood)', '4 boxes, each 3.4 ft wide × 1.75 ft deep, tops at +2.0, +1.6, +1.2 and +0.8 ft; stack from the back wall: 2.0 at y 0–1.75, 1.6 at y 1.75–3.5, 1.2 at y 3.5–5.25, 0.8 at y 5.25–7.0'),
      ('Shepherd ledge', '1.7 ft × 2.6 ft at +0.8 ft (x 0.2–1.9, y 7.0–9.6) for the shepherds, sheep and campfire'),
      ('Faces', '2 in thermocol carved as dry-stone walls, real pebbles on the fronts, soil/sand on the treads, artificial grass and moss'),
      ('Sheepfold', 'ring of pebbles 2.0 × 1.3 ft, walls 3 in high, thorn gate, scale 1:12'),
      ('Watchtower', 'PVC pipe core, finished 1 ft across and 1.5 ft tall, pebble clay'),
      ('Figures', '2 shepherds 1.2 ft tall (1:6): one old with a staff, one young with a lamb; 6 wool sheep about 5 in long; campfire of twigs with an orange flicker LED')],
 steps=['Agree the ridge position with block F (floating angel): the ridge sits at y 4.6–5.6 in the same zone.',
        'Build four plywood boxes 3.4 ft wide × 1.75 ft deep with tops at 0.8, 1.2, 1.6 and 2.0 ft. Screw each to block A in order from the back wall (tallest at the back).',
        'Face the box fronts with 2 in thermocol carved as dry-stone walls; glue real pebbles on the fronts.',
        'Cover the treads with soil or sand, then patches of artificial grass and moss. Paint olive treads, sand paths, limestone walls.',
        'Build the sheepfold (pebble ring 2.0 × 1.3 ft, thorn gate) at x 0.4–2.4, y 1.75–3.05.',
        'Build the watchtower at x 3.0, y 1.0 (1 ft across, 1.5 ft tall) on the +2.0 ft terrace.',
        'Build the shepherd ledge 1.7 × 2.6 ft at +0.8 ft (x 0.2–1.9, y 7.0–9.6). Place the 2 shepherds, 6 sheep and the campfire last.',
        'Wire the campfire LED to hatch A with a 1 ft service loop. Check the boxes lift out one at a time.'],
 )

X['F'] = dict(
 cut=[('Black box', '2.4 ft × 1.4 ft, behind the ridge, screen face-up inside'),
      ('Acrylic 3 mm clear', '2.4 ft wide × 2 ft slant, leaning at 45° toward the viewer, base run 1.4 ft'),
      ('Rock ridge', '2.4 ft × 1.0 ft, 0.8 ft (10 in) high, hides the screen (x 0.3–2.7, y 4.6–5.6)'),
      ('Mister tray', 'shallow tray behind the ridge lip, 3 cm of water, 2 ultrasonic discs and a 5 V fan, float switch'),
      ('Screen', 'tablet or 10–13 in monitor, face-up, maximum brightness, black background video'),
      ('Video', '20 s loop: white angel on pure black, mirrored left-right, angel on screen about 0.7–1 ft')],
 steps=['Build the plywood box 2.4 × 1.4 ft and paint the inside matt black. Fix the screen face-up inside.',
        'Mount the acrylic at 45°, leaning toward the viewer at the top; the screen is lit below it and the glass reflects it.',
        'Cover everything except the acrylic with black cloth. The ridge (0.8 ft high) must hide the screen.',
        'Build the rock ridge from thermocol + plaster 2.4 × 1.0 ft × 0.8 ft; paint it as the rock around it.',
        'Make the 20 s angel video (white on black, mirrored left-right). Test at night from the public spot and tune the glass angle and brightness.',
        'Fit the mister tray behind the ridge lip with 3 cm of water and the float switch, on its own relay (on from 1:00 to 3:30). Keep a lip so mist never reaches the screen.',
        'Before each show wipe the acrylic with a microfibre cloth (fingerprints show as ghosts).'],
 )

X['G'] = dict(
 cut=[('House A', '1.4 × 1.6 ft, 2.0 ft high (x 7.6–9.0, y 9.4–11.0)'),
      ('House B (outside stair)', '1.6 × 1.8 ft, 2.5 ft high (x 7.4–9.0, y 11.3–13.1)'),
      ('House C', '1.4 × 1.6 ft, 1.8 ft high (x 7.6–9.0, y 13.4–15.0)'),
      ('Cobbled street', '1.1 ft wide × 6.7 ft long, sloping from +0.3 ft at the front to +0.8 ft at the back (x 6.2–7.3, y 9.3–16.0)'),
      ('Well', '0.9 ft across, 0.6 ft high, sealed resin pool (centre x 5.6, y 11.2)'),
      ('Census scene', 'table 1.4 × 1.0 ft with soldier, scribe and scrolls, figures 1.2 ft (x 4.5–5.9, y 12.8–13.8); 2 donkeys 1.2 × 0.6 ft, 0.6 ft high, and 2 travellers (x 4.6–5.8, y 10.0–10.6)'),
      ('Lamps', '15 flicker LEDs in the windows on one 3 V line, wires to hatch A')],
 steps=['Cut house blocks from 2 in thermocol: A 1.4 × 1.6 ft × 2.0 ft, B 1.6 × 1.8 ft × 2.5 ft, C 1.4 × 1.6 ft × 1.8 ft. Cut doors (about 0.9 ft high at 1:6) and windows.',
        'Add wood lintels and the outside stair on house B.',
        'Plaster, lime-wash and stain the cut edges with a thin brown glaze. Walls stay 2 in thick.',
        'Make the street 1.1 × 6.7 ft, sloping 0.3 → 0.8 ft; pave with cut cork or grooved clay; add a drainage channel.',
        'Build the well (0.9 ft across, 0.6 ft high) with a sealed resin pool.',
        'Place the houses against the right wall; keep 1 in clear below the drape (block J) bottom.',
        'Fit the 15 window lamps and run the wires through the base to hatch A.',
        'Place the census scene, donkeys and travellers last (figures 1.2 ft tall, 1:6).'],
 )

X['H'] = dict(
 cut=[('Path of light', 'groove 14 mm wide, 0.5 ft (6 in) wide path, 7.7 ft long, from the front edge (x 1.9, y 15.9) to the cave mouth (x 3.7, y 8.5); WS2812B strip 3 m (60 LED/m), channel 10 mm, diffuser 3 mm, fine sand on top'),
      ('Control box', 'under the deck at hatch A (x 7.6–8.8, y 15.2–16.0), ESP32 ×2 (one spare), 8-channel relay, 4 MOSFET dimmers, DFPlayer + amp'),
      ('Power', '12 V 10 A, 5 V 10 A, 24 V 2 A (mister), 12 V 3 A (lamps); a fuse on each rail, one common ground'),
      ('Speakers', '2 × 5 W at hatch C (x 0, y 11.3); sound at 60 dB or less at the public spot'),
      ('UV bars 395 nm', '2 × 1 m behind the backdrop lip, about 5 ft above the deck'),
      ('Lights', '3 RGBW wash bars, 3 warm COB spots, 35 flicker lamps')],
 steps=['Wire everything on a bench board first. Test each channel for 10 seconds.',
        'Keep 12 V and 5 V rails separate, one fuse each, one common ground. Label every cable at both ends and leave a 1 ft service loop at each hatch.',
        'Path of light: cut a 14 mm groove along the path; fit the channel flush; solder the strip (5 V, GND, data) and seal with heat-shrink; add a 470 Ω resistor on the data line and a 1000 µF capacitor across the supply.',
        'Fix the frosted diffuser over the LEDs; glue fine sand on top and pebbles at the edges; the path must never cross a solid object.',
        'Run the data to hatch A. Test the chase at 20 pixels per second (a bright 8-pixel comet runs front edge to cave mouth in 7 s at 2:30).',
        'Program the 4-minute cue sheet (0:00 dusk, 0:30 night, 1:00 stars and mist, 1:40 angel, 2:30 path chase, 3:00 cave glow and cross-shadow, 3:30 all warm, 3:55 fade and loop). Add a start button and manual override.',
        'Set the audio to 60 dB or less at the public spot.',
        'An electrician checks earthing and the RCCB before the first full run. There is no mains voltage inside the crib.'],
 )

X['I'] = dict(
 cut=[('Star burst', '2 ft wide, foam core 25 mm + tinsel, 10 W warm LED in the centre, hung about 1 ft below the ceiling at x 7.8, y 1.2 (ceiling corner)'),
      ('Bead strands', '60 strands, each 6 ft of crystal beads, on a 1.8 ft ring, one every 6°'),
      ('Spiral frame', 'galvanised wire 3 mm, ribbon 2.5 ft wide wound as a 3-turn helix, skinned in polyfill; ends about 4.5 ft above the deck near x 7.3, y 6'),
      ('Angels', '30 mini angels 4–6 in (paper/feather), 5 strings of micro-LED fairy lights (3 m each)'),
      ('Hang points', '7 points on the ceiling: A the star ring (4 lines to the hub), B–G six anchors along a 1.8 ft spiral line; two 20 kg fishing lines or 0.5 mm wires per point'),
      ('Height', 'ceiling about 15 ft above the church floor (13 ft above the deck): CONFIRM on site; if higher, strands and lines get longer')],
 steps=['Measure the ceiling height and check its type (concrete, beam or plasterboard); plasterboard needs toggle anchors or a rope over a beam. Mark the 7 hang points with a plumb line.',
        'Build the 2 ft star on a 25 mm foam core with tinsel and a 10 W warm LED in the centre.',
        'Make the 1.8 ft ring and fix 60 strands of beads, each 6 ft long, one every 6°.',
        'Wind the 3 mm wire helix 2.5 ft wide, 3 turns, brace with cross-wires. Skin it with teased polyfill, sprayed with fire retardant.',
        'Fix the 30 angels (each on a 4 in loop) and tuck the 5 micro-LED strings into the clouds.',
        'Test everything lit at floor level first.',
        'Hang last, with two people and a ladder or scaffold: two lines per hang point, never a single line. Trim only when everything is lit.',
        'Keep the cascade at least 2 m from any sambrani holder.'],
 )

X['J'] = dict(
 cut=[('Hills print', '5 panels, each 5 ft × 5 ft = 25 ft run (back wall 9 ft + right wall 16 ft), twilight Judean hills'),
      ('Blue drape', 'drop 8.5 ft (from 5 ft up to about 13.5 ft), 25 ft run, 1.5× pleat fullness (about 28 m of fabric); bottom hem laps the print by 6 in'),
      ('Track + rope backup', '25 ft ceiling track along both walls, rope backup, rings, hooks, clamps; track about 13 ft above the deck'),
      ('Fibre-optic stars', '250 ends in the top band, bundled to one 1 ft bundle behind the drape at the corner'),
      ('Gold stars', 'about 120 stars of card + glitter, glued in irregular clusters'),
      ('UV angels', '12 angels 2 ft tall in UV-reactive paint; 2 UV bars 395 nm × 1 m behind a 4 in lip at the top of the print')],
 steps=['Measure the real ceiling height: the drape length and cost depend on it.',
        'Fit the ceiling track and a rope backup along both walls first.',
        'Hang the 5 print panels, each 5 × 5 ft, and tape the joins flat. The corner is rounded with a 1.5 ft radius.',
        'Sew and pleat the drape at 1.5× fullness and hang it on rings so its hem laps the print by 6 in.',
        'Push the 250 fibre ends through the top band, tape them behind and route to the fibre engine in the corner.',
        'Glue the gold stars in irregular clusters.',
        'Paint the 12 UV angels (2 ft tall) in thin matt coats.',
        'Fit the 2 UV bars behind the print lip and test in the dark. UV angels must be invisible with the lights on.'],
 )

X['K'] = dict(
 cut=[('Far village strip', '3.8 ft × 0.8 ft on the right-wall crest at +3.0 ft (x 7.8–8.6, y 5.2–9.0); 20 houses 3–5 in tall; 1 in thermocol + clay'),
      ('Magi shelf', '3 ft × 0.3 ft plywood shelf at +3.6 ft on the right wall (x 8.7–9.0, y 5.4–8.4), painted as a road'),
      ('Caravan', '1:24: 3 kings on camels, 1 servant; each king has a micro-LED lantern'),
      ('Lights', '40 micro LEDs 3 mm for the windows and lanterns, wired to hatch A'),
      ('Bearings from V', 'both must sit at 38–49°, clear of the cave house (25–41°)')],
 steps=['Re-run the sightline check from the public spot V before fixing anything: the first layout hid both behind the house.',
        'Cut a 3.8 × 0.8 ft strip and make 20 houses 3–5 in tall; paint them pale with blue shadows (tier D: paler, cooler, less saturated).',
        'Place the strip at y 5.2–9.0 on the right-wall crest at +3.0 ft.',
        'Fix the 3 × 0.3 ft plywood shelf at +3.6 ft and paint a road line on it.',
        'Mount the caravan on the shelf and fit micro-LED lanterns on the kings.',
        'Check from the public spot that both are visible and not hidden by the house.'],
 )

X['L'] = dict(
 cut=[('Olive tree 23', 'front left at x 1.0, y 14.2; canopy about 2 ft wide, 2.0 ft tall; wire, jute, paper, dried leaves, umber trunk'),
      ('Olive tree 24', 'at x 5.4, y 14.9; 1.6 ft tall'),
      ('Plaque', '2 ft × 0.4 ft, 0.8 ft high, at the front edge (x 3.2–5.2, y 15.5–15.9), 12 hidden icons'),
      ('Rope barrier', '15 m jute rope + 4 posts, curved 5 ft from the stage front; keep a 4 ft clear aisle'),
      ('Public spot V', '3 ft left and 3 ft in front of the stage corner; eye height 5.2 ft above the floor; room for 6 people at a time'),
      ('Signs and safety', 'A4 signs, CO₂ extinguisher location, floor marker; cables under a ramp or taped flat')],
 steps=['Mark V on the church floor: 3 ft to the left of and 3 ft in front of the front-left corner of the stage.',
        'Make the two olive trees (wire, jute, paper, dried leaves) with umber trunks; darker and less saturated than the field behind them.',
        'Place olive 23 at x 1.0, y 14.2 and olive 24 at x 5.4, y 14.9 as the dark framing in the front corners.',
        'Make the plaque 2 × 0.4 ft with 12 hidden details and place it at the front edge.',
        'Curve the rope barrier 5 ft from the stage front, with 4 posts; keep a 4 ft clear aisle for wheelchairs.',
        'Place the signs ("Please stand here", "The crib shows every 10 minutes", "Find 12 details").',
        'Confirm the extinguisher location and the exit with the church; run cables under a ramp or tape them flat.',
        'Walk through with six people at V to confirm the sightlines.'],
 )
