import unittest
import io
from unittest.mock import patch

from weather_chaos import chaos_days, main


class WeatherChaosTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '-1 -10 -8 0 2 0 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '3\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        '1'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '1 3'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 2 5 4 274'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_big(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '1\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        '274 275'
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_big2(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), '0\n')

    def test_edge(self):
        self.assertEqual(chaos_days(2, [1, 3]), 1)
        self.assertEqual(chaos_days(5, [1, 2, 5, 4, 8, 10]), 2)
        self.assertEqual(chaos_days(5, [1, 2, 5, 4, 8]), 2)
        self.assertEqual(chaos_days(2, [1, 2]), 1)
        self.assertEqual(chaos_days(2, [2, 1]), 1)

    def test_positive(self):
        self.assertEqual(chaos_days(7, [-1, -10, -8, 0, 2, 0, 5]), 3)
        self.assertEqual(chaos_days(5, [1, 2, 5, 4, 8]), 2)
        self.assertEqual(chaos_days(4, [1, 2, 5, 4]), 1)
