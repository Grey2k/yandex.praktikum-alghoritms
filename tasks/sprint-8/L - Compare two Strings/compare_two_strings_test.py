import unittest
import io
from unittest.mock import patch

from compare_two_strings import main


class CompareTwoStringsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'gggggbbb',
        'bbef'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'z',
        'aaaaaaa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'ccccz',
        'aaaaaz'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
