# Crib 2026: image prompts, version 2 (church context fixed)

**What was wrong before:** the prompts said "church hall" and never said where the altar is. The model had no idea this is inside a church, with the altar at the centre and the crib in the right-hand corner at the end of the altar wall. Version 2 fixes that and gives the model a picture to copy instead of words alone.

## Attach these to the image model (in this order)

1. `crib-2026-ref-view1-visitor.png` : grey block-out of the exact layout, seen from the public spot (for prompts 2, 3 and 4)
2. `crib-2026-ref-view2-aisle.png` : grey block-out of the wide shot from the centre aisle (for prompt 1)
3. `crib-2026-church-key-plan.png` : where the crib sits in the church
4. Your three style images (daylight diorama, night show, cloud/angel cascade)

Tell the model once: **"The grey block-out images are the exact composition. Keep every position, size and angle. Replace the grey boxes with the real materials described below. Do not add objects that are not in the block-out."**

## Colour key for the block-out (paste after the line above)

```
Block-out key:
- big brown block in the centre = rock hill with the cave (cave mouth turned toward the camera)
- white box on top of the brown block = the upper guest room of the house, cut open at the front
- low pale slab across the back = the raised second level (1.5 ft high, dry-stone wall face); the shepherds' field is on the flat floor in front of it and on the slab
- blue panel on the left, above the field = the floating angel (a glowing angel in mid-air, nothing solid)
- three white-grey tall boxes on the right = flat-roofed village houses on a cobbled street
- pale low strip right of the cave, above the houses = far village on the ridge, tiny houses
- thin gold shelf above it on the right wall = Magi caravan, three kings on camels, tiny
- yellow line on the deck = a thin path of light running to the cave mouth
- flat light-blue slab in the front left = a shallow pond, 1.6 ft by 3 ft, pebble edge, a few reeds, cool-white light
- big green cylinders = two olive trees in the front corners
- pink box = Roman census table with a soldier and scribe; light-blue cylinder = stone well; white box front right = small wooden plaque
- white spiral from the corner of the ceiling = a spiral of cotton clouds with tiny white angels, hanging from a gold star burst with crystal strands
- blue wall = deep-blue velvet drape with gold stars; sand-colour lower wall = painted twilight Judean hills
```

## Where the items sit in the frame (from the public spot, computed from the blueprint)

| Item | Left to right in frame | Near or far |
|---|---|---|
| Terraces, sheepfold, watchtower, floating angel | left third (27–44%) | far, small |
| Shepherds with sheep and campfire | left, lower | near-middle |
| Cave, house, star and cascade | dead centre (about 50%) | cave middle, star far |
| Far village, Magi shelf | centre-right (55–67%), above the houses | far, tiny |
| Village street, houses, well, donkeys | right third (60–90%) | near to middle |
| Census table, olive tree, plaque | right, low | near |
| Path of light | starts bottom right of centre (about 75%), runs up to the cave | near to middle |

---

## Prompt 1: wide shot from the aisle (this one fixes the church context)

Attach image 2 (aisle block-out) + the key plan + your style images.

```
Use the attached grey block-out as the exact composition and the attached key plan for the setting. Create ONE real-looking photograph, taken on a phone, inside a Catholic parish church in India, from the centre aisle, standing about 60 feet back from the front, at adult eye height, looking toward the altar end.

SETTING: wooden pews on both sides of the centre aisle in the foreground. The church's altar stands at the centre-left of the frame on the front wall, with a white altar cloth and a few candles. To the RIGHT, at the very end of the front wall, in the right-hand corner of the church, is the Christmas crib: a raised platform about 2 feet high with black pleated skirting, filling the corner. The right side wall of the church runs from that corner toward the camera on the right of the frame. The crib is about one quarter of the frame width. Above the crib, deep-blue velvet drape with gold stars rises up both walls of the corner to the ceiling, and a white spiral of cotton clouds with tiny angels hangs down from a gold star burst in the corner of the ceiling. Everything else in the church is normal and unlit except the crib.

THE CRIB (as in the block-out and the key): a rock hill with a cave in the centre, a stone guest-room house on top, a shepherds' field on the left over two flat levels, a small cobbled village street on the right, a far village and a tiny camel caravan on the right wall above it. A thin path of golden light leads to the cave.

STYLE: real church interior, mixed daylight and warm interior lights, photorealistic, natural phone-camera exposure, slightly wide-angle, 16:9. The crib is handmade museum-quality, real stone, plaster, straw, clay and wool textures.
```

## Prompt 2: visitor view, lights ON

Attach image 1 (visitor block-out) + your daylight diorama style image + the three-image cascade reference.

