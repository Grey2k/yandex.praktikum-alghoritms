import sys


def main():
    amount = int(input().strip())
    n = int(input().strip())

    min_banknotes = [0] + [sys.maxsize] * amount
    banknotes = set(sorted(list(map(int, input().strip().split()))[:n]))

    # F0 = 0
    # F1 = Fa1 = Fan = 1
    # Fn = min((Fn - Fa1), (Fn - Fa2), (Fn - Fa3)) + 1
    for note in banknotes:
        if note > amount:
            continue

        min_banknotes[note] = 1

    # if still not found
    if min_banknotes[amount] == sys.maxsize:
        for summa in range(1, amount + 1):
            for note in banknotes:
                # if note fits and its better than another
                if summa >= note and min_banknotes[summa] > min_banknotes[summa - note] + 1:
                    min_banknotes[summa] = min_banknotes[summa - note] + 1

    if min_banknotes[amount] < sys.maxsize:
        print(str(min_banknotes[amount]))
    else:
        print('-1')


if __name__ == '__main__':
    main()
