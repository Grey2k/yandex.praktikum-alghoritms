def main():
    n = int(input())
    anagrams = input().strip().split()[:n]

    hashes = {}
    indexes = {}

    for index, anagram in enumerate(anagrams):
        key = ''.join(sorted(anagram))
        if hashes.get(key) is None:
            hashes[key] = index
            indexes[index] = [index]
        else:
            indexes[hashes[key]].append(index)

    for index in indexes.keys():
        print(' '.join(map(str, indexes[index])))


if __name__ == '__main__':
    main()
