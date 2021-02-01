import sys


def main():
    h = int(input())
    w = int(input())

    matrix = []

    for _ in range(h):
        matrix.append(list(map(int, sys.stdin.readline().strip().split())))

    i = int(input())
    j = int(input())

    print(" ".join(map(str, sorted(find_neighbours(h - 1, w - 1, matrix, i, j)))))


def find_neighbours(max_i, max_j, matrix, i, j):
    targets = [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1]
    ]

    neighbours = []

    for target in targets:
        if 0 <= target[0] <= max_i and 0 <= target[1] <= max_j:
            neighbours.append(matrix[target[0]][target[1]])

    return neighbours


if __name__ == '__main__':
    main()
