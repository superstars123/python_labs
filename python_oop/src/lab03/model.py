from lab03.validate import (
    check_name,
    check_health,
    check_level,
    check_exp
)

from lab03.base import Character


# ================= PLAYER =================
class Player(Character):

    MAX_LEVEL = 100
    EXP_TO_LEVEL = 100

    def __init__(
        self,
        name,
        health,
        level,
        exp,
        inventory=None
    ):
        super().__init__(name, health, level)

        self._exp = check_exp(exp)

        self._inventory = (
            inventory if inventory is not None else []
        )

    # ================= EXPERIENCE =================

    def add_experience(self, value):

        if value < 0:
            raise ValueError(
                "Опыт не может быть отрицательным"
            )

        self._exp += value

        while self._exp >= Player.EXP_TO_LEVEL:

            if self.level >= Player.MAX_LEVEL:
                self._exp = 0
                break

            self._exp -= Player.EXP_TO_LEVEL
            self._level += 1

    # ================= POWER =================

    def calculate_power(self):

        base_power = self.level * 10

        exp_bonus = self._exp

        return base_power + exp_bonus

    # ================= SERIALIZATION =================

    def to_dict(self):

        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "health": self.health,
            "level": self.level,
            "exp": self._exp
        }

    @staticmethod
    def from_dict(data):

        return Player(
            data["name"],
            data["health"],
            data["level"],
            data["exp"]
        )

    # ================= OTHER =================

    def process(self):

        return (
            f"Player {self.name}: "
            f"power = {self.calculate_power()}"
        )

    def __str__(self):

        return (
            f"Player {self.name} | "
            f"lvl={self.level} | "
            f"hp={self.health} | "
            f"exp={self._exp}"
        )


# ================= ENEMY =================
class Enemy(Character):

    def __init__(
        self,
        name,
        health,
        level,
        damage,
        rarity
    ):
        super().__init__(name, health, level)

        self._damage = damage
        self._rarity = rarity

    def attack(self):
        return self._damage

    def calculate_power(self):

        return self._damage * self.level

    # ================= SERIALIZATION =================

    def to_dict(self):

        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "health": self.health,
            "level": self.level,
            "damage": self._damage,
            "rarity": self._rarity
        }

    @staticmethod
    def from_dict(data):

        return Enemy(
            data["name"],
            data["health"],
            data["level"],
            data["damage"],
            data["rarity"]
        )

    # ================= OTHER =================

    def process(self):

        return (
            f"Enemy {self.name} attacks "
            f"with power {self.calculate_power()}"
        )

    def get_rarity(self):

        return self._rarity

    def __str__(self):

        return (
            f"Enemy {self.name} | "
            f"dmg={self._damage} | "
            f"lvl={self.level} | "
            f"rarity={self._rarity}"
        )


# ================= PREMIUM PLAYER =================
class PremiumPlayer(Character):

    def __init__(
        self,
        name,
        health,
        level,
        exp,
        vip_bonus=0
    ):
        super().__init__(name, health, level)

        self._exp = check_exp(exp)

        self._vip_bonus = vip_bonus

    # ================= POWER =================

    def calculate_power(self):

        base = self.level * 10 + self._exp

        if self.level >= 10:
            base += self._vip_bonus

        return base

    # ================= VIP =================

    def add_vip_bonus(self, value):

        if value < 0:
            raise ValueError(
                "VIP бонус не может быть отрицательным"
            )

        self._vip_bonus += value

    # ================= SERIALIZATION =================

    def to_dict(self):

        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "health": self.health,
            "level": self.level,
            "exp": self._exp,
            "vip_bonus": self._vip_bonus
        }

    @staticmethod
    def from_dict(data):

        return PremiumPlayer(
            data["name"],
            data["health"],
            data["level"],
            data["exp"],
            data["vip_bonus"]
        )

    # ================= OTHER =================

    def process(self):

        return (
            f"VIP Player {self.name}: "
            f"power = {self.calculate_power()}"
        )

    def __str__(self):

        return (
            f"[VIP] {self.name} | "
            f"lvl={self.level} | "
            f"exp={self._exp} | "
            f"bonus={self._vip_bonus}"
        )# from lab03.validate import check_name, check_health, check_level, check_exp
# from lab03.base import Character


# # ================= PLAYER =================
# class Player(Character):
#     MAX_LEVEL = 100
#     EXP_TO_LEVEL = 100

#     def __init__(self, name, health, level, exp, inventory=None):
#         super().__init__(name, health, level)

#         self._exp = check_exp(exp)
#         self._inventory = inventory if inventory is not None else []

#     # -------- experience logic --------
#     def add_experience(self, value):
#         if value < 0:
#             raise ValueError("Опыт не может быть отрицательным")

#         self._exp += value

#         while self._exp >= Player.EXP_TO_LEVEL:
#             if self.level >= Player.MAX_LEVEL:
#                 self._exp = 0
#                 break

#             self._exp -= Player.EXP_TO_LEVEL
#             self._level += 1

#     # -------- override --------
#     def calculate_power(self):
#         base_power = self.level * 10
#         exp_bonus = self._exp
#         return base_power + exp_bonus

#     def process(self):
#         return f"Player {self.name}: power = {self.calculate_power()}"


# # ================= ENEMY =================
# class Enemy(Character):
#     def __init__(self, name, health, level, damage, rarity):
#         super().__init__(name, health, level)

#         self._damage = damage
#         self._rarity = rarity

#     def attack(self):
#         return self._damage

#     def calculate_power(self):
#         # враг считается иначе — через урон
#         return self._damage * self.level

#     def process(self):
#         return f"Enemy {self.name} attacks with power {self.calculate_power()}"

#     def get_rarity(self):
#         return self._rarity

#     def __str__(self):
#         return f"Enemy {self.name} | dmg={self._damage} | lvl={self.level} | rarity={self._rarity}"


# # ================= PREMIUM PLAYER =================
# class PremiumPlayer(Character):
#     def __init__(self, name, health, level, exp, vip_bonus=0):
#         super().__init__(name, health, level)

#         self._exp = check_exp(exp)
#         self._vip_bonus = vip_bonus

#     def calculate_power(self):
#         base = self.level * 10 + self._exp

#         # VIP бонус только для прокачанных игроков
#         if self.level >= 10:
#             base += self._vip_bonus

#         return base

#     def add_vip_bonus(self, value):
#         if value < 0:
#             raise ValueError("VIP бонус не может быть отрицательным")
#         self._vip_bonus += value

#     def process(self):
#         return f"VIP Player {self.name}: power = {self.calculate_power()}"

#     def __str__(self):
#         return f"[VIP] {self.name} | lvl={self.level} | exp={self._exp} | bonus={self._vip_bonus}"

