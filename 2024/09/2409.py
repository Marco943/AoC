def part_1(path: str):
    disk: list[int] = map(
        lambda b: -1 if b == "." else int(b), list(open(path, "r").read().strip())
    )
    # disk =[ 1,2,3,4,5]
    id: int = 0
    blocks: list[int] = []
    for i, block in enumerate(disk):
        if i % 2 != 0:
            blocks.extend([-1] * block)
            continue
        blocks.extend([id] * block)
        id += 1

    is_there_gaps: bool = True
    first_free: int = 0
    last_block: int = len(blocks) - 1
    while is_there_gaps:
        first_free = blocks.index(-1, first_free)

        for block in blocks[first_free:]:
            if block != -1:
                break
        else:
            is_there_gaps = False
            continue

        for i in range(last_block, 0, -1):
            if blocks[i] == -1:
                continue
            blocks[first_free], blocks[i] = blocks[i], -1
            break

        last_block = i

        checksum: int = 0
        for i, block in enumerate(blocks):
            if block == -1:
                break
            checksum += i * block
    return checksum


def part_2(path: str):
    return
