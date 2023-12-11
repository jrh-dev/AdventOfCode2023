def wins(winning: list[int], have: list[int]) -> int:
    s = 0
    for w in winning:
        if w in have:
            s += 1
    return s


def _worth(winners: int) -> int:
    s = 1
    for i in range(1, winners):
        s *= 2
    return s


def calc(winning: list[int], have: list[int]) -> int:
    w = wins(winning, have)
    if w == 0:
        return 0
    else:
        return _worth(w)


class card:
    def __init__(self, index: int, wins: int, n: int):
        self.index = index
        self.wins_tickets = list(range(index + 1, index + wins + 1))
        self.unscratched = n
        self.scratched = 0

    def add(self, n: int):
        self.unscratched += n

    def sub(self, n: int):
        self.unscratched -= n

    def scratch(self, n: int):
        self.scratched += n

    def state(self):
        return [self.index, self.wins_tickets, self.unscratched, self.scratched]

    def __repr__(self):
        return f"Card: {str(self.index)}"


if __name__ == "__main__":
    with open("Data/d04/real.txt") as f:
        input = f.read().split("\n")

    score = 0
    cards = []

    for ii in range(len(input)):
        parts = input[ii].split(" | ")
        char = parts[0].split(":")[0]
        list1 = [int(i) for i in parts[0].split(":")[1].split()]
        list2 = [int(i) for i in parts[1].split()]
        state = [(char, list1, list2)]

        score += calc(state[0][1], state[0][2])
        cards.append(card(ii, wins(state[0][1], state[0][2]), 1))

    try_card = 0

    while try_card < len(cards):
        _, get, n, _ = cards[try_card].state()

        if n > 0:
            for ind in get:
                cards[ind].add(n)
            cards[try_card].sub(n)
            cards[try_card].scratch(n)
            try_card = 0
        else:
            try_card += 1

    for i, ans in enumerate([score, sum([c.scratched for c in cards])]):
        print(f"Part {i + 1} answer: {ans}")
