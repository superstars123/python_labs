from validate import check_name, check_health, check_level, check_exp

class Player:
    MAX_LEVEL = 100
    EXP_TO_LEVEL = 100

    # ------------------- Конструктор -------------------
    def __init__(self, name, health, level, exp):
        self._name = check_name(name)
        self._health = check_health(health)
        self._level = check_level(level)
        self._exp = check_exp(exp)
        self._alive = True

    # ------------------- Магические методы -------------------
    def __str__(self):
        status = "Жив" if self._alive else "Мертв"
        return f"{self._name} | lvl={self._level} | hp={self._health} | {status}"

    def __repr__(self):
        return f"Player(name='{self._name}', level={self._level}, hp={self._health})"

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return (self._name, self._level, self._health) == (other._name, other._level, other._health)

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        # Сортировка сначала по уровню, затем по опыту
        return (self._level, self._exp) < (other._level, other._exp)

    # ------------------- Свойства -------------------
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = check_health(value)
        if self._health == 0:
            self._alive = False

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._exp

    @property
    def active(self):
        return self._alive

    # ------------------- Внутренние методы -------------------
    def _level_up(self):
        if self._level >= Player.MAX_LEVEL:
            return
        self._level += 1
        print(f"{self._name} повысил уровень до {self._level}")

    # ------------------- Бизнес-методы -------------------
    def take_damage(self, dmg):
        if not self._alive:
            raise ValueError("Нельзя нанести урон мертвому игроку")
        if dmg < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= dmg
        if self._health <= 0:
            self._health = 0
            self._alive = False
            print(f"{self._name} погиб")

    def gain_experience(self, value):
        if not self._alive:
            raise ValueError("Мертвый игрок не получает опыт")
        if value < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._exp += value
        while self._exp >= Player.EXP_TO_LEVEL:
            if self._level >= Player.MAX_LEVEL:
                self._exp = 0
                break
            self._exp -= Player.EXP_TO_LEVEL
            self._level_up()

    def revive(self):
        if self._alive:
            raise ValueError("Игрок уже активен")
        self._health = 100
        self._alive = True
        print(f"{self._name} воскрешен")