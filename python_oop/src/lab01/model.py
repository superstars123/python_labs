from validate import (
    validate_name,
    validate_health,
    validate_level,
    validate_experience
)
class Player:
    MAX_LEVEL = 100  # атрибут класса

    def __init__(self, name: str, health: int, level: int, experience: int):
        self._name = validate_name(name)
        self._health = validate_health(health)
        self._level = validate_level(level)
        self._experience = validate_experience(experience)
        self._active = True  # логическое состояние игрока

    # ------------------- properties -------------------
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = validate_health(value)
        if self._health <= 0:
            self._active = False

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    @property
    def active(self):
        return self._active

    # ------------------- magic methods -------------------
    def __str__(self):
        status = "Активен" if self._active else "Неактивен"
        return f"Игрок {self._name} | Уровень: {self._level} | HP: {self._health} | {status}"

    def __repr__(self):
        return f"Player(name='{self._name}', level={self._level})"

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self._name == other._name and self._level == other._level

    # ------------------- бизнес-методы -------------------
    def take_damage(self, damage: int):
        if not self._active:
            raise ValueError("Игрок неактивен")
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")

        self._health -= damage
        if self._health <= 0:
            self._health = 0
            self._active = False

    def gain_experience(self, amount: int):
        if not self._active:
            raise ValueError("Игрок неактивен")
        if amount < 0:
            raise ValueError("Опыт не может быть отрицательным")

        self._experience += amount
        while self._experience >= 100:
            if self._level >= Player.MAX_LEVEL:
                self._experience = 0
                break
            self._experience -= 100
            self._level += 1

    def revive(self):
        if self._active:
            raise ValueError("Игрок уже активен")
        self._health = 100
        self._active = True