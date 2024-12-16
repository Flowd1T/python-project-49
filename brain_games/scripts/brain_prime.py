from random import randint


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def game_prime():
    i = 0
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while i < 3:
        num_question = randint(2, 100)
        print(f"Question: {num_question}")
        answer = input('Your answer: ')
        if IsPrime(num_question) == True and answer.lower() == 'yes':
            print('Correct!')
            i += 1
        elif IsPrime(num_question) == False and answer.lower() == 'no':
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{"yes" if IsPrime(num_question) == True else "no"}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    game_prime()


if __name__ == '__main__':
    main()