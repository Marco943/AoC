def part_1(path: str):
    f = open(path, "r")
    tiles: list[tuple[int, int]] = [
        tuple(map(int, line.split(",")))
        for line in f.read().strip().splitlines()
    ]
    f.close()

    max_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            dx = abs(tiles[i][0] - tiles[j][0]) + 1
            dy = abs(tiles[i][1] - tiles[j][1]) + 1
            area = dx * dy
            if area > max_area:
                max_area = area

    return max_area


def part_2(path: str):
    f = open(path, "r")
    tiles: list[tuple[int, int]] = [
        tuple(map(int, line.split(",")))
        for line in f.read().strip().splitlines()
    ]
    tiles.append(tiles[0])
    f.close()
    perimeter: list[tuple[int, int]] = []
    for i in range(len(tiles) - 1):
        sx, sy = tiles[i]
        ex, ey = tiles[i + 1]
        nx, ny = sx, sy
        dx = 0 if sx == ex else 1 if ex > sx else -1
        dy = 0 if sy == ey else 1 if ey > sy else -1
        while not (nx == ex and ny == ey):
            perimeter.append((nx, ny))
            nx, ny = nx + dx, ny + dy

    def is_block_inside(x, y) -> bool:
        count = 0
        for i in range(0, x + 1):
            for px, py in perimeter:
                if px == i and py == y:
                    count += 1
        if count % 2 == 0:
            return False
        return True

    def is_rectangle_valid(sx, sy, ex, ey) -> bool:
        for nx in range(min(sx, ex), max(sx, ex) + 1):
            for ny in range(min(sy, ey), max(sy, ey) + 1):
                if not is_block_inside(nx, ny):
                    return False
        return True

    max_area = 0
    for i in range(len(tiles)):
        for j in range(i, len(tiles)):
            sx, sy = tiles[i]
            ex, ey = tiles[j]
            if not is_rectangle_valid(sx, sy, ex, ey):
                continue
            dx = abs(tiles[i][0] - tiles[j][0]) + 1
            dy = abs(tiles[i][1] - tiles[j][1]) + 1
            area = dx * dy
            if area > max_area:
                max_area = area

    return max_area
