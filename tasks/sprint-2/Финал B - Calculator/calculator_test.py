import unittest
import io
from unittest.mock import patch

from calculator import main


class CalculatorTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '2 1 + 3 *',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '9\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7 2 + 4 * 2 +',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '38\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7 2 / 4 + 2 +',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '9\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2 1 2 / *',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '42 42 + 84 -',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0 0 * 0 +',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')
