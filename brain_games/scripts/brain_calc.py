import random


def game_calc():
    i = 0

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')

    while i < 3:

        operand = ['+', '-', '*']
        first_num = random.randint(0, 100)
        second_num = random.randint(0, 100)
        rand_operand = random.choice(operand)
        question = str(first_num) + ' ' + rand_operand + ' ' + str(second_num)

        print('What is the result of the expression?')
        print(f'Question: {question}')
        answer = input('Your answer: ')
        answer_int = int(answer)

        if rand_operand == '*':
            answer_true = int(first_num) * int(second_num)
        elif rand_operand == '+':
            answer_true = int(first_num) + int(second_num)
        elif rand_operand == '-':
            answer_true = int(first_num) - int(second_num)

        if answer_int == answer_true:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer_int}' is wrong answer ;(. \
                  Correct answer was '{answer_true}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f'Congratulations, {name}!')


def main():
    game_calc()


if __name__ == '__main__':
    main()