def main():
    needle = input().strip()
    haystack = input().strip()

    print(is_subsequence(needle, haystack))


def is_subsequence(needle, haystack):
    if len(needle) == 0:
        return True

    if len(haystack) == 0:
        return False

    index = 0
    current = needle[index]

    for item in haystack:
        if item == current:
            index += 1
            if len(needle) == index:
                return True

            current = needle[index]

    return False


if __name__ == '__main__':
    main()
