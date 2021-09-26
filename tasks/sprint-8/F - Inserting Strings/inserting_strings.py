def main():
    original = input().strip()
    n = int(input().strip())

    inserts = [(0, '')] * n
    for i in range(n):
        sub, pos = input().strip().split()
        inserts[i] = (int(pos), sub)

    new = ''
    offset = 0
    for pos, sub in sorted(inserts):
        new += original[offset:pos] + sub
        offset = pos

    new += original[offset:]

    print(new)


if __name__ == '__main__':
    main()
