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


get_username()
