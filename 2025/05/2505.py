def part_1(path: str):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()

    available_ids: list[int] = []
    fresh_id_ranges: list[tuple[int, int]] = []

    whitespace = False
    for line in lines:
        if line == "":
            whitespace = True
            continue
        if not whitespace:
            _range = line.split("-", maxsplit=1)
            fresh_id_ranges.append((int(_range[0]), int(_range[1])))
        else:
            available_ids.append(int(line))

    fresh_ids = 0
    for id in available_ids:
        for _min, _max in fresh_id_ranges:
            if id >= _min and id <= _max:
                fresh_ids += 1
                break

    return fresh_ids


def part_2(path: str):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()

    ranges: list[list[int, int]] = []
    for line in lines:
        if line == "":
            break
        _range = line.split("-", maxsplit=1)
        ranges.append([int(_range[0]), int(_range[1])])

    fresh_ids = 0

    for i1 in range(len(ranges)):
        for i2 in range(len(ranges)):
            if i1 == i2:
                continue
            if ranges[i2][0] <= ranges[i1][0] <= ranges[i2][1]:
                ranges[i1][0] = ranges[i2][1] + 1
            if ranges[i2][0] <= ranges[i1][1] <= ranges[i2][1]:
                ranges[i1][1] = ranges[i2][0] - 1

        fresh = ranges[i1][1] - ranges[i1][0] + 1
        if fresh > 0:
            fresh_ids += fresh

    return fresh_ids
