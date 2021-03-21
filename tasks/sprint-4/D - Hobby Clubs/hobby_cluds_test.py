import unittest
import io
from unittest.mock import patch

from hobby_clubs import main


class HobbyClubsTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        'вышивание крестиком',
        'рисование мелками на парте',
        'настольный керлинг',
        'настольный керлинг',
        'кухня африканского племени ужасмай',
        'тяжелая атлетика',
        'таракановедение',
        'таракановедение',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'вышивание крестиком',
            'рисование мелками на парте',
            'настольный керлинг',
            'кухня африканского племени ужасмай',
            'тяжелая атлетика',
            'таракановедение',
        ]) + '\n')
