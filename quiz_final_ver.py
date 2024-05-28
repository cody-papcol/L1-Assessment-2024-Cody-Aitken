import random


def operation_checker(operation_question):
    while True:
        response = input(operation_question).lower()

        # checks if user inputted valid response so that if user inputs
        # an invalid response it can handle the error and ask
        # again
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

        # checks if user inputted valid response so that if user inputs
        # an invalid response it can handle the error and ask
        # again
        if response.isnumeric():
            return int(response)
        else:
            print('You did not choose a valid response.')


def yes_no(yes_no_question):
    while True:
        response = input(yes_no_question).lower()

        # checks if user inputted valid response so that if user inputs
        # an invalid response it can handle the error and ask
        # again
        if response == 'yes' or response == 'y':
            return 'y'
        elif response == 'no' or response == 'n':
            return 'n'
        else:
            print('You did not choose a valid response.')


def diff_checker(diff_question):
    while True:
        response = input(diff_question).lower()

        # checks if user inputted valid response so that if user inputs
        # an invalid response it can handle the error and ask
        # again
        if response == 'easy':
            return 'easy'
        elif response == 'normal':
            return 'normal'
        elif response == 'hard':
            return 'hard'
        else:
            print('You did not choose a valid response.')


# initialise variables for use later in the program
correct = 0
need_instructions = ''
difficulty = 'normal'
num1 = 0
num2 = 0
answer = 0
correct_answer = 0
question = ''
questions_list = []
correct_list = []
answer_list = []
summary_yn = ''
play_again = ''

# welcome message to display that welcomes the user and tells them to enter to start
print()
print('Welcome to The Maths Quiz! Press <enter> to start:')
print()
input()

# asks the user if they want the instructions for each difficulty so they can know how each difficulty works
# so they are more educated on what each difficulty means
need_instructions = yes_no('Would you like instructions for the game? (y/n): ')
if need_instructions == 'y':
    print('''
Before the game starts, you will be asked to choose a difficulty. 

In easy mode, questions are as simple as possible.

In normal mode, questions are medium difficulty.

In hard mode, questions are as hard as the program can go.

Then you will need to choose an operation. Addition, or '+', is quite simple and will be
harder depending on the chosen difficulty.
Subtraction, or '-', is also quite simple. It will scale in difficulty depending on
the chosen difficulty. Note that in subtraction there will never be a
negative answer. Negative answers will be classified as invalid
responses. (Consider yourself lucky)
Multiplication, or '*', will scale in difficulty as usual.
Division, or '/' will scale in difficulty as usual. Note that in division there will
never be a decimal answer, and decimal answers will be classified as an
invalid response.
At the end of the game your total stats will show. This shows how many questions were
correctly answered out of the total, and displays each wrong answer and the correct
answer to that question. Your total score as a percentage will also show.

''')

