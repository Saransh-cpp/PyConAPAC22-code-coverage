import unittest
from calc import add, subtract, divide, multiply


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))
        self.assertEqual(0, add(2, -2))
        self.assertEqual(-2, add(-5, 3))
        self.assertEqual(2, add(5, -3))

    def test_subtract(self):
        self.assertEqual(-1, subtract(2, 3))
        self.assertEqual(4, subtract(2, -2))
        self.assertEqual(-8, subtract(-5, 3))
        self.assertEqual(2, subtract(5, 3))

    def test_multiply(self):
        self.assertEqual(6, multiply(2, 3))
        self.assertEqual(-4, multiply(2, -2))
        self.assertEqual(-15, multiply(-5, 3))
        self.assertEqual(15, multiply(-5, -3))

    def test_divide(self):
        self.assertEqual(2 / 3, divide(2, 3))
        self.assertEqual(-1, divide(2, -2))
        self.assertEqual(-5 / 3, divide(-5, 3))
        self.assertEqual(5 / 3, divide(-5, -3))
        self.assertRaises(ValueError, divide, 2, 0)


if __name__ == "__main__":
    unittest.main()
