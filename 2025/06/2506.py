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
    lines = pattern.splitlines()
    f.close()

    length = len(lines[0])
    height = len(lines)

    operations: list[Literal["+", "*"]] = []
    numbers: list[list[int]] = [[]]
    i_number = 0

    for col in range(length):
        current_number = 0
        for row in range(height):
            char = lines[row][col]
            if char == " ":
                continue
            elif char in ["*", "+"]:
                operations.append(char)
                continue
            current_number = current_number * 10 + int(char)
        if current_number == 0:
            i_number += 1
            numbers.append([])
        else:
            numbers[i_number].append(current_number)

    total = 0
    for col in range(len(operations)):
        if operations[col] == "+":
            col_total = 0
        else:
            col_total = 1

        for number in numbers[col]:
            if operations[col] == "+":
                col_total += number
            else:
                col_total *= number
        total += col_total

    return total
