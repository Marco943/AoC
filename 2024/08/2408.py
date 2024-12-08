from grid import Grid


def part_1(path: str):
    grid = Grid(pattern=open(path, "r").read())
    antennas: dict[str, list[tuple[int, int]]] = {}

    for x in range(grid.w):
        for y in range(grid.h):
            value = grid.get(x, y)
            if value != ".":
                if value not in antennas:
                    antennas[value] = []
                antennas[value].append((x, y))

    antinodes: set[tuple[int, int]] = set()
    for antenna, nodes in antennas.items():
        for i, (x1, y1) in enumerate(nodes):
            for x2, y2 in nodes[i + 1 :]:
                dx, dy = x1 - x2, y1 - y2
                antinode_1 = x1 + dx, y1 + dy
                antinode_2 = x2 - dx, y2 - dy

                for nx, ny in (antinode_1, antinode_2):
                    value = grid.get(nx, ny)
                    if value is None:
                        continue
                    antinodes.add((nx, ny))
    return len(antinodes)


def part_2(path: str):
    grid = Grid(pattern=open(path, "r").read())
    antennas: dict[str, list[tuple[int, int]]] = {}

    for x in range(grid.w):
        for y in range(grid.h):
            value = grid.get(x, y)
            if value != ".":
                if value not in antennas:
                    antennas[value] = []
                antennas[value].append((x, y))

    antinodes: set[tuple[int, int]] = set()
    for antenna, nodes in antennas.items():
        for i, (x1, y1) in enumerate(nodes):
            for x2, y2 in nodes[i + 1 :]:
                dx, dy = x1 - x2, y1 - y2
                for inc in (1, -1):
                    n = 0
                    while True:
                        nx, ny = x1 + n * dx, y1 + n * dy
                        value = grid.get(nx, ny)
                        if value is None:
                            break
                        antinodes.add((nx, ny))
                        n += inc

    return len(antinodes)
