import unittest
import io
from unittest.mock import patch

from strange_comparison import main


class StrangeComparisonTEst(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'mxyskaoghi',
        'qodfrgmslc',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'agg',
        'xdd',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'agg',
        'xda',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'AGG',
        'BDD',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'agg',
        'BDD',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'a',
        'b',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'a',
        'a',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'ab',
        'aa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eight(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'abc',
        'xy',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_nine(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'xy',
        'abc',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_ten(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')
