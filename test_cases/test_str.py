import unittest
import string_incrementor

class TestString(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(string_incrementor.increment_string("foobar0099"), "foobar0100")
        self.assertEqual(string_incrementor.increment_string("foobar001"), "foobar002")
        self.assertEqual(string_incrementor.increment_string("foobar"), "foobar1")
        self.assertEqual(string_incrementor.increment_string("foobar1"), "foobar2")
