import unittest
import io
from unittest.mock import patch

from odd_and_even import odd_and_even, main


class OddAndEvenTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['1 2 -3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout, _):
        main()
        self.assertEqual(stdout.getvalue(), 'FAIL\n')

    def test_negative(self):
        self.assertEqual(odd_and_even(1, 2, -3), False)

    def test_positive(self):
        self.assertEqual(odd_and_even(7, 11, 7), True)
