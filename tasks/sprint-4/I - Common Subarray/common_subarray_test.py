import unittest
import io
from unittest.mock import patch

from common_subarray import main


class CommonSubarrayTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 2 1',
        '5',
        '3 2 1 5 6',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 4 5',
        '3',
        '4 5 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1',
        '3',
        '4 1 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 1 1 1 1',
        '5',
        '1 1 1 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '0 1 1 1 1',
        '4',
        '1 1 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '0 1 1 1 1',
        '4',
        '1 1 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '0 0',
        '6',
        '1 0 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '12',
        '0 0 5 6 1 0 1 1 0 1 1 1',
        '7',
        '1 0 1 0 1 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eight(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '5',
        ]) + '\n')
