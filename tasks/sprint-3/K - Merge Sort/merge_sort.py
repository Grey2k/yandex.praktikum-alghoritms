from merge_algo import merge_sort


def main():
    seq = list(map(int, input().strip().split()))

    merge_sort(seq, 0, len(seq))
    print(' '.join([str(x) for x in seq]))


if __name__ == '__main__':
    main()
