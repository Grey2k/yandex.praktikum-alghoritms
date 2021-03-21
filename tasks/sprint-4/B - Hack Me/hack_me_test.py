import unittest

from hack_me import polinomial_hash


class PolinomialHashTest(unittest.TestCase):
    def test_comparator(self):
        a = 1000
        m = 123_987_123
        self.assertEqual(
            polinomial_hash('ezhgeljkablzwnvuwqvp', a, m) == polinomial_hash('gbpdcvkumyfxillgnqrv', a, m),
            True
        )

        self.assertEqual(
            polinomial_hash('oyfoiKjiia', a, m) == polinomial_hash('yFuBkoegIa', a, m),
            True
        )

        self.assertEqual(
            polinomial_hash('eduotucmeu', a, m) == polinomial_hash('xftrmxxchf', a, m),
            True
        )
