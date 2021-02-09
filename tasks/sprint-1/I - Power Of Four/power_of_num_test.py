import unittest
import io
from unittest.mock import patch

from power_of_num import is_power, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '15',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'False\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '16'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'True\n')

    def test_edge(self):
        self.assertEqual(is_power(4), True)
        self.assertEqual(is_power(0), False)
        self.assertEqual(is_power(1), True)

    def test_positive(self):
        self.assertEqual(is_power(16), True)

    def test_negative(self):
        self.assertEqual(is_power(15), False)
