import sys
from functools import cmp_to_key


def comparator(a, b):
    if a[0] > b[0]:
        return 1

    if a[0] < b[0]:
        return -1

    return 0


def main():
    n = int(input())

    beds = []
    for _ in range(n):
        beds.append(list(map(int, sys.stdin.readline().strip().split())))

    merged = merge_beds(sorted(beds, key=cmp_to_key(comparator)))

    for bed in merged:
        print('{} {}'.format(bed[0], bed[1]))


def merge_beds(beds_list):
    merged = []

    opened = False
    current = [0, 0]
    for bed in beds_list:
        if not opened:
            current = bed[:]
            opened = True
            continue

        if current[0] <= bed[0] <= current[1]:
            if bed[1] >= current[1]:
                current[1] = bed[1]
                continue
            else:
                continue

        merged.append(current)
        current = bed[:]

    if opened:
        merged.append(current)

    return merged


if __name__ == '__main__':
    main()
