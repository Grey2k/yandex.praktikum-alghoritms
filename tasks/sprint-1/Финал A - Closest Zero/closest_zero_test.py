import unittest
import io
from unittest.mock import patch

from closest_zero import find_closest_zeroes, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '0 1 4 9 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0 1 2 1 0\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '0 7 9 4 8 20'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0 1 2 3 4 5\n')

    def test_edge(self):
        self.assertEqual(find_closest_zeroes(1, [0]), [0])
        self.assertEqual(find_closest_zeroes(2, [0, 0]), [0, 0])
        self.assertEqual(find_closest_zeroes(3, [0, 1, 0]), [0, 1, 0])
        self.assertEqual(find_closest_zeroes(4, [0, 1, 2, 0]), [0, 1, 1, 0])

    def test_positive(self):
        self.assertEqual(find_closest_zeroes(4, [3, 1, 2, 0]), [3, 2, 1, 0])
        self.assertEqual(find_closest_zeroes(4, [0, 1, 2, 3]), [0, 1, 2, 3])
        self.assertEqual(find_closest_zeroes(5, [0, 1, 12, 2, 0]), [0, 1, 2, 1, 0])
        self.assertEqual(find_closest_zeroes(5, [1, 0, 12, 2, 0]), [1, 0, 1, 1, 0])
        self.assertEqual(find_closest_zeroes(5, [13, 1, 12, 0, 2]), [3, 2, 1, 0, 1])
        self.assertEqual(find_closest_zeroes(5, [13, 1, 12, 2, 0]), [4, 3, 2, 1, 0])
