import random

# Welcome to this Mental Maths practise game.
# You can choose to test yourself with addition,
# subtraction, multiplication or division.
# There will be 5 questions to answer to test your Mental Maths skills.
# Your score will appear at the end.
# Are you ready? Let's go!


def get_username():
    """
    Get users name to personalise the quiz.
    """
    username = input("Enter your name: ")
    print(f"{username}, welcome to Mental Maths!")
    return username


def choose_operator():
    """
    Ask the user to choose which operator they want to use.
    Sets the operator for their 5 questions.
    Validate the user input.
    """
    print("Choose which mathematical operator you would like to use.")
    print("You can choose from add, subtract, multiply and divide.")
    print("All answers will be whole numbers (integers).")
    operators = ['add', 'subtract', 'multiply', 'divide']
    chosen_operator = ""
    chosen_operator = input("Please enter your mathematical operator: ")
    return chosen_operator
