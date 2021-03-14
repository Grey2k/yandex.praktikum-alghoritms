import unittest
import io
from unittest.mock import patch

from golden_mean import main


class GoldenMeanTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1',
        '1 3',
        '2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '2',
        '1 2',
        '3 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2.5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '10',
        '0 0 0 1 3 3 5 10',
        '4 4 5 7 7 7 8 9 9 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '5',
        ]) + '\n')

    def test_edge(self):
        pass
