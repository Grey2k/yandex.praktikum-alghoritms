MODULE = 10 ** 9 + 7


def main():
    i = int(input().strip())

    print(str(fib_mod(i + 1)))


def fib_mod(i: int) -> int:
    fibs = [0, 1] + [0] * (i - 1)

    for n in range(2, i + 1):
        fibs[n] = (fibs[n - 1] + fibs[n - 2]) % MODULE

    return fibs[i]


if __name__ == '__main__':
    main()
