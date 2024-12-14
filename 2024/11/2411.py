import math
from functools import cache


def n_digitos_par(n: int) -> bool:
    return int(math.log10(n)) % 2 != 0


def part_1(path: str):
    stones: dict[int, int] = {}
    for x in open(path, "r").read().strip().split():
        stones[int(x)] = stones.get(int(x), 0) + 1
    blinks = 25

    for blink in range(blinks):
        new_stones: dict[int, int] = {}
        for stone, n in stones.items():
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + n
                continue
            N = math.floor(math.log10(stone)) + 1
            if N % 2 == 0:
                new_stone_1, new_stone_2 = divmod(stone, math.pow(10, N / 2))
                new_stones[new_stone_1] = new_stones.get(new_stone_1, 0) + n
                new_stones[new_stone_2] = new_stones.get(new_stone_2, 0) + n
                continue
            new_stone = stone * 2024
            new_stones[new_stone] = new_stones.get(new_stone, 0) + n
        stones = new_stones

    return sum(stones.values())


def part_2(path: str):
    stones: dict[int, int] = {}
    for x in open(path, "r").read().strip().split():
        stones[int(x)] = stones.get(int(x), 0) + 1
    blinks = 75

    for blink in range(blinks):
        new_stones: dict[int, int] = {}
        for stone, n in stones.items():
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + n
                continue
            N = math.floor(math.log10(stone)) + 1
            if N % 2 == 0:
                new_stone_1, new_stone_2 = divmod(stone, math.pow(10, N / 2))
                new_stones[new_stone_1] = new_stones.get(new_stone_1, 0) + n
                new_stones[new_stone_2] = new_stones.get(new_stone_2, 0) + n
                continue
            new_stone = stone * 2024
            new_stones[new_stone] = new_stones.get(new_stone, 0) + n
        stones = new_stones

    return sum(stones.values())
