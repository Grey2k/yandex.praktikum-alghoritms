import sys

A = 1000
M = 1000009


def main():
    n, k = tuple(map(int, input().split()))
    string = input()

    if n == 0 or k == 0:
        print('0')
        return

    length = len(string)
    hashes = [0] * (length + 1)

    for i in range(length):
        hashes[i + 1] = (hashes[i] * A + ord(string[i])) % M

    substr_hashes = {}
    indexes = {}
    for left, right in [(i, i + n - 1) for i in range(length - n)]:
        s_hash = substr_hash(A, hashes, left, right, M)
        count = substr_hashes.get(s_hash)
        if count is None:
            substr_hashes[s_hash] = 1
        else:
            substr_hashes[s_hash] += 1

        if indexes.get(s_hash) is None:
            indexes[s_hash] = str(left - 1)

    print(' '.join([value for key, value in indexes.items() if substr_hashes[key] >= k]))


def substr_hash(a, hashes, left, right, m):
    return (hashes[right] - pow(a, right - (left - 1), m) * hashes[left - 1] % m + m) % m


if __name__ == '__main__':
    main()
