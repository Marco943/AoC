import os

os.chdir("Day18")


plan = open("plan.txt", "r").read().strip().split("\n")

directions = {"0": (1, 0), "3": (0, -1), "1": (0, 1), "2": (-1, 0)}
r, c = (0, 0)

path = []
boundary_points = 0


for line in plan:
    color = line[-8:-1]
    meters = int(color[1:6], base=16)
    dir = color[-1]
    path.append((c, r))
    dc, dr = directions[dir]
    r += dr * meters
    c += dc * meters
    boundary_points += meters

# Shoelace
# Calcula a área interior
area_2 = 0
for i in range(len(path)):
    area_2 += path[i][0] * path[i - 1][1] - path[i - 1][0] * path[i][1]
area = abs(area_2) / 2

# Pick's
# i = pontos internos
# b = pontos na borda
# i+b= Área que procuramos
interior_points = area - boundary_points / 2 + 1
print(int(interior_points + boundary_points))
