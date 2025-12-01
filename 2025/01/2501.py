def part_1(path: str):
    f = open(path, "r")
    pos = 50
    zeros = 0

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        direction, distance = line[0], int(line[1:])
        if direction == "L":
            pos -= distance
        else:
            pos += distance

        pos = pos % 100
        if pos == 0:
            zeros += 1

    f.close()

    return zeros


def part_2(path: str):
    f = open(path, "r")
    pos = 50
    zeros = 0

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        direction, distance = line[0], int(line[1:])

        loops, distance = divmod(distance, 100)
        zeros += loops

        if direction == "L":
            new_pos = pos - distance
        else:
            new_pos = pos + distance

        if (new_pos <= 0 and pos > 0) or new_pos > 99:
            zeros += 1

        pos = new_pos % 100

    f.close()

    return zeros
