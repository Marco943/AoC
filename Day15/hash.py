print("\n")


def hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


sequence = open("Day15/hash.txt", "r").read().strip().replace("\n", "").split(",")


boxes = {i: {} for i in range(256)}

for i, cur_value in enumerate(sequence):
    if "-" in cur_value:
        lens = cur_value[:-1]
        box_label = int(hash(lens))
        if lens in boxes[box_label]:
            del boxes[box_label][lens]
    else:
        lens = cur_value[:-2]
        focal = int(cur_value[-1])
        box_label = int(hash(lens))
        boxes[box_label][lens] = focal

focusing_power = 0
for box in boxes.keys():
    lenses = list(boxes[box].keys())
    focals = list(boxes[box].values())
    for slot in range(len(lenses)):
        focusing_power += (box + 1) * (slot + 1) * focals[slot]
        print(lenses[slot], box + 1, slot + 1, focals[slot])

print(focusing_power)
