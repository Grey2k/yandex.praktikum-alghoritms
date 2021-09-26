import unittest
import io
from unittest.mock import patch

from search_with_shift import main


class SearchWithShiftTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '9',
        '3 9 1 2 5 10 9 1 7',
        '2',
        '4 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 8',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 4 5',
        '3',
        '10 11 12',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2 3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 4 5',
        '6',
        '10 11 12 13 14 15',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 4 5',
        '2',
        '15 20',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge2(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '',
        ]) + '\n')
