import os
import sys
import unittest
from pathlib import Path

from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

sys.path.append('C:/Users/karen/Desktop/Prisma_P/unit11_testing_sequence')

import functions.functions as f

instrument_and_import_package(os.path.join(
    Path(__file__).parent.absolute(), '..', 'functions'), 'functions')


class TestCalculator(unittest.TestCase):
    # Addition
    def test_addition(self) -> None:
        # Beggining of the sequence
        initialise_call_hierarchy('start')

        self.calculator = f.Calculator()

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

        # Ending of the sequence
        root_call = finalise_call_hierarchy()

        # Sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Sequence diagram in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__), '..', 'doc', 'sd_addition.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Subtraction
    def test_subtraction(self) -> None:
        # Beggining of the sequence
        initialise_call_hierarchy('start')

        self.calculator = f.Calculator()

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

        # Ending of the sequence
        root_call = finalise_call_hierarchy()

        # Sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Sequence diagram in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__), '..', 'doc', 'sd_subtraction.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Multiplication
    def test_multiplication(self) -> None:
        # Beggining of the sequence
        initialise_call_hierarchy('start')

        self.calculator = f.Calculator()

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

        # Ending of the sequence
        root_call = finalise_call_hierarchy()

        # Sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Sequence diagram in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__), '..', 'doc', 'sd_multiplication.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    # Division
    def test_division(self) -> None:
        # Beggining of the sequence
        initialise_call_hierarchy('start')

        self.calculator = f.Calculator()

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

        # Ending of the sequence
        root_call = finalise_call_hierarchy()

        # Sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Sequence diagram in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__), '..', 'doc', 'sd_division.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)


if __name__ == '__main__':
    unittest.main()
