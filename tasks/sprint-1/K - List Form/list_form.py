def main():
    length = int(input().strip())
    first = str(input().strip())
    second = int(input().strip())

    print(to_list_form(from_list_form(length, first) + second))


def from_list_form(length, list_form):
    return int(''.join(list_form.split()[:length]))


def to_list_form(number):
    return ' '.join(list(str(number)))


if __name__ == '__main__':
    main()
