import unittest
import io
from unittest.mock import patch

from buying_homes import main


class BuyingHomeTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 300',
        '999 999 999',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 1000',
        '350 999 200',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')
