import unittest
import io
from unittest.mock import patch

from pyramid_sort import main


class PyramidSortTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 4 100',
        'gena 6 1000',
        'gosha 2 90',
        'rita 2 90',
        'timofey 4 80',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'gena',
            'timofey',
            'alla',
            'gosha',
            'rita',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 0 0',
        'gena 0 0',
        'rita 0 0',
        'timofey 0 0',
        'gosha 0 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena',
            'gosha',
            'rita',
            'timofey',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 1 0',
        'gena 0 0',
        'gosha 1 100',
        'rita 0 0',
        'timofey 0 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gosha',
            'gena',
            'rita',
            'timofey',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 1 0',
        'gena 0 0',
        'gosha 1 100',
        'rita 2 0',
        'timofey 2 100',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'rita',
            'timofey',
            'alla',
            'gosha',
            'gena',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '1',
        'alla 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'alla 1 0',
        'gena 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_six(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'gena 1 0',
        'alla 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'gena 2 10',
        'alla 2 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eight(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'gena 1 10',
        'alla 2 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_nine(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 1 10',
        'gena 1 10',
        'gosha 1 10',
        'rita 2 100',
        'timofey 2 100',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_ten(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'rita',
            'timofey',
            'alla',
            'gena',
            'gosha',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'alla 1 0',
        'gena 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eleven(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'alla 2 0',
        'gena 2 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_twelve(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '2',
        'alla 2 0',
        'gena 1 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_thirteen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'alla 1 0',
        'gosha 1 0',
        'gena 1 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_fourteen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena',
            'gosha'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'alla 2 0',
        'gosha 2 0',
        'gena 2 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_fifteen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gosha',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'alla 2 0',
        'gosha 1 10',
        'gena 1 10',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_sixteen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'alla',
            'gena',
            'gosha'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'alla 1 100',
        'gena 1 1000',
        'gosha 1 90',
        'rita 1 90',
        'timofey 10 80',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_seventeen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'timofey',
            'gosha',
            'rita',
            'alla',
            'gena'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '13',
        'tufhdbi 76 58',
        'rqyoazgbmv 59 78',
        'qvgtrlkmyrm 35 27',
        'tgcytmfpj 70 27',
        'xvf 84 19',
        'jzpnpgpcqbsmczrgvsu 30 3',
        'evjphqnevjqakze 92 15',
        'wwzwv 87 8',
        'tfpiqpwmkkduhcupp 1 82',
        'tzamkyqadmybky 5 81',
        'amotrxgba 0 6',
        'easfsifbzkfezn 100 28',
        'kivdiy 70 47',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_eighteen(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'easfsifbzkfezn',
            'evjphqnevjqakze',
            'wwzwv',
            'xvf',
            'tufhdbi',
            'tgcytmfpj',
            'kivdiy',
            'rqyoazgbmv',
            'qvgtrlkmyrm',
            'jzpnpgpcqbsmczrgvsu',
            'tzamkyqadmybky',
            'tfpiqpwmkkduhcupp',
            'amotrxgba',
        ]) + '\n')

    def test_comparator(self):
        self.assertEqual((-1, 0, 'alla') > (-2, 0, 'gosha'), True)
        self.assertEqual((-1, 0, 'alla') < (-1, 0, 'gosha'), True)
        self.assertEqual((-1, 10, 'alla') > (-1, 0, 'gosha'), True)
