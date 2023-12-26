import os
import string

ano, dia, input = "2022", "03", "input"
prioridade = string.ascii_lowercase + string.ascii_uppercase

os.chdir(f"{ano}/{dia}")
lines = open(f"{input}.txt").read().splitlines()

n = 0
for line in lines:
    length = int(len(line) / 2)
    items1 = line[0:length]
    items2 = line[length:]
    comum = ""
    for i1 in items1:
        for i2 in items2:
            if i1 == i2:
                comum = i1
    n += prioridade.index(comum[0]) + 1

print("PARTE 1:", n)

n = 0
for group in range(0, int(len(lines) / 3)):
    items1 = lines[0 + 3 * group]
    items2 = lines[1 + 3 * group]
    items3 = lines[2 + 3 * group]
    comum = ""
    for i1 in items1:
        for i2 in items2:
            for i3 in items3:
                if i1 == i2 == i3:
                    comum = i1
    n += prioridade.index(comum[0]) + 1

print("PARTE 2:", n)
