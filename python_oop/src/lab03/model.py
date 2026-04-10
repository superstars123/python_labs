from validate import check_name, check_health, check_level, check_exp

from base import Character
# ================= БАЗОВЫЙ КЛАСС =================
class Player:
    MAX_LEVEL = 100
    EXP_TO_LEVEL = 100

    def __init__(self, name, health, level, exp, inventory=None):
        self._name = check_name(name)
        self._health = check_health(health)
        self._level = check_level(level)
        self._exp = check_exp(exp)
        self._inventory = inventory or []
        self._alive = True

    # ---------------- Магические методы ----------------
    def __str__(self):
        status = "Жив" if self._alive else "Мертв"
        return f"{self._name} | lvl={self._level} | hp={self._health} | {status}"

    def __repr__(self):
        return f"Player(name='{self._name}', level={self._level}, hp={self._health})"

    # ---------------- Свойства ----------------
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._exp

    @property
    def active(self):
        return self._alive

    # ---------------- Базовые методы ----------------
    def calculate_power(self):
        return self._level * 10 + self._exp

    def process(self):
        return f"{self._name}: power = {self.calculate_power()}"

    def get_type(self):
        return self.__class__.__name__

    # ---------------- Логика ----------------
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
            self._level += 1
            print(f"{self._name} повысил уровень до {self._level}")

    def revive(self):
        if self._alive:
            raise ValueError("Игрок уже активен")
        self._health = 100
        self._alive = True
        print(f"{self._name} воскрешен")


# ================= ВРАГ =================
class Enemy(Player):
    def __init__(self, name, health, level, damage, rarity):
        super().__init__(name, health, level, exp=0)
        self._damage = damage
        self._rarity = rarity

    def attack(self):
        return self._damage

    # полиморфизм
    def calculate_power(self):
        return self._damage * self._level

    def __str__(self):
        return f"Enemy {self._name} | dmg={self._damage} | lvl={self._level}"

    def process(self):
        return f"{self._name} attacks with power {self.calculate_power()}"


# ================= ПРЕМИУМ ИГРОК =================
class PremiumPlayer(Player):
    def __init__(self, name, health, level, exp, vip_bonus=0):
        super().__init__(name, health, level, exp)
        self._vip_bonus = vip_bonus

    # переопределение
    def calculate_power(self):
        base = super().calculate_power()
        if self._level > 10:
            base += self._vip_bonus
        return base

    def __str__(self):
        return f"[VIP] {self._name} | lvl={self._level} | bonus={self._vip_bonus}"

    def process(self):
        return f"{self._name} VIP power = {self.calculate_power()}"