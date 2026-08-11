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
assets/img/logo.svg    PLACEHOLDER MARK — replace with the real logo

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

### The footprint map

`tools/build_map.py` dissolves public district boundaries into state outlines, simplifies
them to ~2km tolerance and projects them to SVG paths (35 states and union territories,
about 50KB total). Only the six states with programme data are coloured and clickable;
the rest render as a pale base layer. To change which states are active, edit the
`states` list in `gen_data.py` — the map picks them up automatically by name.

---

## Before this goes live

Items that need real information — each is marked with a `TODO` comment in the source:

1. **Logo** — `assets/img/logo.svg` is a placeholder. Drop in the official US logo
   (SVG preferred; a PNG works if you update the `<img src>` in all four pages).
2. **Donation form** — every "Donate" button currently points at an anchor on
   `donate.html`. Swap in the real payment URL (Givebutter, Donorbox, Benevity, etc.).
   Search for `#donate-options` and `#give`.
3. **Contact address** — `info@mantra4changeus.org` is a guess. Replace throughout.
4. **EIN / determination letter** — referenced in the tax-deductibility FAQ on both
   `index.html` and `donate.html` but not stated. Add the number once confirmed.
5. **Programme links** — the seven cards on `our-work.html` link to the closest existing
   page on the India site. Only Project Based Learning and STEP have dedicated pages;
   confirm the right destination for the other five.
6. **Photography** — there are no photographs anywhere yet. Board members show initials;
   the hero and section bands rely on the map and typography. Adding real classroom
   photography is the single biggest visual upgrade available.
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
