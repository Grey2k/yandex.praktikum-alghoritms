import string

ALPHABET = set(list(string.ascii_lowercase)[1::2])


def main():
    try:
        first = ''.join(filter(lambda char: char in ALPHABET, list(input().strip())))
    except EOFError:
        first = ''

    try:
        second = ''.join(filter(lambda char: char in ALPHABET, list(input().strip())))
    except EOFError:
        second = ''

    if first < second:
        print('-1')
    elif first > second:
        print('1')
    else:
        print('0')


if __name__ == '__main__':
    main()
