"""
ЛР-6 — Generics, TypeVar, Protocol
Игровая система персонажей
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lab06.container import TypedCollection, D, S
from lab03.model import Player, Enemy, PremiumPlayer

# ================= HELPER =================

def title(text: str) -> None:
    print("\n" + "=" * 70)
    print(text.center(70))
    print("=" * 70)


def generate_game_units():
    return [
        Player("Steve", 120, 8, 250),
        Player("End Hunter", 90, 6, 180),

        Enemy("Zombie", 70, 4, 20, "common"),
        Enemy("Wither", 250, 18, 65, "epic"),

        PremiumPlayer("Diamond Knight", 160, 20, 900, 350),
        PremiumPlayer("Nether Lord", 140, 16, 700, 250)
    ]



# ================= SCENARIO 1 =================

def scenario_annotations():
    title("СЦЕНАРИЙ 1 — TYPE ANNOTATIONS")

    unit = Player("Tester", 100, 5, 200)

    print("Создан объект Player")
    print(unit)

    print("\nАннотированы:")
    print("- параметры конструктора")
    print("- возвращаемые значения")
    print("- атрибуты класса")

    print("\n✓ typing используется во всех моделях")


# ================= SCENARIO 2 =================

def scenario_generic_collection():
    title("СЦЕНАРИЙ 2 — GENERIC COLLECTION")

    inventory: TypedCollection[str] = TypedCollection()

    inventory.add("Attack")
    inventory.add("Defense")
    inventory.add("Healing")


    print("Игровой инвентарь:")
    print(inventory.get_all())

    levels: TypedCollection[int] = TypedCollection()

    levels.add(5)
    levels.add(10)
    levels.add(15)

    print("\nУровни:")
    print(levels.get_all())

    game_units = TypedCollection()

    for obj in generate_game_units()[:3]:
        game_units.add(obj)

    print(
        f"\nВ коллекции персонажей: "
        f"{len(game_units)} объектов"
    )

    print("✓ Generic-класс работает с разными типами")


# ================= SCENARIO 3 =================

def scenario_find_filter_map():
    title("СЦЕНАРИЙ 3 — FIND / FILTER / MAP")

    collection = TypedCollection()

    for obj in generate_game_units():
        collection.add(obj)

    # ===== FIND =====

    boss = collection.find(
        lambda x: x.score() > 800
    )

    print("find():")

    if boss:
        print(f"Найден сильный персонаж -> {boss.name}")
    else:
        print("Ничего не найдено")

    # ===== FIND NONE =====

    impossible = collection.find(
        lambda x: x.score() > 999999
    )

    print(f"\nfind(None): {impossible}")

    # ===== FILTER =====

    elite_units = collection.filter(
        lambda x: x.level >= 15
    )

    print("\nfilter():")

    for unit in elite_units:
        print(f"- {unit.name} | level={unit.level}")

    # ===== MAP =====

    names = collection.map(
        lambda x: x.name
    )

    powers = collection.map(
        lambda x: x.score()
    )

    print("\nmap() -> list[str]")
    print(names)

    print("\nmap() -> list[float]")
    print(powers)

    print("\n✓ map() возвращает другой тип данных")


# ================= SCENARIO 4 =================

def scenario_displayable():
    title("СЦЕНАРИЙ 4 — PROTOCOL DISPLAYABLE")

    units: TypedCollection[D] = TypedCollection()

    units.add(Player("Knight", 110, 9, 300))
    units.add(Enemy("Orc", 180, 11, 40, "rare"))
    units.add(PremiumPlayer("VIP_King", 200, 25, 1500, 500))

    print("Все объекты имеют метод display():")

    for obj in units.get_all():
        print(obj.display())

    print(
        "\n✓ Protocol работает через структурную типизацию"
    )


# ================= SCENARIO 5 =================

def scenario_scorable():
    title("СЦЕНАРИЙ 5 — PROTOCOL SCORABLE")

    ranked_units: TypedCollection[S] = TypedCollection()

    for obj in generate_game_units():
        ranked_units.add(obj)

    print("Подсчёт score() для объектов:\n")

    for obj in ranked_units.get_all():
        print(
            f"{obj.name:<15} -> "
            f"{obj.score():.2f}"
        )

    print(
        "\n✓ TypedCollection поддерживает "
        "разные Protocol-ограничения"
    )


# ================= MAIN =================

def main():
    print("\n" + "#" * 70)
    print("LABORATORY WORK №6".center(70))
    print("GENERICS • TYPING • PROTOCOL".center(70))
    print("#" * 70)

    scenario_annotations()
    scenario_generic_collection()
    scenario_find_filter_map()
    scenario_displayable()
    scenario_scorable()


if __name__ == "__main__":
    main()