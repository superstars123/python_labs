def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    return name


def validate_health(health):
    if not isinstance(health, int):
        raise TypeError("Здоровье должно быть целым числом")
    if health < 0:
        raise ValueError("Здоровье не может быть отрицательным")
    return health


def validate_level(level):
    if not isinstance(level, int):
        raise TypeError("Уровень должен быть целым числом")
    if level <= 0 or level > 100:
        raise ValueError("Уровень должен быть от 1 до 100")
    return level


def validate_experience(exp):
    if not isinstance(exp, int):
        raise TypeError("Опыт должен быть целым числом")
    if exp < 0:
        raise ValueError("Опыт не может быть отрицательным")
    return exp