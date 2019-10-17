import unittest
from happynumber import happy, sum_of_squares


class Test_HappyNumber(unittest.TestCase):

    def test_happy_number_um_is_happy(self):
        self.assertEqual(happy(1), True)
 
    def test_happy_number_four_is_not_happy(self):
        self.assertEqual(happy(4), False)

    def test_happy_number_ten_is_happy(self):
        self.assertEqual(happy(10), True)

    def test_happy_number_is_postive(self):
        self.assertEqual(happy(-1), True)

if __name__ == '__main__':
    unittest.main()
