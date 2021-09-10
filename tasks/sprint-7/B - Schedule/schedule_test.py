import unittest
import io
from unittest.mock import patch

from schedule import main


class ScheduleTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '9 10',
        '9.3 10.3',
        '10 11',
        '10.3 11.3',
        '11 12',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '9 10',
            '10 11',
            '11 12',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '9 10',
        '11 12.25',
        '12.15 13.3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
            '9 10',
            '11 12.25',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '19 19',
        '7 14',
        '12 14',
        '8 22',
        '22 23',
        '5 21',
        '9 23',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '7 14',
            '19 19',
            '22 23',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '19 19',
        '7 14',
        '12 14',
        '8 22',
        '19 19',
        '22 23',
        '5 21',
        '9 23',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
            '7 14',
            '19 19',
            '19 19',
            '22 23',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '19 19',
        '12 14',
        '7 14',
        '8 22',
        '19 19',
        '22 23',
        '5 21',
        '9 23',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge2(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
            '7 14',
            '19 19',
            '19 19',
            '22 23',
        ]) + '\n')
