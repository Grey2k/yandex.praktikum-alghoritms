import unittest
import io
from unittest.mock import patch

from atm_variants import main


class AtmVariantsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '3',
        '3 2 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '2',
        '2 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '1',
        '5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '1',
        '8',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '5',
        '10 6 1 3 8',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')
