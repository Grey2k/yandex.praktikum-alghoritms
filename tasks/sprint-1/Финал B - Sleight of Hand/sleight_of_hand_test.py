import unittest
import io
from unittest.mock import patch

from sleight_of_hand import score_hands, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '1231',
        '2..2',
        '2..2',
        '2..2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '2\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '1111',
        '9999',
        '1111',
        '9911',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '1111',
        '1111',
        '1111',
        '1111',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')

    def test_edge(self):
        self.assertEqual(score_hands(4, [
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', '1'],
        ]), 0)

        self.assertEqual(score_hands(4, [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]), 0)
