import unittest
import io
from unittest.mock import patch

from polinomial_hash import main


class PolinomialHashTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '123',
        '100003',
        'a',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '97',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '123',
        '100003',
        'hash',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '6080',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '123',
        '100003',
        'HaSH',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '56156',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '13',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        '13',
        'H',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '7',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1000',
        '1000000000',
        'loremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitametloremipsumdolorsitamet',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '109101116',
        ]) + '\n')
