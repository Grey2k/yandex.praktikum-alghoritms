import unittest
import io
from unittest.mock import patch

from frequent_word import main


class FrequentWordTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'caba',
        'aba',
        'caba',
        'abac',
        'aba',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'aba',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'b',
        'bc',
        'bcd',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'b',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '10',
        'ciwlaxtnhhrnenw',
        'ciwnvsuni',
        'ciwaxeujmsmvpojqjkxk',
        'ciwnvsuni',
        'ciwnvsuni',
        'ciwuxlkecnofovq',
        'ciwuxlkecnofovq',
        'ciwodramivid',
        'ciwlaxtnhhrnenw',
        'ciwnvsuni',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'ciwnvsuni',
        ]) + '\n')
