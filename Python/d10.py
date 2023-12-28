def trace_pipe(moves, area_map):
    visited = []

    # find initial "S" as start point
    for y in range(len(area_map)):
        for x in range(len(area_map[y])):
            if area_map[y][x] == "S":
                break
        if area_map[y][x] == "S":
            break

    visited.append((x, y))

    # find a path away from start
    if area_map[y][x + 1] in ["-", "J", "7"]:
        x, y = x + 1, y
    elif area_map[y][x - 1] in ["-", "L", "F"]:
        x, y = x - 1, y
    elif area_map[y + 1][x] in ["|", "7", "F"]:
        x, y = x, y + 1
    elif area_map[y - 1][x] in ["|", "L", "J"]:
        x, y = x, y - 1

    visited.append((x, y))

    plotting = True

    while plotting:
        current = input[y][x]
        opts = (moves[current][0](x, y), moves[current][1](x, y))
        plotting = False
        for o in opts:
            if o in visited:
                pass
            else:
                plotting = True
                visited.append(o)
                x, y = o
                break

    return visited


def enclosed(pipe):
    """
    Pick's theorem & Shoelace formula implementation
    Credit to u/bakibol https://shorturl.at/uD018 for python implementation.
    """
    x, y = zip(*pipe)
    area = 0.5 * abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(pipe))))
    return int(area - 0.5 * len(pipe) + 1)


moves = {
    "|": [lambda x, y: (x, y + 1), lambda x, y: (x, y - 1)],
    "-": [lambda x, y: (x + 1, y), lambda x, y: (x - 1, y)],
    "L": [lambda x, y: (x, y - 1), lambda x, y: (x + 1, y)],
    "J": [lambda x, y: (x - 1, y), lambda x, y: (x, y - 1)],
    "7": [lambda x, y: (x - 1, y), lambda x, y: (x, y + 1)],
    "F": [lambda x, y: (x + 1, y), lambda x, y: (x, y + 1)],
}

if __name__ == "__main__":
    with open("Data/d10/real.txt") as f:
        input = [line for line in f.read().split("\n")]

    pipe_path = trace_pipe(moves, input)

    for i, ans in enumerate([len(pipe_path) // 2, enclosed(pipe_path)]):
        print(f"Part {i + 1} answer: {ans}")
