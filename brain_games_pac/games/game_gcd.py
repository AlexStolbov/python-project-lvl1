from random import randint
from math import gcd
from brain_games_pac.engine import run_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = randint(1, 20)
    number_two = randint(1, 20)
    question = '{} {}'.format(number_one, number_two)
    answer = str(gcd)
    return question, answer


def is_even(number):
    return number % 2 == 0


def run_game_gcd(user_name):
    run_game(user_name, DESCRIPTION, get_question_and_answer)
