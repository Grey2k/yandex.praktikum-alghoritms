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
        start = pos + 1

    return occurrences


def find(search: list, pattern: list, start: int) -> int:
    result = -1

    if start >= len(search):
        return result

    for i in range(start, len(search)):
        shift = None
        for j in range(len(pattern)):
            if search[i] == pattern[j] or shift is None:
                shift = search[i] - pattern[j]
            elif shift is not None and (search[i] + shift) == pattern[j]:
                continue
            else:
                return result

        return i


    return result


if __name__ == '__main__':
    main()
