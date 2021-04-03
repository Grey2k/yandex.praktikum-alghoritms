import unittest
import io
from unittest.mock import patch

from search_engine import main


class SearchEngineTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'i love coffee',
        'coffee with milk and sugar',
        'free tea for everyone',
        '3',
        'i like black coffee without milk',
        'everyone loves new year',
        'mary likes black coffee without milk',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2',
            '3',
            '2 1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        'buy flat in moscow',
        'rent flat in moscow',
        'sell flat in moscow',
        'want flat in moscow like crazy',
        'clean flat in moscow on weekends',
        'renovate flat in moscow',
        '1',
        'flat in moscow for crazy weekends',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4 5 1 2 3',
        ]) + '\n')
