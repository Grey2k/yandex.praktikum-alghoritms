def main():
    n = int(input())
    seq = list(map(int, input().strip().split()))[:n]
    k = int(input())

    # bruteforce pairs
    # print(sorted([abs(seq[j] - seq[i]) for i in range(len(seq)) for j in range(i + 1, len(seq))])[k - 1])

    print(trash_index(sorted(seq), k))

    """
    https://yandex-students.slack.com/archives/G01KQPM6999/p1615369853026600
    """


def trash_index(squares, k):
    if len(squares) == 2:
        return abs(squares[0] - squares[-1])

    # possible minimum module
    left = 0
    # max difference
    right = squares[-1] - squares[0]
    mid = (left + right) // 2

    while right > left:
        i = 1
        prev = 0
        count = 0
        while i < len(squares) and prev < len(squares):
            if prev > i:
                break

            diff = squares[i] - squares[prev]
            if diff > mid:
                prev += 1
                continue

            count += (i - prev)
            i += 1

            if count >= k:
                break

        if count >= k:
            left = left
            right = mid
        else:
            left = mid + 1
            right = right

        mid = (left + right) // 2

    return left


if __name__ == '__main__':
    main()
