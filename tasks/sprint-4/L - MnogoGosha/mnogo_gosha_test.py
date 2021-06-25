import unittest
import io
from unittest.mock import patch

from mnogo_gosha import main


class MnogoGoshaTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '10 2',
        'gggggooooogggggoooooogggggssshaa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 5',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 4',
        'allallallallalla',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0 4',
        'allallallallalla',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
