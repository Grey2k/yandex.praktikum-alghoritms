"""
-- ПРИНЦИП РАБОТЫ --
Будем решать данную задачу разбив ее на две
1. Найти общий префикс - посимвольно сравниваем каждый символ
строки с другим символом на этой позиции, найдя длину - выводим сам префикс

2. Распаковать строку - посимвольно считываем строку,
если строка требует распаковки то делаем это рекурсивно считая правильную последовательность скобок

Для оптимизации распаковки добавленно кеширование

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Корректность работы подтверждена тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Для поиска общего префикса сложность
O (M * N) - где M - длина строки (максимальная), N - кол-во строк
Для распаковки строки сложность
O (M * N * K) - где M - длина строки (максимальная) K - кол-во вложенных уровней выражения, N - кол-во строк
Таким образом общая сложность будет равна O(M*N) + O(M*N*K) = O (M*N + M*N*K)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для поиска префикса - сложность O(1)
Для распаковки строк O(M) - с учетом кеширования O(M*N), M - длина строки (максимальная), N - кол-во строк

-- ID успешной посылки --
53621518
"""
from string import digits

OPEN = '['
CLOSE = ']'
cache = {}


def main():
    n = int(input().strip())
    unpacked = [''] * n

    for i in range(n):
        try:
            packed = input().strip()
        except EOFError:
            packed = ''

        unpacked[i] = unpack(packed)

    print(find_prefix(unpacked))


def unpack(string: str, multiplier=1) -> str:
    if cache.get(string) is not None:
        return cache[string] * multiplier

    chunks = []
    string_len = len(string)

    if string_len == 0:
        cache[string] = ''
        return cache[string]

    mul = ''
    opened = 0
    flushed = True
    start = 0
    end = 0
    for i in range(string_len):
        char = string[i]

        if char in digits and not opened:
            mul += char
            continue

        if char == OPEN:
            if not opened:
                if end > start:
                    chunks.append(string[start:end])
                opened += 1
                flushed = True
                start = i
                continue

            opened += 1
            continue

        if char == CLOSE:
            if opened == 1:
                end = i
                opened = False
                if end - start > 1:
                    chunks.append(unpack(string[start + 1:end], int(mul if len(mul) > 0 else '1')))

                mul = ''
                flushed = True
                start = i + 1
                continue

            opened -= 1
            continue

        flushed = False
        end = i + 1

    if not flushed and start < end:
        chunks.append(string[start:end])

    cache[string] = ''.join(chunks)

    return cache[string] * multiplier


def find_prefix(strings: list) -> str:
    prefix = 0

    min_len = 10 ** 7 + 1
    max_len = 0

    for i in range(len(strings)):
        if len(strings[i]) > max_len:
            max_len = len(strings[i])

        if len(strings[i]) < min_len:
            min_len = len(strings[i])

    if min_len * max_len == 0:
        return ''

    if len(strings) == 0:
        return ''

    for i in range(max_len):
        try:
            char = None
            match = True
            for string in strings:
                if char is None:
                    char = string[i]

                if char != string[i]:
                    match = False
                    break

            if match:
                prefix += 1
                continue

            break
        except IndexError:
            break

    return strings[0][:prefix]


if __name__ == '__main__':
    main()
