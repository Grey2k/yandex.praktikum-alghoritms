import unittest
import io
from unittest.mock import patch

from hash_table import HashTable, main


class SearchInBrokenArrayTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        'get 1',
        'put 1 10',
        'put 2 4',
        'get 1',
        'get 2',
        'delete 2',
        'get 2',
        'put 1 5',
        'get 1',
        'delete 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            '10',
            '4',
            '4',
            'None',
            '5',
            'None',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        'get 9',
        'delete 9',
        'put 9 1',
        'get 9',
        'put 9 2',
        'get 9',
        'put 9 3',
        'get 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            'None',
            '1',
            '2',
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        'get 9',
        'get 9',
        'put 9 1',
        'get 9',
        'delete 9',
        'get 9',
        'put 9 3',
        'get 9',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            'None',
            '1',
            '1',
            'None',
            '3',
        ]) + '\n')

    def test_edge(self):
        hash_table = HashTable()
        hash_table.put(0, 12)
        self.assertEqual(hash_table.get(0), 12)
        hash_table.put(10 ** 5, 13)
        self.assertEqual(hash_table.get(10 ** 5), 13)
