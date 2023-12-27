import math


def lcm_list(nums: list[int]) -> int:
    """Return lowest common multiple form a list of int."""
    lcm = nums[0]
    for i in nums[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


def parse_input_helper(text: str) -> str:
    """Return only alphabetic characters from a string, specifically targeted at the puzzle input for d8."""
    return "".join(c for c in text if c.isalpha())


if __name__ == "__main__":
    with open("Data/d08/real.txt") as f:
        input = [i.split(" ") for i in f.read().split("\n")]

    direct = input[0][0]
    maps = {}

    for i in input[2:]:
        maps[i[0]] = (parse_input_helper(i[2]), parse_input_helper(i[3]))

    ## Part 1
    current = "AAA"
    idx = 0

    while current != "ZZZ":
        d = direct[idx % len(direct)]
        idx += 1
        current = maps[current][0] if d == "L" else maps[current][1]

    p1 = idx

    ## Part 2
    currents = []
    steps = []

    for k, _ in maps.items():
        if k[2] == "A":
            currents.append(k)

    for current in currents:
        idx = 0

        while current[2] != "Z":
            d = direct[idx % len(direct)]
            idx += 1
            current = maps[current][0] if d == "L" else maps[current][1]

        steps.append(idx)

    p2 = lcm_list(steps)

    for i, ans in enumerate([p1, p2]):
        print(f"Part {i + 1} answer: {ans}")
