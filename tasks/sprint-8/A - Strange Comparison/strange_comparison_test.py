import unittest
import io
from unittest.mock import patch

from strange_comparison import main


class StrangeComparisonTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'mxyskaoghi',
        'qodfrgmslc',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'agg',
        'xdd',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'agg',
        'xda',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'a',
        'aa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'aba',
        'xxx',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')
