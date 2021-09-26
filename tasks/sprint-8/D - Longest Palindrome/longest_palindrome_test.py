import unittest
import io
from unittest.mock import patch

from longest_palindrome import main


class LongestPalindromeTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'aaaabb'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'aabbaa',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'pabcd',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'a',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'aaabbb'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'ababa',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'bb'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'bb',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'a'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'a',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        ''
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '',
        ]) + '\n')
