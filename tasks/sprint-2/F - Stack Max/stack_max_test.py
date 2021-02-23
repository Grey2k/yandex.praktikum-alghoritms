import unittest
import io
from unittest.mock import patch

from stack_max import main


class StackMaxTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        'get_max',
        'push 7',
        'pop',
        'push -2',
        'push -1',
        'pop',
        'get_max',
        'get_max'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            '-2',
            '-2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        'get_max',
        'pop',
        'pop',
        'pop',
        'push 10',
        'get_max',
        'push -9',

    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            'error',
            'error',
            'error',
            '10',
        ]) + '\n')
