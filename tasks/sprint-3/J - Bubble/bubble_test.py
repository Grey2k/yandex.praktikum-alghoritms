import unittest
import io
from unittest.mock import patch

from bubble import main


class BubbleTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '4 3 9 2 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3 4 2 1 9',
            '3 2 1 4 9',
            '2 1 3 4 9',
            '1 2 3 4 9',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '12 8 9 10 11',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8 9 10 11 12',
        ]) + '\n')
