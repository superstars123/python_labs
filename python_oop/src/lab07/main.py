import sys
import os
import json
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from lab04.models import Player, Enemy, PremiumPlayer




# ================= DATA =================

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "players.json")


# ================= SAVE / LOAD =================

def save_players(players, filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    data = []
    for p in players:
        data.append({
            "type": p.__class__.__name__,
            "name": p.name,
            "health": p.health,
            "level": p.level,
            "exp": getattr(p, "_exp", 0),
        })

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_players(filepath: str):
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    players = []

    for item in data:
        t = item.get("type")

        if t == "PremiumPlayer":
            p = PremiumPlayer(
                item["name"],
                item["health"],
                item["level"],
                item["exp"]
            )
        else:
            p = Player(
                item["name"],
                item["health"],
                item["level"],
                item["exp"]
            )

        players.append(p)

    return players


# ================= GAME LOGIC =================

def print_players(players):
    if not players:
        print("\nНет игроков")
        return

    print("\n--- PLAYERS ---")
    for p in players:
        print(f"{p.name} | HP:{p.health} | LVL:{p.level} | POWER:{p.calculate_power()}")


def find_player(players, name):
    for p in players:
        if p.name.lower() == name.lower():
            return p
    return None


def sort_players(players, reverse=False):
    return sorted(players, key=lambda x: x.calculate_power(), reverse=reverse)


def add_demo_players():
    return [
        Player("Artem", 100, 5, 20),
        Player("Mira", 120, 7, 40),
        Enemy("Goblin", 80, 3, 15, "common"),
        Enemy("Dragon", 300, 10, 50, "legendary"),
        PremiumPlayer("VIP_King", 200, 12, 80, vip_bonus=30),
    ]


# ================= MAIN =================

def main():
    players = load_players(DATA_FILE)

    print(f"\nЗагружено игроков: {len(players)}")

    if not players:
        players = add_demo_players()

    while True:
        print("\n===== GAME MENU =====")
        print("1. Показать игроков")
        print("2. Добавить игрока")
        print("3. Найти игрока")
        print("4. Удалить игрока")
        print("5. Сортировка по силе")
        print("6. Добавить опыт")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        # -------- SHOW --------
        if choice == "1":
            print_players(players)

        # -------- ADD --------
        elif choice == "2":
            name = input("Имя: ")
            hp = int(input("HP: "))
            lvl = int(input("Level: "))
            exp = int(input("Exp: "))

            players.append(Player(name, hp, lvl, exp))
            print("Игрок добавлен;)")
            print_players(players)

        # -------- FIND --------
        elif choice == "3":
            name = input("Имя: ")
            p = find_player(players, name)

            if p:
                print(f"{p.name} | HP:{p.health} | LVL:{p.level} | EXP:{getattr(p,'_exp',0)} | POWER:{p.calculate_power()}")
            else:
                print("Не найден")
          

        # -------- DELETE --------
        elif choice == "4":
            name = input("Имя: ")
            p = find_player(players, name)

            if p:
                players.remove(p)
                print("Удалено")
            else:
                print("Не найден")
            print_players(players)

        # -------- SORT --------
        elif choice == "5":
            order = input("1-↑ 2-↓: ")
            players = sort_players(players, reverse=(order == "2"))
            print("Отсортировано")
            print_players(players)

        # -------- EXP --------
        elif choice == "6":
            name = input("Имя: ")
            p = find_player(players, name)

            if not p:
                print("Не найден")
                continue

            value = int(input("Сколько опыта добавить: "))
            if hasattr(p, "add_experience"):
                p.add_experience(value)
                print("Добавлено")
            else:
                print("У этого персонажа нет exp")
            print_players(players)

        # -------- EXIT --------
        elif choice == "0":
            save_players(players, DATA_FILE)
            print("Сохранено. Выход.")
            break

        else:
            print("Неверный пункт")
            print_players(players)
            


if __name__ == "__main__":
    main()