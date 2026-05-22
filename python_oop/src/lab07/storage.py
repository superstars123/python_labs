from lab04.models import Player, PremiumPlayer
import json


def save(players: list, filepath: str) -> None:
    """Сохранение игроков в JSON."""

    data = []

    for player in players:

        if isinstance(player, PremiumPlayer):
            player_type = "PremiumPlayer"

        else:
            player_type = "Player"

        data.append({
            "type": player_type,
            "name": player.name,
            "health": player.health,
            "level": player.level,
            "exp": player._exp
        })

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load(filepath: str) -> list:
    """Загрузка игроков из JSON."""
    
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        players = []

        for item in data:

            if item["type"] == "PremiumPlayer":
                player = PremiumPlayer(
                    item["name"],
                    item["health"],
                    item["level"],
                    item["exp"]
                )

            else:
                player = Player(
                    item["name"],
                    item["health"],
                    item["level"],
                    item["exp"]
                )

            players.append(player)

        return players

    except FileNotFoundError:
        return []