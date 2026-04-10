from datetime import datetime


# ================= БАЗОВЫЙ КЛАСС =================
class Character:
    """Базовый класс игрового персонажа"""

    game_name = "Python RPG"
    _next_id = 1

    def __init__(self, name, health, level):
        self.name = self._validate_name(name)
        self._health = self._validate_health(health)
        self._level = self._validate_level(level)

        self.id = Character._next_id
        Character._next_id += 1

        self.status = "жив"
        self._created = datetime.now()

    # ================= VALIDATION =================
    def _validate_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Некорректное имя")
        return name.strip()

    def _validate_health(self, health):
        if not isinstance(health, (int, float)) or health < 0:
            raise ValueError("Некорректный health")
        return int(health)

    def _validate_level(self, level):
        if not isinstance(level, int) or level < 1:
            raise ValueError("Некорректный level")
        return level

    # ================= PROPERTIES =================
    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    # ================= CORE LOGIC =================
    def is_alive(self):
        return self.status == "жив"

    def calculate_power(self):
        """Базовая формула силы (полиморфизм)"""
        return self._level * 10 + self._health

    def process(self):
        """Общий интерфейс"""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.get_type(),
            "power": self.calculate_power(),
            "status": self.status
        }

    def get_type(self):
        return "Character"

    # ================= GAME LOGIC =================
    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")

        if not self.is_alive():
            raise ValueError("Персонаж уже мёртв")

        self._health -= damage

        if self._health <= 0:
            self._health = 0
            self.status = "мёртв"

    def heal(self, value):
        if value < 0:
            raise ValueError("Лечение не может быть отрицательным")

        if not self.is_alive():
            raise ValueError("Нельзя лечить мёртвого")

        self._health += value

    def revive(self):
        if self.is_alive():
            raise ValueError("Персонаж уже жив")

        self._health = 100
        self.status = "жив"

    # ================= MAGIC METHODS =================
    def __str__(self):
        return f"[{self.get_type()}] {self.name} (HP: {self._health}, LVL: {self._level})"

    def __repr__(self):
        return f"{self.get_type()}(name={self.name}, lvl={self._level}, hp={self._health})"

    def __lt__(self, other):
        return self.calculate_power() < other.calculate_power()


# ================= COLLECTION =================
class CharacterCollection:
    """Коллекция персонажей (как AccountCollection)"""

    def __init__(self, items=None):
        self._items = items if items else []

    def add(self, character):
        if not isinstance(character, Character):
            raise TypeError("Только Character")

        if any(c.id == character.id for c in self._items):
            raise ValueError("Персонаж уже существует")

        self._items.append(character)

    def get_by_type(self, cls):
        return CharacterCollection([c for c in self._items if isinstance(c, cls)])

    def process_all(self):
        """Полиморфная обработка"""
        return [c.process() for c in self._items]

    def total_power(self):
        return sum(c.calculate_power() for c in self._items)

    def alive_only(self):
        return CharacterCollection([c for c in self._items if c.is_alive()])

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "\n".join(str(c) for c in self._items)