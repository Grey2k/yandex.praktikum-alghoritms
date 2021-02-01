def main():
    days = int(input())

    # Remove all values which don't match our conditions
    weather = [x for x in map(int, input().split()) if abs(x) <= 273][:days]

    # If we've filtered too much
    days = len(weather)
    print(chaos_days(days, weather))


def chaos_days(days, weather):
    counter = 0

    # Edge conditions
    if days == 0:
        return counter

    if days == 1:
        return 1

    # First condition
    if weather[0] > weather[1]:
        counter += 1

    # Last condition
    if weather[-1] > weather[-2]:
        counter += 1

    if days > 2:
        for i in range(1, days - 1):
            if weather[i - 1] < weather[i] and weather[i] > weather[i + 1]:
                counter += 1

    return counter


if __name__ == '__main__':
    main()
