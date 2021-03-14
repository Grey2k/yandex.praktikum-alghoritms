NOT_ENOUGH_MONEY = -1


def main():
    n = int(input())
    seq = input().split()
    amount = int(input())

    one = day_search(seq, amount, 0, n)
    two = - 1 if one == NOT_ENOUGH_MONEY else day_search(seq, amount * 2, one - 1, n)

    print('{} {}'.format(one, two))


def day_search(haystack, needle, left, right):
    result = NOT_ENOUGH_MONEY

    if left == right:
        return result

    if right - left == 1:
        return result if int(haystack[left]) < needle else left + 1

    l, m, r = left, (left + right) // 2, right

    while (r - l) > 1:
        if int(haystack[m - 1]) < needle <= int(haystack[m]):
            return m + 1

        if int(haystack[m]) < needle:
            l = m
            m = (l + r) // 2
            continue

        if int(haystack[m]) >= needle:
            r = m
            m = (r - l) // 2

    if int(haystack[l]) >= needle:
        return l + 1

    return result


if __name__ == '__main__':
    main()
