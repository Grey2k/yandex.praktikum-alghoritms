import unittest
import io
from unittest.mock import patch

from grouped_anagrams import main


class LongestSubstringTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        'tan eat tea ate nat bat',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 4',
            '1 2 3',
            '5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        'bbbb',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
