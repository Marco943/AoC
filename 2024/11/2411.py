import math
from functools import cache


def n_digitos_par(n: int) -> bool:
    return int(math.log10(n)) % 2 != 0


def part_1(path: str):
    stones: list[int] = [int(x) for x in open(path, "r").read().strip().split()]

    for blink in range(25):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == 0:
                stones[i] = 1
                i += 1
                continue

            N = math.floor(math.log10(stone)) + 1
            if N % 2 == 0:
                stones[i], new_stone = divmod(stone, math.pow(10, N / 2))
                stones.insert(i + 1, new_stone)
                i += 2
                continue

            stones[i] = stones[i] * 2024
            i += 1
    # print(stones)
    return len(stones)


def part_2(path: str):
    stones: list[int] = [int(x) for x in open(path, "r").read().strip().split()]
    stones.insert(0, -1)
    blinks = 75

    @cache
    def is_even_digits(stone) -> bool:
        N = math.floor(math.log10(stone)) + 1
        if N % 2 != 0:
            return False
        return divmod(stone, math.pow(10, N / 2))

    @cache
    def handle_stone(stone):
        if stone < 0:
            print("blink", -stone)
            return [stone - 1]
        if stone == 0:
            return [1]
        if stones := is_even_digits(stone):
            return stones
        return [stone * 2024]

    while True:
        stone = stones.pop(0)
        if stone < -blinks:
            break
        stones.extend(handle_stone(stone))

    # print(stones)

    return len(stones)
