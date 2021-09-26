def main():
    n = int(input().strip())
    strings = [''] * n

    min_len = 10 ** 7 + 1
    max_len = 0

    for i in range(n):
        strings[i] = input().strip()

        if len(strings[i]) > max_len:
            max_len = len(strings[i])

        if len(strings[i]) < min_len:
            min_len = len(strings[i])

    print(find_prefix(strings, min_len, max_len))


def find_prefix(strings: list, min_len, max_len) -> int:
    prefix = 0

    if min_len * max_len == 0:
        return 0

    if len(strings) == 0:
        return 0

    for i in range(max_len):
        try:
            char = None
            match = True
            for string in strings:
                if char is None:
                    char = string[i]

                if char != string[i]:
                    match = False
                    break

            if match:
                prefix += 1
                continue

            break
        except IndexError:
            break

    return prefix


if __name__ == '__main__':
    main()
