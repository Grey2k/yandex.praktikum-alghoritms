import unittest
import io
from unittest.mock import patch

from atm_min import main


class AtmMinTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '130',
        '4',
        '10 3 40 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '100',
        '2',
        '7 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '16',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '14',
        '2',
        '10 7',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '15',
        '2',
        '10 7',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6615',
        '8',
        '4280 1540 9434 4041 5952 3337 3872 6615',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')
