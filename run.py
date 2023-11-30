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
    username = input("Enter your name: ")
    while username == "":
        username = input("No name entered, please enter your name: ")
    print(f"Welcome, {username}, to Mental Maths!")
    return username


def choose_operator():
    """
    Gives the user the choice of which operand they want to use
    for the quiz.
    Validates the input to ensure it is one of the 4 options.
    """
    print("Please choose your operator for the quiz.")
    print("The options are add, subtract, multiply & divide.")
    operators = ['add', 'subtract', 'multiply', 'divide']
    user_operator = ""
    user_operator = input("Please enter your operator of choice: ")
    while user_operator not in operators:
        print("Not a valid option.")
        user_operator = input("Please enter a valid operator: ")
    return user_operator
