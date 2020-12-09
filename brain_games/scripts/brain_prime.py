from brain_games.games.game_prime import run_game_prime
from brain_games.scripts.brain_games import main as games_main


def main():
    user_name = games_main()
    run_game_prime(user_name)


if __name__ == '__main__':
    main()
