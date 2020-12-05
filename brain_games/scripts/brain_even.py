from brain_games.games.game_even import run_game_even
from brain_games.scripts.brain_games import main as games_main


def main():
    user_name = games_main()
    run_game_even(user_name)


if __name__ == '__main__':
    main()
