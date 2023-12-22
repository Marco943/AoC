from dataclasses import dataclass
from functools import cache
from typing import Literal


@dataclass
class Rocks:
    pattern: str

    def __post_init__(self):
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.replace("\n", "")

    def col(self, x: int):
        return self.pattern[x :: self.w]

    def set_col(self, x: int, data: str):
        new_pattern = ""
        for y in range(self.h):
            new_pattern += (
                self.pattern[y * self.w : y * self.w + x]
                + data[y]
                + self.pattern[y * self.w + x + 1 : (1 + y) * self.w]
            )
        self.pattern = new_pattern

    def row(self, y: int):
        return self.pattern[y * self.w : (y + 1) * self.w]

    def set_row(self, y: int, data: str):
        self.pattern = (
            self.pattern[0 : y * self.w] + data + self.pattern[(y + 1) * self.w :]
        )

    def __str__(self):
        return "\n".join([self.row(i) for i in range(self.h)]) + "\n"

    def fill_rocks(self, bit: str) -> str:
        rocks = "O" * bit.count("O")
        length = len(bit)
        result = rocks.ljust(length, ".")
        return result

    def gravity(self, row: str) -> str:
        return "#".join(map(self.fill_rocks, row.split("#")))

    def tilt(self, direction: Literal["n", "s", "e", "w"]):
        if direction == "n":
            for x in range(self.w):
                self.set_col(x, self.gravity(self.col(x)))
        elif direction == "s":
            for x in range(self.w):
                self.set_col(x, self.gravity(self.col(x)[::-1])[::-1])
        elif direction == "w":
            for y in range(self.h):
                self.set_row(y, self.gravity(self.row(y)))
        elif direction == "e":
            for y in range(self.h):
                self.set_row(y, self.gravity(self.row(y)[::-1])[::-1])

    def calc_indexes(self):
        return tuple(i for i, c in enumerate(self.pattern) if c == "O")

    def compute_weight(self):
        return sum([self.row(y).count("O") * (self.h - y) for y in range(self.h)])


rocks = Rocks(open("Day14/rocks.txt", "r").read().strip())
print(rocks, "\n")
historico = {}
cycle = 0
while True:
    for direction in ("n", "w", "s", "e"):
        rocks.tilt(direction)
    indexes = rocks.calc_indexes()
    peso = rocks.compute_weight()
    print("Cycle", cycle, "Weight", peso)
    if indexes in historico:
        break
    historico[indexes] = peso
    cycle += 1

cycle_end = cycle
cycle_start = list(historico.keys()).index(indexes)
cycle_duration = cycle_end - cycle_start
print("Cycle start:", cycle_start)
print("Cycle end:", cycle_end)
print("Cycle duration:", cycle_duration)
indexes_cycle = [
    indexes for i, indexes in enumerate(historico.keys()) if i >= cycle_start
]

print(
    "Weight at cycle 1000000000:",
    historico[indexes_cycle[(1000000000 - cycle_start - 1) % cycle_duration]],
)
