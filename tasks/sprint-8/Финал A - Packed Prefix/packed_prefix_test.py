import unittest
import io
from unittest.mock import patch

from packed_prefix import main


class PackedPrefixTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '2[a]2[ab]',
        '3[a]2[r2[t]]',
        'a2[aa3[b]]',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'aaa'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'abacabaca',
        '2[abac]a',
        '3[aba]',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'aba'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        'cbcbababacccaaa',
        '2[2[cb]2[ab]]2[ab]',
        '3[2[cb]abcccc]',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'cbcbab'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '3[2[bkyb]2[eszi]1[k]1[ep]]2[w]3[3[a]]1[krr]2[lh]1[pj]',
        '3[2[bkyb]2[eszi]1[k]1[ep]]2[w]3[3[a]]1[3[i]2[t]]',
        '3[2[bkyb]2[eszi]1[k]1[ep]]2[w]3[3[a]]1[1[i]2[nbiv]1[i]]1[blrw]3[gh]2[g]3[gt]',
        '3[2[bkyb]2[eszi]1[k]1[ep]]2[w]3[3[a]]3[1[f]1[uze]]3[3[f]1[zw]]',
        '3[2[bkyb]2[eszi]1[k]1[ep]]2[w]3[3[a]]3[al]1[kywr]2[1[lhgo]]',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'bkybbkybeszieszikepbkybbkybeszieszikepbkybbkybeszieszikepwwaaaaaaaaa'
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        'vkskkkcuqaqaqauuisissxjesxjewqwqwqbbgz2[fm]1[3[tama]2[xyk]3[j]2[rp]1[af]]3[3[atp]]1[3[jzs]3[cah]2[o]3[sfmr]2[lp]3[v]]2[2[u]3[ah]]3[ydrr]',
        'vkskkkcuqaqaqauuisissxjesxjewqwqwqbbgz2[rgr]1[x]3[1[ded]]1[1[qx]2[ang]]1[wx]',
        'vkskkkcuqaqaqauuisissxjesxjewqwqwqbbgz1[3[qif]3[we]3[ljt]2[rlps]3[i]]',
        '1[vks]3[k]1[cu]1[3[qa]2[u]2[is]2[sxje]3[wq]1[bbgz]]3[1[xfob]]2[s]3[h]2[2[fz]3[qs]]1[jxrf]2[ze]',
        '1[vks]3[k]1[cu]1[3[qa]2[u]2[is]2[sxje]3[wq]1[bbgz]]3[fe]3[2[hbll]3[jvt]]2[eca]',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            'vkskkkcuqaqaqauuisissxjesxjewqwqwqbbgz'
        ]) + '\n')
