MODULO = 10 ** 9 + 7


def main():
    n, k = map(int, input().strip().split())

    # F0 = 0
    # F1 = 1
    # FN = Fn - 1 + ... Fn-k

    variants = [0, 1] + [0] * (n - 1)

    for stair in range(2, n + 1):
        for step in range(1, k + 1):
            if step <= stair:
                variants[stair] += variants[stair - step]

        variants[stair] = variants[stair] % MODULO

    print(str(variants[n]))


if __name__ == '__main__':
    main()
