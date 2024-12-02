YEAR, DAY = 2024, 2
INPUTS = "test.txt", "input.txt"


def part_1(path: str) -> None:
    print("PART 1")

    reports: list[list[int]] = []

    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        levels = list(map(int, line.split(" ")))
        reports.append(levels)

    safe_count = 0

    def is_safe(report: list[int]) -> bool:
        asc = None
        for i in range(len(report) - 1):
            difference = report[i + 1] - report[i]
            if abs(difference) < 1 or abs(difference) > 3:
                return False
            if difference < 0 and asc is True:
                return False
            elif difference > 0 and asc is False:
                return False
            asc = difference > 0
        return True

    for report in reports:
        safe = is_safe(report)
        if safe:
            safe_count += 1

    print(safe_count)


def part_2(path: str) -> None:
    print("PART 2")

    reports: list[list[int]] = []

    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        levels = list(map(int, line.split(" ")))
        reports.append(levels)

    safe_count = 0

    def is_safe(report: list[int]) -> bool:
        asc = None
        for i in range(len(report) - 1):
            difference = report[i + 1] - report[i]
            if abs(difference) < 1 or abs(difference) > 3:
                return False
            if difference < 0 and asc is True:
                return False
            elif difference > 0 and asc is False:
                return False
            asc = difference > 0
        return True

    def is_almost_safe(report: list[int]) -> bool:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if is_safe(new_report):
                return True
        return False

    for report in reports:
        safe = is_safe(report)
        if safe:
            safe_count += 1
        else:
            safe_count += int(is_almost_safe(report))

    print(safe_count)


part_1(f"{YEAR}/{DAY:0>2}/test.txt")
part_1(f"{YEAR}/{DAY:0>2}/input.txt")
part_2(f"{YEAR}/{DAY:0>2}/test.txt")
part_2(f"{YEAR}/{DAY:0>2}/input.txt")
