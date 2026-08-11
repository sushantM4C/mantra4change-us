"""Square-crop board headshots, centred on the detected face where possible."""
import cv2, os, glob, pathlib
from PIL import Image, ImageOps

SRC = "../_source-photos"   # folder of original headshots, named "First Last.jpg"
DST = pathlib.Path("../assets/img/board"); DST.mkdir(parents=True, exist_ok=True)

NAME_MAP = {
    "Aditya Vishwanath": "aditya-vishwanath",
    "Ambili Sukesan":    "ambili-sukesan",
    "Charag Krishnan":   "charag-krishnan",
    "Cornelius Walter":  "cornelius-walter",
    "Esther":            "esther-wojcicki",
    "Kirti Reddy":       "kirti-reddy",
    "Pradeep Nair":      "pradeep-nair",
    "Prashant Reddy":    "prashanth-reddy",
    "Radhika Shah":      "radhika-shah",
    "Rajiv Murali":      "rajiv-murali",
    "Rashi Mehta":       "rashi-mehta",
    "VIVEK-RAGAVAN":     "vivek-ragavan",
}

cascade = cv2.CascadeClassifier(
    os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml"))

def face_box(path):
    img = cv2.imread(path)
    if img is None:
        return None, None
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey)
    faces = cascade.detectMultiScale(grey, 1.08, 5, minSize=(40, 40))
    if len(faces) == 0:
        return None, img.shape
    # biggest face wins
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    return (x, y, w, h), img.shape

TARGET = 700
for path in sorted(glob.glob(SRC + "/*")):
    stem = pathlib.Path(path).stem.strip()
    slug = NAME_MAP.get(stem)
    if not slug:
        print("!! unmapped:", stem); continue

    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    W, H = im.size
    side = min(W, H)

    box, _ = face_box(path)
    if box:
        fx, fy, fw, fh = box
        cx = fx + fw / 2
        # place the face a little above centre, which reads better in a square frame
        cy = fy + fh * 0.52
        detected = "face"
    else:
        cx = W / 2
        cy = H * (0.38 if H > W else 0.5)   # portraits: bias upward toward the head
        detected = "heuristic"

    left = int(round(max(0, min(cx - side / 2, W - side))))
    top  = int(round(max(0, min(cy - side / 2, H - side))))
    out = im.crop((left, top, left + side, top + side))

    if out.width > TARGET:
        out = out.resize((TARGET, TARGET), Image.LANCZOS)
    out.save(DST / f"{slug}.jpg", "JPEG", quality=86, optimize=True, progressive=True)
    print(f"{slug:20} {W}x{H} -> {out.size[0]}px  ({detected})")
