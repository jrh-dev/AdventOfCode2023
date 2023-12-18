import math


def solve(time, distance):
    total = 1
    for t, d in zip(time, distance):
        c = 0
        for ms in range(math.ceil(d / t), t):
            if p := ((t - ms) * ms) > d:
                c += 1
        total = total * c
    return total


if __name__ == "__main__":
    with open("Data/d06/real.txt", "r") as file:
        lines = file.readlines()
        time = [int(i) for i in lines[0].split() if i.isdigit()]
        distance = [int(i) for i in lines[1].split() if i.isdigit()]

    p1 = solve(time, distance)
    p2 = solve(
        [int("".join(str(i) for i in time))], [int("".join(str(i) for i in distance))]
    )

    for i, ans in enumerate([p1, p2]):
        print(f"Part {i + 1} answer: {ans}")
