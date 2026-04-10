from model import Player, Enemy, PremiumPlayer
# ===== Коллекция =====
def print_header(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


class CharacterCollection:
    def __init__(self):
        self.characters = []

    def add(self, character):
        self.characters.append(character)

    def show_all(self):
        for c in self.characters:
            print(c)

    def process_all(self):
        for c in self.characters:
            print(c.process())

    def get_by_type(self, cls):
        return [c for c in self.characters if isinstance(c, cls)]

    def count_by_type(self):
        result = {}
        for c in self.characters:
            t = c.get_type()
            result[t] = result.get(t, 0) + 1
        return result


# СЦЕНАРИЙ 1: НАСЛЕДОВАНИЕ

def scenario_1():
    print_header("СЦЕНАРИЙ 1: НАСЛЕДОВАНИЕ")
    # ===== Игроки =====
    p1 = Player("Маша", 100, 5, 150, [])
    p2 = Player("Виктория", 120, 7, 300, [])
    p3 = Player("Иван", 90, 4, 80, [])

    # ===== Враг =====
    e1 = Enemy("Гоблин", 50, 2, 10, "common")

    # ===== VIP игрок =====
    vip = PremiumPlayer("Король", 500, 15, 1000, vip_bonus=200)

    print("\n1. Игроки:")
    print(f"[Игрок] {p1}")
    print(f"[Игрок] {p2}")
    print(f"[Игрок] {p3}")

    print("\n2. Враг:")
    print(f"[Враг] {e1}")

    print("\n3. Премиум игрок:")
    print(f"[VIP] {vip}")


# СЦЕНАРИЙ 2: ПОЛИМОРФИЗМ

def scenario_2():
    print_header("СЦЕНАРИЙ 2: ПОЛИМОРФИЗМ")

    collection = CharacterCollection()

    collection.add(Player("Маша", 100, 5, 150, []))
    collection.add(Player("Виктория", 120, 7, 300, []))
    collection.add(Player("Иван", 90, 4, 80, []))

    collection.add(Enemy("Гоблин", 80, 3, 20, "rare"))
    collection.add(Enemy("Дракон", 150, 6, 50, "epic"))

    collection.add(PremiumPlayer("Король", 300, 8, 400, vip_bonus=100))

    print("\nКоллекция:")
    collection.show_all()

    # --- isinstance ---
    print("\n1. Типы через isinstance():")
    for c in collection.characters:
        if isinstance(c, PremiumPlayer):
            print(f"{c.name}: Премиум")
        elif isinstance(c, Enemy):
            print(f"{c.name}: Враг")
        elif isinstance(c, Player):
            print(f"{c.name}: Игрок")
            

    # --- Полиморфизм ---
    print("\n2. Полиморфный calculate_power():")
    for c in collection.characters:
        print(f"{c.name}: {c.calculate_power()}")


# СЦЕНАРИЙ 3: ИНТЕРФЕЙС + КОЛЛЕКЦИЯ

def scenario_3():
    print_header("СЦЕНАРИЙ 3: ИНТЕРФЕЙС + КОЛЛЕКЦИЯ")

    collection = CharacterCollection()

    # игроки
    collection.add(Player("Маша", 100, 5, 150, []))
    collection.add(Player("Виктория", 120, 7, 300, []))
    collection.add(Player("Иван", 90, 4, 80, []))

    # другие сущности
    collection.add(Enemy("Гоблин", 50, 2, 10, "common"))
    collection.add(PremiumPlayer("Король", 500, 15, 1000, vip_bonus=200))

    print("\n--- process() для всех (полиморфизм) ---")
    collection.process_all()

    print("\n--- Фильтрация Player ---")
    players = collection.get_by_type(Player)
    for p in players:
        print(p)

    print("\n--- Фильтрация Enemy ---")
    enemies = collection.get_by_type(Enemy)
    for e in enemies:
        print(e)

    print("\n--- Подсчёт типов ---")
    print(collection.count_by_type())


# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()