def main():
    number = int(input())

    print(to_base(number))


def to_base(number, base=2):
    if number < base:
        return str(number)

    converted = []

    while number >= base:
        converted.append(str(number % base))
        number //= base

    converted.append(str(number))

    return ''.join(converted[::-1])


if __name__ == '__main__':
    main()
