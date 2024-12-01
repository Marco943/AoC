list_1: list[int] = []
list_2: list[int] = []


def part_1(path: str) -> None:
    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        number_1, number_2 = map(int, line.split("   ", 2))
        list_1.append(number_1)
        list_2.append(number_2)

    list_1.sort()
    list_2.sort()

    distances: list[int] = []
    for i in range(len(list_1)):
        distances.append(abs(list_1[i] - list_2[i]))

    print(sum(distances))


part_1("2024/01/test.txt")
part_1("2024/01/input.txt")
