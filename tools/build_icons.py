"""Pick the best icons, clean their alpha, recolour to brand navy + white."""
from PIL import Image, ImageFilter
import numpy as np, pathlib

PICK = {
  "megaphone":     "ico-002.png",
  "flag-hill":     "ico-015.png",
  "math":          "ico-016.png",
  "book-open":     "ico-017.png",
  "magnifier":     "ico-018.png",
  "mic":           "ico-019.png",
  "lightbulb":     "ico-020.png",
  "sprout":        "ico-021.png",
  "pencil":        "ico-022.png",
  "paper-plane":   "ico-023.png",
  "head-puzzle":   "ico-024.png",
  "people-talk":   "ico-025.png",
  "lift-up":       "ico-026.png",
  "journey":       "ico-027.png",
  "heart-hands":   "ico-028.png",
  "reading-child": "ico-009.png",
  "children":      "ico-010.png",
  "family":        "ico-011.png",
  "speech-pencil": "ico-008.png",
}
NAVY = (39, 63, 125)
OUT = pathlib.Path("../m4c-us/assets/img/icons"); OUT.mkdir(parents=True, exist_ok=True)
SIZE = 128

def render(src, rgb, dest):
    im = Image.open(src).convert("RGBA")
    a = np.array(im.getchannel("A")).astype(np.float32)
    # Alpha was derived from luminance, and the source strokes only reach ~45%
    # brightness. Normalise per icon against its own stroke level so the line art
    # ends up fully opaque rather than a pale ghost.
    ink = a[a > 25]
    peak = float(np.percentile(ink, 88)) if ink.size else 255.0
    a = np.clip((a - 18) * (255.0 / max(peak - 18, 1)), 0, 255)
    alpha = Image.fromarray(a.astype(np.uint8), "L").filter(ImageFilter.GaussianBlur(0.4))

    # square canvas with padding, preserving aspect
    w, h = im.size
    scale = (SIZE - 12) / max(w, h)
    nw, nh = max(1, round(w * scale)), max(1, round(h * scale))
    alpha = alpha.resize((nw, nh), Image.LANCZOS)

    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    solid = Image.new("RGBA", (nw, nh), rgb + (255,))
    solid.putalpha(alpha)
    canvas.paste(solid, ((SIZE - nw) // 2, (SIZE - nh) // 2), solid)
    canvas.save(dest, optimize=True)

for name, src in PICK.items():
    render(f"icons/{src}", NAVY,          OUT / f"{name}.png")
    render(f"icons/{src}", (255,255,255), OUT / f"{name}-white.png")
    print(f"  {name}")
print("built", len(PICK), "icons x2 colourways")
