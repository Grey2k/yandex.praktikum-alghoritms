from collections import deque

DIGITS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def main():
    digit_seq = input().strip()

    result = []
    generator(deque(digit_seq), result=result)

    print(' '.join(result))


def generator(sequence, result, line=''):
    if len(sequence) == 0:
        result.append(line)
        return line

    else:
        digit = int(sequence.popleft())

        for char in DIGITS.get(digit):
            generator(sequence.copy(), result, line + char)


if __name__ == '__main__':
    main()
