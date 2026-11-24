# Titanium X Assets

The independent artwork repository for **Titanium X** (Kodi 21).
The Titanium X Artwork Engine polls `index.json` in this repo and
caches matching artwork on the device — no skin update needed when
new artwork is added.

## Layout
Title artwork is named by IMDb ID (`tt0133093.gif`); collection
artwork is named by slug.

- `animated-posters/` — animatedposter
- `animated-fanart/` — animatedfanart
- `animated-keyart/` — animatedkeyart
- `characters/` — transparent character PNGs (characterart)
- `keyart/` — extra keyart
- `discart/` — custom disc art
- `genres/`, `networks/`, `franchises/`, `decades/` — collection covers

## Manifest
Run `python3 build_index.py` after adding files to regenerate
`index.json` (version = build timestamp; the engine detects updates
by version).

## Licensing
Original Titanium X artwork and appropriately licensed assets only.
