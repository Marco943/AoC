from dataclasses import dataclass
from functools import cache
from typing import Literal

import numpy as np


@dataclass
class Rocks:
    pattern: np.array

    def __post_init__(self):
        self.w, self.h = self.pattern.shape

    def set_col(self, x: int, data: str):
        # self.pattern = "".join(
        #     (
        #         f"{self.pattern[y*self.w :y*self.w+x]}{data[y]}{self.pattern[y*self.w+x+1 :(1+y)*self.w-1]}"
        #         for y in range(self.h)
        #     )
        # )
        for y in range(self.h):
            self.pattern = (
                self.pattern[0 : x + self.w * y]
                + data[y]
                + self.pattern[x + self.w * y + 1 :]
            )

    def set_row(self, y: int, data):
        self.pattern = (
            self.pattern[0 : y * self.w] + data + self.pattern[(y + 1) * self.w :]
        )

    def __str__(self):
        return (
            "\n"
            + "\n".join(" ".join(j for j in self.pattern[i, :]) for i in range(self.h))
            + "\n"
        )

    # @classmethod
    # @cache
    def fill_rocks(self, bit: np.array) -> np.array:
        length = bit.shape[0]
        if length <= 1:
            return bit
        rocks = np.count_nonzero(bit == "O")
        has_square = bit[0] == "#"
        if has_square:
            return np.array(tuple("#" + "O" * rocks + "." * (length - rocks - 1)))
        return np.array(tuple("O" * rocks + "." * (length - rocks)))

    def gravity(self, row):
        stop_idx = np.where(row == "#")[0]
        old_row_split = np.array_split(row, stop_idx)
        return np.hstack(tuple(map(rocks.fill_rocks, old_row_split)))

    def tilt(self, direction: Literal["n", "s", "e", "w"]):
        if direction == "n":
            for x in range(self.w):
                self.pattern[:, x] = self.gravity(self.pattern[:, x])
        elif direction == "s":
            for x in range(self.w):
                self.pattern[:, x] = self.gravity(self.pattern[:, x][::-1])[::-1]
        elif direction == "w":
            for y in range(self.h):
                self.pattern[y, :] = self.gravity(self.pattern[y, :])
        elif direction == "e":
            for y in range(self.h):
                self.pattern[y, :] = self.gravity(self.pattern[y, :][::-1])[::-1]

    def compute_weight(self):
        return sum(
            [
                np.count_nonzero(self.pattern[y, :] == "O") * (self.h - y)
                for y in range(self.h)
            ]
        )


rocks = Rocks(
    np.array(
        list(map(list, open("Day14/rocks_test.txt", "r").read().strip().split("\n")))
    )
)
print(rocks)
for cycle in range(1000000000):
    if cycle % 10000 == 0:
        print(cycle)
    for direction in ("n", "w", "s", "e"):
        rocks.tilt(direction)
    # print(rocks)

print(rocks.compute_weight())
