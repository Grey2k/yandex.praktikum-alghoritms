import unittest
import io
from unittest.mock import patch

from queue_list import main


class QueueListTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        'put -34',
        'put -23',
        'get',
        'size',
        'get',
        'size',
        'get',
        'get',
        'put 80',
        'size',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-34',
            '1',
            '-23',
            '0',
            'error',
            'error',
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        'put -66',
        'put 98',
        'size',
        'size',
        'get',
        'get',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
            '2',
            '-66',
            '98',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '9',
        'get',
        'size',
        'put 74',
        'get',
        'size',
        'put 90',
        'size',
        'size',
        'size',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'error',
            '0',
            '74',
            '0',
            '1',
            '1',
            '1',
        ]) + '\n')
