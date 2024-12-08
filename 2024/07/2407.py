def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def concat(a, b):
    return int(str(a) + str(b))


operations: callable = [mul, add]
operations_2: callable = [mul, add, concat]


def is_valid(value: int, numbers: list[int]) -> bool:
    n = len(numbers) - 1
    cases = [[(i >> j) & 1 for j in range(n)] for i in range(2**n)]
    for case in cases:
        test_value = numbers[0]
        for i, op in enumerate(case):
            test_value = operations[op](test_value, numbers[i + 1])
        if test_value == value:
            return True


def is_valid_2(value: int, numbers: list[int]) -> bool:
    cases: list[list[int]] = [[]]
    for i in range(len(numbers) - 1):
        new_cases: list[list[int]] = []
        for i in range(len(cases)):
            for j in (0, 1, 2):
                new_case = [n for n in cases[i]] + [j]
                new_cases.append(new_case)
        cases = new_cases

    for case in cases:
        test_value = numbers[0]
        for i, op in enumerate(case):
            test_value = operations_2[op](test_value, numbers[i + 1])
        if test_value == value:
            return True


def part_1(path: str):
    result = 0

    for line in open(path, "r").readlines():
        value, numbers = line.split(":", 1)
        value = int(value)
        numbers = [int(number.strip()) for number in numbers.strip().split(" ")]
        if is_valid(value, numbers):
            result += value

    return result


def part_2(path: str):
    result = 0

    for line in open(path, "r").readlines():
        value, numbers = line.split(":", 1)
        value = int(value)
        numbers = [int(number.strip()) for number in numbers.strip().split(" ")]
        if is_valid_2(value, numbers):
            result += value

    return result
