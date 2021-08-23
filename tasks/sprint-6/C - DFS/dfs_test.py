import unittest
import io
from unittest.mock import patch

from dfs import main


class DFSTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4 4',
        '3 2',
        '4 3',
        '1 4',
        '1 2',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3 2 1 4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 1',
        '1 2',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4 2',
        '1 2',
        '2 3',
        '4'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4 2',
        '1 2',
        '2 3',
        '2'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2 1 3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6 7',
        '3 2',
        '5 4',
        '3 1',
        '1 4',
        '1 6',
        '1 2',
        '1 5',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2 3 4 5 6',
        ]) + '\n')
