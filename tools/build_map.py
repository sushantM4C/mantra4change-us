import json, math, collections
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

SRC = "india.geojson"
TOL = 0.022          # degrees ~2.4km — plenty for a web map
W   = 1000           # target svg width

data = json.load(open(SRC))

groups = collections.defaultdict(list)
for f in data["features"]:
    st = (f["properties"].get("st_nm") or "").strip()
    if not st:
        continue
    g = shape(f["geometry"])
    if not g.is_valid:
        g = g.buffer(0)
    groups[st].append(g)

states = {}
for st, geoms in groups.items():
    u = unary_union(geoms).buffer(0.004).buffer(-0.004)   # close hairline seams between districts
    u = u.simplify(TOL, preserve_topology=True)
    states[st] = u

# ---- Mercator projection ----
def merc(lon, lat):
    lat = max(min(lat, 84.0), -84.0)
    return lon, math.degrees(math.log(math.tan(math.pi/4 + math.radians(lat)/2)))

minx = miny = 1e9
maxx = maxy = -1e9
for u in states.values():
    a, b, c, d = u.bounds
    x1, y1 = merc(a, b); x2, y2 = merc(c, d)
    minx = min(minx, x1); maxx = max(maxx, x2)
    miny = min(miny, y1); maxy = max(maxy, y2)

spanx, spany = maxx - minx, maxy - miny
scale = W / spanx
H = spany * scale

def pt(lon, lat):
    x, y = merc(lon, lat)
    return ((x - minx) * scale, (maxy - y) * scale)

def ring_to_d(coords):
    out = []
    for i, (lon, lat) in enumerate(coords):
        x, y = pt(lon, lat)
        out.append(("M" if i == 0 else "L") + f"{x:.1f} {y:.1f}")
    return "".join(out) + "Z"

def geom_to_d(g, min_area=0.004):
    parts = []
    polys = list(g.geoms) if g.geom_type == "MultiPolygon" else [g]
    for p in polys:
        if p.area < min_area:      # drop specks, keep real islands
            continue
        parts.append(ring_to_d(list(p.exterior.coords)))
        for r in p.interiors:
            parts.append(ring_to_d(list(r.coords)))
    return "".join(parts)

paths = {}
for st, g in sorted(states.items()):
    d = geom_to_d(g)
    if d:
        paths[st] = d

def slug(s):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-")

out = {
    "viewBox": f"0 0 {W:.0f} {H:.0f}",
    "states": [{"name": n, "id": slug(n), "d": d} for n, d in paths.items()],
}

with open("india-map.json", "w") as fh:
    json.dump(out, fh, separators=(",", ":"))

print("states:", len(paths))
print("viewBox:", out["viewBox"])
print("bytes:", len(json.dumps(out, separators=(',', ':'))))
print("\n".join(sorted(paths)))
