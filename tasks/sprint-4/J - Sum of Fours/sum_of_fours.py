import itertools


def main():
    n = int(input())
    s = int(input())

    if n == 0:
        print(0)
        return

    array = list(map(int, input().split()))[:n]

    fours = {}
    for four in itertools.combinations(sorted(array), 4):
        item = tuple(sorted(four))
        if item not in fours and sum(four) == s:
            fours[item] = item

    print(len(fours))
    for four in fours:
        print(' '.join(map(str, four)))


if __name__ == '__main__':
    main()
