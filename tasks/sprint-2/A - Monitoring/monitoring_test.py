import unittest
import io
from unittest.mock import patch

from monitoring import transpose_matrix, main


class FunctionValueTest(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '3',
        '1 2 3',
        '0 2 6',
        '7 4 1',
        '2 7 0'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 0 7 2',
            '2 2 4 7',
            '3 6 1 0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '9',
        '5',
        '-7 -1 0 -4 -9',
        '5 -1 2 2 9',
        '3 1 -8 -1 -7',
        '9 0 8 -8 -1',
        '2 4 5 2 8',
        '-7 10 0 -4 -8',
        '-3 10 -7 10 3',
        '1 6 -7 -5 9',
        '-1 9 9 1 9',

    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-7 5 3 9 2 -7 -3 1 -1',
            '-1 -1 1 0 4 10 10 6 9',
            '0 2 -8 8 5 0 -7 -7 9',
            '-4 2 -1 -8 2 -4 10 -5 1',
            '-9 9 -7 -1 8 -8 3 9 9',
        ]) + '\n')

    def test_edge(self):
        self.assertEqual(transpose_matrix(1, 1, [[1]]), [[1]])
        self.assertEqual(transpose_matrix(2, 2,
                                          [
                                              [1, 0],
                                              [0, 1]
                                          ]
                                          ),
                         [
                             [1, 0],
                             [0, 1]
                         ])

    def test_positive(self):
        self.assertEqual(transpose_matrix(4, 3,
                                          [
                                              [1, 2, 3],
                                              [0, 2, 6],
                                              [7, 4, 1],
                                              [2, 7, 0]
                                          ]
                                          ),
                         [
                             [1, 0, 7, 2],
                             [2, 2, 4, 7],
                             [3, 6, 1, 0],
                         ])
