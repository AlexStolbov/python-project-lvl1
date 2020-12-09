from random import randint
from brain_games.games.game_core import run_game

GAME_RULE = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = get_progression()
    pos = randint(0, len(progression) - 1)
    answer = progression[pos]
    progression[pos] = '..'
    question = ' '.join(element for element in progression)
    return question, answer


def get_progression():
    start = randint(0, 20)
    length = randint(5, 10)
    step = randint(1, 10)
    all = range(start, start + (length * step), step)
    return list(str(element) for element in all)


def run_game_progression(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    run_game_progression("Michael")
