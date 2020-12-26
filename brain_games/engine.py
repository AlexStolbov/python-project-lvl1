from prompt import string

ROUNDS_COUNT = 3
MESSAGE_QUESTION = 'Question: {}'
MESSAGE_ANSWER = 'Your answer: '
MESSAGE_CORRECT = 'Correct!'
MESSAGE_WRONG = "'{}' is wrong answer ;(. Correct answer was '{}'"
MESSAGE_TRY = 'Let\'s try again, {}!'
MESSAGE_CONGRATULATIONS = 'Congratulations, {}!'


def run_game(game):
    user_name = string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.DESCRIPTION)
    correct_count = 0
    while correct_count < ROUNDS_COUNT:
        question, correct_answer = game.get_question_and_answer()
        print(MESSAGE_QUESTION.format(question))
        answer = string(MESSAGE_ANSWER)
        if answer == correct_answer:
            correct_count += 1
            print(MESSAGE_CORRECT)
        else:
            print(MESSAGE_WRONG.format(answer, correct_answer))
            print(MESSAGE_TRY.format(user_name))
            break
    if correct_count >= ROUNDS_COUNT:
        print(MESSAGE_CONGRATULATIONS.format(user_name))
