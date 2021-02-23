def main():
    n = int(input())

    print(fibonacci_recursive(n))


def fibonacci_recursive(n):
    if n == 1:
        return 1

    if n == 0:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == '__main__':
    main()