# loops while the 'play again' variable is not 'n', the variable is set to y or n at the end of the loop
# it means that the user can set 'play_again' at the end of the game to 'y' to play again, and can keep
# setting it to 'y' until they set it to 'n' and stop the game
while play_again != 'n':
    # gets the difficulty that the user wants so the program can edit the difficulty of the questions
    # depending on the chosen difficulty
    print()
    difficulty = diff_checker('What difficulty would you like? (\'easy\', \'normal\', \'hard\'): ')
    print()

    # gets the operation that the user wants so the program can make the questions depending on
    # the chosen operation
    print()
    operation = operation_checker('What operation (+, -, * or /): ')
    print()

    # gets the user to choose a number of questions with a maximum of 100. This will determine
    # how many times the question loop runs
    num_of_questions = answer_checker('Please choose a number of questions: ')
    while num_of_questions > 100:
        if num_of_questions > 100:
            print('That number is too high. The maximum amount of questions is 100.')
            num_of_questions = answer_checker('Please choose a number of questions: ')

    # detects if questions = zero because cannot have 0
    # questions but can have 0 as an answer
    while num_of_questions == 0:
        if num_of_questions == 0:
            print('You cannot have 0 questions!')
            num_of_questions = answer_checker('Please choose a number of questions: ')

    # actual game question loop that loops for the number in 'num_of_questions'
    for n in range(num_of_questions):
        print('Question ' + str(n + 1))

        # if the chosen operation is addition - questions, harder depending on chosen difficulty
        if operation == '+':
            if difficulty == 'easy':
                num1 = random.randint(0, 10)
                num2 = random.randint(0, 10)
                correct_answer = num1 + num2
                question = str(num1) + ' + ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'normal':
                num1 = random.randint(0, 50)
                num2 = random.randint(0, 50)
                correct_answer = num1 + num2
                question = str(num1) + ' + ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'hard':
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)
                correct_answer = num1 + num2
                question = str(num1) + ' + ' + str(num2) + ' = '
                answer = answer_checker(question)

            if int(answer) == correct_answer:
                print('Good job, the answer was correct.')
                correct += 1
            else:
                print('Sorry, that was incorrect.')
            answer_list.append(int(answer))
            correct_list.append(int(correct_answer))
            questions_list.append(question)

        # if the chosen operation is subtraction - questions, harder depending on chosen difficulty
        if operation == '-':
            if difficulty == 'easy':
                num2 = random.randint(0, 10)
                num1 = random.randint(num1, 10)
                correct_answer = num1 - num2
                question = str(num1) + ' - ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'normal':
                num2 = random.randint(0, 30)
                num1 = random.randint(num1, 30)
                correct_answer = num1 - num2
                question = str(num1) + ' - ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'hard':
                num2 = random.randint(0, 100)
                num1 = random.randint(num1, 100)
                correct_answer = num1 - num2
                question = str(num1) + ' - ' + str(num2) + ' = '
                answer = answer_checker(question)

            if int(answer) == correct_answer:
                print('Good job, the answer was correct.')
                correct += 1
            else:
                print('Sorry, that was incorrect.')
            answer_list.append(int(answer))
            correct_list.append(int(correct_answer))
            questions_list.append(question)

        # if the chosen operation is multiplication - questions, harder depending on chosen difficulty
        if operation == '*':
            if difficulty == 'easy':
                num1 = random.randint(1, 6)
                num2 = random.randint(1, 6)
                correct_answer = num1 * num2
                question = str(num1) + ' * ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'normal':
                num1 = random.randint(6, 12)
                num2 = random.randint(6, 12)
                correct_answer = num1 * num2
                question = str(num1) + ' * ' + str(num2) + ' = '
                answer = answer_checker(question)

            if difficulty == 'hard':
                num1 = random.randint(12, 20)
                num2 = random.randint(12, 20)
                correct_answer = num1 * num2
                question = str(num1) + ' * ' + str(num2) + ' = '
                answer = answer_checker(question)

            if int(answer) == correct_answer:
                print('Good job, the answer was correct.')
                correct += 1
            else:
                print('Sorry, that was incorrect.')
            answer_list.append(int(answer))
            correct_list.append(int(correct_answer))
            questions_list.append(question)

        # if the chosen operation is division - questions, harder depending on chosen difficulty
        if operation == '/':
            if difficulty == 'easy':
                num1 = random.randint(2, 5)
                num2 = random.randint(1, 5)
                result = num1 * num2
                correct_answer = result / num1
                question = str(result) + ' / ' + str(num1) + ' = '
                answer = answer_checker(question)

            if difficulty == 'normal':
                num1 = random.randint(5, 12)
                num2 = random.randint(4, 12)
                result = num1 * num2
                correct_answer = result / num1
                question = str(result) + ' / ' + str(num1) + ' = '
                answer = answer_checker(question)

            if difficulty == 'hard':
                num1 = random.randint(11, 15)
                num2 = random.randint(10, 15)
                result = num1 * num2
                correct_answer = result / num1
                question = str(result) + ' / ' + str(num1) + ' = '
                answer = answer_checker(question)

            if int(answer) == correct_answer:
                print('Good job, the answer was correct.')
                correct += 1
            else:
                print('Sorry, that was incorrect.')
            answer_list.append(int(answer))
            correct_list.append(int(correct_answer))
            questions_list.append(question)

    # asks user if they want their statistics so the program can decide if it should display them
    user_summary = yes_no('Would you likes stats on your game performance? (y/n): ')
    if user_summary == 'y':
        # summary blocks of printing code to organize the summary so it is easy to read
        print()
        print('Summary:')
        print()
        num = 1

        # showing each question and answer and if they were correct or not to show the user their results
        for ans in answer_list:
            if correct_list[num - 1] == ans:
                print('Question', str(num) + ':', 'The question was', '\'' + str(questions_list[-1]) + '\'' +
                      '. The correct answer was', str(correct_list[num - 1]) + '. Your answer was',
                      str(ans) + '.' + ' ✅')
                print()
            else:
                print('Question', str(num) + ':', 'The question was', '\'' + str(questions_list[-1]) + '\'' +
                      '. The correct answer was', str(correct_list[num - 1]) + '. Your answer was',
                      str(ans) + '.' + ' ❌')
                print()
            num += 1

        # displays score percentage to show what the users score was out of 100%
        final_score = correct / num_of_questions
        final_score = final_score * 100
        print()
        print('Your final score as a percentage is', str(final_score) + '%')
        print()

    # asks user if they want to play again so the program can loop if the 'play_again' variable is set to 'y'
    play_again = yes_no('Would you like to play again? (y/n): ')
