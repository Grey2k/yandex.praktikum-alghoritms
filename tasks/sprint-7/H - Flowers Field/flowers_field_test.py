import unittest
import io
from unittest.mock import patch

from flowers_field import main


class FlowersFieldTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '2 3',
        '101',
        '110',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3 3',
        '100',
        '110',
        '001',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')
