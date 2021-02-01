def main():
    a, x, b, c = map(int, input().split())
    print(function_value(a, x, b, c))


def function_value(a, x, b, c):
    return a * x ** 2 + b * x + c


if __name__ == '__main__':
    main()
