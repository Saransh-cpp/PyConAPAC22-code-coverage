import unittest
import threading
from calc_thread import add, subtract, divide, multiply


class TestCalc(unittest.TestCase):
    def test_add(self):
        ret = {}
        t = threading.Thread(target=add, args=(2, 3, ret))
        t.start()
        t.join()

        self.assertEqual(5, ret["result"])

    def test_subtract(self):
        ret = {}
        t = threading.Thread(target=subtract, args=(ret, 2, 3))
        t.start()
        t.join()

        self.assertEqual(-1, ret["result"])

    def test_multiply(self):
        ret = {}
        t = threading.Thread(target=multiply, args=(ret, 2, 3))
        t.start()
        t.join()

        self.assertEqual(6, ret["result"])

    def test_divide(self):
        ret = {}
        t = threading.Thread(target=divide, args=(ret, 2, 3))
        t.start()
        t.join()

        self.assertEqual(2 / 3, ret["result"])
        self.assertRaises(ValueError, divide, {}, 2, 0)


if __name__ == "__main__":
    unittest.main()
