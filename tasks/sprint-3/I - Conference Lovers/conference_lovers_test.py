import unittest
import io
from unittest.mock import patch

from conference_lovers import main


class ConferenceLoverTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '1 2 3 1 2 3 4',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2 3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 1 1 2 2 3',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')
