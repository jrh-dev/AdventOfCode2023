def empty_sectors(universe):
    gal_width = len(universe[0])
    gal_height = len(universe)
    empty_rows = []
    empty_cols = []

    for row in range(gal_height):
        if "#" not in universe[row]:
            empty_rows.append(row)

    for col in range(gal_width):
        if "#" not in [universe[row][col] for row in range(gal_height)]:
            empty_cols.append(col)

    return empty_rows, empty_cols


def get_galaxy_locations(universe):
    galaxies = []
    for row in range(len(universe)):
        for col in range(len(universe[0])):
            if universe[row][col] == "#":
                galaxies.append((row, col))
    return galaxies


def get_distances(coords):
    """Returns a list of distances between all pairs of coordinates using Manhattan distance"""
    distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            distances.append(distance)
    return distances


def expand_universe(location, expansion, by):
    row_exp, col_exp = expansion
    r, c = location
    r = r + sum([r >= re for re in row_exp]) * by
    c = c + sum([c >= ce for ce in col_exp]) * by
    return r, c


if __name__ == "__main__":
    with open("Data/d11/real.txt") as f:
        universe = [line for line in f.read().split("\n")]

    expansion = empty_sectors(universe)
    galaxies = get_galaxy_locations(universe)

    for i, ans in enumerate([1, 999999]):
        print(
            f"Part {i + 1} answer: {sum(get_distances([expand_universe(l, expansion, ans) for l in galaxies]))}"
        )
