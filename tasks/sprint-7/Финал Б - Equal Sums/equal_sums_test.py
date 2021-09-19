import unittest
import io
from unittest.mock import patch

from equal_sums import main


class EqualSumsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '1 5 7 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '2 10 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'False'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '10 8 6',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'False'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'False'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '7 9 3 4 6 7',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '11 11 9 9 5 5 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True'
        ]) + '\n')
