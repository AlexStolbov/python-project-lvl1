from random import randint, choice
from brain_games.games.game_core import run_game

GAME_RULE = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def get_question_and_answer():
    operand_one = randint(1, 10)
    operand_two = randint(1, 10)
    question = '{} {} {}'.format(operand_one, choice(OPERATORS), operand_two)
    answer = str(eval(question))
    return question, answer


def call_run_game(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    call_run_game("Mishael")
