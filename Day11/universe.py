from dataclasses import dataclass


@dataclass
class Universe:
    file_path: str

    def __post_init__(self):
        universe = open(self.file_path, "r").read()
        self.width = len(universe.split("\n")[0])
        self.universe = universe.replace("\n", "")
        self.height = int(len(universe) / self.width)
        self.extra_cols = []
        self.extra_rows = []

    def row(self, i):
        return self.universe[i * self.width : (i + 1) * self.width]

    def col(self, i):
        return self.universe[i :: self.width]

    def print(self):
        for i in range(self.height):
            print(self.universe[i * self.width : (i * self.width) + self.width])

    def get(self, x, y):
        index = y * self.width + x
        return self.universe[index]

    def find_galaxies(self):
        self.galaxies = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if self.get(x, y) == "#"
        ]

    def expand(self, size: int = 2):
        self.extra_cols = [
            (x, size - 1) for x in range(self.width) if "#" not in self.col(x)
        ]
        self.extra_rows = [
            (y, size - 1) for y in range(self.height) if "#" not in self.row(y)
        ]

    def compute_lengths(self):
        self.find_galaxies()
        self.lengths = 0
        for i in range(len(self.galaxies)):
            for j in range(i + 1, len(self.galaxies)):
                self.lengths += abs(self.galaxies[i][0] - self.galaxies[j][0])
                self.lengths += abs(self.galaxies[i][1] - self.galaxies[j][1])
                for extra_col in self.extra_cols:
                    if (
                        self.galaxies[i][0] < extra_col[0] < self.galaxies[j][0]
                        or self.galaxies[i][0] > extra_col[0] > self.galaxies[j][0]
                    ):
                        self.lengths += extra_col[1]
                for extra_row in self.extra_rows:
                    if (
                        self.galaxies[i][1] < extra_row[0] < self.galaxies[j][1]
                        or self.galaxies[i][1] > extra_row[0] > self.galaxies[j][1]
                    ):
                        self.lengths += extra_row[1]
        return self.lengths


self = Universe("universe.txt")

# self.find_galaxies()
# len(self.galaxies)
# self.height
# self.width
# self.print()
self.expand(1000000)

print(self.compute_lengths())
