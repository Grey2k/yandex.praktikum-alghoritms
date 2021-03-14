def main():
    n = int(input())
    seq = list(map(int, input().strip().split()))[:n]

    bubble_sort(seq)


def bubble_sort(items):
    was_sorted = True
    while True:
        changes = 0

        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                changes += 1
                was_sorted = False

        if changes == 0:
            break

        print(' '.join([str(item) for item in items]))

    if was_sorted:
        print(' '.join([str(item) for item in items]))

    return items


if __name__ == '__main__':
    main()
