import unittest
import io
from unittest.mock import patch

from deck import Deck, main


class DeckTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '4',
        'push_front 861',
        'push_front -819',
        'pop_back',
        'pop_back',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '861',
            '-819'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '7',
        '10',
        'push_front -855',
        'push_front 720',
        'pop_back',
        'pop_back',
        'push_back 844',
        'pop_back',
        'push_back 823',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-855',
            '720',
            '844',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '6',
        'push_front -201',
        'push_back 959',
        'push_back 102',
        'push_front 20',
        'pop_front',
        'pop_back',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '20',
            '102',
        ]) + '\n')

    def test_empty_deck(self):
        d = Deck(10)

        self.assertRaises(ValueError, d.pop_back)
        self.assertRaises(ValueError, d.pop_front)

    def test_edge_cases_overflow(self):
        d = Deck()

        self.assertRaises(OverflowError, d.push_front, (True,))
        self.assertRaises(OverflowError, d.push_back, (True,))

        d2 = Deck(2)
        d2.push_front(True)
        d2.push_back(True)
        self.assertRaises(OverflowError, d2.push_front, (True,))
        self.assertRaises(OverflowError, d2.push_back, (True,))

        d3 = Deck(2)
        d3.push_back(True)
        d3.push_back(True)
        self.assertRaises(OverflowError, d3.push_front, (True,))
        self.assertRaises(OverflowError, d3.push_back, (True,))

        d4 = Deck(2)
        d4.push_front(True)
        d4.push_front(True)
        self.assertRaises(OverflowError, d4.push_front, (True,))
        self.assertRaises(OverflowError, d4.push_back, (True,))
