from random import randint
from brain_games_pac.engine import run_game

DESCRIPTION = 'Answer "yes" if this number is even, otherwise answer "no"'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer


def run_game_even(user_name):
    run_game(user_name, DESCRIPTION, get_question_and_answer)