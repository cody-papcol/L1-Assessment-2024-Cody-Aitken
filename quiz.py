import random

# initialise variables
operation = ''
correct = 0
incorrect = 0
difficulty = ''
need_instructions = ''

# welcome message
print()
print('Welcome to The Maths Quiz! Press <enter> to start:')
print()
input()

# asks the user if they want the instructions for each difficulty
while need_instructions != 'y' and need_instructions != 'n':
    need_instructions = input('You need to choose a difficulty. Do you want descriptions of each difficulty? (y/n): ')
    if need_instructions == 'y':
        print('''

                    * * * Difficulties * * *

In easy mode, you can choose the length of the quiz (minimum 5 questions).
You can choose the operation that is used in the quiz and you are told if
their answer is correct or incorrect as soon as you enter it. If the answer
is wrong you can choose to try again or pass. you can reattempt the question
as many times as you want. Total stats are displayed for the quiz at the
end.

In normal mode, you can choose the length of the quiz (minimum 10 questions).
you can choose the operation used in the quiz. When entering an answer you are
told if it was correct or incorrect and cannot try again. If you get a question
wrong, you are told what the correct answer was and move on. Total stats are
displayed for the quiz at the end.

In hard mode, you cannot choose the length of the quiz (exactly 20 questions),
cannot choose the operation and the quiz includes a mix of operations. When entering
an answer you are told if the answer is correct or incorrect. When you get a question
wrong you are not told what the correct answer was and move on. Total stats are
displayed for the quiz at the end.


        ''')
        print()
        print('game goes here')
    elif need_instructions == 'n':
        print('game goes here')
    else:
        need_instructions = input('Please enter a valid response (y/n): ')

