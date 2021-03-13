import unittest
import io
from unittest.mock import patch

from bracket_generator import generator, main


class BracketGeneratorTest(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '(())',
            '()()',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()',
        ]) + '\n')

    def test_edge(self):
        result = []
        generator(1, result)
        self.assertEqual(result, ['()'])

        result = []
        generator(0, result)
        self.assertEqual(result, [''])

    def test_positive(self):
        result = []
        generator(2, result)
        self.assertEqual(result, [
            '(())',
            '()()',
        ])
