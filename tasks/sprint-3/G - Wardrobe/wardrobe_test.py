import unittest
import io
from unittest.mock import patch

from wardrobe import main


class WardrobeTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '0 2 1 2 0 0 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 0 0 1 1 2 2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '2 1 2 0 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 1 2 2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '2 1 1 2 0 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0 1 1 2 2 2',
        ]) + '\n')
