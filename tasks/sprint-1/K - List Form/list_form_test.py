import unittest
import io
from unittest.mock import patch

from list_form import from_list_form, to_list_form, main


class LongestWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '1 2 0 0',
        '34',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1 2 3 4\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '9 5',
        '17'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1 1 2\n')

    def test_edge(self):
        self.assertEqual(from_list_form(1, '1'), 1)

    def test_positive(self):
        self.assertEqual(from_list_form(4, '1 2 0 0'), 1200)
        self.assertEqual(to_list_form(1200), '1 2 0 0')
