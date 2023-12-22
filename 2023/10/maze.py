from maze_instructions import direction_check_map, instructions

maze = list(map(list, open("Day10/pipes.txt", "r").read().strip().split("\n")))
maze_height = len(maze)
maze_width = len(maze[0])


def direction_to_idx(dir, coords):
    x, y = coords
    if dir == "u":
        if y == 0:
            return None
        return (x, y - 1)
    elif dir == "r":
        if x == maze_width - 1:
            return None
        return (x + 1, y)
    elif dir == "l":
        if x == 0:
            return None
        return (x - 1, y)
    elif dir == "d":
        if y == maze_height - 1:
            return None
        return (x, y + 1)


st_x, st_y = 0, 0
while maze[st_y][st_x] != "S":
    st_x += 1
    if (st_x // maze_width) != 0:
        st_y += 1
        st_x = 0
starting_idx = (st_x, st_y)


for starting_direction in ("u", "r", "l", "d"):
    # starting_direction = "r"
    print(starting_direction)
    new_idx = direction_to_idx(starting_direction, starting_idx)
    if new_idx is None:
        continue
    new_direction = starting_direction

    steps = [starting_direction]
    path_idxs = [starting_idx]

    path = True
    found = False
    while path and not found:
        path_idxs.append(new_idx)
        steps.append(new_direction)
        new_instruction = maze[new_idx[1]][new_idx[0]]
        # print(new_instruction)

        new_direction = instructions[new_instruction].get(new_direction, None)
        if new_direction is None:
            print("sem direção")
            path = False
            continue
        new_idx = direction_to_idx(new_direction, new_idx)
        if new_idx is None:
            print("sem índice")
            path = False
            continue
        if new_idx == starting_idx:
            print("achou")
            found = True
            break

    if path is False:
        continue
    if found is True:
        # print(steps)
        break

print("Mais longe", int(len(steps) / 2))
print("passos", len(path_idxs))

# outside_idxs = set()
# for idx, direction in zip(path_idxs, steps):
#     direction_check = direction_check_map[direction]
#     idx_check = direction_to_idx(direction_check, idx)
#     if idx_check is None:
#         continue
#     if idx_check not in path_idxs:
#         # maze = maze[0:idx_check] + "I" + maze[idx_check + 1 :]
#         outside_idxs.add(idx_check)


# outside_idxs = list(outside_idxs)
# idx = 0
# while True:
#     if idx >= len(outside_idxs):
#         break
#     outside_idx = outside_idxs[idx]
#     for direction_check in ("u", "r", "l", "d"):
#         idx_check = direction_to_idx(direction_check, outside_idx)
#         if idx_check is None:
#             continue
#         elif idx_check in path_idxs:
#             continue
#         elif idx_check in outside_idxs:
#             continue
#         else:
#             outside_idxs.append(idx_check)
#     idx += 1

start_symbol = [
    symbol
    for symbol, direction in instructions.items()
    if direction.get(steps[-1]) == steps[0]
][0]
maze[st_y][st_x] = start_symbol

inside_idxs = []
y = 0
while y < maze_height:
    inside = False
    recent_corner = ""
    x = 0
    while x < maze_width:
        if (x, y) in path_idxs:
            idx = path_idxs.index((x, y))
            direction = steps[idx]
            instruction = maze[y][x]
            if instruction == "|":
                inside = not inside
            elif instruction in "FLJ7":
                if recent_corner == "F" and instruction == "J":
                    inside = not inside
                elif recent_corner == "L" and instruction == "7":
                    inside = not inside
                recent_corner = instruction
        elif inside:
            inside_idxs.append((x, y))
        x += 1
    y += 1
maze

print("Dentro", len(inside_idxs))
print("Fora", maze_height * maze_width - len(inside_idxs) - len(path_idxs))
