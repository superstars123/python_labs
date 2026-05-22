from typing import Optional

from lab04.models import Player, PremiumPlayer
from lab05.strategies import (
    by_name,
    by_level,
    by_health,
    by_power,
    make_level_filter
)

from lab06.container import TypedCollection

from exceptions import (
    PlayerNotFoundError,
    DuplicatePlayerError
)


class GameApp:
    """Бизнес-логика приложения."""

    def __init__(self) -> None:
        self.players: TypedCollection[Player] = TypedCollection()

    # ================= LOAD =================

    def load_players(self, players: list[Player]) -> None:
        """Загрузка игроков в коллекцию."""

        for player in players:
            self.players.add(player)

    # ================= CRUD =================

    def add_player(self, player: Player) -> None:
        """Добавление игрока."""

        existing = self.find_player(player.name)

        if existing is not None:
            raise DuplicatePlayerError(
                "Игрок с таким именем уже существует."
            )

        self.players.add(player)

    def get_all_players(self) -> list[Player]:
        """Получить всех игроков."""

        return self.players.get_all()

    def find_player(self, name: str) -> Optional[Player]:
        """Поиск игрока по имени."""

        return self.players.find(
            lambda x: x.name.lower() == name.lower()
        )

    def delete_player(self, name: str) -> None:
        """Удаление игрока."""

        player = self.find_player(name)

        if player is None:
            raise PlayerNotFoundError("Игрок не найден.")

        self.players.remove(player)

    # ================= FILTER =================

    def filter_by_level(self, min_level: int) -> list[Player]:
        """Фильтрация по уровню."""

        strategy = make_level_filter(min_level)

        return self.players.filter(strategy)

    # ================= SORT =================

    def sort_players(self, mode: int) -> list[Player]:
        """Сортировка игроков."""

        players = self.players.get_all()

        if mode == 1:
            return sorted(players, key=by_name)

        if mode == 2:
            return sorted(players, key=by_level)

        if mode == 3:
            return sorted(players, key=by_health)

        if mode == 4:
            return sorted(players, key=by_power)

        return players

    # ================= ACTIONS =================

    def add_experience(
        self,
        name: str,
        exp: int
    ) -> None:
        """Добавить опыт игроку."""

        player = self.find_player(name)

        if player is None:
            raise PlayerNotFoundError("Игрок не найден.")

        player.add_experience(exp)