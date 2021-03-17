"""
-- ПРИНЦИП РАБОТЫ --
Принцип описан в условии задачи - основная модификация алгоритма происходит при партиционировании массива,
вместо выделения O(n) дополнительной памяти мы создаем указатели и проверяя поэлементно с опорным элементом
меняем элементы местами если они находятся не в том поряде

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы не производим копирования массива - соответственно не выделяем память,
входные и выходные данные проверены написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Этот алгоритм является модификацией QuickSort - в худщем случае получим O(n^2) , в общем O(N * logN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы храним только указатели и ссылку на массив, так что не учитывая входные данные, O(n)
Сам алгоритм используем константную память O(1), точнее O(h) - где h - глубина рекурсии

-- ID успешной посылки --
49577281
"""
import sys


def main():
    n = int(input())

    participants = []

    for _ in range(n):
        login, completed, penalty = sys.stdin.readline().strip().split()
        participants.append((-int(completed), int(penalty), login))

    quick_sort_effective(participants, 0, len(participants) - 1)

    for person in participants:
        print(person[2])


def swap(array, left_swap, right_swap):
    array[left_swap], array[right_swap] = array[right_swap], array[left_swap]
    return array


def partition(haystack, left, right):
    median = (left + right) // 2
    pivot = haystack[median]

    swap_left = None
    swap_right = None

    while right - left > 1:
        if swap_left is None and haystack[left] < pivot:
            left += 1
        else:
            swap_left = left

        if swap_right is None and haystack[right] > pivot:
            right -= 1
        else:
            swap_right = right

        if swap_right is not None and swap_left is not None:
            swap(haystack, swap_left, swap_right)
            swap_left = None
            swap_right = None

    if haystack[left] > haystack[right]:
        swap(haystack, left, right)

    return left, right


def quick_sort_effective(haystack, left, right):
    if right == left:
        return

    if right - left == 1:
        if haystack[left] > haystack[right]:
            swap(haystack, left, right)
        return

    part_left, part_right = partition(haystack, left, right)

    quick_sort_effective(haystack, left, part_left)
    quick_sort_effective(haystack, part_right, right)
    return


if __name__ == '__main__':
    main()
