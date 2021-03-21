import unittest
import io
from unittest.mock import patch

from prefix_hashes import main


class PrefixHashTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '1000',
        '1000009',
        'abcdefgh',
        '7',
        '1 1',
        '1 5',
        '2 3',
        '3 4',
        '4 4',
        '1 8',
        '5 8',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '97',
            '225076',
            '98099',
            '99100',
            '100',
            '436420',
            '193195',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '100',
        '10',
        'a',
        '1',
        '1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '7',
        ]) + '\n')
