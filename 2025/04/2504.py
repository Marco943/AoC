from grid import Grid

dirs = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))


def part_1(path: str):
    f = open(path, "r")
    pattern = f.read()
    f.close()

    grid = Grid(pattern=pattern)

    forklifted = 0
    for x in range(grid.w):
        for y in range(grid.h):
            if grid.get(x, y) == ".":
                continue
            adjacent = 0
            for dx, dy in dirs:
                if grid.get(x + dx, y + dy) == "@":
                    adjacent += 1
            if adjacent < 4:
                forklifted += 1

    return forklifted


def part_2(path: str):
    f = open(path, "r")
    pattern = f.read()
    f.close()

    grid = Grid(pattern=pattern)

    forklifted_total = 0
    while True:
        forklifted_xy: list[tuple[int, int]] = []
        for x in range(grid.w):
            for y in range(grid.h):
                if grid.get(x, y) == ".":
                    continue
                adjacent = 0
                for dx, dy in dirs:
                    if grid.get(x + dx, y + dy) == "@":
                        adjacent += 1
                if adjacent < 4:
                    forklifted_xy.append((x, y))
        if len(forklifted_xy) == 0:
            break
        forklifted_total += len(forklifted_xy)
        for x, y in forklifted_xy:
            grid.set(x, y, ".")

    return forklifted_total
