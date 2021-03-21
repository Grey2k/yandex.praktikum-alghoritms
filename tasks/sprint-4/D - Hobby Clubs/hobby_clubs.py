import sys


def main():
    n = int(input())
    clubs = {}

    for _ in range(n):
        club = sys.stdin.readline().strip()
        clubs[club] = 1 if clubs.get(club) is None else clubs.get(club) + 1

    for key in clubs.keys():
        print(key)


if __name__ == '__main__':
    main()
