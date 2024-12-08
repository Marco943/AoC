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


def part_2(path: str):
    pass
