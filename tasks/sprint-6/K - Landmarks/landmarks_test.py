import unittest
import io
from unittest.mock import patch

from landmarks import main


class LandmarksTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4 4',
        '1 2 1',
        '2 3 3',
        '3 4 5',
        '1 4 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 4 2',
            '1 0 3 3',
            '4 3 0 5',
            '2 3 5 0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 2',
        '1 2 1',
        '1 2 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 -1',
            '1 0 -1',
            '-1 -1 0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 -1',
            '-1 0',
        ]) + '\n')
