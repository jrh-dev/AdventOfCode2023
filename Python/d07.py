from collections import Counter


def ranker(s, map_hands):
    counts = Counter(s)
    if 5 in counts.values():
        return map_hands["5kind"]
    elif 4 in counts.values():
        return map_hands["4kind"]
    elif 3 in counts.values() and 2 in counts.values():
        return map_hands["fullhouse"]
    elif 3 in counts.values():
        return map_hands["3kind"]
    elif 2 in Counter(counts.values()).values():
        return map_hands["2pair"]
    elif 2 in counts.values():
        return map_hands["1pair"]
    else:
        return 1


def solve(hands, worth, map_cards, map_hands, part_1=True):
    by_value = [[] for _ in range(7)]

    for ii in range(len(hands)):
        if part_1:
            r = ranker(hands[ii], map_hands)
        else:
            s = hands[ii]
            counts = Counter(s.replace("J", ""))
            r = ranker(
                s
                if s == "JJJJJ"
                else s.replace(
                    "J",
                    list(counts.keys())[
                        list(counts.values()).index(max(counts.values()))
                    ],
                ),
                map_hands,
            )
        by_value[r - 1].append(hands[ii])

    for ii in range(len(by_value)):
        by_value[ii] = sorted(by_value[ii], key=lambda s: [map_cards[i] for i in s])

    by_value = [item for sublist in by_value for item in sublist]

    winnings = 0
    rank = 1

    for hand in by_value:
        winnings += rank * worth[hand]
        rank += 1

    return winnings


if __name__ == "__main__":
    with open("Data/d07/real.txt") as f:
        input = [i.split(" ") for i in f.read().split("\n")]

    worth = {}
    hands = []
    for k, v in input:
        worth[k] = int(v)
        hands.append(k)

    map_hands = {
        k: v + 2
        for v, k in enumerate(
            ["1pair", "2pair", "3kind", "fullhouse", "4kind", "5kind"]
        )
    }

    p1 = solve(
        hands=hands,
        worth=worth,
        map_cards={k: v + 1 for v, k in enumerate(list("23456789TJQKA"))},
        map_hands=map_hands,
        part_1=True,
    )

    p2 = solve(
        hands=hands,
        worth=worth,
        map_cards={k: v + 1 for v, k in enumerate(list("J23456789TQKA"))},
        map_hands=map_hands,
        part_1=False,
    )

    for i, ans in enumerate([p1, p2]):
        print(f"Part {i + 1} answer: {ans}")
