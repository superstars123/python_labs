
import sys
import os

from src.lab05.collection import PlayerCollection
import src.lab05.strategies as st
from src.lab03.base import Character


def print_section(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


# ========== СОЗДАНИЕ КОЛЛЕКЦИИ ==========

def create_collection():
    col = PlayerCollection()

    col.add(Character("Маша", 100, 5))
    col.add(Character("Иван", 90, 12))
    col.add(Character("Анна", 80, 2))
    col.add(Character("Гоблин", 70, 4))
    col.add(Character("Король", 500, 20))


    return col


# ========== СЦЕНАРИЙ 1: SORT ==========

def scenario_sorting(col):
    print_section("СЦЕНАРИЙ 1: СОРТИРОВКА")

    print("По здоровью:")
    for p in col.sort_by(lambda x: x.health):
        print(f"   {p.name}: {p.health}")

    print("\nПо силе:")
    for p in col.sort_by(lambda x: x.power):
        print(f"   {p.name}: {p.power}")

    print("\nПо имени:")
    for p in col.sort_by(lambda x: x.name):
        print(f"   {p.name}")


# ========== СЦЕНАРИЙ 2: FILTER ==========

def scenario_filtering(col):
    print_section("СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ")

    strong = col.filter_by(lambda x: x.power >= 10)
    print("Сильные игроки (power >= 10):")
    for p in strong:
        print(f"   {p.name}: {p.power}")

    weak = col.filter_by(lambda x: x.health < 100)
    print("\nСлабые игроки (health < 100):")
    for p in weak:
        print(f"   {p.name}: {p.health}")


# ========== СЦЕНАРИЙ 3: MAP ==========

def scenario_map(col):
    print_section("СЦЕНАРИЙ 3: MAP")

    names = list(map(lambda x: x.name, col))
    print("Имена игроков:")
    print(names)

    powers = list(map(lambda x: x.power, col))
    print("\nСилы игроков:")
    print(powers)


# ========== СЦЕНАРИЙ 4: ЦЕПОЧКА ==========

def scenario_chain(col):
    print_section("СЦЕНАРИЙ 4: FILTER → SORT → APPLY")

    res = col.filter_by(lambda x: x.power >= 5)
    print("После filter (power >= 5):")
    for p in res:
        print(f"   {p.name}: {p.power}")

    res = res.sort_by(lambda x: x.health)
    print("\nПосле sort (по health):")
    for p in res:
        print(f"   {p.name}: {p.health}")

    res = res.apply(lambda x: x)
    print("\nПосле apply:")
    for r in res:
        print("   ", r)


# ========== СЦЕНАРИЙ 5: СТРАТЕГИИ ==========

def scenario_strategies(col):
    print_section("СЦЕНАРИЙ 5: СТРАТЕГИИ")

    boost = st.BoostStrategy(50)

    print("Boost стратегия:")
    for p in col:
        print(f"   {p.name}: {boost(p)}")


# ========== MAIN ==========

def main():
    print("\n" + "=" * 60)
    print("  ЛАБОРАТОРНАЯ РАБОТА: PLAYER + STRATEGIES")
    print("=" * 60)

    col = create_collection()
    print(f"\nСоздано игроков: {len(col)}")

    scenario_sorting(col)
    scenario_filtering(col)
    scenario_map(col)
    scenario_chain(col)
    scenario_strategies(col)


if __name__ == "__main__":
    main()
    