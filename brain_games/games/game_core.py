from prompt import string

COUNT_Q = 3
MESSAGE_ONE = 'Question: {}'
MESSAGE_TWO = 'Your answer: '
MESSAGE_THREE = 'Correct!'
MESSAGE_FOUR = "'{}' is wrong answer ;(. Correct answer was '{}'"
MESSAGE_FIVE = 'Let\'s try again, {}!'
MESSAGE_SIX = 'Congratulations, {}!'


def run_game(user_name, rule, get_question_and_correct_answer):
    print(rule)
    correct_count = 0
    correct = True
    while correct_count < COUNT_Q and correct:
        question, correct_answer = get_question_and_correct_answer()
        print(MESSAGE_ONE.format(question))
        answer = string(MESSAGE_TWO)
        if answer == correct_answer:
            correct_count += 1
            print(MESSAGE_THREE)
        else:
            print(MESSAGE_FOUR.format(answer, correct_answer))
            print(MESSAGE_FIVE.format(user_name))
            correct = False
    if correct:
        print(MESSAGE_SIX.format(user_name))
