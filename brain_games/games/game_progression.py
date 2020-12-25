from random import randint

DESCRIPTION = 'What number is missing in the progression?'


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
