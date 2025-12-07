from grid import Grid


def part_1(path: str):
    f = open(path, "r")
    grid = Grid(f.read())
    f.close()

    for x in range(grid.w):
        if grid.get(x, 0) == "S":
            starting_x = x
            break

    beams_y: set[int] = set([starting_x])

    n_split = 0
    for y in range(grid.h):
        new_beams_y: set[int] = set()
        for beam_x in beams_y:
            if grid.get(beam_x, y) == ".":
                new_beams_y.add(beam_x)
            else:
                n_split += 1
                new_beams_y.add(beam_x + 1)
                new_beams_y.add(beam_x - 1)
        beams_y = new_beams_y

    return n_split


def part_2(path: str):
    f = open(path, "r")
    grid = Grid(f.read())
    f.close()

    for x in range(grid.w):
        if grid.get(x, 0) == "S":
            starting_x = x
            break

    timeline_map: dict[tuple[int, int], int] = {}

    def timelines_from_node(x: int, y: int, current: int) -> int:
        if y == grid.h - 1:
            timelines = current + 1
        else:
            if (x, y) in timeline_map:
                timelines = timeline_map.get((x, y))
            elif grid.get(x, y) == ".":
                timelines = timelines_from_node(x, y + 1, current)
            else:
                timelines = timelines_from_node(
                    x - 1, y + 1, current
                ) + timelines_from_node(x + 1, y + 1, current)
        timeline_map[(x, y)] = timelines
        return timelines

    return timelines_from_node(starting_x, 1, 0)
