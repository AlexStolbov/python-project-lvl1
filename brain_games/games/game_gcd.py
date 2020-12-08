from random import randint
from brain_games.games.game_core import run_game

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = randint(0, 20)
    number_two = randint(1, 20)
    question = '{} {}'.format(number_one, number_two)
    answer = gcd(number_one, number_two)
    return question, answer


def gcd(number_one, number_two):
    if number_one == 0:
        return str(number_two)
    if number_two == 0:
        return str(number_one)
    if number_one == 1 or number_two == 1:
        return '1'
    result = 1
    while number_one > 1 and number_two > 1:
        if number_one == number_two:
            result = str(number_one)
            break
        elif not is_even(number_one) and not is_even(number_two):
            if number_one > number_two:
                number_one = int((number_one - number_two) / 2)
            else:
                number_two = int((number_two - number_one) / 2)
        elif is_even(number_one) and is_even(number_two):
            result = result * 2
            number_one = int(number_one / 2)
            number_two = int(number_two / 2)
        elif is_even(number_one):
            number_one = int(number_one / 2)
        else:
            number_two = int(number_two / 2)
    return str(result)


def is_even(number):
    return number % 2 == 0


def run_game_gcd(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    run_game_gcd("Michael")
