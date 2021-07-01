import math


def main():
    nodes = int(input())

    print(catalan_number(nodes))


def catalan_number(n: int) -> int:
    return int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1)))


if __name__ == '__main__':
    main()
