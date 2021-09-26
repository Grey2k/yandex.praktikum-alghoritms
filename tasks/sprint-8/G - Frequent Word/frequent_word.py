def main():
    n = int(input().strip())
    words = {}

    for _ in range(n):
        word = input().strip()

        if words.get(word) is None:
            words[word] = 1
        else:
            words[word] += 1

    frequency = 0
    most_frequent = None

    for word in sorted(words.keys()):
        if words[word] > frequency:
            frequency = words[word]
            most_frequent = word

    print(most_frequent)


if __name__ == '__main__':
    main()
