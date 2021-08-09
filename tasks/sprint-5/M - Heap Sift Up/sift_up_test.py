import unittest

from sift_up import sift_up


def print_heap(heap: list, _prefix="", idx: int = 1, _last=True):
    print(_prefix, "- " if _last else "|- ", heap[idx], sep="")
    _prefix += "   " if _last else "|  "

    left, right = get_children(heap, idx)

    if left is not None:
        print_heap(heap, _prefix, left[1], get_children(heap, left[1]) == (None, None))
    if right is not None:
        print_heap(heap, _prefix, right[1], get_children(heap, right[1]) == (None, None))


def get_children(heap: list, index: int):
    left_index = 2 * index
    right_index = 2 * index + 1

    left = (heap[left_index], left_index) if len(heap) > left_index else None
    right = (heap[right_index], right_index) if len(heap) > right_index else None

    return left, right


class SiftUpTest(unittest.TestCase):
    def test_edge(self):
        heap = [0, 1]

        print()
        print_heap(heap)
        result = sift_up(heap, 1)
        print()
        print_heap(heap)
        self.assertEqual(result, 1)

    def test_one(self):
        heap = [0, 12, 6, 8, 3, 15, 7]

        print()
        print_heap(heap)
        result = sift_up(heap, 5)
        print()
        print_heap(heap)
        self.assertEqual(result, 1)

    def test_two(self):
        heap = [0, 4, 12, 8, 3, 1, 7]

        print()
        print_heap(heap)
        result = sift_up(heap, 2)
        print()
        print_heap(heap)
        self.assertEqual(result, 1)

    def test_three(self):
        heap = [0, 89, 69, 49]

        print()
        print_heap(heap)
        result = sift_up(heap, 2)
        print()
        print_heap(heap)
        self.assertEqual(result, 2)

    def test_four(self):
        heap = [0, 4, 29, 49]

        print()
        print_heap(heap)
        result = sift_up(heap, 3)
        print()
        print_heap(heap)
        self.assertEqual(1, result)

    def test_five(self):
        heap = [0, 4, 29]

        print()
        print_heap(heap)
        result = sift_up(heap, 2)
        print()
        print_heap(heap)
        self.assertEqual(1, result)

    def test_six(self):
        heap = [0, 29, 4, 8, 15]

        print()
        print_heap(heap)
        result = sift_up(heap, 4)
        print()
        print_heap(heap)
        self.assertEqual(2, result)
