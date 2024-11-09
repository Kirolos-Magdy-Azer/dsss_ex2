import unittest
from math_quiz import random_integer, operator_random_choice, simpl_calculator


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            self.assertIsInstance(rand_num , int, "Result should be an integer")
            self.assertGreaterEqual(rand_num , 1, "Result should be >= min")
            self.assertLessEqual(rand_num , 10, "Result should be <= max")
    def test_operator_random_choice(self):
        def test_valid_output(self):
        valid_operators = ['+', '-', '*']
        
        # Call the function multiple times to check for randomness and validity
        for _ in range(10):
            operator = operator_random_choice()
            self.assertIn(operator, valid_operators, "Result should be one of '+', '-', '*'")
            self.assertIsInstance(operator, str, "Result should be a string")

    def test_simpl_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:   
                with self.subTest(num1=num1, num2=num2, operator=operator):
                    operation, answer = simpl_calculator(num1, num2, operator)
                    self.assertEqual(operation, expected_problem, f"Expected operation: {expected_problem}, got: {actual_problem}")
                    self.assertEqual(answer, expected_answer, f"Expected result: {expected_answer}, got: {actual_answer}")


if __name__ == "__main__":
    unittest.main()
