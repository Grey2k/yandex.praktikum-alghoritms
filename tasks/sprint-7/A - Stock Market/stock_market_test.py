import unittest
import io
from unittest.mock import patch

from stock_market import main


class StockMarketTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '7 1 5 3 6 4'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '7',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 3 4 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 12 12 16 1 8',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '22',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '10 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge2(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge3(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '9',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge4(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '33',
        '1 29 22 65 82 83 5 10 22 76 93 29 97 26 81 62 5 36 25 41 6 65 1 10 41 91 78 13 85 43 93 10 36',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '644',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '27',
        '61 65 9 97 80 75 63 65 71 37 79 16 92 98 33 75 6 92 17 75 20 27 63 48 4 31 95',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '544',
        ]) + '\n')
