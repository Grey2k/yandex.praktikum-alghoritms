RESULT_OK = 'OK'
RESULT_FAIL = 'FAIL'


def main():
    try:
        first = input().strip()
    except EOFError:
        first = ''

    try:
        second = input().strip()
    except EOFError:
        second = ''

    print(RESULT_OK if control(first, second) else RESULT_FAIL)


def control(first: str, second: str) -> bool:
    len_first = len(first)
    len_second = len(second)

    if abs(len_first - len_second) > 1:
        return False

    max_len = max(len_first, len_second)

    i = 0
    j = 0

    diff = 0
    while i < max_len and j < max_len:
        try:
            if first[i] == second[j]:
                i += 1
                j += 1
                continue
            elif first[i] != second[j] and len_second != len_first:
                if len_first > len_second:
                    i += 1
                else:
                    j += 1

                diff += 1
            else:
                diff += 1
                i += 1
                j += 1
        except IndexError:
            if len_first > len_second:
                i += 1
            else:
                j += 1

            diff += 1

        if diff > 1:
            return False

    return True


if __name__ == '__main__':
    main()
