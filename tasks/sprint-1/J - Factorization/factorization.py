def main():
    number = int(input().strip())

    print(' '.join(map(str, factorization(number))))


def factorization(number):
    # minimal simple number
    divisor = 2

    if number == divisor:
        return [divisor]

    result = []

    # while divisor <= sqrt(number)
    while divisor * divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
            number //= divisor
        else:
            divisor += 1

    # number is simple if do not divided by any dividers
    if number > 1:
        result.append(number)

    return sorted(result)


if __name__ == '__main__':
    main()
