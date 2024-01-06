import os
from collections import deque

from icecream import ic

year, day = "2023", "23"
os.chdir(year + "/" + day)
path = open("input.txt", "r").read().strip().split("\n")

# r, c, dr, dc, tiles, seen
tiles = deque([[0, 1, 1, 0, 0, set()]])
done = []
while tiles:
    r, c, dr, dc, n, s = tiles.popleft()
    s = s.copy()
    if (r, c) == (len(path) - 1, len(path[0]) - 2):
        done.append(s)
        continue
    if (r, c) in s:
        continue
    s.add((r, c))
    t = path[r][c]
    if t in "<>^v":
        dirs = ({"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}.get(t),)
    else:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for ndr, ndc in dirs:
        nr = r + ndr
        nc = c + ndc
        if nr < 0 or nr >= len(path) or nc < 0 or nc >= len(path[0]):
            continue

        nt = path[nr][nc]
        if nt == "#":
            continue
        tiles.append((nr, nc, ndr, ndc, n + 1, s))

# explored_paths = open("paths.txt", "w")
# for path_done in done:
#     new_path = path.copy()
#     for r, c in path_done:
#         if new_path[r][c] not in "<>^v":
#             new_path[r] = new_path[r][0:c] + "O" + new_path[r][c + 1 :]
#     explored_paths.write(str(len(path_done)) + "\n")
#     for row in new_path:
#         explored_paths.write(row + "\n")

# r, c, dr, dc, tiles, seen

tiles = deque([[0, 1, 1, 0, 0, set()]])
max_path = 0
while tiles:
    r, c, dr, dc, n, s = tiles.popleft()
    s = s.copy()
    if (r, c) == (len(path) - 1, len(path[0]) - 2):
        max_path = max(max_path, n)
        continue
    if (r, c) in s:
        continue
    s.add((r, c))

    for ndr, ndc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = r + ndr
        nc = c + ndc
        if nr < 0 or nr >= len(path) or nc < 0 or nc >= len(path[0]):
            continue

        nt = path[nr][nc]
        if nt == "#":
            continue
        tiles.append((nr, nc, ndr, ndc, n + 1, s))

print("PARTE 2:", max(map(len, done)))
