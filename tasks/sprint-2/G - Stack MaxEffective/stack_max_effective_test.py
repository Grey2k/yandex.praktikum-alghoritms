import unittest
import io
from unittest.mock import patch

from stack_max_effective import main


class StackMaxEffectiveTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        'pop',
        'pop',
        'push 4',
        'push -5',
        'push 7',
        'pop',
        'pop',
        'get_max',
        'pop',
        'get_max',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'error',
            'error',
            '4',
            'None',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        'get_max',
        'push -6',
        'pop',
        'pop',
        'get_max',
        'push 2',
        'get_max',
        'pop',
        'push -2',
        'push -6',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'None',
            'error',
            'None',
            '2',
        ]) + '\n')
