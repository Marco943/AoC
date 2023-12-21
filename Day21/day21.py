import os
from collections import deque
from dataclasses import dataclass

os.chdir("Day21")


@dataclass
class Grid:
    pattern: str

    def __post_init__(self):
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.replace("\n", "")

    def get(self, x: int, y: int):
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

    def def_positions(self, positions: list = []) -> None:
        if positions:
            for x, y in positions:
                idx = y * self.w + x
                self.pattern = self.pattern[0:idx] + "O" + self.pattern[idx + 1 :]


grid = Grid(open("input.txt", "r").read().strip())

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

starting_idx = grid.pattern.index("S")
starting_pos = (starting_idx % grid.w, starting_idx // grid.h)

positions = deque([starting_pos])

for steps in range(64):
    n = len(positions)
    for i in range(n):
        x, y = positions.pop()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if (
                not (0 <= nx < grid.w)
                or not (0 <= ny < grid.h)
                or grid.get(nx, ny) == "#"
                or (nx, ny) in positions
            ):
                continue
            positions.appendleft((nx, ny))
            grid.set(nx, ny, "O")
        grid.set(x, y, ".")
    # print(f"Passo {n}:\n{grid}")

print("PARTE 1:", len(positions))
