from grid import Grid


def is_there_xmas(grid: Grid, x: int, y: int, dir: tuple[int, int]) -> bool:
    xmas = "XMAS"
    for i, letter in enumerate(xmas):
        dx, dy = i * dir[0], i * dir[1]
        nx, ny = x + dx, y + dy
        if grid.get(nx, ny) != letter:
            return False
    return True


def is_there_x_mas(grid: Grid, x: int, y: int) -> bool:
    center = grid.get(x, y)
    if center != "A":
        return False

    diagonal_1 = [grid.get(x - 1, y - 1), center, grid.get(x + 1, y + 1)]
    diagonal_2 = [grid.get(x - 1, y + 1), center, grid.get(x + 1, y - 1)]

    if not (all(diagonal_1) or all(diagonal_2)):
        return False

    if ("".join(diagonal_1) in ("MAS", "SAM")) and (
        "".join(diagonal_2) in ("MAS", "SAM")
    ):
        return True
    return False


def part_1(path: str):
    with open(path, "r") as f:
        lines = f.read().strip()

    grid = Grid(lines)

    xmas_count = 0
    for x in range(grid.w):
        for y in range(grid.h):
            for dir in (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (1, -1),
                (-1, -1),
                (-1, 1),
            ):
                if is_there_xmas(grid, x, y, dir):
                    xmas_count += 1

    return xmas_count


def part_2(path: str):
    with open(path, "r") as f:
        lines = f.read().strip()

    grid = Grid(lines)

    xmas_count = 0
    for x in range(grid.w):
        for y in range(grid.h):
            if is_there_x_mas(grid, x, y):
                xmas_count += 1

    return xmas_count
