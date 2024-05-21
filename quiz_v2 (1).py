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
            print('You did not choose a valid response.')


def answer_checker(answer_question):
    while True:
        response = input(answer_question).lower()

        # checks if user inputted valid response
        if response.isnumeric():
            return int(response)
        else:
            print('You did not choose a valid response.')


def yes_no(yes_no_question):
    while True:
        response = input(yes_no_question).lower()

        # checks if user inputted valid response
        if response == 'yes' or response == 'y':
            return 'y'
        elif response == 'no' or response == 'n':
            return 'n'
        else:
            print('You did not choose a valid response.')


def diff_checker(diff_question):
    while True:
        response = input(diff_question).lower()

        # checks if user inputted valid response
        if response == 'easy':
            return 'easy'
        elif response == 'normal':
            return 'normal'
        elif response == 'hard':
            return 'hard'
        else:
            print('You did not choose a valid response.')


# initialise variables
correct = 0
incorrect = 0
need_instructions = ''
difficulty = 'normal'
num1 = 0
num2 = 0
answer = 0
correct_answer = 0
question = ''
correct_list = []
answer_list = []

# welcome message
print()
print('Welcome to The Maths Quiz! Press <enter> to start:')
print()
input()

# asks the user if they want the instructions for each difficulty
need_instructions = yes_no('You need to choose a difficulty. Do you want descriptions of each difficulty? (y/n): ')
if need_instructions == 'y':
    print('''

In easy mode, questions are as simple as possible.

In normal mode, questions are medium difficulty.

In hard mode, questions are as hard as the program can go.

Total stats shows how many questions were correctly answered out of the total, and 
displays each wrong answer and the correct answer to that question.

''')

# gets the difficulty that the user wants
print()
difficulty = diff_checker('What difficulty would you like? (\'easy\', \'normal\', \'hard\'): ')
print()

# gets the operation that the user wants
print()
operation = operation_checker('What operation (+, -, * or /): ')
print()

# gets the user to choose a number of questions with a maximum of 100
num_of_questions = answer_checker('Please choose a number of questions: ')
while num_of_questions > 100:
    if num_of_questions > 100:
        print('That number is too high. The maximum amount of questions is 100.')
        num_of_questions = answer_checker('Please choose a number of questions: ')

# actual game question loop
for n in range(num_of_questions):
    print('Question ' + str(n + 1))

    if operation == '+':
        if difficulty == 'easy':
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            correct_answer = num1 + num2
            answer = answer_checker(str(num1) + ' + ' + str(num2) + ' = ')

        if difficulty == 'normal':
            num1 = random.randint(0, 50)
            num2 = random.randint(0, 50)
            correct_answer = num1 + num2
            answer = answer_checker(str(num1) + ' + ' + str(num2) + ' = ')

        if difficulty == 'hard':
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
        if difficulty == 'easy':
            num2 = random.randint(0, 10)
            num1 = random.randint(num1, 10)
            correct_answer = num1 - num2
            answer = answer_checker(str(num1) + ' - ' + str(num2) + ' = ')

        if difficulty == 'normal':
            num2 = random.randint(0, 30)
            num1 = random.randint(num1, 30)
            correct_answer = num1 - num2
            answer = answer_checker(str(num1) + ' - ' + str(num2) + ' = ')

        if difficulty == 'hard':
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
        if difficulty == 'easy':
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            correct_answer = num1 * num2
            answer = answer_checker(str(num1) + ' * ' + str(num2) + ' = ')

        if difficulty == 'normal':
            num1 = random.randint(6, 12)
            num2 = random.randint(6, 12)
            correct_answer = num1 * num2
            answer = answer_checker(str(num1) + ' * ' + str(num2) + ' = ')

        if difficulty == 'hard':
            num1 = random.randint(12, 20)
            num2 = random.randint(12, 20)
            correct_answer = num1 * num2
            answer = answer_checker(str(num1) + ' * ' + str(num2) + ' = ')

        if int(answer) == correct_answer:
            print('Good job, the answer was correct.')
        else:
            print('Sorry, that was incorrect.')
        answer_list.append(int(answer))
        correct_list.append(int(correct_answer))

    if operation == '/':
        if difficulty == 'easy':
            num1 = random.randint(2, 5)
            num2 = random.randint(1, 5)
            result = num1 * num2
            correct_answer = result / num1
            answer = answer_checker(str(result) + ' / ' + str(num1) + ' = ')

        if difficulty == 'normal':
            num1 = random.randint(5, 12)
            num2 = random.randint(4, 12)
            result = num1 * num2
            correct_answer = result / num1
            answer = answer_checker(str(result) + ' / ' + str(num1) + ' = ')

        if difficulty == 'hard':
            num1 = random.randint(11, 15)
            num2 = random.randint(10, 15)
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
for ans in answer_list:
    if correct_list[num - 1] == ans:
        print('Question', str(num) + ':', 'The correct answer was', str(correct_list[num - 1]) + '. Your answer was',
              str(ans) + '.' + ' ✅')
    else:
        print('Question', str(num) + ':', 'The correct answer was', str(correct_list[num - 1]) + '. Your answer was',
              str(ans) + '.' + ' ❌')
    num += 1
