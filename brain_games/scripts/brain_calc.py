from brain_games.games.game_calc import call_run_game
from brain_games.scripts.brain_games import main as games_main


def main():
    user_name = games_main()
    call_run_game(user_name)


if __name__ == '__main__':
    main()
