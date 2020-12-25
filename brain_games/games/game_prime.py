from random import randint
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 20)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer


def is_prime(number):
    result = False if number < 2 else True
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            result = False
            break
    return result
