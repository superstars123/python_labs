
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lab04.models import Player, Enemy, PremiumPlayer
from lab02.collection import PlayerCollection
from lab04.interfaces import Printable, Comparable


def header(text):
    print("\n" + "=" * 60)
    print(f" {text}")
    print("=" * 60)


# ========== СЦЕНАРИЙ 1: ПРОВЕРКА ИНТЕРФЕЙСОВ ==========
def scenario1():
    header("СЦЕНАРИЙ 1: ПРОВЕРКА ИНТЕРФЕЙСОВ")

    p1 = Player("Иван", 100, 5, 50)
    p2 = PremiumPlayer("Анна", 120, 10, 80, vip_bonus=20)
    e1 = Enemy("Сергей", 80, 3, damage=15, rarity="обычный")

    objects = [p1, p2, e1]

    print("1. Проверка isinstance:")
    for obj in objects:
        interfaces = []
        if isinstance(obj, Printable):
            interfaces.append("Printable")
        if isinstance(obj, Comparable):
            interfaces.append("Comparable")
        print(f"   {obj.name}: {', '.join(interfaces)}")

    print("\n2. Вызов to_string():")
    for obj in objects:
        print(f"   {obj.to_string()}")

    print("\n3. Сравнение через compare_to():")
    print(f"   Иван vs Анна: {p1.compare_to(p2)}")
    print(f"   Анна vs Сергей: {p2.compare_to(e1)}")


# ========== СЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП ==========
def scenario2():
    header("СЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП")

    coll = PlayerCollection()
    coll.add(Player("Олег", 90, 4, 30))
    coll.add(PremiumPlayer("Марина", 130, 12, 90, vip_bonus=25))
    coll.add(Enemy("Дмитрий", 70, 2, damage=10, rarity="редкий"))

    def print_all(items: list[Printable]):
        for item in items:
            print(f"   {item.to_string()}")

    def find_max(items: list[Comparable]):
        if not items:
            return None
        max_item = items[0]
        for item in items[1:]:
            if item.compare_to(max_item) > 0:
                max_item = item
        return max_item

    print("1. Вывод через Printable:")
    print_all(coll.get_printable())

    print("\n2. Поиск самого сильного:")
    best = find_max(coll.get_comparable())
    print(f"   Лучший: {best.to_string()}")


# ========== СЦЕНАРИЙ 3: ПОЛИМОРФИЗМ ==========
def scenario3():
    header("СЦЕНАРИЙ 3: ПОЛИМОРФИЗМ")

    coll = PlayerCollection()
    coll.add(Player("Игорь", 100, 5, 50))
    coll.add(PremiumPlayer("Ольга", 150, 15, 100, vip_bonus=30))
    coll.add(Enemy("Павел", 80, 4, damage=20, rarity="редкий"))

    print("1. Исходная коллекция:")
    coll.print_all()

    print("\n2. Сортировка по силе:")
    coll.sort_by_comparable()
    coll.print_all()

    print("\n3. Полиморфизм (разное поведение):")
    for obj in coll:
        print(f"   {obj.to_string()}")


# ========== СЦЕНАРИЙ 4: ИНТЕГРАЦИЯ С ЛР-2 ==========
def scenario4():
    header("СЦЕНАРИЙ 4: ИНТЕГРАЦИЯ С ЛР-2")

    coll = PlayerCollection()
    coll.add(Player("Алексей", 100, 5, 50))
    coll.add(Player("Никита", 60, 2, 10))
    coll.add(PremiumPlayer("Екатерина", 140, 12, 80, vip_bonus=20))
    coll.add(Enemy("Виктор", 90, 6, damage=25, rarity="эпический"))

    print("1. Фильтрация по интерфейсам:")
    print(f"   Printable: {len(coll.get_printable())}")
    print(f"   Comparable: {len(coll.get_comparable())}")

    print("\n2. Вывод всех объектов:")
    coll.print_all()

    print("\n3. Методы из ЛР-2:")
    print(f"   Всего объектов: {len(coll)}")
    print(f"   Высокий уровень (>=5): {len(coll.get_high_level(5))}")

    print("\n4. Общая сила всех:")
    total = sum(obj.calculate_power() for obj in coll)
    print(f"   Общая сила: {total}")


# ========== СЦЕНАРИЙ 5: АРХИТЕКТУРНОЕ ПОВЕДЕНИЕ ==========
def scenario5():
    header("СЦЕНАРИЙ 5: АРХИТЕКТУРНОЕ ПОВЕДЕНИЕ")

    coll = PlayerCollection()
    coll.add(Player("Степан", 80, 3, 20))
    coll.add(PremiumPlayer("Мария", 160, 14, 100, vip_bonus=40))
    coll.add(Enemy("Андрей", 100, 7, damage=30, rarity="легендарный"))

    print("1. Исходные значения силы:")
    for obj in coll:
        print(f"   {obj.name}: {obj.calculate_power()}")

    print("\n2. Поиск самого сильного:")
    best = max(coll, key=lambda x: x.calculate_power())
    print(f"   Лучший: {best.name}")

    print("\n3. Сортировка по убыванию:")
    coll.sort_by_comparable()
    coll._items.reverse()
    coll.print_all()

    print("\n4. Полиморфный вывод:")
    for obj in coll.get_printable():
        print(f"   {obj.to_string()}")


def main():
    print("=" * 60)
    print(" ЛР-4: ИГРОВАЯ ЛОГИКА (ИНТЕРФЕЙСЫ)")
    print("=" * 60)

    scenario1()
    input("\n>>> Enter...")

    scenario2()
    input("\n>>> Enter...")

    scenario3()
    input("\n>>> Enter...")

    scenario4()
    input("\n>>> Enter...")

    scenario5()

    print("\n" + "=" * 60)
    print(" ВСЕ СЦЕНАРИИ ВЫПОЛНЕНЫ!")
    print("=" * 60)


if __name__ == "__main__":
    main()