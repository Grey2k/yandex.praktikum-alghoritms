import unittest
import io
from unittest.mock import patch

from cheat_sheet import main


class CheatSheetTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'examiwillpasstheexam',
        '5',
        'will',
        'pass',
        'the',
        'exam',
        'i',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'abacaba',
        '2',
        'abac',
        'caba',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'abacaba',
        '3',
        'abac',
        'caba',
        'aba',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES'
        ]) + '\n')
