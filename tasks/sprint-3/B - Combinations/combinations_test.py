import unittest
import io
from unittest.mock import patch
from collections import deque

from combinations import generator, main


class CombinationsTest(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '23',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'ad ae af bd be bf cd ce cf',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '92',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'wa wb wc xa xb xc ya yb yc za zb zc',
        ]) + '\n')

    def test_edge(self):
        result = []
        generator(deque('2'), result)
        self.assertEqual(result, ['a', 'b', 'c'])
