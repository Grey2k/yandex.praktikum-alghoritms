import unittest
import io
from unittest.mock import patch

from extra_letter import find_extra, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abcd',
        'abcde',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'e\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'go',
        'ogg'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'g\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'xtkpx',
        'xkctpx'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), 'c\n')

    def test_edge(self):
        self.assertEqual(find_extra('a', 'a'), None)

    def test_positive(self):
        self.assertEqual(find_extra('abcd', 'abcde'), 'e')
        self.assertEqual(find_extra('go', 'ogg'), 'g')
        self.assertEqual(find_extra('xtkpx', 'xkctpx'), 'c')
