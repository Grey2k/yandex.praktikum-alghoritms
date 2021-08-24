import unittest
import io
from unittest.mock import patch

from max_distance import main


class MaxDistanceTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5 4',
        '2 1',
        '4 5',
        '4 3',
        '3 2',
        '2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 3',
        '3 1',
        '1 2',
        '2 3',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6 8',
        '6 1',
        '1 3',
        '5 1',
        '3 5',
        '3 4',
        '6 5',
        '5 2',
        '6 2',
        '4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')
