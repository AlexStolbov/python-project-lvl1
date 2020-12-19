from random import randint, choice
from brain_games_pac.engine import run_game
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {'+': add, '-': sub, '*': mul}


def get_question_and_answer():
    operand_one = randint(1, 10)
    operand_two = randint(1, 10)
    operator, fun = choice(list(OPERATORS.items()))
    question = '{} {} {}'.format(operand_one, operator, operand_two)
    answer = str(fun(operand_one, operand_two))
    return question, answer


def call_run_game(user_name):
    run_game(user_name, DESCRIPTION, get_question_and_answer)
