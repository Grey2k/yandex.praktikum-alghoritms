import unittest
import io
from unittest.mock import patch

from effective_quick_sort import main


class SearchInBrokenArrayTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 4 100',
        'gena 6 1000',
        'gosha 2 90',
        'rita 2 90',
        'timofey 4 80',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'gena',
            'timofey',
            'alla',
            'gosha',
            'rita',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 0 0',
        'gena 0 0',
        'gosha 0 0',
        'rita 0 0',
        'timofey 0 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena',
            'gosha',
            'rita',
            'timofey',
        ]) + '\n')
