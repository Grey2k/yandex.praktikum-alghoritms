import unittest
import io
from unittest.mock import patch

from longest_word import longest_word, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '17',
        ' sybtbv jxqwbu cj',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'sybtbv\n6\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '19',
        'i love segment tree'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'segment\n7\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '21',
        'frog jumps from river'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'jumps\n5\n')

    def test_empty(self):
        self.assertEqual(longest_word(0, ""), "")

    def test_non_ascii(self):
        self.assertEqual(longest_word(8, "   3    "), "")

    def test_one(self):
        self.assertEqual(longest_word(8, "   b    "), "b")

    def test_no_space(self):
        self.assertEqual(longest_word(25, "frog jumps from riverdale"), "riverdale")

    def test_cases(self):
        self.assertEqual(longest_word(21, "frog jumps from river"), "jumps")
