import unittest
import io
from unittest.mock import patch

from longest_substring import longest_substring, main


class LongestSubstringTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abcabcbb',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'bbbb',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    def test_positive(self):
        self.assertEqual(
            longest_substring('abccccabcdefggggergddkjjkkg'), 7)
