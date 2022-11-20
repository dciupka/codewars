import unittest

class TestIsInteresting(unittest.TestCase):

    def test_same_digit_interesting(self):
        number =1111
        awesome_phrases = [1111]
        result = is_interesting(number,awesome_phrases)
        self.assertEqual(res,2)