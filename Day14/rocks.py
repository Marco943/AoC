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
        self.rocks_filled = {}
        self.gravity_works = {}
        self.results = {}

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
        return "\n".join([self.row(i) for i in range(self.h)])

    def fill_rocks(self, bit: str) -> str:
        if bit in self.rocks_filled:
            return self.rocks_filled[bit]
        rocks = "O" * bit.count("O")
        length = len(bit)
        result = rocks.ljust(length, ".")
        self.rocks_filled[bit] = result
        return result

    def gravity(self, row: str) -> str:
        if row in self.gravity_works.keys():
            return self.gravity_works[row]
        result = "#".join(map(self.fill_rocks, row.split("#")))
        self.gravity_works[row] = result
        return result

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

    def compute_weight(self):
        if self.pattern in self.results.keys():
            print("repetido")
            return self.results[self.pattern]
        result = sum([self.row(y).count("O") * (self.h - y) for y in range(self.h)])

        self.results[self.pattern] = result
        return result


rocks = Rocks(open("Day14/rocks_test.txt", "r").read().strip())
print(rocks, "\n")
for cycle in range(1000000000):
    if cycle % 10000 == 0:
        print(cycle)
    for direction in ("n", "s"):
        rocks.tilt(direction)
    # print(rocks, "\n")

print(rocks.compute_weight())
