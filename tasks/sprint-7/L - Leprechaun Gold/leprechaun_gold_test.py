import unittest
import io
from unittest.mock import patch

from leprechaun_gold import main


class LeprechaunGoldTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5 15',
        '3 8 1 2 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '15'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5 19',
        '10 10 7 7 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '18'
        ]) + '\n')
