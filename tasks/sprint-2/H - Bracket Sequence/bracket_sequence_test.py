import unittest
import io
from unittest.mock import patch

from bracket_sequence import parse_sequence, main


class BracketSequenceTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '{[()]}',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '()',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'True',
        ]) + '\n')

    def test_edge(self):
        self.assertEqual(parse_sequence(''), True)

    def test_negative(self):
        self.assertEqual(parse_sequence('}'), False)
        self.assertEqual(parse_sequence('['), False)
        self.assertEqual(parse_sequence('[([]{})[]{([])}'), False)

    def test_positive(self):
        self.assertEqual(parse_sequence('[]'), True)
        self.assertEqual(parse_sequence('[([]{})][]{([])}'), True)
