import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_numbers_(self) -> None:
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

    def test_subtract_numbers_(self) -> None:
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

    def test_multiply_numbers_(self) -> None:
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

    def test_divide_numbers_(self) -> None:
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


if __name__ == '__main__':
    unittest.main()
