from grid import Grid

DIRS: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_hikes(grid: Grid, trailhead: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = trailhead
    h = 0
    paths: list[tuple[int, int, int]] = [(x, y, h)]
    completed_hikes: list[tuple[int, int]] = []
    while len(paths) > 0:
        cx, cy, ch = paths.pop()
        if ch == 9:
            completed_hikes.append((cx, cy))
            continue
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            nh = grid.get(nx, ny)
            if nh == "." or nh is None or (int(nh) - ch) != 1:
                continue
            paths.append((nx, ny, int(nh)))
    return completed_hikes


def part_1(path: str):
    grid = Grid(pattern=open(path, "r").read())
    score = 0
    for x in range(grid.w):
        for y in range(grid.h):
            if grid.get(x, y) == "0":
                score += len(set(get_hikes(grid, (x, y))))

    return score


def part_2(path: str):
    grid = Grid(pattern=open(path, "r").read())
    score = 0
    for x in range(grid.w):
        for y in range(grid.h):
            if grid.get(x, y) == "0":
                score += len(get_hikes(grid, (x, y)))

    return score
