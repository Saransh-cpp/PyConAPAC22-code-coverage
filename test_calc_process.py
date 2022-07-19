import unittest
import multiprocessing
from calc_process import add, subtract, divide, multiply


class TestCalc(unittest.TestCase):
    def test_add(self):
        queue = multiprocessing.Queue()

        p = multiprocessing.Process(target=add, args=(2, 3, queue),)
        p.start()
        result = queue.get()
        p.join()

        self.assertEqual(result, 5)

    def test_subtract(self):
        queue = multiprocessing.Queue()

        p = multiprocessing.Process(target=subtract, args=(queue, 2, 3),)
        p.start()
        result = queue.get()
        p.join()

        self.assertEqual(result, -1)

    def test_multiply(self):
        queue = multiprocessing.Queue()

        p = multiprocessing.Process(target=multiply, args=(queue, 2, 3),)
        p.start()
        result = queue.get()
        p.join()

        self.assertEqual(result, 6)

    def test_divide(self):
        queue = multiprocessing.Queue()

        p = multiprocessing.Process(target=divide, args=(queue, 2, 3),)
        p.start()
        result = queue.get()
        p.join()

        self.assertEqual(result, 2 / 3)
        self.assertRaises(ValueError, divide, [], 2, 0)


if __name__ == "__main__":
    unittest.main()
