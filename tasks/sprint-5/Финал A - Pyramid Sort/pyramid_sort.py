"""
-- ПРИНЦИП РАБОТЫ --
Из входных данных мы формируем кучу (бинарное дерево) и после вставки с помощью алгоритма просеивания
вверх с учетом компаратора восстанавливаем свойства кучи. После добавления всех элементов в кучу,
мы начинаем извлекать их в упорядоченном порядке в результирующий массив, восстанавливая свойства кучи
на каждой итерации выполняя просеивание вниз

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Алгоритм соотвествует корректности так как куча представляет собой приоритетную очередь по определению
а "приоритет" высчитывается c помощью компаратора в соответствии с задачей.
Так же написаны unit тесты для тестирования различных кейсов

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Пирамидальная сортировка в худшем случае покажет результат O(NLogN) где N - кол-во элеметов в заданном массиве

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы выделяем память под массив в котором храним все элементы кучи O(N)

-- ID успешной посылки --
52327353
"""
import sys


def main():
    n: int = int(input())

    # fake zero-index element
    participants: list = [-1]

    for idx in range(1, n + 1):
        login, completed, penalty = sys.stdin.readline().strip().split()
        participants.append((-int(completed), int(penalty), login))
        sift_up(participants, idx)

    for idx in range(n, 0, -1):
        print(participants[1][2])
        if idx > 1:
            participants[1] = participants.pop()
        sift_down(participants, 1)


def sift_up(heap: list, idx: int) -> int:
    if idx == 1:
        return idx

    parent_idx = idx // 2

    if heap[parent_idx] > heap[idx]:
        heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        idx = sift_up(heap, parent_idx)

    return idx


def sift_down(heap: list, idx: int) -> int:
    left_index = 2 * idx
    right_index = 2 * idx + 1
    heap_size = (len(heap) - 1)

    # no children
    if heap_size < left_index:
        return idx

    # has left & right children
    if right_index <= heap_size and heap[left_index] > heap[right_index]:
        index_largest = right_index
    else:
        index_largest = left_index

    if heap[idx] > heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        idx = sift_down(heap, index_largest)

    return idx


if __name__ == '__main__':
    main()
