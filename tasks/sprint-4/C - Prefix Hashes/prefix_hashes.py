import sys


def main():
    a = int(input())
    m = int(input())
    string = input()
    n = int(input())

    positions = []

    for _ in range(n):
        left, right = sys.stdin.readline().strip().split()
        positions.append((int(left), int(right)))

    length = len(string)
    hashes = [0] * (length + 1)

    for i in range(length):
        hashes[i + 1] = (hashes[i] * a + ord(string[i])) % m

    for left, right in positions:
        print(substr_hash(a, hashes, left, right, m))


def substr_hash(a, hashes, left, right, m):
    return (hashes[right] - pow(a, right - (left - 1), m) * hashes[left - 1] % m + m) % m


if __name__ == '__main__':
    main()
