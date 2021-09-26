import unittest
import io
from unittest.mock import patch

from prefix_function import main


class SearchWithShiftTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abracadabra',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 0 0 1 0 1 0 1 2 3 4',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'xxzzxxz',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 0 0 1 2 3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'aaaaa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 2 3 4',
        ]) + '\n')
