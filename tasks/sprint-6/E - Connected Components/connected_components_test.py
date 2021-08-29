import unittest
import io
from unittest.mock import patch

from connected_components import main


class ConnectedComponentsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '6 3',
        '1 2',
        '6 5',
        '2 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '1 2 3',
            '4',
            '5 6',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
            '1',
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4 3',
        '2 3',
        '2 1',
        '4 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
            '1 2 3 4',
        ]) + '\n')
