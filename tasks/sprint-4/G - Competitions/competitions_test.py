import unittest
import io
from unittest.mock import patch

from competitions import main


class CompetitionsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '0 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one_second(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '0 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        '0 0 1 0 1 1 1 0 0 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '1 1 1 1 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '12',
        '1 1 1 1 1 1 0 0 0 0 0 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '12',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0',
        ''
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        '1 1 1 1 1 1 1 1 1 1'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eight(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
