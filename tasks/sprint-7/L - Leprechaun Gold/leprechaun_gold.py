import copy


def main():
    n, m = map(int, input().split())
    bars = sorted(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(2)]

    idx = 0
    idx_prev = 1

    for i in range(n):
        bar = bars[i]
        dp[idx] = copy.copy(dp[idx_prev])
        for j in range(bar, m + 1):
            dp[idx][j] = dp[idx_prev][j] \
                if dp[idx_prev][j] > (bar + dp[idx_prev][j - bar]) \
                else (bar + dp[idx_prev][j - bar])

        idx, idx_prev = idx_prev, idx

    print(dp[idx_prev][m])


if __name__ == '__main__':
    main()
