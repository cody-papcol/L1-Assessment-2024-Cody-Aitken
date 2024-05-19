import random

# initialising variables as placeholder for actual variables in main game
difficulty = 'normal'
num_of_questions = 3
operation = input('What operation (+, -, * or /): ')
num1 = 0
num2 = 0
answer = 0
correct_answer = 0
question = ''
correct_list = []
answer_list = []

# question loop
for n in range(num_of_questions):
    print('Question ' + str(n + 1))
    if operation == '+':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        correct_answer = num1 + num2
        question = str(num1) + ' + ' + str(num2) + ' = '
        answer = input(question)
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
        question = str(num1) + ' - ' + str(num2) + ' = '
        answer = input(question)
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
        question = str(num1) + ' * ' + str(num2) + ' = '
        answer = input(question)
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
        question = str(result) + ' / ' + str(num1) + ' = '
        answer = input(question)
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
    print('Question', str(num) + ':', 'The correct answer was', str(correct_list[num - 1]) + '. Your answer was', str(a) + '.')
    num += 1

