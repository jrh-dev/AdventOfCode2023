import math
import re


def solver(describe: str, maximums: list[int]) -> tuple[int]:
    """
    Solves part 1 & 2 of the problem for day 2
    Args:
        describe (str): A string describing the observation of a game
        maximums (list[int]): The maximum cubes available (red, green, blue)
    Returns:
        tuple(int): The game id of the game if it is valid, else 0 and the
        product of the max cubes in the game 
    """
    gid = re.sub("\D", "", describe.split(":")[0])
    outcomes = describe.split(":")[1].split(";")
    collect = [0, 0, 0]
    for state in outcomes:
        for i in state.split(","):
            if "red" in i:
                collect[0] = max(collect[0], int(re.sub("\D", "", i)))
            if "green" in i:
                collect[1] = max(collect[1], int(re.sub("\D", "", i)))
            if "blue" in i:
                collect[2] = max(collect[2], int(re.sub("\D", "", i)))
    if (
        collect[0] <= maximums[0]
        and collect[1] <= maximums[1]
        and collect[2] <= maximums[2]
    ):
        part_1 = int(gid)
    else:
        part_1 = 0
    part_2 = math.prod(collect)

    return part_1, part_2


if __name__ == "__main__":
    with open("Data/d02/real.txt") as f:
        input = f.read().split("\n")

    part_1 = 0
    part_2 = 0

    for i in input:
        p1, p2 = solver(i, [12, 13, 14])
        part_1 += p1
        part_2 += p2
    
    for i, ans in enumerate([part_1, part_2]):
        print(f"Part {i + 1} answer: {ans}")