import unittest
import io
from unittest.mock import patch

from palindrome import palindrome, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'A man, a plan, a canal: Panama',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'True\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'zo'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'False\n')

    def test_edge(self):
        self.assertEqual(palindrome(""), True)
        self.assertEqual(palindrome("a"), True)
        self.assertEqual(palindrome("A"), True)
        self.assertEqual(palindrome("3"), True)

    def test_positive(self):
        self.assertEqual(palindrome("A man, a plan, a canal: Panama"), True)
