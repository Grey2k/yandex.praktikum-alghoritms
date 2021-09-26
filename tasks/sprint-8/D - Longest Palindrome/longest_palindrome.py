def main():
    try:
        letters = list(input().strip())
    except EOFError:
        letters = []

    print(palindrome(letters))


def palindrome(letters: list) -> str:
    center = None
    sequence = [''] * (len(letters) // 2)
    gist = {}

    if len(letters) == 0:
        return ''

    for char in letters:
        if gist.get(char) is None:
            gist[char] = 1
        else:
            gist[char] += 1

    i = 0
    for char in sorted(gist.keys()):
        if gist[char] % 2 == 1:
            if center is None:
                center = char
            gist[char] -= 1

        for _ in range(gist[char] // 2):
            sequence[i] = char
            i += 1

    return ''.join(sequence) + (center if center is not None else '') + ''.join(reversed(sequence))


if __name__ == '__main__':
    main()
