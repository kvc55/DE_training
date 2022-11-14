import unittest
import sys
import datetime

sys.path.append('C:/Users/karen/Desktop/Prisma_P/unit11_testing_txt')

from functions.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_numbers(self) -> None:
        # positive numbers' case
        self.assertEqual(self.calculator.add_numbers(5, 10, 3), 18)
        # negative numbers' case
        self.assertEqual(self.calculator.add_numbers(-1, -1, -3, -6), -11)
        # negative and positive numbers' case
        self.assertEqual(self.calculator.add_numbers(-1, 1), 0)
        # int and float numbers' case
        self.assertEqual(self.calculator.add_numbers(-1.5, 1, 5), 4.5)
        # test value type error
        with self.assertRaises(TypeError):
            self.calculator.add_numbers('5', 10)
            self.calculator.add_numbers([-3, 6.4, 2], 10, 5.5)

    def test_subtract_numbers(self) -> None:
        # positive numbers' case
        self.assertEqual(self.calculator.subtract_numbers(10, 5, 3), 2)
        # negative numbers' case
        self.assertEqual(self.calculator.subtract_numbers(-1, -1, -6), 6)
        # negative and numbers' case
        self.assertEqual(self.calculator.subtract_numbers(-1, 1, 0), -2)
        # int and float numbers' case
        self.assertEqual(self.calculator.subtract_numbers(-1.5, 1, 5), -7.5)
        # test value type error
        with self.assertRaises(TypeError):
            self.calculator.subtract_numbers('5', 10)
            self.calculator.subtract_numbers([-3, 6.4, 2], 10, 5.5)

    def test_multiply_numbers(self) -> None:
        # positive numbers' case
        self.assertEqual(self.calculator.multiply_numbers(10, 5, 3), 150)
        # negative numbers' case
        self.assertEqual(self.calculator.multiply_numbers(-1, -1, -2), -2)
        # negative and positive numbers' case
        self.assertEqual(self.calculator.multiply_numbers(-1, 1, 8), -8)
        # int and float numbers' case
        self.assertEqual(self.calculator.multiply_numbers(-1.5, 1, 5), -7.5)
        # test value type error
        with self.assertRaises(TypeError):
            self.calculator.multiply_numbers('5', 10)
            self.calculator.multiply_numbers([-3, 6.4, 2], 10, 5.5)

    def test_divide_numbers(self) -> None:
        # positive numbers' case
        self.assertEqual(self.calculator.divide_numbers(10, 5, 4), 0.5)
        # negative numbers' case
        self.assertEqual(self.calculator.divide_numbers(-1, -1, -5), -0.2)
        # negative and positive numbers' case
        self.assertEqual(self.calculator.divide_numbers(-1, 1, 5), -0.2)
        # int and float numbers' case
        self.assertEqual(self.calculator.divide_numbers(-1.5, 1, 5), -0.3)
        # test value type error
        with self.assertRaises(TypeError):
            self.calculator.divide_numbers('5', 10)
            self.calculator.divide_numbers([-3, 6.4, 2], 10, 5.5)
        # test zero division error
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide_numbers(10, 0, 3)


def insert_header(f):
    f.write('\n')
    f.write('******************TESTING**************************')
    f.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time)
    f.write('\n')
    return f


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('C:/Users/karen/Desktop/Prisma_P/unit11_testing_txt'
              '/tests/testing.txt', 'a') as f:
        f = insert_header(f)
        main(f)
