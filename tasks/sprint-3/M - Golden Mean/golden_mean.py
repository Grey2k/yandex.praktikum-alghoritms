def main():
    n = int(input())
    k = int(input())

    north = list(map(int, input().split()))[:n]
    south = list(map(int, input().split()))[:k]

    print('{0:g}'.format(calculate_mean(sorted(north + south))))


def calculate_mean(seq):
    mean = 0

    if len(seq) == 0:
        return mean

    if len(seq) == 1:
        return seq[0]

    l, m, r = 0, len(seq) // 2, len(seq)

    mean = seq[m] if (r - l) % 2 != 0 else (seq[m] + seq[m - 1]) / 2

    return mean


if __name__ == '__main__':
    main()
