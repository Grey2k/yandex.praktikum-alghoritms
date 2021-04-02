import unittest
import io
from unittest.mock import patch

from nearest_station import main


class NearestStationTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '-1 0',
        '1 0',
        '2 5',
        '3',
        '10 0',
        '20 0',
        '22 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '-1 0',
        '1 0',
        '0 5',
        '3',
        '10 0',
        '20 0',
        '20 5',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
        ]) + '\n')
