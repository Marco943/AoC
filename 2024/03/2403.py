import re

find_section_re = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")


def part_1(path: str):
    with open(path, "r") as f:
        text = f.read()

    result = 0
    for match in find_section_re.finditer(text):
        groups = match.groups()
        if not groups[0]:
            continue
        result += int(groups[1]) * int(groups[2])

    return result


def part_2(path: str):
    with open(path, "r") as f:
        text = f.read()

    result = 0
    do = True
    for match in find_section_re.finditer(text):
        groups = match.groups()
        if groups[3] is not None:
            do = True
        elif groups[4] is not None:
            do = False
        elif do:
            result += int(groups[1]) * int(groups[2])

    return result
