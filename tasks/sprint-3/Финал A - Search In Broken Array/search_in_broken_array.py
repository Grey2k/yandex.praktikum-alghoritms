"""
-- ПРИНЦИП РАБОТЫ --
Если масив был сдвинут то дополнительно для использования бинарного поиска нам нужно
организоавть проверку на нахождение отсортированной половины массива, сравнив левый конец с медианой
Далее воспользуемся обычным бинарным поиском

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
По условию задачи мы имеем дело с массивом с уникальными элементами, остальные случаи проверены написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
при каждой итерации мы сокращаем интервал поиска в два раза, соответственно сложность будет O(logN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы храним искомый массив + дополнительные счетчики + используем рекурсивный алгоритм, из-за этого сложность O(logN)
Так как мы делаем O(logN) вызовов в худшем случае и храним на стеке значения каждого вызова,
в python не используется оптимизация хвостовой рекурсии (TCO)

-- ID успешной посылки --
49458142
"""


def main():
    n = int(input())
    needle = int(input())
    array = list(map(int, input().strip().split()))[:n]

    print(binary_search(array, 0, len(array) - 1, needle))


def binary_search(haystack, left, right, needle):
    mid = (left + right) // 2

    if haystack[mid] == needle:
        return mid

    if right - left <= 0:
        return -1

    # if left part sorted
    if haystack[left] < haystack[mid]:
        if haystack[left] <= needle < haystack[mid]:
            return binary_search(haystack, left, mid, needle)
        else:
            return binary_search(haystack, mid + 1, right, needle)

    # if right part sorted
    if haystack[left] >= haystack[mid]:
        if haystack[mid] < needle <= haystack[right]:
            return binary_search(haystack, mid + 1, right, needle)
        else:
            return binary_search(haystack, left, mid, needle)


if __name__ == '__main__':
    main()
