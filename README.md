# Mantra4Change US — website

A static, no-build website for the Mantra4Change US entity. Four pages, one stylesheet,
two scripts. It deploys to GitHub Pages as-is — there is nothing to compile.

Brand palette, typography and content follow the Mantra4Change brandbook and the
[Comms Resource Center](https://sushantm4c.github.io/comms-resource-center/).

---

## Preview it locally

The pages load data from `assets/js/`, so open them through a local server rather than
double-clicking the file:

```bash
cd m4c-us
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy to GitHub Pages

```bash
# 1. create an empty repo on github.com (no README, no .gitignore)

# 2. from this folder
git remote add origin https://github.com/<your-account>/<repo-name>.git
git branch -M main
git push -u origin main
```

Then in the repo: **Settings → Pages → Source: Deploy from a branch → `main` / `(root)` → Save.**
The site goes live at `https://<your-account>.github.io/<repo-name>/` within a minute or two.

To serve it at `mantra4changeus.org` instead:

1. Add a file named `CNAME` at the root containing just `www.mantra4changeus.org`
2. At your DNS provider, point `www` at `<your-account>.github.io` with a CNAME record
3. Settings → Pages → Custom domain → enter the domain → tick **Enforce HTTPS**

`.nojekyll` is already present so GitHub serves the files verbatim.

---

## Structure

```
index.html          Home
our-work.html       Approach, programmes, interactive footprint map, impact
donate.html         Giving ladder, reasons, ways to give, transparency, donor FAQs
board.html          US board / India board / leadership, with bio modals

assets/css/style.css   All styling. Brand tokens are the first block in the file.
assets/js/data.js      Generated — map geometry, per-state figures, board roster
assets/js/site.js      Nav, scroll reveals, counters, accordion, tabs, map, modal
assets/img/logo-full.png   Official US lockup, used in header and footer
assets/img/logo-mark.png   Mark only, used as the favicon
assets/img/birds-*.png     Bird motif from the logo, used as section decoration
assets/img/hero.jpg        HERO PHOTO — add this file, it appears automatically
assets/img/board/          Board photos, named <slug>.jpg (see README.txt there)

tools/build_map.py     Regenerates the India map paths from public district boundaries
tools/gen_data.py      Regenerates assets/js/data.js
```

The header and footer are written out in each page rather than injected by JavaScript,
so the site works without JS and search engines see the real markup. If you change a nav
link, change it in all four files.

## Editing content

- **Copy** — edit the HTML directly. Sections are commented and in the same order as the
  content audit.
- **State figures and board members** — edit `tools/gen_data.py`, then run
  `python3 tools/gen_data.py` from the `tools/` folder to rebuild `assets/js/data.js`.
  (Needs `india-map.json`, produced by `build_map.py`.) For one-off tweaks it is fine to
  edit `assets/js/data.js` by hand.
- **Colours and type** — the `:root` block at the top of `style.css`. Every colour on the
  site comes from a token there, so changing one changes it everywhere.

### Brand tokens

| Token | Hex | Role |
|---|---|---|
| `--navy` | `#273f7d` | Primary |
| `--sky` | `#00b1ff` | Primary — actions and accents |
| `--green` | `#38c68b` | Secondary |
| `--amber` | `#ffcb37` | Secondary |
| `--orange` | `#f59a3d` | Secondary |
| `--mist` | `#c1ebf4` | Secondary |
| `--steel` | `#95b3d7` | Secondary |

Per the brandbook, a primary blue appears on every page; secondaries are accents only.
Type is **Figtree** for display and **Inter** for body, loaded from Google Fonts.

### Icons

The icon set is extracted from the Future Readiness design pack — hand-drawn line
icons in the Mantra style, rather than generic stroke glyphs. They live in
`assets/img/icons/` in navy and white, at 128px. `tools/extract_icons.py` splits
the clustered artwork into individual icons and `tools/build_icons.py` recolours
and pads them. To add one, drop the source cluster in and rerun both.

### Hero carousel

Five photographs crossfade in the home hero on a 3-second cycle. It pauses on
hover and on focus, stops when the tab is hidden, and holds on the first frame
when the visitor prefers reduced motion. Dots sit bottom-left (a centred strip
collides with the floating stat card). To change the photographs, edit the
`<img class="carousel__slide">` list in `index.html`; the dots build themselves
from however many slides are present. Timing is the `data-interval` attribute.

### Donations

Every donate call to action points at
`https://www.every.org/mantra-4-change#/donate/card` and opens in a new tab.
Nav and footer "Donate" links still go to `donate.html`, which carries the
giving levels, ways to give, transparency and donor FAQs. To change the
processor, search for `every.org` across the four HTML files.

### Video

The home page embeds *Mantra4Change | Our Journey* as a click-to-play facade:
nothing loads from YouTube until a visitor presses play, which keeps the page
light and avoids third-party cookies on arrival. Change the video by editing the
`data-yt` attribute on the `<figure class="video">` in `index.html`.

### Photography

| File | Where it appears |
|---|---|
| `assets/img/hero-1..5.jpg` | Home hero carousel, crossfading every 3s |
| `assets/img/break-wide.jpg` | Home, full-bleed band between Challenge and Approach |
| `assets/img/community.jpg` | Our Work, beside the communities narrative |
| `assets/img/board/*.jpg` | Board cards and bio modals |

Board photos are square crops centred on the face, generated with
`tools/crop_faces.py`. Any member without a file falls back to their initials,
so photos can be added or replaced one at a time with no code change.

### The footprint map

`tools/build_map.py` dissolves public district boundaries into state outlines, simplifies
them to ~2km tolerance and projects them to SVG paths (35 states and union territories,
about 50KB total). Only the six states with programme data are coloured and clickable;
the rest render as a pale base layer. To change which states are active, edit the
`states` list in `gen_data.py` — the map picks them up automatically by name.

---

## Before this goes live

Items that need real information — each is marked with a `TODO` comment in the source:

1. **More photography** — three photographs are in use (hero, a full-bleed break on
   the home page, and the community image on Our Work). The Donate page and the
   Board hero could each take one more. Drop files into `assets/img/` and reference
   them the same way.
2. **Donation form** — every "Donate" button currently points at an anchor on
   `donate.html`. Swap in the real payment URL (Givebutter, Donorbox, Benevity, etc.).
   Search for `#donate-options` and `#give`.
3. **Contact address** — `info@mantra4changeus.org` is a guess. Replace throughout.
4. **EIN / determination letter** — referenced in the tax-deductibility FAQ on both
   `index.html` and `donate.html` but not stated. Add the number once confirmed.
5. **Programme links** — the seven cards on `our-work.html` link to the closest existing
   page on the India site. Only Project Based Learning and STEP have dedicated pages;
   confirm the right destination for the other five.
7. **Impact figures** — see the note below.

### A note on the numbers

The content audit lists *57.7 lakh students, 29,000 schools, 12,000 teachers, 8+ states*.
The Comms Resource Center (September 2026 deck) lists *227,000+ schools, 232,000+ leaders,
32.3 crore… i.e. 32.3 million children, across 6 states*. These disagree substantially.

This build uses the **Comms Resource Center** figures, because they are more recent and
carry per-state sources. Lakh and crore have been converted to millions for a US
audience. Please confirm which set is correct before publishing — the numbers appear on
`index.html` (hero strip and impact band) and `our-work.html` (impact band), and per-state
figures live in `assets/js/data.js`.

## Accessibility and support

Keyboard navigable throughout, including the map (states are focusable buttons) and the
bio modal. Visible focus rings, `prefers-reduced-motion` respected, skip link, semantic
headings. Tested in Chromium at 1440px and 390px.
