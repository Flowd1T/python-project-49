from random import randint


def game_even():
    i = 0
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        num = randint(0, 100)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        if num % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            i += 1
        elif num % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
            i += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    game_even()    


if __name__ == '__main__':
    main()
