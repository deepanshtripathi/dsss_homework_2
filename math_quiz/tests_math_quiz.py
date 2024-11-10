import unittest
from math_quiz import generate_random_number, choose_operator, generate_problem_and_answer

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        """
        Test if generate_random_number will produces values within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(100):  # Test a reasonable number of random values
            random_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= random_num <= max_val, "Generated number out of range")

    def test_choose_operator(self):
        """
        Test if choose_operator returns one of the valid operators
        """
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times to cover randomness
            operator = choose_operator()
            self.assertIn(operator, valid_operators, "Invalid operator returned")

    def test_generate_problem_and_answer(self):
        """
        Testing to generate_problem_and_answer with predefined cases to ensure correct outputs
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem string incorrect for {num1} {operator} {num2}")
            self.assertEqual(answer, expected_answer, f"Answer incorrect for {num1} {operator} {num2}")

if __name__ == "__main__":
    unittest.main()
