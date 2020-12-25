from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = randint(1, 20)
    number_two = randint(1, 20)
    question = '{} {}'.format(number_one, number_two)
    answer = str(gcd(number_one, number_two))
    return question, answer


def is_even(number):
    return number % 2 == 0

