def main():
    n = int(input().strip())

    try:
        values = list(map(int, input().strip().split()))
    except EOFError:
        values = []

    print(str(max_profit(values, n)))


def max_profit(prices: list, n: int):
    if not prices:
        return 0

    max_prof = 0
    i = 0

    while True:
        buy_price = prices[i]
        sell_price = 0

        # find first minimum
        if i < n - 2:
            for j in range(i + 1, n - 1):
                if prices[j] > buy_price:
                    break

                if prices[j] <= buy_price:
                    buy_price = prices[j]
                    i = j
                    continue

        # find next maximum
        for k in range(i + 1, n):
            if prices[k] < sell_price:
                break

            if prices[k] >= buy_price:
                sell_price = prices[k]
                i = k
                continue

        # if pair found - calculate
        if buy_price < sell_price:
            max_prof += sell_price - buy_price
        else:
            break

        if i < n - 2:
            i += 1
            continue

        break

    return max_prof


if __name__ == '__main__':
    main()
