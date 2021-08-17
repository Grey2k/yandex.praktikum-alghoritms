import unittest
import io
from unittest.mock import patch

from adjacency_matrix import main


class AdjacencyMatrixTest(unittest.TestCase):
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
            '0 0 1 0 0',
            '0 0 1 0 0',
            '0 0 0 0 0',
            '0 0 0 0 0',
            '0 1 0 0 0',
        ]) + '\n')
