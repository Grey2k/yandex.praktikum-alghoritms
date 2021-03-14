import unittest
import io
from unittest.mock import patch

from two_bicycles import main


class TwoBicyclesTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 2 4 4 6 8',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3 5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 2 4 4 4 4',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3 -1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 2 4 4 4 4',
        '10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1 -1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '1 2 4 4 4 4 10',
        '10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '7 -1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '15',
        '1 2 3 4 4 4 4 4 4 4 4 4 4 5 8',
        '4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4 15',
        ]) + '\n')

    def test_edge(self):
        pass
