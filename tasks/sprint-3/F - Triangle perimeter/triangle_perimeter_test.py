import unittest
import io
from unittest.mock import patch

from triangle_perimeter import main


class BuyingHomeTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '6 3 3 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '5 3 7 2 8 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '20',
        ]) + '\n')
