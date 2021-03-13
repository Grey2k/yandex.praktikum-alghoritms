import unittest
import io
from unittest.mock import patch

from big_number import main


class BigNumberTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '15 56 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '56215',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '1 783 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '78321',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '2 4 5 2 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '542210',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '900',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '900',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '9 0 0 0 1 80 16',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '980161000',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '258 28 238 107',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '28258238107',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '74 748',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '74874',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '74 746',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eight(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '74746',
        ]) + '\n')
