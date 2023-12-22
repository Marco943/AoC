with open("Day1/input.txt", "r") as f:
    doc = f.readlines()


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_index(s: str) -> str:
    subs = s[0]
    if subs.isnumeric():
        return subs
    for n in range(1, len(s)):
        subs = s[0:n]
        for x, y in numbers.items():
            if x == subs:
                return y
    return None


def parse_line(line: str) -> int:
    nums = []
    for i in range(len(line)):
        num = parse_index(line[i:])
        if num is not None:
            nums.append(num)
    return int(nums[0] + nums[-1])


nums = [parse_line(line) for line in doc]
print(nums)
print(sum(nums))
