import unittest
import io
from unittest.mock import patch

from matrix_neighbours import find_neighbours, main


class MatrixNeighboursTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '3',
        '1 2 3',
        '0 2 6',
        '7 4 1',
        '2 7 0',
        '3',
        '0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '7 7\n')

    def test_positive(self):
        self.assertEqual(find_neighbours(
            3,
            2,
            [
                [1, 2, 3],
                [0, 2, 6],
                [7, 4, 1],
                [2, 7, 0]
            ],
            3,
            0
        ), [7, 7])
