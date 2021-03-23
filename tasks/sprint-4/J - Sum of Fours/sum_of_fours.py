import itertools

N = 4


def main():
    n = int(input())
    s = int(input())

    if n == 0:
        print(0)
        return

    array = list(map(int, input().split()))
    sums = {}
    for item in itertools.combinations(range(len(array)), N // 2):
        cost = array[item[0]] + array[item[1]]

        if sums.get(cost) is None:
            sums[cost] = [item]
        else:
            sums[cost].append(item)

    fours = {}

    for cost in sorted(sums.keys()):
        if sums.get(cost) is None:
            continue

        if sums.get(s - cost) is None:
            del sums[cost]
            continue
        else:
            for item1 in sums[cost]:
                for item2 in sums[(s - cost)]:
                    if len(set(item1).intersection(set(item2))) > 0:
                        continue

                    item = tuple(sorted([array[item1[0]], array[item1[1]], array[item2[0]], array[item2[1]]]))
                    if fours.get(item) is None:
                        fours[item] = item

            del sums[s - cost]
            if sums.get(cost) is not None:
                del sums[cost]

    print(len(fours))
    for key in sorted(fours.keys()):
        print(' '.join(map(str, fours[key])))


if __name__ == '__main__':
    main()
