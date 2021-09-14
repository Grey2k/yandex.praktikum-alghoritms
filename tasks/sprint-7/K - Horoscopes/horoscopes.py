def main():
    n = int(input().strip())
    first = list(map(int, input().strip().split()))[:n]

    m = int(input().strip())
    second = list(map(int, input().strip().split()))[:m]

    print("".join(map(str, first)))
    print("".join(map(str, second)))


if __name__ == '__main__':
    main()
