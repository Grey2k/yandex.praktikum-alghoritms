import unittest
import io
from unittest.mock import patch

from fibonacci_recursive import main


class FibonacciRecursiveTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')
