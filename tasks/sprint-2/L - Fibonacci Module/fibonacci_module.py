def main():
    n, k = map(int, input().strip().split())

    print(fibonacci(n) % (10 ** k))


def fibonacci(n):
    if n == 1:
        return 1

    if n == 0:
        return 1

    prev1 = 1
    prev2 = 1

    for _ in range(2, n):
        prev1, prev2 = prev2, prev1 + prev2

    return prev1 + prev2


if __name__ == '__main__':
    main()
