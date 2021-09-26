import unittest
import io
from unittest.mock import patch

from common_prefix import main


class CommonPrefixTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'abacaba',
        'abudabi',
        'abcdefg',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'tutu',
        'kukuku',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'qwe',
        'qwerty',
        'qwerpy',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')
