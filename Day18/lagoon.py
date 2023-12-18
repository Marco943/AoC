import os

os.chdir("Day18")


plan = open("plan.txt", "r").readlines()

directions = {"R": (1, 0), "U": (0, -1), "D": (0, 1), "L": (-1, 0)}
r, c = (0, 0)

path = []
boundary_points = 0

for line in plan:
    dir, meters, _ = line.split(" ")
    meters = int(meters)
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
