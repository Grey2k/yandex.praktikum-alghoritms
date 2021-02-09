import unittest
import io
from unittest.mock import patch

from binary_system import sum_base, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '10\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1010',
        '1011'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '10101\n')

    def test_edge(self):
        self.assertEqual(sum_base("0", "0"), '0')
        self.assertEqual(sum_base("0", "1"), "1")
        self.assertEqual(sum_base("0000", "0001"), "1")

    def test_positive(self):
        self.assertEqual(sum_base("1010", "1011"), '10101')
