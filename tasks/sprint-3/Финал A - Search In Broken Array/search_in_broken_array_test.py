import unittest
import io
from unittest.mock import patch

from search_in_broken_array import binary_search, main


class SearchInBrokenArrayTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '9',
        '5',
        '19 21 100 101 1 4 5 7 12',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '6'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '9',
        '50',
        '19 21 100 101 1 4 5 7 12',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1',
        ]) + '\n')

    def test_edge(self):
        array = [1]
        self.assertEqual(binary_search(array, 0, 0, 1), 0)

        array = [1, 2]
        self.assertEqual(binary_search(array, 0, 1, 2), 1)

        array = [2, 1]
        self.assertEqual(binary_search(array, 0, 1, 2), 0)

    def test_positive(self):
        array = [2, 3, 1]
        self.assertEqual(binary_search(array, 0, 2, 3), 1)

        array = [1, 2, 3]
        self.assertEqual(binary_search(array, 0, 2, 3), 2)

        array = [3, 1, 2]
        self.assertEqual(binary_search(array, 0, 2, 3), 0)

        array = [3, 4, 1, 2]
        self.assertEqual(binary_search(array, 0, 3, 3), 0)

        array = [2, 3, 4, 1]
        self.assertEqual(binary_search(array, 0, 3, 3), 1)

        array = [1, 2, 3, 4]
        self.assertEqual(binary_search(array, 0, 3, 3), 2)

        array = [4, 1, 2, 3]
        self.assertEqual(binary_search(array, 0, 3, 3), 3)

    def test_negative(self):
        array = [2, 3, 1]
        self.assertEqual(binary_search(array, 0, 2, 4), -1)

        array = [1, 2, 3]
        self.assertEqual(binary_search(array, 0, 2, 4), -1)

        array = [3, 1, 2]
        self.assertEqual(binary_search(array, 0, 2, 4), -1)

        array = [3, 4, 1, 2]
        self.assertEqual(binary_search(array, 0, 3, 0), -1)

        array = [2, 3, 4, 1]
        self.assertEqual(binary_search(array, 0, 3, 0), -1)

        array = [1, 2, 3, 4]
        self.assertEqual(binary_search(array, 0, 3, 0), -1)

        array = [4, 1, 2, 3]
        self.assertEqual(binary_search(array, 0, 3, 0), -1)
