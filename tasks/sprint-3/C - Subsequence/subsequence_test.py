import unittest
import io
from unittest.mock import patch

from subsequence import is_subsequence, main


class SubsequenceTest(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        'abc',
        'ahbgdcu',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'abcp',
        'ahpc',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'False',
        ]) + '\n')

    def test_edge(self):
        self.assertEqual(is_subsequence('a', 'a'), True)
        self.assertEqual(is_subsequence('', ''), True)
