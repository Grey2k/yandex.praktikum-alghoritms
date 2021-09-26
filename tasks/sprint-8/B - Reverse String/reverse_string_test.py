import unittest
import io
from unittest.mock import patch

from reverse_string import main


class ReverseStringTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'one two three'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'three two one',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'hello',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'hello',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'may the force be with you',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'you with be force the may',
        ]) + '\n')
