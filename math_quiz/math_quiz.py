import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (including them).
    """
    return random.randint(min_value, max_value)

def choose_operator():
    """
    Randomly will select an operator from addition, subtraction, or multiplication.
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1, num2, operator):
    """
    Will create a math problem string and calculates the answer based on the given operator

    Args:
        num1 (int) - The first number.
        num2 (int) - The second number.
        operator (str) - The operator for the problem ('+', '-','*')

    Returns:
        tuple - Containing the problem string and the answer
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Will run a math quiz game where the user is presented with math problems
    and earns points for correct answers.
    """
    score = 0
    total_questions = 5  # Changed from an incorrect value (3.14159265359) to an integer.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and an operator for the problem.
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)  # Changed max from 5.5 to 5 for integer compatibility.
        operator = choose_operator()

        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get user input and handle invalid inputs.
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check the answer and update the score.
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
