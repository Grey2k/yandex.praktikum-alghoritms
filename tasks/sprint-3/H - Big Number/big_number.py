from functools import cmp_to_key


def comparator(a, b):
    if int(a + b) > int(b + a):
        return 1
    if int(a + b) < int(b + a):
        return -1
    return 0


def main():
    n = int(input())
    numbers = input().strip().split()[:n]

    print(''.join(sorted(numbers, key=cmp_to_key(comparator))[::-1]))


if __name__ == '__main__':
    main()
