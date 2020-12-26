from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(0, 20)
    length = randint(5, 10)
    step = randint(1, 10)
    progression = list(map(str, make_progression(start, length, step)))
    replace_position = randint(0, len(progression) - 1)
    answer = progression[replace_position]
    progression[replace_position] = '..'
    question = ' '.join(progression)
    return question, answer


def make_progression(start, length, step):
    return list(range(start, start + (length * step), step))
