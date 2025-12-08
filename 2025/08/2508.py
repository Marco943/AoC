def part_1(path: str):
    f = open(path, "r")
    boxes = [
        tuple(map(int, line.split(",")))
        for line in f.read().strip().splitlines()
    ]
    f.close()

    distances: list[tuple(int, int, float)] = []

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append(
                (
                    i,
                    j,
                    pow(boxes[i][0] - boxes[j][0], 2)
                    + pow(boxes[i][1] - boxes[j][1], 2)
                    + pow(boxes[i][2] - boxes[j][2], 2),
                )
            )

    distances.sort(key=lambda d: d[2])

    box_to_circuit: dict[int, int] = {}
    current_circuit = 1

    if len(boxes) > 50:
        pairs = 1000
    else:
        pairs = 10

    for i, j, _ in distances[:pairs]:
        if i in box_to_circuit and j in box_to_circuit:
            i_circuit = box_to_circuit[i]
            j_circuit = box_to_circuit[j]
            if i_circuit != j_circuit:
                for box in box_to_circuit.keys():
                    if box_to_circuit[box] == j_circuit:
                        box_to_circuit[box] = i_circuit
        elif i in box_to_circuit:
            box_to_circuit[j] = box_to_circuit[i]
        elif j in box_to_circuit:
            box_to_circuit[i] = box_to_circuit[j]
        else:
            box_to_circuit[i] = current_circuit
            box_to_circuit[j] = current_circuit
            current_circuit += 1

    circuits_to_boxes: dict[int, int] = {}

    for circuit in box_to_circuit.values():
        circuits_to_boxes[circuit] = circuits_to_boxes.get(circuit, 0) + 1

    prod = 1
    three_largest = sorted(circuits_to_boxes.values(), reverse=True)[:3]
    for c in three_largest:
        prod *= c

    return prod


def part_2(path: str):
    f = open(path, "r")
    boxes = [
        tuple(map(int, line.split(",")))
        for line in f.read().strip().splitlines()
    ]
    f.close()

    distances: list[tuple(int, int, float)] = []

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append(
                (
                    i,
                    j,
                    pow(boxes[i][0] - boxes[j][0], 2)
                    + pow(boxes[i][1] - boxes[j][1], 2)
                    + pow(boxes[i][2] - boxes[j][2], 2),
                )
            )

    distances.sort(key=lambda d: d[2])

    box_to_circuit: dict[int, int] = {n: n for n in range(len(boxes))}
    current_circuit = 1

    for i, j, _ in distances:
        if i in box_to_circuit and j in box_to_circuit:
            i_circuit = box_to_circuit[i]
            j_circuit = box_to_circuit[j]
            if i_circuit != j_circuit:
                for box in box_to_circuit.keys():
                    if box_to_circuit[box] == j_circuit:
                        box_to_circuit[box] = i_circuit
        elif i in box_to_circuit:
            box_to_circuit[j] = box_to_circuit[i]
        elif j in box_to_circuit:
            box_to_circuit[i] = box_to_circuit[j]
        else:
            box_to_circuit[i] = current_circuit
            box_to_circuit[j] = current_circuit
            current_circuit += 1
        if len(set(box_to_circuit.values())) <= 1:
            break

    return boxes[i][0] * boxes[j][0]
