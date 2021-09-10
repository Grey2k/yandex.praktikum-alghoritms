import unittest
import io
from unittest.mock import patch

from gold_rush import main


class GoldRushTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        '3',
        '8 1',
        '2 10',
        '4 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '36',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10000',
        '1',
        '4 20',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '80',
        ]) + '\n')
