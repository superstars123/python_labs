from model import Player

# ------------------- 1. Создание объектов -------------------
print("~~~ Создание объектов ~~~")
p1 = Player("Vika", 100, 1, 0)
p2 = Player("Masha", 100, 1, 0)
p3 = Player("Dasha", 120, 2, 50)

players = [p1, p2, p3]

for p in players:
    print(p)
    print(repr(p))

# ------------------- 2. Геттеры -------------------
print("\n~~~ Демонстрация геттеров ~~~")
for p in players:
    print(f"\nИгрок {p.name}:")
    print(" Здоровье:", p.health)
    print(" Уровень:", p.level)
    print(" Опыт:", p.experience)
    print(" Активен:", p.active)

# ------------------- 3. Сеттер -------------------
print("\n~~~ Демонстрация сеттера ~~~")
p1.health = 80
p2.health = 90
p3.health = 110

for p in players:
    print(f"{p.name} HP:", p.health)

# ------------------- 4. Валидация -------------------
print("\n~~~ Демонстрация валидации ~~~")
try:
    bad = Player("", -10, 0, -5)
except Exception as e:
    print(" Ошибка создания:", e)

try:
    p1.health = -50
except Exception as e:
    print(" Ошибка сеттера:", e)

# ------------------- 5. Атрибуты класса -------------------
print("\n~~~ Демонстрация атрибутов класса ~~~")
print(" MAX_LEVEL через класс:", Player.MAX_LEVEL)
for p in players:
    print(f" MAX_LEVEL через {p.name}:", p.MAX_LEVEL)

# ------------------- 6. Логическое состояние -------------------
print("\n~~~ Демонстрация логического состояния ~~~")
for p in players:
    print(f"{p.name} активен:", p.active)

p1.take_damage(200)
p2.take_damage(50)
p3.take_damage(130)

for p in players:
    print(f"После урона {p.name}:", p)
    print(" Активен:", p.active)

# ------------------- 7. Изменение состояния -------------------
print("\n~~~ Демонстрация изменения состояния ~~~")
for p in players:
    if not p.active:
        p.revive()
        print(f"{p.name} был оживлён:", p)
    else:
        print(f"{p.name} уже активен")

# ------------------- 8. Бизнес-логика -------------------
print("\n~~~ Демонстрация опыта и уровня ~~~")
p1.gain_experience(250)
p2.gain_experience(150)
p3.gain_experience(300)

for p in players:
    print(p)

# ------------------- 9. Сравнение -------------------
print("\n~~~ Сравнение объектов ~~~")
print(" p1 == p2:", p1 == p2)
print(" p2 == p3:", p2 == p3)
# from model import Player

# # ------------------- 1. Создание объектов -------------------
# print("~~~ Создание объектов ~~~")
# p1 = Player("Vika", 100, 1, 0)
# p2 = Player("Masha", 100, 1, 0)
# print(p1)
# print(repr(p1))

# # ------------------- 2. Геттеры -------------------
# print("~~~ Демонстрация геттеров ~~~")
# print(" Имя:", p1.name)
# print(" Здоровье:", p1.health)
# print(" Уровень:", p1.level)
# print(" Опыт:", p1.experience)
# print(" Активен:", p1.active)

# # ------------------- 3. Сеттер -------------------
# print("\n~~~ Демонстрация сеттера ~~~")
# p1.health = 80
# print(" После изменения HP:", p1.health)

# # ------------------- 4. Валидация -------------------
# print("\n~~~ Демонстрация валидации ~~~")
# try:
#     bad = Player("", -10, 0, -5)
# except Exception as e:
#     print(" Ошибка создания:", e)

# try:
#     p1.health = -50
# except Exception as e:
#     print(" Ошибка сеттера:", e)

# # ------------------- 5. Атрибуты класса -------------------
# print("\n~~~ Демонстрация атрибутов класса ~~~")
# print(" MAX_LEVEL через класс:", Player.MAX_LEVEL)
# print(" MAX_LEVEL через объект:", p1.MAX_LEVEL)

# # ------------------- 6. Логическое состояние -------------------
# print("\n~~~Демонстрация логического состояния ~~~")
# print(" Активен:", p1.active)
# p1.take_damage(200)
# print(" После смерти:", p1)
# print(" Активен:", p1.active)

# # ------------------- 7. Изменение состояния -------------------
# print("\n~~~ Демонстрация изменения состояния ~~~")
# p1.revive()
# print(" После revive:", p1)
# print(" Активен:", p1.active)

# # ------------------- 8. Бизнес-логика -------------------
# print("\n~~~ Демонстрация опыта и уровня ~~~")
# p1.gain_experience(250)
# print(p1)

# # ------------------- 9. Сравнение -------------------
# print("\n~~~ Сравнение объектов ~~~")
# print(" p1 == p2:", p1 == p2)