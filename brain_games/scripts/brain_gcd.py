from brain_games.games.game_gcd import run_game_gcd
from brain_games.scripts.brain_games import main as games_main


def main():
    user_name = games_main()
    run_game_gcd(user_name)


if __name__ == '__main__':
    main()
