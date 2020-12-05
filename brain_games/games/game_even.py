from random import randint
from prompt import string

COUNT_Q = 3
GAME_RULE = 'Answer "yes" if this number is even, otherwise answer "no"'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer


def run_game(user_name, rule, get_question_and_correct_answer):
    print(rule)
    correct_count = 0
    wrong = False
    while correct_count < COUNT_Q and not wrong:
        question, correct_answer = get_question_and_correct_answer()
        print('Question: {}'.format(question))
        answer = string('Your answer: ')
        if answer == correct_answer:
            correct_count += 1
            print('Correct!')
        else:
            print('{} is wrong answer ;(. Correct answer was {}'.format(answer, correct_answer))
            print('Let\'s try again, {}'.format(user_name))
            wrong = True
    if not wrong:
        print('Congratulations, {}'.format(user_name))


def run_game_even(user_name):
    run_game(user_name, GAME_RULE, get_question_and_answer)


if __name__ == '__main__':
    run_game_even("Mishael")
