from operator import sub, truediv
from functools import reduce


class Calculator:
    """Contains the four basic operations
    """

    def add_numbers(self, *numbers: float) -> float:
        """Takes a variable number of inputs and returns the sum of them.

        :raises TypeError: When the input is not a number
        :return: Sum of numbers
        :rtype: float
        """

        try:
            return sum(numbers)
        except BaseException:
            raise TypeError('Some values are not valid')

    def subtract_numbers(self, *numbers: float) -> float:
        """Takes a variable number of inputs and returns the subtraction.

        :raises TypeError: When the input is not a number
        :return: Subtraction of numbers
        :rtype: float
        """

        try:
            return reduce(sub, numbers)
        except BaseException:
            raise TypeError('Some values are not valid')

    def multiply_numbers(self, *numbers: float) -> float:
        """Takes two numbers and returns the multiplication of them.

        :raises TypeError: When the input is not a number
        :return: Multiplication of numbers
        :rtype: float
        """
        try:
            return reduce((lambda x, y: x * y), numbers)
        except BaseException:
            raise TypeError('Some values are not valid')

    def divide_numbers(self, *numbers: float) -> float:
        """Takes a variable number of inputs and returns the division of them.

        :raises ZeroDivisionError: When the input is zero
        :raises TypeError: When the input is not a number
        :return:  Division of the numbers
        :rtype: float
        """

        try:
            return reduce(truediv, numbers)
        except BaseException:
            if 0 in numbers:
                raise ZeroDivisionError('Zero division')
            else:
                raise TypeError('Some values are not valid')
