import unittest
import io
from unittest.mock import patch

from global_replace import main


class GlobalReplaceTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        'pingpong',
        'ng',
        'mpi',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'pimpipompi',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        'aaa',
        'a',
        'ab',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'ababab',
        ]) + '\n')
