import unittest
from L8.popmihaylov_L8_T1 import bisection, func1, func2, NumbersShouldNotHaveSameSign, AndBshouldBeNumbers


class TestBisection(unittest.TestCase):

    def test_func1(self):
        message = "Did not pass for funct1"
        self.assertAlmostEqual(float(bisection(0, 3, func1)), 1.1543, places=4, msg=message)

    def test_func2(self):
        message = "Did not pass for funct2"
        self.assertAlmostEqual(float(bisection(0, 3, func2)), 1.6816, places=4, msg=message)

    def test_AndBshouldBeNumbers_a(self):
        with self.assertRaises(AndBshouldBeNumbers):
            bisection("hi", 3, func2)

    def test_AndBshouldBeNumbers_b(self):
        with self.assertRaises(AndBshouldBeNumbers):
            bisection(3, "Hi", func2)

    def test_AndBshouldBeNumbers_both(self):
        with self.assertRaises(AndBshouldBeNumbers):
            bisection("hi", "Hi", func2)

    def test_positive_NumbersShouldNotHaveSameSign(self):
        with self.assertRaises(NumbersShouldNotHaveSameSign):
            bisection(3, 3, func2)

    def test_negative_NumbersShouldNotHaveSameSign(self):
        with self.assertRaises(NumbersShouldNotHaveSameSign):
            bisection(-3, -3, func2)


if __name__ == '__main__':
    unittest.main()
