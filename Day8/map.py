import re
from math import lcm

with open("map.txt", "r") as f:
    map = f.read().strip()

re_instructions = re.compile("([RL]+)\s")
instructions = re_instructions.findall(map)[0].replace("L", "0").replace("R", "1")
length_instructions = len(instructions)

re_network = re.compile("([0-9A-Z]{3}) \= \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)")
network = {i[0]: (i[1], i[2]) for i in re_network.findall(map)}

nodes = [node for node in network.keys() if node[-1] == "A"][0:2]
steps = 0
done = False
indices = [None for node in nodes]
while not done:
    # print(steps, nodes)
    instruction = int(instructions[steps % length_instructions])
    # done = True
    for i, node in enumerate(nodes):
        new_node = network[node][instruction]
        nodes[i] = new_node
        if new_node[-1] == "Z":
            indices[i] = steps + 1
        if all(indices):
            done = True
    steps += 1

print(lcm(*indices), "steps")
