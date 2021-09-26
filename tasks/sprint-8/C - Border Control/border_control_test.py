import unittest
import io
from unittest.mock import patch

from border_control import main


class BorderControlTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abcdefg',
        'abdefg',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'OK',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'helo',
        'hello',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'OK',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'dog',
        'fog',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'OK',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'mama',
        'papa',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'FAIL',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'm',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'OK',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'mama',
        'mam',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'OK',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'mapa',
        'mam',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'FAIL',
        ]) + '\n')
