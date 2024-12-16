import random


def game_progression():
    i = 0
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f'Hello, {name}!')

    print('What number is missing in the progression?')
    while i < 3:
        coll = random.randint(1, 10)
        colls = coll
        coll_all = []
        x = 0

        while x < 10:
            coll_all.append(str(colls))
            colls += coll
            x += 1

        coll_point = random.choice(coll_all)
        result = ' '.join(coll_all)
        res = result.replace(coll_point, '..', 1)

        print(f"Question: {res}")
        player_answer = input('Your answer: ')

        if player_answer == coll_point:
            print('Correct!')
            i += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(. \
                  Correct answer was '{coll_point}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    game_progression()


if __name__ == '__main__':
    main()