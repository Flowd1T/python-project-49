import math
from random import randint


def game_gcd():
    i = 0
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')

    print('Find the greatest common divisor of given numbers.')
    while i < 3:

        f_num = randint(1, 100)
        s_num = randint(1, 100)
        all_num = str(f_num) + ' ' + str(s_num)

        true_answer = math.gcd(f_num, s_num)
        print(f'Question: {all_num}')

        player_answer = int(input('Your answer: '))
        if true_answer == player_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(. \
                  Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    game_gcd()


if __name__ == '__main__':
    main()