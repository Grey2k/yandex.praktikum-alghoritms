def main():
    number = int(input().strip())

    print('True' if is_power(number) else 'False')


def is_power(number, power=4, limit=10_000):
    if number == 1:
        return True

    n = power
    powers = {n}

    while n <= limit:
        n *= n
        powers.add(n)

    return number in powers


if __name__ == '__main__':
    main()
