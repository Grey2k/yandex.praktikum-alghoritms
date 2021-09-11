cache = {}


def main():
    amount = int(input().strip())
    n = int(input().strip())

    banknotes = set(sorted(list(map(int, input().strip().split()))[:n]))

    print(how_many(amount, list(banknotes)))


def how_many(amount, banknotes: list):
    prob = tuple([amount] + banknotes)  # Problem signature
    if prob in cache:
        return cache[prob]  # We computed this before
    if amount == 0:
        return 1  # It's always possible to give an exact change of 0 cents
    if len(banknotes) == 1:
        if amount % banknotes[0] == 0:
            return 1  # We can match prescribed amount with this coin
        else:
            return 0  # It's impossible
    total = 0
    n = 0
    while n * banknotes[0] <= amount:
        total += how_many(amount - n * banknotes[0], banknotes[1:])
        n += 1
    cache[prob] = total  # Store in cache to avoid repeating this computation
    return total


if __name__ == '__main__':
    main()
