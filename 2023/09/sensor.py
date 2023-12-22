histories = [
    [[int(value) for value in reversed(values.split(" "))]]
    for values in open("Day9/sensor.txt", "r").read().strip().split("\n")
]
generate_deltas = lambda h: [h[i + 1] - h[i] for i in range(0, len(h) - 1)]  # noqa: E731
for history in histories:
    while any(map(bool, history[-1])):
        history.append(generate_deltas(history[-1]))
    history[-1].append(0)
    for i in range(len(history) - 1, 0, -1):
        history[i - 1].append(history[i - 1][-1] + history[i][-1])


print(sum(map(lambda x: x[0][-1], histories)))
