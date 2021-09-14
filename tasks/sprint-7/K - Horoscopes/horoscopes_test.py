import unittest
import io
from unittest.mock import patch

from horoscopes import main


class HoroscopesTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '4 9 2 4 6',
        '7',
        '9 4 0 0 2 8 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '1 3 4',
            '2 5 7',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '1 1 1 1',
        '2',
        '2 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '1 2 1 9 1 2 1 9',
        '5',
        '9 9 1 9 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0'
        ]) + '\n')
