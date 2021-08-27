import unittest
import io
from unittest.mock import patch

from time_to_exit import main


class TimeToExitTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '6 8',
        '2 6',
        '1 6',
        '3 1',
        '2 5',
        '4 3',
        '3 2',
        '1 2',
        '1 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 11',
            '1 6',
            '8 9',
            '7 10',
            '2 3',
            '4 5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 2',
        '1 2',
        '2 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 5',
            '1 4',
            '2 3',
        ]) + '\n')
