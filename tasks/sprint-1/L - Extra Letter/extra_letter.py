def main():
    first = str(input().strip())
    second = str(input().strip())

    print(find_extra(first, second))


def find_extra(first, second):
    letters = {}

    for char in first:
        letters[char] = letters[char] + 1 if letters.get(char) is not None else 1

    for char in second:
        if letters.get(char) in {None, 0}:
            return char

        letters[char] -= 1

    return None


if __name__ == '__main__':
    main()
