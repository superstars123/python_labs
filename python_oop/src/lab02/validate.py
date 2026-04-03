def check_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    return name

def check_health(hp):
    if not isinstance(hp, int):
        raise TypeError("HP должен быть int")
    if hp < 0:
        raise ValueError("HP не может быть < 0")
    return hp

def check_level(lvl):
    if not isinstance(lvl, int):
        raise TypeError("Level должен быть int")
    if not (1 <= lvl <= 100):
        raise ValueError("Level должен быть 1-100")
    return lvl

def check_exp(exp):
    if not isinstance(exp, int):
        raise TypeError("Exp должен быть int")
    if exp < 0:
        raise ValueError("Exp не может быть < 0")
    return exp
