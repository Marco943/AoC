import string

from rich.pretty import pprint

symbols = string.punctuation
adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]

with open("Day3/engine.txt", "r") as f:
    engine = f.read().strip().split("\n")
    h = len(engine)
    w = len(engine[0])
    for i in range(h):
        engine[i] = "." + engine[i] + "."
    engine = ["." * (w + 2)] + engine + ["." * (w + 2)]

part_numbers = []
row = 0
while row < len(engine):
    col = 0
    while col < len(engine[row]):
        char = engine[row][col]
        if not char.isdigit():
            col += 1
            continue

        col_end = col + 1
        while col_end <= len(engine[row]):
            if engine[row][col : col_end + 1].isdigit():
                col_end += 1
            else:
                break

        keep = False

        for row_check in range(row - 1, row + 2):
            for col_check in range(col - 1, col_end + 1):
                char_check = engine[row_check][col_check]
                if char_check != "." and not char_check.isdigit():
                    keep = True

        if not keep:
            engine[row] = (
                engine[row][0:col] + "." * (col_end - col) + engine[row][col_end:]
            )
        if keep:
            part_numbers.append(
                {
                    "id": f"{row}{col}{col_end}",
                    "number": engine[row][col:col_end],
                    "row": row,
                    "col_start": col,
                    "col_end": col_end,
                }
            )
        col = col_end
    row += 1

sum = 0
row = 0
while row < len(engine):
    col = 0
    while col < len(engine[row]):
        char = engine[row][col]
        if char != "*":
            col += 1
            continue
        gear_numbers_id = set()
        for row_check in range(row - 1, row + 2):
            for col_check in range(col - 1, col + 2):
                for part_number in part_numbers:
                    if row_check == part_number["row"] and col_check in range(
                        part_number["col_start"], part_number["col_end"]
                    ):
                        gear_numbers_id.add(part_number["id"])
        gear_numbers = [
            int(part_number["number"])
            for part_number in part_numbers
            if part_number["id"] in gear_numbers_id
        ]
        if len(gear_numbers) == 2:
            sum += gear_numbers[0] * gear_numbers[1]
        col += 1
    row += 1

pprint(sum)
