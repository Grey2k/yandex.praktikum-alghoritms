import unittest
import io
from unittest.mock import patch

from fibonacci import main


class FibonacciTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '89',
        ]) + '\n')
