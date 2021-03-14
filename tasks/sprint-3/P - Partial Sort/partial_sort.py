def main():
    n = int(input())
    seq = list(map(int, input().strip().split()))[:n]

    print(len(get_partitions(seq)))


def get_partitions(seq):
    partitions = []

    if len(seq) == 0:
        return partitions

    if len(seq) == 1:
        partitions.append(seq)
        return partitions

    current = seq.copy()
    size = 1

    while len(current) > 0:
        while size <= len(current):
            if size == len(current):
                partitions.append(current)
                current = []
                break

            block = current[:size]
            if max(block) > min(current[size:]):
                size += 1
                continue

            partitions.append(block)
            current = current[size:]
            size = 1

    return partitions


if __name__ == '__main__':
    main()
