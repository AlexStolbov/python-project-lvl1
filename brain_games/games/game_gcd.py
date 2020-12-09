from random import randint
from brain_games.games.game_core import run_game

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = randint(1, 20)
    number_two = randint(1, 20)

    number_one = 25
    number_two = 50

    question = '{} {}'.format(number_one, number_two)
    answer = gcd(number_one, number_two)
    return question, answer


def gcd(number_one, number_two):
    result = 1
    while number_one > 1 and number_two > 1:
        while number_one % 2 == 0 and number_two % 2 == 0:
            number_one = int(number_one / 2)
            number_two = int(number_two / 2)
            result = result * 2
        while number_one % 2 == 0:
            number_one = int(number_one / 2)
        while number_two % 2 == 0:
            number_two = int(number_two / 2)
        if number_one == number_two:
            result = str(result * number_one)
            break
        elif number_one > number_two:
            number_one = int((number_one - number_two) / 2)
        else:
            number_two = int((number_two - number_one) / 2)
    return str(result)


def is_even(number):
    return number % 2 == 0


def run_game_gcd(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    run_game_gcd("Michael")