```
Use the attached grey block-out as the exact composition. Create ONE real-looking photograph, taken on a phone, of a handmade Christmas crib built in the right-hand corner of a Catholic church, at the end of the altar wall, with the church lights on.

CAMERA: standing at the front-left corner of the crib platform, about 3 feet to its left and 3 feet in front of it, at adult standing eye height, wide-angle phone lens, looking diagonally into the far corner. The platform is about 2 feet high with black pleated skirting on its two open sides, filling the bottom of the frame. The short 9-foot altar wall is on the LEFT of the picture and the long 16-foot right wall recedes on the RIGHT. The church ceiling is visible at the top. The altar itself is NOT in the frame (it is behind the camera's left shoulder).

BACKDROP: on both walls, the lower 5 feet is a painted twilight Judean hills backdrop (rolling hills, a flat-topped conical fortress, an olive grove). Above it, deep-blue velvet drape with gold paper stars rises to the ceiling.

SCENE (first-century Bethlehem, hyper-realistic museum diorama, forced perspective: large figures at the front, small pale buildings far back):
- Centre: a limestone rock hill with a cave mouth 3 feet wide, turned toward the camera. In the cave: a carved stone manger with straw, an ox and a donkey, and Mary, Joseph and baby Jesus (2-foot figures). On top of the hill: a whitewashed stone house cut open to show an upper guest room full of sleeping travellers and clay jars.
- Left: a field on two flat levels (the back level raised 1.5 ft behind a dry-stone wall), a sheepfold, a round watchtower, two shepherds with real wool sheep and a campfire, a low rocky ridge.
- Right: a narrow cobbled street rising toward the back with three flat-roofed whitewashed houses, a stone well, donkeys, a Roman soldier at a census table. A gnarled olive tree at each front corner and a small wooden plaque at the front edge.
- Front left: a shallow rectangular pond with a pebble edge and a few reeds, lit softly in cool white.
- A narrow sandy path winds from the front-right of the platform to the cave mouth.
- On the right wall: a far village on the ridge, tiny and pale, and above it a shelf with a tiny caravan of three kings on camels.
- Overhead, from the far corner of the ceiling: a gold star burst with strands of crystal beads and a spiral of white cotton clouds with tiny white angels descending toward the hill (clouds, beads and angels only; no Christmas tree, no snow).

STYLE: real stone, plaster, straw, clay and wool, handmade, slightly imperfect, natural phone-camera exposure, mixed fluorescent and warm church lighting, photorealistic, 16:9.
```

## Prompt 3: visitor view, lights OFF (peak of the 4-minute show)

Attach image 1 (visitor block-out) + your night-show and cascade style images.

```
Use the attached grey block-out as the exact composition. Create ONE real-looking photograph, taken on a phone, of the same handmade crib in the right-hand corner of a Catholic church during its light show. The rest of the church is almost completely dark.

CAMERA: as in the block-out: standing at the front-left corner of the platform, 3 feet left and 3 feet in front, adult eye height, wide-angle, looking diagonally into the far corner. The short 9-foot wall is on the left, the long 16-foot wall on the right. Black pleated skirting at the bottom. The altar is not in the frame.

THE SHOW AT ITS PEAK:
- Backdrop: deep-blue velvet with hundreds of tiny twinkling fibre-optic stars and a few gold stars; across it a choir of twelve angels glows violet-white in ultraviolet light. The painted hills below are dim blue.
- Overhead in the far corner: a glowing white star burst with falling crystal-bead strands, and a spiral of softly lit cotton clouds with small glowing angels curling down toward the hill (no tree, no snow).
- Left: a translucent glowing angel floats in mid-air above the shepherds' field, lighting the shepherds and their wool sheep in white-gold light; low mist drifts through the valley below.
- Centre: the cave glows warm gold; Mary, Joseph and baby Jesus (2-foot figures) at the stone manger; ox and donkey in shadow. A thin trail of golden light runs along the sandy path from the front-right of the platform to the cave mouth.
- Above the cave: the cut-open guest room is warmly lit, with sleeping travellers.
- Right: the village street with small flickering oil lamps in the windows and on the walls, the well lit; on the far right wall, tiny lanterns of a camel caravan and a few lamps in the far village.

STYLE: cinematic contrast between cool blue night and warm lamplight, light haze, real stone, plaster, straw and clay textures, natural phone night exposure, photorealistic, 16:9.
```

## Prompt 4: the cave close-up (the shadow moment)

```
A real close-up photograph, taken on a phone, from the front-left of a handmade Christmas crib in a dark church: a rough limestone cave turned slightly toward the camera, lit by one low warm lamp behind the manger. Realistic statues of Mary, seated in blue and cream, and Joseph, standing with a clay oil lamp, look at baby Jesus lying on straw in a carved stone manger. An ox and a donkey rest in the shadows. On the back wall of the cave the shadow of the manger and a wooden roof beam cross to form the shape of a cross. Above, soft cotton clouds and a few tiny angels drift down from a glowing star. Real stone, straw and clay textures, deep shadows, warm golden glow, shallow depth of field, 4:3.
```

---

## If the result is still wrong

| Problem | Add this |
|---|---|
| Looks like a hall, not a church | "inside a traditional Catholic church: pews, a stone-and-plaster interior, a high ceiling, an altar on the front wall" |
| Altar in the wrong place (prompt 1) | "the altar is on the front wall, left of centre in the frame; the crib is in the right-hand corner of the same wall, far right" |
| Crib is too big or too small (prompt 1) | "the crib fills about one quarter of the frame width" |
| Viewpoint wrong (prompts 2, 3) | "the short 9-foot wall is on the left and the long 16-foot wall recedes on the right; camera at the front-left corner, 3 feet away" |
| Layout drifts from the block-out | "keep the exact positions from the grey block-out, only replace the boxes with real materials" |
| Cave faces the wrong way | "the cave mouth is turned about 33 degrees toward the camera" |
| Tree or snow appears | "no Christmas tree, no snow, no white fir trees" |
| Looks like CGI | "not an illustration, not CGI, a real physical handmade model photographed in a church" |
| Too many figures | "only one Holy Family; shepherds and travellers are small" |

## If it is still not right

Send me the image you got. I will say exactly which part of the prompt or the block-out caused it, and fix the wording.
