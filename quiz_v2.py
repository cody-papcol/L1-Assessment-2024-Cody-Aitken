import random


def operation_checker(operation_question):
    while True:
        response = input(operation_question).lower()

        # checks if user inputted valid response
        if response == '+':
            return '+'
        elif response == '-':
            return '-'
        elif response == '*':
            return '*'
        elif response == '/':
            return '/'
        else:
            print('you did not choose a valid response')


def answer_checker(answer_question):
    while True:
        response = input(answer_question).lower()

        # checks if user inputted valid response
        if response.isnumeric():
            return int(response)
        else:
            print('you did not choose a valid response')


def yes_no(yes_no_question):
    while True:
        response = input(yes_no_question).lower()

        # checks if user inputted valid response
        if response == 'yes' or response == 'y':
            return 'y'
        elif response == 'no' or response == 'n':
            return 'n'
        else:
            print('you did not choose a valid response')



# initialise variables
correct = 0
incorrect = 0
difficulty = ''
need_instructions = ''
difficulty = 'normal'
num1 = 0
num2 = 0
answer = 0
correct_answer = 0
question = ''
correct_list = []
answer_list = []
are_sure = ''

# welcome message
print()
print('Welcome to The Maths Quiz! Press <enter> to start:')
print()
input()

# asks the user if they want the instructions for each difficulty
need_instructions = yes_no('You need to choose a difficulty. Do you want descriptions of each difficulty? (y/n): ')
if need_instructions == 'y':
    print('''

In easy mode, you can choose the length of the quiz. 
Questions are as simple as possible.

In normal mode, you can choose the length of the quiz.
Questions are medium difficulty.

In hard mode, you cannot choose the length of the quiz.
Questions are as hard as the program can go.

Total stats shows how many questions were correctly answered out of the total, and 
displays each wrong answer and the correct answer to that question.

''')

print()
operation = operation_checker('What operation (+, -, * or /): ')
print()

# NEEDS DEBUGGING, DOES NOT WORK PROPERLY
num_of_questions = answer_checker('Please choose a number of questions: ')
if num_of_questions > 100:
    while are_sure != 'n':
        are_sure = yes_no('Are you sure you want that many questions? (y/n): ')
        if are_sure == 'n':
            num_of_questions = answer_checker('Please choose a number of questions: ')

# question loop
for n in range(num_of_questions):
    print('Question ' + str(n + 1))
    if operation == '+':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        correct_answer = num1 + num2
        answer = answer_checker(str(num1) + ' + ' + str(num2) + ' = ')
        if int(answer) == correct_answer:
            print('Good job, the answer was correct.')
        else:
            print('Sorry, that was incorrect.')
        answer_list.append(int(answer))
        correct_list.append(int(correct_answer))
    if operation == '-':
        num2 = random.randint(0, 100)
        num1 = random.randint(num1, 100)
        correct_answer = num1 - num2
        answer = answer_checker(str(num1) + ' - ' + str(num2) + ' = ')
        if int(answer) == correct_answer:
            print('Good job, the answer was correct.')
        else:
            print('Sorry, that was incorrect.')
        answer_list.append(int(answer))
        correct_list.append(int(correct_answer))
    if operation == '*':
        num1 = random.randint(0, 15)
        num2 = random.randint(0, 15)
        correct_answer = num1 * num2
        answer = answer_checker(str(num1) + ' * ' + str(num2) + ' = ')
        if int(answer) == correct_answer:
            print('Good job, the answer was correct.')
        else:
            print('Sorry, that was incorrect.')
        answer_list.append(int(answer))
        correct_list.append(int(correct_answer))
    if operation == '/':
        num1 = random.randint(2, 15)
        num2 = random.randint(1, 15)
        result = num1 * num2
        correct_answer = result / num1
        answer = answer_checker(str(result) + ' / ' + str(num1) + ' = ')
        if int(answer) == correct_answer:
            print('Good job, the answer was correct.')
        else:
            print('Sorry, that was incorrect.')
        answer_list.append(int(answer))
        correct_list.append(int(correct_answer))

print()
print('Summary:')
print()
num = 1
for a in answer_list:
    print('Question', str(num) + ':', 'The correct answer was', str(correct_list[num - 1]) + '. Your answer was',
          str(a) + '.')
    num += 1
