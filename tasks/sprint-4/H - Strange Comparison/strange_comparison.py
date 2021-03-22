from string import ascii_lowercase


def main():
    one = input()
    two = input()

    print('YES' if comparator(one, two) else 'NO')


def comparator(check, match):
    if not set(check).issubset(ascii_lowercase) or not set(match).issubset(ascii_lowercase):
        return False

    if len(check) != len(match):
        return False

    charset = {}
    used = {}

    for i, char in enumerate(match):
        if charset.get(char) is None and check[i] not in used:
            charset[char] = check[i]
            used[check[i]] = True
        elif charset.get(char) == check[i]:
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    main()
