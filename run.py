import random

# Welcome to this Mental Maths practise game.
# You can choose to test yourself with addition,
# subtraction, multiplication or division.
# There will be 5 questions to answer to test your Mental Maths skills.
# Your score will appear at the end.
# Are you ready? Let's go!


def get_username():
    """
    Get users name to personalise the quiz
    """
    username = input("Enter your name: ")
    print(f"{username}, welcome to Mental Maths!")


get_username()
