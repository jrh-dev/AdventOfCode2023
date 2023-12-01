import re


def parsey(string: str, mappings: dict) -> str:
    """
    Parse a string replacing numbers as words with corresponding
    digits whilst keeping existing digits. Allows overlaps of words.
    """
    parse = ""
    for i in range(len(string)):
        if string[i].isnumeric():
            parse += string[i]
        else:
            for k, v in mappings.items():
                length = len(k)
                if string[i : i + length] == k:
                    parse += v
    return parse


mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# cSpell:ignore parsey

if __name__ == "__main__":
    with open("Data/d01/real.txt") as f:
        input = f.read().split("\n")

    parsed_p1 = [re.findall("\d", i) for i in input]

    parsed_p2 = [parsey(i, mappings) for i in input]

    for i, parsed in enumerate([parsed_p1, parsed_p2]):
        print(f"Part {i} answer: {sum([int(p[0] + p[-1]) for p in parsed])}")
