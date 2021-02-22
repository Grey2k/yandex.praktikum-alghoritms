def main():
    i = int(input())
    j = int(input())

    matrix = [[]] * i

    for n in range(i):
        matrix[n] = [x for x in map(int, input().split())][:j]

    transposed = transpose_matrix(i, j, matrix)

    for n in range(len(transposed)):
        print(' '.join(map(str, transposed[n])))


def transpose_matrix(i, j, matrix):
    transposed = [[None] * i for _ in range(j)]

    for x in range(i):
        for y in range(j):
            transposed[y][x] = matrix[x][y]

    return transposed


if __name__ == '__main__':
    main()
