import unittest
import io
from unittest.mock import patch

from expensive_network import main


class ExpensiveNetworkTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4 4',
        '1 2 5',
        '1 3 6',
        '2 4 8',
        '3 4 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '19',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 3',
        '1 2 1',
        '1 2 2',
        '2 3 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Oops! I did it again',
        ]) + '\n')
