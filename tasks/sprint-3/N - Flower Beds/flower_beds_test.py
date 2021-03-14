import unittest
import io
from unittest.mock import patch

from flower_beds import main


class GoldenMeanTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '7 8',
        '7 8',
        '2 3',
        '6 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2 3',
            '6 10',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '2 3',
        '5 6',
        '3 4',
        '3 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2 4',
            '5 6',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 3',
        '3 5',
        '4 6',
        '5 6',
        '2 4',
        '7 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 6',
            '7 10',
        ]) + '\n')

    def test_edge(self):
        pass
