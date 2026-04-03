from model import Player
from collection import PlayerCollection


def create_players():
    p1 = Player(1, "Иван Иванович", 10, 100, 2000, "active")
    p2 = Player(2, "Ксения Никитична", 5, 80, 1200, "inactive")
    p3 = Player(3, "Максим Андреевич", 15, 60, 3000, "active")
    return p1, p2, p3


def scenario1():
    print("=== Сценарий 1: Базовые операции ===")

    players = PlayerCollection()
    p1, p2, p3 = create_players()

    players.add(p1)
    players.add(p2)
    players.add(p3)

    print("\nВсе игроки:")
    for p in players:
        print(p)

    print("\nУдаляем Ксения Никитична(remove)")
    players.remove(p2)

    print("\nПосле удаления:")
    for p in players:
        print(p)

    print("\nПроверка дубликата:")
    try:
        players.add(Player(1, "Дубликат", 1, 1, 1, "active"))
    except ValueError as e:
        print("Ошибка:", e)


def scenario2():
    print("\n=== Сценарий 2: Поиск и фильтрация ===")

    players = PlayerCollection()
    p1, p2, p3 = create_players()

    players.add(p1)
    players.add(p2)
    players.add(p3)

    print("\nПоиск по имени 'Иван Иванович'(find_by_name):")
    print(players.find_by_name("Иван Иванович"))

    print("\nПоиск по уровню 5-12:(find_by_level_range)")
    print(players.find_by_level_range(5, 12))

    print("\nАктивные игроки:(get_active)")
    print(players.get_active())

    print("\nНеактивные игроки:(get_inactive)")
    print(players.get_inactive())

    print("\nИгроки уровня >= 10:(get_high_level)")
    print(players.get_high_level(10))

    print("\nКоличество игроков:(len)", len(players))


def scenario3():
    print("\n=== Сценарий 3: Индексация и сортировка ===")

    players = PlayerCollection()
    p1, p2, p3 = create_players()

    players.add(p1)
    players.add(p2)
    players.add(p3)

    print("\nПервый игрок:")
    print(players[0])

    print("\nСрез [0:2]:")
    print(players[0:2])

    print("\nУдаление по индексу 1(remove)")
    players.remove_at(1)
    print(players)

    print("\nСортировка по уровню:(sort_by_leve)")
    print(players.sort_by_level())

    print("\nСортировка по имени:(sort_by_name)")
    print(players.sort_by_name())


def scenario4():
    print("\n=== Сценарий 4: Цепочки операций ===")

    players = PlayerCollection()
    p1, p2, p3 = create_players()

    # добавим ещё одного для интереса
    p4 = Player(4, "Алексей Сергеевич", 20, 120, 5000, "active")

    players.add(p1)
    players.add(p2)
    players.add(p3)
    players.add(p4)

    print("\nАктивные с высоким уровнем:(get_active.get_high_level)")
    print(players.get_active().get_high_level(10))

    print("\nПоиск 'Иван Иванович' + сортировка:(find_by_name.sort_by_level)")
    print(players.find_by_name("Иван Иванович").sort_by_level())

    print("\nВысокий уровень + срез:(get_high_leve)")
    print(players.get_high_level(10)[0:2])

    print("\nЦепочка фильтров:(get_active.get_high_level.sort_by_name)")
    print(players.get_active().get_high_level(10).sort_by_name())


if __name__ == "__main__":
    scenario1()
    scenario2()
    scenario3()
    scenario4()