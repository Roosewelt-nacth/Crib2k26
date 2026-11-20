# CLAUDE.md: Parish Christmas crib archive (2023 → 2026 and onward)

Read this file first in any new chat. It carries everything decided so far, so work can continue without the old conversation.

## What this project is
A parish builds a large Christmas crib on a stage inside the church every year. This repo is the archive and working folder: layouts, references, blueprints, prompts, build packs, costs and the showcase site (`index.html`, served by GitHub Pages).

## How to work with the user
- Keep replies short. Put the effort into the output, not the explanation.
- Money is in rupees (₹), Indian digit grouping (₹1,50,535).
- Use they/them for the user unless they say otherwise.
- The user generates photoreal images with other models. Claude writes prompts and layouts; Claude cannot produce photoreal images itself.
- The 2023 layout and the user's sketches are reference only. Do not repeat the 2023 theme.
- Show a result, then ask only what is genuinely blocking.

## Years
| Year | Theme | Status | Files |
|---|---|---|---|
| 2023 | The neighbourhood in miniature: church at 45°, with local landmarks (temple, courts, apartment, father's house, Asha Nivas, shops, skywalk, park, a statue) | Built | `2023/final-layout-crib-2023.pdf`, `2023/layout-page.jpg` |
| 2026 | **That Night in Bethlehem** | Planned; opens 24 Dec 2026 | `2026/` |

Missing from this repo (not saved in the chat): the 2023 final crib photo and the user's two hand sketches (3D view and top view with 16 ft × 9 ft). Ask the user to add them to `2023/` as `final-photo.jpg`, `sketch-3d.jpg`, `sketch-top.jpg`.

## 2026 theme: "That Night in Bethlehem"
The Nativity as it most likely happened: a limestone village in Judea at night. A crowded guest room (kataluma) sits above a cave where the animals are kept; the birth is in the cave under it. The Roman census is on; shepherds are in terraced fields below, a far village and a tiny Magi caravan are on the ridge. Daylight: museum-quality diorama with forced perspective. Dark: a 4-minute light show.

### Stage and viewing geometry (confirmed by the user)
- Stage 9 ft along the back (altar) wall × 16 ft along the right wall, in the right-hand corner of the church at the end of the altar wall. Altar at the centre of the front wall (assumed, to confirm).
- Open sides: left and front, covered by black pleated skirting. Deck assumed 2 ft (to confirm). The stage is rented.
- Public viewing spot V = 3 ft left of and 3 ft in front of the front-left corner. Eye height 5.2 ft above the floor.
- Cave and house turned about 32.5° toward V.
- Ceiling assumed about 15 ft (to confirm); star hook position and ceiling type unknown.
- TWO LAYERS ONLY, NO SLOPE (user, 18 Nov): the flat deck, and a second layer +1.5 ft high across the full 9 ft width for the back 4.5 ft (it starts 11.5 ft from the front), with a dry-stone wall face. Cave and rock hill stand on the lower layer, backs against the step (cave floor at deck level; arch 2.5 ft; the hill top and house floor are at +3.3 ft so about 10 in of rock sits above the arch; room 1.5 ft, roof +4.8 ft); shepherds, sheep and campfire on the lower layer; sheepfold, watchtower and the pipe-cleaner angel choir on the upper layer; street and village houses flat at deck level; far village on a 3 ft rock ridge. All updated on 19 Nov: blueprint, views, guides, owner guide, crew pack, prompts.
- Scale tiers by distance from V: A under 11 ft (1:3, 2 ft hero figures), B 11–15 ft (1:6), C 15–18 ft (1:12), D over 18 ft (1:24). Farther is paler, cooler and less saturated.

### The 32 numbered items (the same numbers on every sheet)
1 path of light · 2 cave · 3 Holy Family, ox, donkey, manger · 4 house with upper guest room · 5 rock hill · 6 cloud and angel spiral · 7 star burst with bead strands · 8 shepherds, sheep, campfire · 9 floating angel (Pepper's ghost) · 10 rock ridge with mist tray · 11 sheepfold · 12 second layer (upper level, +1.5 ft) · 13 watchtower · 14 far village · 15 Magi caravan (wall shelf) · 16–18 village houses · 19 cobbled street · 20 well · 21 census table, soldier, scribe · 22 donkeys and travellers · 23–24 olive trees · 25 "find 12 details" plaque · 26 backdrop (hills print, blue drape, gold stars, fibre-optic stars, UV angel choir) · 27 control box · 28 speakers · 29 UV bars · 30 public view spot and rope · 31 pond · 32 selfie mirror (block M, church floor only; the pond 31 moved into block N on 20 Nov because it must be part of the crib, set into the scene between the field and the front rocks) · 33–36 foreground (block N, 20 Nov): rock outcrop, shepherd boy with lamb, front wall, dog/jar/herbs.

Coordinates and checks live in `source/blueprint.py` (no overlaps, nothing outside 9 × 16 ft, path of light clear of solids).

### A fix worth remembering
From V the cave's house hid the Magi caravan and far village completely (they sat at bearings 21–36°, the house covers 25–41°). They now sit on the right-wall crest and a wall shelf (bearings 38–49°). Always run a sightline check from V before placing a new item.

### The 4-minute show
0:00 dusk amber wash · 0:30 night, oil lamps and campfire · 1:00 fibre-optic stars, mist, ambient sound · 1:40 "Glory to God": field flood and the floating angel · 1:50 UV angel choir appears · 2:30 star brightens, path of light chases to the cave · 3:00 cave glow and the 8-second cross-shadow · 3:30 everything warm, Magi lanterns · 3:55 fade and loop. Runs on an ESP32 with relay and MOSFET boards and a DFPlayer for sound.

### Colour and composition (twelve colours, no more)
Hero (complementary): Lamp gold `#F2B84B`, Warm white `#FFF1CF`, Mary blue `#3A5BA8`. Cool family: Midnight blue `#1F2F66`, Dusk violet `#5B4A9A`, Mist blue `#AEBBD9`. Earth family: Limestone `#EDE3CB`, Sand `#D2BC8C`, Ochre `#B98A3E`, Olive `#7D8A4A`. Tiny accent: Terracotta `#A5583A`. Neutral: Near-black `#15151A`.
Rules: gold only in five places (cave, star, path, lamps, Magi lanterns); about 60% cool, 30% earth, 10% gold; focal point is the cave and star at the centre of the view; leading lines are the path and the cascade spiral; no Christmas red, bright green, pink, primaries, colour-cycling or strobing.

## Costs (rough, ±25%, 10% contingency included)
| Tier | Total | What it counts |
|---|---|---|
| Prop-only | ₹74,525 | Prop materials only. Figures reused from 2023, stage rented, lights rented. Half the 2023 plywood reused. Smaller rock, painted hills, simpler backdrop and cascade. |
| Lean | ₹1,43,935 | Reuse and DIY where possible, own lights, own electrics |
| Full | ₹2,42,000 | Everything bought new |
Totals as rebuilt on 20 Nov (evening) for the FULLER plan (adds block N, five houses, field detail, silhouettes; they replace ₹70,015 / ₹1,34,640 / ₹2,26,765 of 20 Nov morning, ₹71,885 / ₹1,37,720 / ₹2,30,835 of 19 Nov and the earlier ₹82,885 / ₹1,50,535 / ₹2,53,660 and ₹84,645 / ₹1,58,015 / ₹2,66,640). Per block: see the owner guide start page. Block H (lights) is ₹11,550 / ₹22,550 / ₹34,900. All costs are estimates; get quotes. The interactive pack, `build-pack.pdf` and `index.html` still show the old plan and numbers.

## Schedule (today when written: 16 Nov 2026)
Week 1 (16–22 Nov): measure on site, order long-lead items, start frame and backdrop. 23 Nov → 13 Dec: build in the workshop. 14–17 Dec: install in the church. 18–23 Dec: wire, aim, rehearse. 24 Dec: open. About 80 person-days with 6–8 volunteers.

## Crew (set 18 Nov 2026; names are in `TEAMS` in `source/make_blocks.py`)
Team 1 Rufus, Sanjeetha, Andrew, Samuel: E · Team 2 Lenin, Runo, Aarthi, Milton, Monus: C, N · Team 3 Austin Joel, Richard, Allwyn: H, I, F, J · Team 4 Janet, Mithul, Yugesh, Stephen, Alvin: B, K · Team 5 Jino, Shibi, Suja, Adrian, Deric, Vk: G · Stage team Vk, Samuel: A, L, M (M assigned 20 Nov). Vk is in teams 5 and stage; Samuel is in team 1 and stage. Block M (pond and selfie mirror, approved 18 Nov): pond 1.6 × 3 ft along the left edge, long side front to back (x 0.35–1.95, y 10.3–13.3), blue cloth under a clear sheet (no water on the deck); selfie mirror 2 × 5 ft acrylic on the church floor at x −6, y 19, faces the queue, turned about 23° toward the crib. Built by the Stage team (assigned 20 Nov). The speaker and hatch C are at the front-left corner (x 0, y 15–16) and hatch A (the light box) is at the back-left of the upper layer.

## Still to confirm on site
Deck height (2 ft assumed) · ceiling height (about 15 ft assumed) and ceiling type · altar centred on the front wall and crib at its right end · power point and exit · deck load rating and work-at-height rules · how much of the 2023 plywood exists.

## Image work
- `2026/docs/image-prompts.md`: four whole-scene prompts. They need the grey block-outs in `2026/images/` (view1-visitor, view2-aisle) and `church-key-plan.png` attached, plus the style images in `references/`.
- `2026/docs/component-prompts.md`: one studio-shot prompt per component.
- The first prompts failed because they said "church hall" and never said where the altar is. Version 2 fixed that. If a generated image is wrong, compare it against the blueprint before changing the prompt.

## FINAL plan (19 Nov 2026, built into every guide)
- Two flat layers, no slope; craft props only (no screen, mist, resin, UV, microcontroller); pipe-cleaner angel choir is block F; lights are block H: one plug from the church socket (right behind the stage, back-left corner) into one box at the back-left of the upper layer, 12 V inside, three hand switches (Lamps, Night sky, Glory), Austin Joel's team (Team 3) builds it. Colour rule: gold only in the cave, star, path, lamps and Magi lanterns; warm white, cool white and deep indigo otherwise; no red, bright green, pink, multicolour, flashing or UV.
- Approved looks (replaced 20 Nov with the fuller layout): `crib-final-3q.jpg` (day) and `crib-final-night.jpg` (night) from the public spot, plus one per block (stage-bare-3q, B-cave-holy-family, C-upper-house, E-shepherds-field, F-angel-choir, G-village-street, H-lights-control, I-sky-cascade, J-backdrop, K-far-village-magi, L-foreground-view-spot, N-foreground); `crib-final-top.jpg` is still the old layout. Earlier: `2026/images/generated/crib-final-3q.jpg` and `crib-final-top.jpg` (the finished crib), `stage-bare-3q.jpg` and `stage-bare-top.jpg` (the empty stage). Reference drawings: `2026/images/top-view-reference.png`, `stage-only-reference.png`, `lighting-plan.png`.
- All-sides prompts (20 Nov): `2026/docs/all-sides-prompts.md`, one shared description of the fuller crib + 6 camera views (public spot, front, left side, above, cave close-up, night).
- Prompts: `2026/docs/final-prompts.md` (finished crib, night version, bare stage, top views). Plans: `craft-simplification-plan.md`, `lighting-plan.md`.
- Houses (C guest room, G houses A/B/C) are PLYWOOD (20 Nov, user): 4–6 mm walls and roof on 1 × 1 in corner strips, 9–12 mm base, screwed for reuse, putty + sand texture, whitewash. Guest room under 12 kg. Reuse first everywhere (2023 figures, plywood, LEDs).
- FULLER LAYOUT (20 Nov, user said the crib looked empty and out of scale): one size rule: Holy Family 2 ft (deliberate hero), 1:6 zone people 1 ft and houses 2.5–3.5 ft, 1:24 far zone; nearer = bigger and darker. G = five plywood houses 3.5/3.0/2.5/2.0/1.5 ft along the right wall (front to back), street narrowing 1.25 → 0.55 ft, market stall, palm, chickens. E = terrace wall, 3 shepherds, 14 sheep, goat-hair tent, boulders, thorn bushes, trough, fig tree. New block N (Team 2): front-left rocks with olive 23, shepherd boy 1.3 ft, front wall. J adds far-hill silhouette + 3 palm cut-outs; I adds 5 gold rays star → cave roof. Olive 24 moved to x 3.7, y 12.3. `source/check_layout.py` checks overlaps and sightlines from V; run it after any move.
- Team packs: `2026/crew/team-1..5.pdf`, `stage-team.pdf` (cover with a 1 ft-grid map of only that team’s objects, shopping list without prices, then its blocks). Every object card has a Box W × D × H in feet and a small drawing (`object_guide.BOX`, `source/team_pages.py`); 3 objects per page.
- Crew pack (84 pages, was 66): per block pages 1–4 plus "Every object, one by one" pages (size, materials, reuse tip, simple steps; 6 objects per page) from `source/object_guide.py`. No prices anywhere in the crew pack (`nop()` strips ₹ from "before").
- Outputs to send: crew = `2026/crew/crew-pack.pdf` (no prices). Keep: owner = `2026/owner/owner-guide.pdf`.
- Regenerate everything: `make_views.py`, `make_topview_ref.py`, `make_lighting.py`, `make_stage_ref.py`, then `make_crew.py` and `make_crew_pack.py` (block data in `make_blocks.py`, steps in `crew_steps.py`, image looks in `make_prompts.py`).
- `2026/blocks/` and `2026/share/` (older block sheets and share pack) were removed because they showed the old plan.

## Files
- `index.html`: the showcase site (GitHub Pages). `2026/pack/index.html`: the full interactive build pack.
- `2026/images/`: blueprint, two block-outs, church key plan, "Book of Bethlehem" concept render.
- `2026/docs/`: build pack PDF, 23 concepts, final theme, prompts, the first five concepts page.
- `references/`: three AI style images (daylight diorama, night show, a real cascade with blue drape) and two UI references for the site design (glass folders, dark moss course).
- `2026/share/`: `final-blueprint-3-views.png` (front, side, top and the tilted view from V), made by `source/make_views.py`.
- `2026/crew/`: the CREW pack, no prices (`crew-pack.pdf`, `<letter>-crew.pdf`, `crew-prompts.md`): per block 4 pages (card with picture and image prompt, full-page blueprint drawing, parts table with exact size and place plus cut list, exact numbered build steps). Made by `source/make_crew_pack.py`; build data in `source/crew_steps.py`.
- `2026/owner/`: the OWNER guide with prices, dated steps, shopping lists and budget (`owner-guide.pdf`, `<letter>-card.pdf`, `owner-prompts.md`). Keep this one for the project owner; send the crew `2026/crew/`. Made by `source/make_crew.py`. 12 blocks: A, B, C, E–M (no D: rock hill merged into B). Generated photos are in `2026/images/generated/`.
- `source/`: Python that generates everything: `blueprint.py` (geometry, plan, section, schedule), `persp.py` (grey block-outs), `church.py` (key plan), `drawkit.py`, `drawings.py`, `drawings_fix.py` (part sheets), `pack.py` (PDF), `build_html.py` (web pack). Needs Python 3, Pillow, pypdfium2 and Chrome for rendering. Some paths are absolute to the original machine and need adjusting.

## Adding a new year
1. Make `20XX/` with `images/` and `docs/`; copy the 2026 structure.
2. Add a folder card in `index.html` (copy the 2026 card).
3. Add a row to the Years table above and update the status.
4. Keep the stage geometry and the 30-item numbering if the stage is the same.
