def odd_and_even(a, b, c):
    return a % 2 == b % 2 == c % 2


def main():
    a, b, c = map(int, input().strip().split())

    print('WIN' if odd_and_even(a, b, c) else 'FAIL')


if __name__ == '__main__':
    main()
