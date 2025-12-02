def is_id_valid_1(id: int) -> bool:
    id_str = str(id).lstrip("0")
    length = len(id_str)
    if length % 2 == 0 and length >= 2:
        half = length // 2
        if id_str[:half] == id_str[half:]:
            return False
    return True


def is_id_valid_2(id: int) -> bool:
    id_str = str(id).lstrip("0")
    length = len(id_str)

    for divider in range(2, length + 1):
        if length % divider != 0:
            continue
        sublength = length // divider
        first_sequence = id_str[:sublength]
        for i in range(1, divider):
            pos = sublength * i
            sequence = id_str[pos : pos + sublength]
            if sequence != first_sequence:
                break
        else:
            return False
    return True


def part_1(path: str):
    f = open(path, "r")

    ranges = f.read().split(",")

    invalid_digits_sum = 0
    for _range in ranges:
        id1, id2 = _range.split("-")
        id1 = int(id1)
        id2 = int(id2)
        for id in range(id1, id2 + 1):
            valid = is_id_valid_1(id)
            if not valid:
                invalid_digits_sum += id

    f.close()

    return invalid_digits_sum


def part_2(path: str):
    f = open(path, "r")

    ranges = f.read().split(",")

    invalid_digits_sum = 0
    for _range in ranges:
        id1, id2 = _range.split("-")
        id1 = int(id1)
        id2 = int(id2)
        for id in range(id1, id2 + 1):
            valid = is_id_valid_2(id)
            if not valid:
                invalid_digits_sum += id

    f.close()

    return invalid_digits_sum
