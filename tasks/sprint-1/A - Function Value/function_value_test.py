import unittest
import io
from unittest.mock import patch

from function_value import function_value, main


class FunctionValueTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['1 2 3 4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, stdout, _):
        main()
        self.assertEqual(stdout.getvalue(), '14\n')

    def test_simple(self):
        self.assertEqual(function_value(1, 2, 3, 4), 14)

    def test_error(self):
        self.assertRaises(TypeError, function_value, ("1", "2", "3", "4"))
