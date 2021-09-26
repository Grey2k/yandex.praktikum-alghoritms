def main():
    n = int(input().strip())

    try:
        search = list(map(int, input().strip().split()[:n]))
    except EOFError:
        search = []

    m = int(input().strip())

    try:
        pattern = list(map(int, input().strip().split()[:m]))
    except EOFError:
        pattern = []

    print(' '.join(map(str, find_all(search, pattern))))


def find_all(search: list, pattern: list) -> list:
    occurrences = []

    len_pattern = len(pattern)
    len_search = len(search)

    if len_pattern > len_search:
        return occurrences

    start = 0

    while True:
        pos = find(search, pattern, start)

        if pos == -1:
            break

        occurrences.append(pos)
        start = pos

    return occurrences


def find(search: list, pattern: list, start: int) -> int:
    result = -1

    if start >= len(search):
        return result

    if len(search) - start < len(pattern):
        return result

    for pos in range(start, len(search) - len(pattern) + 1):
        shift = None
        match = True

        for offset in range(len(pattern)):
            if shift is None:
                shift = pattern[offset] - search[pos]

            if search[pos + offset] + shift != pattern[offset]:
                match = False
                break

        if match:
            result = pos + 1
            break

    return result


if __name__ == '__main__':
    main()
