import random

# Welcome to this Mental Maths practise game.
# You can choose to test yourself with addition,
# subtraction, multiplication or division.
# There will be 5 questions to answer to test your Mental Maths skills.
# Your score will appear at the end.
# Are you ready? Let's go!


def get_username():
    """
    Allows users to enter their name to personalise the quiz.
    Validates the input to make sure something is entered before
    adding the username to the welcome message.
    """
    while True:
        username = input("Enter your name: ")
        if username.strip():
            print(f"Welcome, {username}, to Mental Maths!")
            return username
        else:
            print("Please enter a valid username")


def get_operator():
    """
    Gives the user the choice of which operand they want to use
    for the quiz.
    Validates the input to ensure it is one of the 4 options.
    """
    print("Please choose your operator for the quiz.")
    print("The options are add, subtract, multiply & divide.")
    while True:
        operator = input("Choose an operator from (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please choose +, -, * or /.")


def get_answer():
    """
    Checks user answer and validates that it's an integer
    """
    while True:
        try:
            answer = int(input("Enter answer here: "))
        except ValueError:
            print("Invalid answer. Please enter a valid integer: ")


def generate_question(operator):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer
