from itertools import groupby


def remap(mapping, follow):
    for m in mapping:
        start = m[1]
        end = m[1] + m[2]
        remap = m[0]
        if follow >= start and follow <= end:
            return remap + (follow - start)
    return follow


def min_loc(seeds, range_maps):
    output = []
    for seed in seeds:
        for rm in range_maps:
            seed = remap(rm[1:], seed)
        output.append(seed)

    return min(output)


def revmap(mapping, follow):
    for m in mapping:
        start = m[0]
        end = m[0] + m[2]
        remap = m[1]
        if follow >= start and follow <= end:
            return remap + (follow - start)
    return follow


def search_seed(try_loc, increment, range_maps_reversed, seed_ranges):
    searching = True
    while searching:
        loc = try_loc
        for rm in range_maps_reversed:
            loc = revmap(rm[1:], loc)
        for sr in seed_ranges:
            if loc >= sr[0] and loc <= sr[0] + sr[1]:
                if increment == 1:
                    idx = try_loc
                    searching = False
                else:
                    idx = search(
                        try_loc - increment,
                        increment // 10,
                        range_maps_reversed,
                        seed_ranges,
                    )
                    searching = False
        try_loc += increment
    return idx


if __name__ == "__main__":
    with open("Data/d05/real.txt") as f:
        input = f.read().split("\n")

    # input parsing
    split_input = [
        list(group) for key, group in groupby(input, lambda x: x == "") if not key
    ]

    for ii in range(len(split_input)):
        for jj in range(len(split_input[ii])):
            split_input[ii][jj] = tuple(
                int(i) for i in split_input[ii][jj].split() if i.isdigit()
            )

    # get answers
    p1 = min_loc(split_input[0][0], split_input[1:])

    seed_ranges = [
        (split_input[0][0][i], split_input[0][0][i + 1])
        for i in range(0, len(split_input[0][0]), 2)
    ]

    p2 = search_seed(0, 100000, split_input[1:][::-1], seed_ranges)

    for i, ans in enumerate([p1, p2]):
        print(f"Part {i + 1} answer: {ans}")
