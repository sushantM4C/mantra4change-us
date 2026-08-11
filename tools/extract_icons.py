"""Split the Future Readiness icon clusters into individual transparent icons."""
import cv2, numpy as np, pathlib
from PIL import Image

SRC = ["embedded/1-033_889x1280.png","embedded/1-035_801x1152.png","embedded/1-036_712x1024.png",
       "embedded/1-039_1080x1350.png","embedded/1-043_864x1080.png","embedded/1-044_1080x1350.png",
       "embedded/1-050_1080x1350.png","embedded/1-054_1080x1350.png","embedded/1-057_1080x1350.png",
       "embedded/1-058_1080x1350.png","embedded/1-062_1080x1350.png"]
OUT = pathlib.Path("icons"); OUT.mkdir(exist_ok=True)
for f in OUT.glob("*.png"): f.unlink()

n = 0
for src in SRC:
    im = Image.open(src).convert("RGB")
    arr = np.array(im)
    grey = np.array(im.convert("L"))
    binary = (grey > 38).astype(np.uint8)

    # dilate so the separate strokes of one icon merge into one blob
    k = max(9, int(min(im.size) * 0.035)) | 1
    merged = cv2.dilate(binary, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
    cnt, labels, stats, _ = cv2.connectedComponentsWithStats(merged, connectivity=8)

    for i in range(1, cnt):
        x, y, w, h, area = stats[i]
        if w < 55 or h < 55: continue              # noise
        if w > im.width * 0.9 and h > im.height * 0.9: continue   # whole-canvas blob
        pad = 6
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(im.width, x + w + pad), min(im.height, y + h + pad)

        sub_rgb  = arr[y0:y1, x0:x1]
        sub_grey = grey[y0:y1, x0:x1]
        # limit to this blob so neighbouring icons don't bleed in
        blob = (labels[y0:y1, x0:x1] == i)
        alpha = np.where(blob, sub_grey, 0)
        if (alpha > 40).sum() < 400: continue      # too little actual ink

        rgba = np.dstack([sub_rgb, alpha]).astype(np.uint8)
        icon = Image.fromarray(rgba, "RGBA")
        bb = icon.getchannel("A").point(lambda v: 255 if v > 30 else 0).getbbox()
        if not bb: continue
        icon = icon.crop(bb)
        if min(icon.size) < 40: continue
        n += 1
        icon.save(OUT / f"ico-{n:03d}.png")

print("icons extracted:", n)
