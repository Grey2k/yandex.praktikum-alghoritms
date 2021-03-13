COLOR_PINK = '0'
COLOR_YELLOW = '1'
COLOR_CRIMSON = '2'


def main():
    n = int(input())
    colors = input().strip().split()[:n]

    pink = []
    yellow = []
    crimson = []

    for color in colors:
        if color == COLOR_PINK:
            pink.append(color)
            continue

        if color == COLOR_YELLOW:
            yellow.append(color)
            continue

        if color == COLOR_CRIMSON:
            crimson.append(color)
            continue

    print(' '.join(pink + yellow + crimson))


if __name__ == '__main__':
    main()
