"""
Success #  48258539
"""


def main():
    length = int(input())
    houses = [0 if x == '0' else 1 for x in input().split()]

    print(' '.join(map(str, find_closest_zeroes(length, houses))))


def find_closest_zeroes(length, houses):
    result = list(range(length - 1, -1, -1))

    has_zero = False
    steps = 0

    for i, house in enumerate(houses):
        if house == 0:
            result[i] = 0

            if has_zero and i > 0:
                for j in range(1, (steps // 2) + 1):
                    result[i - j] = j
            elif not has_zero and 0 < i < length - 1:
                for j in range(1, i + 1):
                    result[i - j] = j

            has_zero = True
            steps = 0

        elif has_zero:
            steps += 1
            result[i] = steps

    return result


if __name__ == '__main__':
    main()
