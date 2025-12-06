from typing import Literal


def part_1(path: str):
    f = open(path, "r")
    pattern = f.read()
    while "  " in pattern:
        pattern = pattern.replace("  ", " ")
    lines = [line.strip() for line in pattern.splitlines()]
    f.close()

    operations: list[Literal["*", "+"]] = lines[-1].split(" ")
    totals: list[int] = [1 if i == "*" else 0 for i in operations]

    for line in lines[:-1]:
        numbers = [int(n) for n in line.split(" ")]
        for i in range(len(numbers)):
            if operations[i] == "*":
                totals[i] = totals[i] * numbers[i]
            else:
                totals[i] = totals[i] + numbers[i]

    return sum(totals)


def part_2(path: str):
    f = open(path, "r")
    pattern = f.read()
    while "  " in pattern:
        pattern = pattern.replace("  ", " ")
    lines = [line.strip() for line in pattern.splitlines()]
    f.close()

    operations: list[Literal["*", "+"]] = lines[-1].split(" ")
    totals: list[int] = [1 if i == "*" else 0 for i in operations]
    numbers: list[list[int]] = [[] for i in operations]

    for line in lines[:-1]:
        for i, number in enumerate(line.split(" ")):
            numbers[i].append(int(number))

    print(numbers)
    print(operations)

    return
