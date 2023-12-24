import os

year, day, input = "2023", "24", "input"

ranges = (200000000000000, 400000000000000)

os.chdir(f"{year}/{day}")
lines = open(f"{input}.txt", "r").read().splitlines()

stones = []

for i, line in enumerate(lines):
    pos, vel = line.split(" @ ")
    pos = list(map(int, pos.split(",")))
    vel = list(map(int, vel.split(",")))
    stones.append({"p": pos, "v": vel})

cross_inside = 0
for i, a in enumerate(stones):
    xa0, ya0, _ = a["p"]
    vxa, vya, _ = a["v"]
    for j, b in enumerate(stones[i:]):
        xb0, yb0, _ = b["p"]
        vxb, vyb, _ = b["v"]
        if vxa / vya == vxb / vyb:
            continue
        y = (ya0 * vxa / vya - yb0 * vxb / vyb + xb0 - xa0) / (vxa / vya - vxb / vyb)
        x = (y - yb0) / vyb * vxb + xb0
        ta = (x - xa0) / vxa
        tb = (x - xb0) / vxb

        if (
            ranges[0] <= x <= ranges[1]
            and ranges[0] <= y <= ranges[1]
            and ta > 0
            and tb > 0
        ):
            cross_inside += 1

print(cross_inside)
