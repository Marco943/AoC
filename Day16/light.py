from dataclasses import dataclass
from typing import Literal, Tuple


@dataclass
class Beam:
    index: Tuple[int, int]
    i_dir: Literal["r", "l", "u", "d"]


@dataclass
class Grid:
    pattern: str

    def __post_init__(self):
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.replace("\n", "")

    def get(self, x: int, y: int):
        return self.pattern[y * self.w + x]

    def col(self, x: int):
        return self.pattern[x :: self.w]

    def row(self, y: int):
        return self.pattern[y * self.w : (y + 1) * self.w]

    def __str__(self):
        return "\n".join([self.row(i) for i in range(self.h)]) + "\n"

    def move(self, beam: Beam):
        beams = [
            beam,
        ]
        self.energized_tiles = set()
        self.hash_tiles = set()
        while len(beams) > 0:
            new_beams = []
            for beam in beams:
                # beam = Beam((7, 7), "u")
                x, y = beam.index
                hash = (y * self.w + x, beam.i_dir)
                if hash in self.hash_tiles:
                    continue
                if x < 0 or x >= self.w or y < 0 or y >= self.h:
                    continue
                self.energized_tiles.add(beam.index)
                self.hash_tiles.add(hash)
                tile = self.get(*beam.index)

                if tile in "/\\":
                    o_dir = {
                        "/": {"u": "r", "r": "u", "d": "l", "l": "d"},
                        "\\": {"u": "l", "l": "u", "d": "r", "r": "d"},
                    }[tile][beam.i_dir]
                elif tile == "|" and beam.i_dir in "lr":
                    new_beams.extend([Beam((x, y - 1), "u"), Beam((x, y + 1), "d")])
                    continue
                elif tile == "-" and beam.i_dir in "ud":
                    new_beams.extend([Beam((x - 1, y), "l"), Beam((x + 1, y), "r")])
                    continue
                else:
                    o_dir = beam.i_dir
                if o_dir == "u":
                    y -= 1
                elif o_dir == "d":
                    y += 1
                elif o_dir == "l":
                    x -= 1
                elif o_dir == "r":
                    x += 1
                new_beams.append(Beam((x, y), o_dir))
            beams = new_beams
        return len(self.energized_tiles)


grid = Grid(open("Day16/light.txt", "r").read().strip())

top = [grid.move(Beam((x, 0), "d")) for x in range(grid.w)]
bottom = [grid.move(Beam((x, grid.h - 1), "u")) for x in range(grid.w)]
left = [grid.move(Beam((0, y), "r")) for y in range(grid.h)]
right = [grid.move(Beam((grid.w - 1, y), "l")) for y in range(grid.h)]

print(max(top + bottom + right + left))
