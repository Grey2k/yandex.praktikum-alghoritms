import unittest
import io
from unittest.mock import patch

from jumps import main


class JumpsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '6 3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '13',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7 7',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '32',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '79 34',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '470472762',
        ]) + '\n')
