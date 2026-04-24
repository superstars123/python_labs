from lab04.interfaces import Printable, Comparable, Damageable


from lab03.model import Player as BasePlayer
from lab03.model import Enemy as BaseEnemy
from lab03.model import PremiumPlayer as BasePremiumPlayer


# ================= PLAYER =================
class Player(BasePlayer, Printable, Comparable, Damageable):
    """
    Игрок с поддержкой интерфейсов
    """

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other):
        return self.calculate_power() - other.calculate_power()


# ================= ENEMY =================
class Enemy(BaseEnemy, Printable, Comparable, Damageable):
    """
    Враг с интерфейсами
    """

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not hasattr(other, "calculate_power"):
            raise TypeError("Объект нельзя сравнить")
        return self.calculate_power() - other.calculate_power()


# ================= PREMIUM PLAYER =================
class PremiumPlayer(BasePremiumPlayer, Printable, Comparable, Damageable):
    """
    VIP игрок с интерфейсами
    """

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not hasattr(other, "calculate_power"):
            raise TypeError("Объект нельзя сравнить")
        return self.calculate_power() - other.calculate_power()