def main():
    m, n = map(int, input().strip().split())
    field = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        field[i] = [0] + list(map(int, list(input())))

    max_flowers = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(1, n + 1):
            max_flowers[i][j] = max(max_flowers[i][j - 1], max_flowers[i + 1][j]) + field[i][j]

    print(max_flowers[0][n])


if __name__ == '__main__':
    main()
