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
- Raked stage: 0 at the front to +3 ft at the hill crest. Terraces +0.8 to +2.0 ft.
- Scale tiers by distance from V: A under 11 ft (1:3, 2 ft hero figures), B 11–15 ft (1:6), C 15–18 ft (1:12), D over 18 ft (1:24). Farther is paler, cooler and less saturated.

### The 30 numbered items (the same numbers on every sheet)
1 path of light · 2 cave · 3 Holy Family, ox, donkey, manger · 4 house with upper guest room · 5 rock hill · 6 cloud and angel spiral · 7 star burst with bead strands · 8 shepherds, sheep, campfire · 9 floating angel (Pepper's ghost) · 10 rock ridge with mist tray · 11 sheepfold · 12 terraces · 13 watchtower · 14 far village · 15 Magi caravan (wall shelf) · 16–18 village houses · 19 cobbled street · 20 well · 21 census table, soldier, scribe · 22 donkeys and travellers · 23–24 olive trees · 25 "find 12 details" plaque · 26 backdrop (hills print, blue drape, gold stars, fibre-optic stars, UV angel choir) · 27 control box · 28 speakers · 29 UV bars · 30 public view spot and rope.

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
| Prop-only | ₹82,885 | Prop materials only. Figures reused from 2023, stage rented, lights rented. Half the 2023 plywood reused. Smaller rock, painted hills, simpler backdrop and cascade. |
| Lean | ₹1,50,535 | Reuse and DIY where possible, own lights, own electrics |
| Full | ₹2,53,660 | Everything bought new |
Levers: contingency 5% gives about ₹79,000; skipping the far village and Magi shelf saves about ₹2,100; all of the plywood reused saves a further ₹3,250. Details per part are in `2026/pack/` and `2026/docs/build-pack.pdf`.

## Schedule (today when written: 16 Nov 2026)
Week 1 (16–22 Nov): measure on site, order long-lead items, start frame and backdrop. 23 Nov → 13 Dec: build in the workshop. 14–17 Dec: install in the church. 18–23 Dec: wire, aim, rehearse. 24 Dec: open. About 80 person-days with 6–8 volunteers.

## Still to confirm on site
Deck height (2 ft assumed) · ceiling height (about 15 ft assumed) and ceiling type · altar centred on the front wall and crib at its right end · power point and exit · deck load rating and work-at-height rules · how much of the 2023 plywood exists.

## Image work
- `2026/docs/image-prompts.md`: four whole-scene prompts. They need the grey block-outs in `2026/images/` (view1-visitor, view2-aisle) and `church-key-plan.png` attached, plus the style images in `references/`.
- `2026/docs/component-prompts.md`: one studio-shot prompt per component.
- The first prompts failed because they said "church hall" and never said where the altar is. Version 2 fixed that. If a generated image is wrong, compare it against the blueprint before changing the prompt.

## Files
- `index.html`: the showcase site (GitHub Pages). `2026/pack/index.html`: the full interactive build pack.
- `2026/images/`: blueprint, two block-outs, church key plan, "Book of Bethlehem" concept render.
- `2026/docs/`: build pack PDF, 23 concepts, final theme, prompts, the first five concepts page.
- `references/`: three AI style images (daylight diorama, night show, a real cascade with blue drape) and two UI references for the site design (glass folders, dark moss course).
- `2026/blocks/`: one blueprint and build guide per block A–L (PDF and HTML), plus `all-blocks.pdf` and `00-overview.pdf`. Block list and order in `2026/docs/build-blocks.md`. Generated by `source/make_blocks.py` from the pack; images `layout-plan-only.png` and `layout-plan-blocks.png` in `2026/images/`.
- `2026/share/`: group share pack: `final-blueprint-3-views.png` (front, side, top and the tilted view from V), `block-views/<A-L>-views.png`, `block-view-prompts.md`, `share-pack.pdf`. Generated by `source/make_views.py` and `source/make_prompts.py`. The eye-view image prompt is `2026/docs/eye-view-prompt.md` (v3, corrected for the 33-degree tilt).
- `2026/crew/`: the CREW pack, no prices (`crew-pack.pdf`, `<letter>-crew.pdf`, `crew-prompts.md`): per block 4 pages (card with picture and image prompt, full-page blueprint drawing, parts table with exact size and place plus cut list, exact numbered build steps). Made by `source/make_crew_pack.py`; build data in `source/crew_steps.py`.
- `2026/owner/`: the OWNER guide with prices, dated steps, shopping lists and budget (`owner-guide.pdf`, `<letter>-card.pdf`, `owner-prompts.md`). Keep this one for the project owner; send the crew `2026/crew/`. Made by `source/make_crew.py`. 11 blocks: A, B, C, E–L (no D: rock hill merged into B). Generated target-look photos are in `2026/images/generated/` (add `F-floating-angel.jpg` there for block F).
- `source/`: Python that generates everything: `blueprint.py` (geometry, plan, section, schedule), `persp.py` (grey block-outs), `church.py` (key plan), `drawkit.py`, `drawings.py`, `drawings_fix.py` (part sheets), `pack.py` (PDF), `build_html.py` (web pack). Needs Python 3, Pillow, pypdfium2 and Chrome for rendering. Some paths are absolute to the original machine and need adjusting.

## Adding a new year
1. Make `20XX/` with `images/` and `docs/`; copy the 2026 structure.
2. Add a folder card in `index.html` (copy the 2026 card).
3. Add a row to the Years table above and update the status.
4. Keep the stage geometry and the 30-item numbering if the stage is the same.
