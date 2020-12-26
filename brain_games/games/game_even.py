from random import randint


DESCRIPTION = 'Answer "yes" if this number is even, otherwise answer "no"'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


def is_even(number):
    return number % 2 == 0
