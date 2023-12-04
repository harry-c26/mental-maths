import random

print("**************************************************************")
print("Welcome to this Mental Maths practise game.")
print("You can choose to test yourself with addition,")
print("subtraction, multiplication or division.")
print("There will be 5 questions to answer to test your Mental Maths skills.")
print("Your score will appear at the end.")
print("Are you ready? Let's go!")
print("**************************************************************")


def get_username():
    """
    Allows users to enter their name to personalise the quiz.
    Validates the input to make sure something is entered before
    adding the username to the welcome message.
    """
    while True:
        username = input("Enter your name:\n")
        if username.strip():
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
        operator = input("Choose an operator from (+, -, *, /):\n")
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
            answer = int(input("Enter answer here:\n"))
            return answer
        except ValueError:
            print("Invalid answer. Please enter a valid integer.")


def generate_question(operator):
    """
    Creates the questions using random integers and the operator
    the user chose.
    If statement for division makes sure the answer is an integer.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operator == '/':
        num3 = num1 * num2
        question = f"{num3} {operator} {num2}"
        answer = eval(question)
        return question, answer

    else:
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
        return question, answer


def main():
    """
    Defines how the game is structured pulling in the other functions
    """
    username = get_username()
    print(f"Welcome, {username}, to Mental Maths!")

    operator = get_operator()

    score = 0
    for _ in range(5):
        question, correct_answer = generate_question(operator)
        print("Question:", question)
        user_answer = get_answer()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

    print(f"Congratulations, {username}! You got {score}/5 questions correct.")


if __name__ == "__main__":
    main()
