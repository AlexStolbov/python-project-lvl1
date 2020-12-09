from brain_games.games.game_core import run_game
from random import randint
from math import sqrt

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 20)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer


def is_prime(number):
    result = True
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            result = False
            break
    return result


def run_game_prime(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    run_game_prime("Michael")
