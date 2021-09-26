RESULT_YES = 'YES'
RESULT_NO = 'NO'


def main():
    try:
        first = input().strip()
    except EOFError:
        first = ''

    try:
        second = input().strip()
    except EOFError:
        second = ''

    print(RESULT_YES if compare(first, second) else RESULT_NO)


def compare(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    if len(first) == len(second) == 0:
        return True

    alphabet = {k: None for k in first}
    used = {k: False for k in second}

    for i in range(len(first)):
        if alphabet.get(first[i]) is None and not used[second[i]]:
            alphabet[first[i]] = second[i]
            used[second[i]] = True
        elif alphabet.get(first[i]) != second[i]:
            return False

    return True


if __name__ == '__main__':
    main()
