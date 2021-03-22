WIN = '1'


def main():
    n = int(input())
    try:
        rounds = input().strip().split()[:n]
    except EOFError:
        rounds = []

    score_history = {0: 0}
    max_period = 0
    current_period = 0
    current_score = 0

    if len(rounds) in (0, 1):
        print(max_period)
        return

    for index, result in enumerate(rounds):
        current_score += 1 if result == WIN else -1

        if current_score in score_history:
            current_period = index - score_history[current_score] + 1
        else:
            score_history[current_score] = index + 1

        if current_period > max_period:
            max_period = current_period

    print(max_period)


if __name__ == '__main__':
    main()
