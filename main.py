import random

# initialise variables
operation = ''
correct = 0
incorrect = 0

input('Welcome to BorAs, the best maths quiz ever! Press <enter> to being.')
difInstructions = input('Would you like to know the difference between Easy, Normal, or Hard Mode? (y/n)')
if difInstructions == 'y':
    print('''
    In easy mode, the user can choose the length of the quiz (minimum 5 questions). The user can choose
    the operation that is used in the quiz and they are told if their answer is correct or incorrect as soon
    as they enter it. If the answer is wrong they can choose to try again or pass. They can reattempt the question
    as many times as they want. Total stats are displayed for the quiz at the end.

    In normal mode, the user can choose the length of the quiz (minimum 10 questions). The user can choose the operation
    used in the quiz. When entering an answer they are told if it was correct or incorrect and cannot try again. If
    the user gets a question wrong, they are told what the correct answer was and move on. Total stats are displayed
    for the quiz at the end.

    In hard mode, the user cannot choose the length of the quiz (exactly 20 questions), cannot choose the operation
    and the quiz includes a mix of operations. When entering an answer the user is told if the answer is correct or
    incorrect. When the user gets a question wrong they are not told what the correct answer was and move on. Total
    stats are displayed for the quiz at the end.
    ''')
elif difInstructions == 'n':
    print('game')
else:
    difInstructions = input('Please enter y or n')