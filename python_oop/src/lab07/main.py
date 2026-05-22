import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from lab07.app import GameApp
from lab07.cli import CLI
from lab07.storage import save, load   # ВАЖНО: такие имена

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "players.json")


def main() -> None:
    """Точка входа."""

    app = GameApp()

    # ЗАГРУЗКА
    players = load(DATA_FILE)

    app.load_players(players)

    print(f"\nЗагружено игроков: {len(players)}")

    cli = CLI(app)
    cli.run()

    # СОХРАНЕНИЕ
    save(
        app.get_all_players(),
        DATA_FILE
    )

    print("Данные сохранены.")


if __name__ == "__main__":
    main()