from dataclasses import dataclass


@dataclass
class Pattern:
    pattern: str

    def __post_init__(self):
        self.w = self.pattern.index("\n")
        self.h = self.pattern.count("\n") + 1
        self.pattern = self.pattern.replace("\n", "")

    def col(self, x):
        return self.pattern[x :: self.w]

    def row(self, y):
        return self.pattern[y * self.w : (y + 1) * self.w]

    def __str__(self):
        return "\n".join([self.row(i) for i in range(self.h)])

    def find_reflection(self, old=0):
        # Vertical
        for x in range(1, self.w):
            if x == old:
                continue
            reflection = True
            dx = 0
            while (x - dx - 1 >= 0) and (x + dx < self.w) and reflection:
                # Check left
                left_col = self.col(x - dx - 1)
                # Check right
                right_col = self.col(x + dx)
                if right_col != left_col:
                    reflection = False
                dx += 1
            if reflection:
                return x

        # Horizontal
        for y in range(1, self.h):
            if y * 100 == old:
                continue
            reflection = True
            dy = 0
            while (y - dy - 1 >= 0) and (y + dy < self.h) and reflection:
                # Check left
                above_row = self.row(y - dy - 1)
                # Check right
                below_row = self.row(y + dy)
                if above_row != below_row:
                    reflection = False
                dy += 1
            if reflection and y * 100 != old:
                return y * 100
        return 0


mirrors = open("mirror.txt", "r").read().strip().split("\n\n")

old_number = 0
number = 0
for n, mirror in enumerate(mirrors):
    old_pattern = Pattern(mirror)
    print("#" * 30)
    print("Pattern", n)
    old_reflection_number = old_pattern.find_reflection()
    old_number += old_reflection_number
    print("Old Reflection:", old_reflection_number)

    for i_smudge in range(len(mirror)):
        if mirror[i_smudge] == ".":
            pattern = mirror[0:i_smudge] + "#" + mirror[i_smudge + 1 :]
        if mirror[i_smudge] == "#":
            pattern = mirror[0:i_smudge] + "." + mirror[i_smudge + 1 :]
        if mirror[i_smudge] == "\n":
            continue
        new_pattern = Pattern(pattern)

        new_reflection_number = new_pattern.find_reflection(old=old_reflection_number)

        if new_reflection_number != 0:
            number += new_reflection_number
            print("New Reflection:", new_reflection_number)
            break
print("#" * 30)
print("Old:", old_number)
print("New:", number)
