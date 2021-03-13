import unittest
import io
from unittest.mock import patch

from cookies import match_cookies, main


class CookiesTest(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1 2',
        '3',
        '2 1 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '2 1 3',
        '2',
        '1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    def test_edge(self):
        self.assertEqual(match_cookies([1], [1]), 1)
        self.assertEqual(match_cookies([0], [1]), 1)
        self.assertEqual(match_cookies([1], [0]), 0)
