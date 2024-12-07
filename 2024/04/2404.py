from dataclasses import dataclass


@dataclass
class Grid:
    pattern: str

    def __post_init__(self):
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.strip().replace("\n", "")

    def get(self, x: int, y: int):
        if y < 0 or x < 0 or y >= self.h or x >= self.w:
            return None
        return self.pattern[y * self.w + x]

    def set(self, x: int, y: int, value: str):
        self.pattern = (
            self.pattern[0 : y * self.w + x]
            + value
            + self.pattern[y * self.w + x + 1 :]
        )

    def col(self, x: int):
        return self.pattern[x :: self.w]

    def row(self, y: int):
        return self.pattern[y * self.w : (y + 1) * self.w]

    def set_col(self, x: int, data: str):
        new_pattern = ""
        for y in range(self.h):
            new_pattern += (
                self.pattern[y * self.w : y * self.w + x]
                + data[y]
                + self.pattern[y * self.w + x + 1 : (1 + y) * self.w]
            )
        self.pattern = new_pattern

    def set_row(self, y: int, data: str):
        self.pattern = (
            self.pattern[0 : y * self.w] + data + self.pattern[(y + 1) * self.w :]
        )

    def __str__(self):
        return "\n".join([self.row(i) for i in range(self.h)]) + "\n"


YEAR, DAY = 2024, 4
INPUTS = "test.txt", "input.txt"


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


def part_1(path: str) -> None:
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

    print(xmas_count)


def part_2(path: str) -> None:
    with open(path, "r") as f:
        lines = f.read().strip()

    grid = Grid(lines)

    xmas_count = 0
    for x in range(grid.w):
        for y in range(grid.h):
            if is_there_x_mas(grid, x, y):
                xmas_count += 1

    print(xmas_count)


part_1(f"{YEAR}/{DAY:0>2}/test.txt")
part_1(f"{YEAR}/{DAY:0>2}/input.txt")
part_2(f"{YEAR}/{DAY:0>2}/test.txt")
part_2(f"{YEAR}/{DAY:0>2}/input.txt")
