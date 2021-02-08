import unittest
import io
from unittest.mock import patch

from remote_work import to_base, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '101\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '14'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1110\n')

    def test_edge(self):
        self.assertEqual(to_base(0), '0')
        self.assertEqual(to_base(1), '1')
        self.assertEqual(to_base(2), '10')

    def test_positive(self):
        self.assertEqual(to_base(5), '101')
        self.assertEqual(to_base(14), '1110')
