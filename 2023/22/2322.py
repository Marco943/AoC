import os

year = "2023"
day = "22"
os.chdir(year + "/" + day)

blocks = open("input_test.txt", "r").read().strip().split("\n")


def parse_blocks(block: str) -> dict:
    block0, block1 = block.split("~")
    x0, y0, z0 = map(int, block0.split(","))
    x1, y1, z1 = map(int, block1.split(","))
    lowest = min(z0, z1)
    return {"end0": [x0, y0, z0], "end1": [x1, y1, z1], "falling": lowest != 1}


blocks = tuple(map(parse_blocks, blocks))
blocks[0]
print(blocks)
