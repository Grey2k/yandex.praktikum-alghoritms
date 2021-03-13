def main():
    homes_num, budget = map(int, input().strip().split())
    homes = list(map(int, input().strip().split()))[:homes_num]

    bought = 0

    for home in sorted(homes):
        if home > budget:
            break

        budget -= home
        bought += 1

    print(bought)


if __name__ == '__main__':
    main()
