class Player:
    def __init__(self, player_id: int, name: str, level: int, health: int, experience: int, status: str):
        self.id = player_id
        self.name = name
        self.level = level
        self.health = health
        self.experience = experience
        self.status = status  # "active" или "inactive"

    def __repr__(self):
        return (f"Player(id={self.id}, name='{self.name}', level={self.level}, "
                f"health={self.health}, exp={self.experience}, status='{self.status}')")