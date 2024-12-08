from grid import Grid


def find_starting_pos(grid: Grid) -> tuple[int, int]:
    for x in range(grid.w):
        for y in range(grid.h):
            if grid.get(x, y) == "^":
                return (x, y)


def part_1(path: str):
    grid = Grid(open(path, "r").read().strip())

    x, y = find_starting_pos(grid)
    dx, dy = (0, -1)
    count = 0
    while True:
        if grid.get(x, y) is None:
            break
        if grid.get(x, y) != "X":
            count += 1
            grid.set(x, y, "X")

        nx, ny = x + dx, y + dy
        if grid.get(nx, ny) is None:
            break
        if grid.get(nx, ny) != "#":
            x, y = nx, ny
            continue

        dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return count


def is_there_loop(grid: Grid, x: int, y: int, dx: int, dy: int) -> bool:
    visited: set[tuple[int, int, int, int]] = set()
    while True:
        cur_cell = grid.get(x, y)
        if cur_cell is None:
            break
        elif cur_cell == "#":
            x, y = x - dx, y - dy
            dx, dy = -dy, dx
            continue

        if (x, y, dx, dy) in visited:
            return True
        visited.add((x, y, dx, dy))
        x, y = x + dx, y + dy

    return False


def part_2(path: str):
    grid = Grid(open(path, "r").read().strip())

    sx, sy = find_starting_pos(grid)
    dx, dy = (0, -1)
    count = 0

    for bx in range(grid.w):
        for by in range(grid.h):
            if sx == bx and sy == by:
                continue
            old = grid.get(bx, by)
            grid.set(bx, by, "#")
            if is_there_loop(grid, sx, sy, dx, dy):
                count += 1
            grid.set(bx, by, old)

    return count
