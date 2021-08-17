import unittest
import io
from unittest.mock import patch

from adjacency_list import main


class AdjacencyListTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5 3',
        '1 3',
        '2 3',
        '5 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 3',
            '1 3',
            '0 ',
            '0 ',
            '1 2',
        ]) + '\n')
