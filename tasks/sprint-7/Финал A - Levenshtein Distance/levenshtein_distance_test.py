import unittest
import io
from unittest.mock import patch

from levenshtein_distance import main


class LevenshteinDistanceTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abacaba',
        'abaabc',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'innokentiy',
        'innnokkentia',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'r',
        'x',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'dxqrpmratn',
        'jdpmykgmaitn',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'vfffsjypne',
        'bimgzrrelk',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '10'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'xyz',
        'xyz',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge2(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0'
        ]) + '\n')
