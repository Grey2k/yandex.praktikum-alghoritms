def main():
    first = input().strip()
    second = input().strip()

    max_len = len(first) if len(first) > len(second) else len(second)

    first = first.zfill(max_len)
    second = second.zfill(max_len)

    print(sum_base(first, second))


def sum_base(first, second, base=2):
    carry = 0
    result = []

    for i in reversed(range(len(first))):
        digit = (int(first[i]) + int(second[i]) + carry)
        result.append(digit % base)

        if digit >= base:
            carry = 1
        else:
            carry = 0

    if carry > 0:
        result.append(carry)

    return ''.join(map(str, reversed(result))).lstrip('0') or '0'


if __name__ == '__main__':
    main()
