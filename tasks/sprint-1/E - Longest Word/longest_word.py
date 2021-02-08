import string


def main():
    length = int(input())
    sentence = input()

    # Find longest word
    word = longest_word(length, sentence)

    print(word)
    print(len(word))


def longest_word(length, sentence):
    word = []

    flag = False
    tmp = []

    for i in range(length):
        if flag is True:
            if sentence[i] == ' ':
                flag = False

                if len(tmp) > len(word):
                    word = tmp[:]

                tmp.clear()
                continue

            if sentence[i] in string.ascii_lowercase:
                tmp.append(sentence[i])

            if i == length - 1:
                if len(tmp) > len(word):
                    word = tmp[:]

                tmp.clear()

            continue

        if flag is False:
            if sentence[i] in string.ascii_lowercase:
                flag = True
                tmp.append(sentence[i])
                continue

    return ''.join(word)


if __name__ == '__main__':
    main()
