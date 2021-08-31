import unittest
import io
from unittest.mock import patch

from rail_roads import main


class RailRoadsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'RB',
        'R',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        'BBB',
        'RB',
        'B',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'YES',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'RRRB',
        'BRR',
        'BR',
        'R',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'NO',
        ]) + '\n')
