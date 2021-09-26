import unittest
import io
from unittest.mock import patch

from inserting_strings import main


class InsertingStringsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'abacaba',
        '3',
        'queue 2',
        'deque 0',
        'stack 7',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'dequeabqueueacabastack',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'kukareku',
        '2',
        'p 1',
        'q 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'kpuqkareku',
        ]) + '\n')
