import unittest
import io
from unittest.mock import patch

from factorization import factorization, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '2 2 2\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '13'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '13\n')

    def test_edge(self):
        self.assertEqual(factorization(2), [2])

    def test_positive(self):
        self.assertEqual(factorization(8), [2, 2, 2])
        self.assertEqual(factorization(13), [13])
