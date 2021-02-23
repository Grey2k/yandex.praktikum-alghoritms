import unittest
import io
from unittest.mock import patch

from queue_sized import main


class QueueSizedTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '2',
        'peek',
        'push 5',
        'push 2',
        'peek',
        'size',
        'size',
        'push 1',
        'size',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            '5',
            '2',
            '2',
            'error',
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        '1',
        'push 1',
        'size',
        'push 3',
        'size',
        'push 1',
        'pop',
        'push 1',
        'pop',
        'push 3',
        'push 3'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
            'error',
            '1',
            'error',
            '1',
            '1',
            'error',
        ]) + '\n')
