def main():
    string = input()

    print(longest_substring(string))


def longest_substring(string):
    char_list = {}

    longest_length = 0
    current_start = 0
    for i, char in enumerate(string):
        if char in char_list and char_list[char] >= current_start:
            current_start = char_list[char] + 1

        current_length = i - current_start + 1
        longest_length = max(current_length, longest_length)
        char_list[char] = i

    return longest_length


if __name__ == '__main__':
    main()
