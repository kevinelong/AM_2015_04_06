import unittest
import simple_math


class TestSimpleMath(unittest.TestCase):
    def setUp(self):
        self.sample_list = (1, 3, 4, 9)


    def test_add(self):
        expected = 5
        result = simple_math.add(2, 3)
        self.assertEquals(result, expected)

    def test_total(self):
        expected = 17
        result = simple_math.total(self.sample_list)
        self.assertEquals(result, expected)

    def test_total_length(self):
        expected = 4
        result = len(self.sample_list)
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()