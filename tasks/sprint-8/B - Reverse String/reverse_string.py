def main():
    try:
        words = input().strip().split()
    except EOFError:
        words = []

    print(' '.join(words[::-1]))


if __name__ == '__main__':
    main()
