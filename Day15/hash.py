print("\n")


def hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


sequence = sum(
    map(
        hash,
        open("Day15/hash.txt", "r").read().strip().replace("\n", "").split(","),
    )
)
print(sequence)
