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
    while username == "":
        username = input("No name entered, please enter your name: ")
    print(f"Welcome, {username}, to Mental Maths!")
    return username


get_username()
