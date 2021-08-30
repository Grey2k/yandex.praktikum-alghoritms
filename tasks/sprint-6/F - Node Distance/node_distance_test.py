import unittest
import io
from unittest.mock import patch

from node_distance import main


class NodeDistanceTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5 5',
        '2 4',
        '3 5',
        '2 1',
        '2 3',
        '4 5',
        '1 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4 3',
        '2 3',
        '4 3',
        '2 4',
        '1 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 1',
        '2 1',
        '1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
