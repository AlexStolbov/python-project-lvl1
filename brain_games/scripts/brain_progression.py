from brain_games.games.game_progression import run_game_progression
from brain_games.scripts.brain_games import main as games_main


def main():
    user_name = games_main()
    run_game_progression(user_name)


if __name__ == '__main__':
    main()
