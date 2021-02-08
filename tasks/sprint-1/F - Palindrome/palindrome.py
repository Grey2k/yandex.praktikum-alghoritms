import string


def main():
    sentence = input().strip()

    print('True' if palindrome(sentence) else 'False')


def palindrome(sentence):
    filtered = [ch.lower() for ch in sentence if ch in string.digits or ch in string.ascii_letters]

    return filtered == filtered[::-1]


if __name__ == '__main__':
    main()
