YEAR, DAY = 2024, 5
INPUTS = "test.txt", "input.txt"


def part_1(path: str) -> None:
    with open(path, "r") as f:
        lines = f.read().strip()
    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []

    rules_lines, updates_lines = lines.split("\n\n", 1)

    for line in rules_lines.split("\n"):
        page_1, page_2 = line.split("|", 1)
        rules.append((int(page_1), int(page_2)))

    for line in updates_lines.split("\n"):
        updates.append(list(map(int, line.split(","))))

    def is_update_valid(update: list[int]) -> bool:
        for n1, n2 in rules:
            if (n1 in update) and (n2 in update):
                if update.index(n1) > update.index(n2):
                    return False
        return True

    result = 0
    for update in updates:
        if is_update_valid(update):
            result += update[len(update) // 2]

    print(result)


def part_2(path: str) -> None:
    with open(path, "r") as f:
        lines = f.read().strip()
    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []

    rules_lines, updates_lines = lines.split("\n\n", 1)

    for line in rules_lines.split("\n"):
        page_1, page_2 = line.split("|", 1)
        rules.append((int(page_1), int(page_2)))

    for line in updates_lines.split("\n"):
        updates.append(list(map(int, line.split(","))))

    def is_update_valid(update: list[int]) -> bool:
        for n1, n2 in rules:
            if (n1 in update) and (n2 in update):
                i1 = update.index(n1)
                i2 = update.index(n2)
                if i1 > i2:
                    update[i1], update[i2] = n2, n1
                    return False
        return True

    result = 0
    for update in updates:
        if is_update_valid(update):
            continue
        while True:
            if is_update_valid(update):
                break
        result += update[len(update) // 2]

    print(result)


part_1(f"{YEAR}/{DAY:0>2}/test.txt")
part_1(f"{YEAR}/{DAY:0>2}/input.txt")
part_2(f"{YEAR}/{DAY:0>2}/test.txt")
part_2(f"{YEAR}/{DAY:0>2}/input.txt")
