def main():
    string = input().strip()

    print(' '.join(map(str, prefix_function(string))))


def prefix_function(s: str) -> list:
    p = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = p[j - 1]
            else:  # j == 0
                i += 1
        else:  # s[j] == s[i]
            p[i] = j + 1
            i += 1
            j += 1

    return p


if __name__ == '__main__':
    main()
