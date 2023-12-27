from itertools import pairwise

def next_n(l: list[int]) -> list[int]:
    next_from = l[-1]
    dif = []
    while len(set(l)) != 1:
        l = [b - a for a, b in pairwise(l)]
        dif.append(l[-1])
    return sum(dif) + next_from

def solve(input: list[int], reverse) -> int:
    if reverse:
        input = [i[::-1] for i in input]
    return sum([next_n(i) for i in input])

if __name__ == "__main__":
    with open("Data/d09/real.txt") as f:
        input = [[int(i) for i in line.split(" ")] for line in f.read().split("\n")]
    
    for i, ans in enumerate([False, True]):
        print(f"Part {i + 1} answer: {solve(input, ans)}")
