import unittest
import io
from unittest.mock import patch

from bfs import main


class BFSTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4 4',
        '1 2',
        '2 3',
        '3 4',
        '1 4',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3 2 4 1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 1',
        '2 1',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2',
        ]) + '\n')
