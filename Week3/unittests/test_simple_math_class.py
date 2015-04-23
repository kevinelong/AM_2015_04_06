__author__ = 'kevin'
import unittest
import simple_math_class


class TestSimpleMath(unittest.TestCase):
    sample_list = (1, 3, 4, 9)

    def setUp(self):
        self.sm = simple_math_class.SimpleMath()

    def test_add(self):
        expected = 5
        result = self.sm.add(2, 3)
        self.assertEquals(result, expected)

    def test_total(self):
        expected = 17
        result = self.sm.total(self.sample_list)
        self.assertEquals(result, expected)

    def test_total_length(self):
        expected = 4
        result = len(self.sample_list)
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()