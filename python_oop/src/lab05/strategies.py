"""
Стратегии для ЛР-5
"""

# ===== SORT STRATEGIES =====

def by_name(x):
    return x.name


def by_level(x):
    return x.level


def by_health(x):
    return x.health


def by_power(x):
    return x.calculate_power()


# ===== FILTERS =====

def high_level(x):
    return x.level >= 10


def low_health(x):
    return x.health < 100


# ===== FACTORY =====

def make_level_filter(min_level):
    def f(x):
        return x.level >= min_level
    return f


# ===== ACTIONS =====

def level_up(x):
    x.level += 1
    return x


def heal(x):
    x.health += 50
    return x


# ===== CALLABLE STRATEGY =====

class BoostStrategy:
    def __init__(self, bonus):
        self.bonus = bonus

    def __call__(self, x):
        x.health += self.bonus
        return x