from dataclasses import dataclass


@dataclass
class Grid:
    pattern: str

    def __post_init__(self):
        self.pattern = self.pattern.strip()
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.replace("\n", "")

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
