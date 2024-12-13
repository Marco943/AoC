def part_1(path: str):
    disk: list[int] = [int(x) for x in open(path, "r").read().strip()]

    i = 0
    j = len(disk) - 1
    blocks: list[int] = []

    while i <= j:
        if disk[i] == 0:
            i += 1
            continue
        if i % 2 == 0:
            blocks.extend([i // 2] * disk[i])
            disk[i] = 0
            i += 1
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
    indexes: list[int] = [i * 2 for i in range(len(disk) // 2, 0, -1)]

    for i in range(len(disk)):
        if i % 2 == 0:
            if disk[i] < 0:
                blocks.extend([-1] * (-disk[i]))
            else:
                blocks.extend([i // 2] * disk[i])
            disk[i] = 0
        else:
            j = 0
            while j < len(indexes):
                index = indexes[j]
                if disk[i] == 0:
                    break
                if disk[index] <= disk[i]:
                    blocks.extend([int(index / 2)] * disk[index])
                    disk[i] -= disk[index]
                    disk[index] = -disk[index]
                    indexes.pop(j)
                else:
                    j += 1
            blocks.extend([-1] * disk[i])

    checksum = 0
    for i, block in enumerate(blocks):
        if block == -1:
            continue
        checksum += i * block
    return checksum
