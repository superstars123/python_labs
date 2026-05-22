from lab04.models import Player, PremiumPlayer
from app import GameApp

from exceptions import (
    DuplicatePlayerError,
    PlayerNotFoundError
)


class CLI:
    """CLI интерфейс."""

    def __init__(self, app: GameApp) -> None:
        self.app = app

    # ================= MENU =================

    def show_menu(self) -> None:

        print("\n===== GAME MENU =====")

        print("1. Показать игроков")
        print("2. Добавить игрока")
        print("3. Найти игрока")
        print("4. Удалить игрока")
        print("5. Сортировка по силе")
        print("6. Добавить опыт")
        print("0. Выход")

    # ================= MAIN LOOP =================

    def run(self) -> None:

        while True:

            self.show_menu()

            try:
                choice = int(input("Выберите пункт: "))

                match choice:

                    case 1:
                        self.show_players_ui()

                    case 2:
                        self.add_player_ui()

                    case 3:
                        self.find_player_ui()

                    case 4:
                        self.delete_player_ui()

                    case 5:
                        self.sort_by_power_ui()

                    case 6:
                        self.add_exp_ui()

                    case 0:
                        print("Выход...")
                        break

                    case _:
                        print("Неверный пункт меню.")

            except ValueError:
                print("Ошибка: введите число.")

    # ================= ADD =================

    def add_player_ui(self) -> None:

        try:

            player_type = input(
                "Тип игрока (1-обычный, 2-premium): "
            )

            name = input("Имя: ")

            health = int(input("Здоровье: "))

            level = int(input("Уровень: "))

            exp = int(input("Опыт: "))

            if player_type == "2":

                bonus = int(input("VIP бонус: "))

                player = PremiumPlayer(
                    name,
                    health,
                    level,
                    exp,
                    bonus
                )

            else:

                player = Player(
                    name,
                    health,
                    level,
                    exp
                )

            self.app.add_player(player)

            print("Игрок успешно добавлен.")

        except ValueError:
            print("Ошибка ввода данных.")

        except DuplicatePlayerError as error:
            print(error)

    # ================= SHOW =================

    def show_players_ui(self) -> None:

        players = self.app.get_all_players()

        if not players:
            print("Коллекция пуста.")
            return

        print("\n===== PLAYERS =====")

        for player in players:

            print(
                f"{player.name:<15}"
                f" lvl={player.level:<5}"
                f" hp={player.health:<5}"
                f" power={player.calculate_power()}"
            )

    # ================= FIND =================

    def find_player_ui(self) -> None:

        name = input("Введите имя игрока: ")

        player = self.app.find_player(name)

        if player is None:
            print("Игрок не найден.")
            return

        print(player)

    # ================= DELETE =================

    def delete_player_ui(self) -> None:

        try:

            name = input("Введите имя игрока: ")

            confirm = input(
                f'Удалить "{name}"? (y/n): '
            )

            if confirm.lower() == "y":

                self.app.delete_player(name)

                print("Игрок удалён.")

        except PlayerNotFoundError as error:
            print(error)

    # ================= SORT =================

    def sort_by_power_ui(self) -> None:

        result = self.app.sort_players(4)

        if not result:
            print("Игроки отсутствуют.")
            return

        print("\n===== SORT BY POWER =====")

        for player in result:
            print(player)

    # ================= EXPERIENCE =================

    def add_exp_ui(self) -> None:

        try:

            name = input("Имя игрока: ")

            exp = int(input("Опыт: "))

            self.app.add_experience(name, exp)

            print("Опыт добавлен.")

        except ValueError:
            print("Введите число.")

        except PlayerNotFoundError as error:
            print(error)