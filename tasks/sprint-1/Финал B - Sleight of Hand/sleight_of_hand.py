import sys

FIELD_SIZE = 4
PLAYERS_HANDS = 2

"""
Success #  48259202
"""


def main():
    fingers = int(input())

    field = [[]] * FIELD_SIZE
    for i in range(FIELD_SIZE):
        field[i] = list(sys.stdin.readline().strip())

    print(score_hands(fingers, field))


def score_hands(fingers, field, hands=PLAYERS_HANDS):
    variants = dict()

    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if field[i][j] == '.':
                continue

            variants[field[i][j]] = variants[field[i][j]] + 1 if variants.get(field[i][j]) is not None else 1

    score = 0

    for value in variants.values():
        score += 1 if value <= fingers * hands else 0

    return score


if __name__ == '__main__':
    main()
