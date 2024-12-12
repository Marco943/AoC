def part_1(path: str):
    disk: list[int] = [int(x) for x in open(path, "r").read().strip()]

    i = 0
    j = len(disk) - 1
    blocks: list[int] = []

    while i < len(disk):
        if disk[i] == 0:
            i += 1
            continue
        if i % 2 == 0:
            blocks.append(i // 2)
        else:
            while j % 2 != 0 or disk[j] == 0:
                j -= 1
            if j > 0:
                blocks.append(j // 2)
                disk[j] -= 1
        disk[i] -= 1

    checksum = 0
    for i, block in enumerate(blocks):
        checksum += i * block

    return checksum


def part_2(path: str):
    disk: list[int] = [int(x) for x in open(path, "r").read().strip()]

    i = 0
    blocks: list[int] = []

    for i in range(len(disk)):
        if i % 2 == 0:
            blocks.extend([i // 2] * disk[i])
        else:
            blocks.extend([-1] * disk[i])

    for i in range(len(disk) - 1, 0, -1):
        break

    checksum = 0
    for i, block in enumerate(blocks):
        if block == -1:
            continue
        checksum += i * block
    return checksum
