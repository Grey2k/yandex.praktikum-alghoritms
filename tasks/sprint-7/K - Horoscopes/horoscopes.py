def main():
    n = int(input().strip())
    first = list(map(int, input().strip().split()))[:n]

    m = int(input().strip())
    second = list(map(int, input().strip().split()))[:m]

    # print("".join(map(str, first)))
    # print("".join(map(str, second)))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    if n == 0 or m == 0:
        print(0)
    else:
        # restore
        answer = []
        lcs_first = []
        lcs_second = []

        i = n
        j = m

        while dp[i][j] != 0:
            if first[i - 1] == second[j - 1]:
                answer.append(first[i-1])
                lcs_first.append(i)
                lcs_second.append(j)
                i -= 1
                j -= 1
                continue
            elif dp[i][j] == dp[i - 1][j]:
                i -= 1
                continue
            elif dp[i][j] == dp[i][j - 1]:
                j -= 1
                continue

        print(dp[n][m])

        if dp[n][m] > 0:
            print(' '.join(map(str, reversed(lcs_first))))
            print(' '.join(map(str, reversed(lcs_second))))


if __name__ == '__main__':
    main()
