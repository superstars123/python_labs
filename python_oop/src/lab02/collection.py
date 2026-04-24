from lab03.base import Character
from lab04.interfaces import Printable, Comparable


class PlayerCollection:
    def __init__(self):
        self._items = []

    # ================= ADD / REMOVE =================
    def add(self, item):
        # ЛР-4: коллекция работает с интерфейсами / базовым классом
        if not isinstance(item, Character):
            raise TypeError("Можно добавлять только Character")

        if any(p.id == item.id for p in self._items):
            raise ValueError("Объект с таким id уже существует")

        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def remove_at(self, index: int):
        self._items.pop(index)

    def get_all(self):
        return self._items

    # ================= INTERFACE FILTERS =================
    def get_printable(self):
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparable(self):
        return [item for item in self._items if isinstance(item, Comparable)]

    # ================= SEARCH =================
    def find_by_name(self, name: str):
        result = PlayerCollection()
        for p in self._items:
            if p.name == name:
                result.add(p)
        return result

    def find_by_level_range(self, min_lvl, max_lvl):
        result = PlayerCollection()
        for p in self._items:
            if min_lvl <= p.level <= max_lvl:
                result.add(p)
        return result

    def find_by_status(self, status: str):
        result = PlayerCollection()
        for p in self._items:
            if getattr(p, "status", None) == status:
                result.add(p)
        return result

    def get_high_level(self, threshold):
        result = PlayerCollection()
        for p in self._items:
            if p.level >= threshold:
                result.add(p)
        return result

    # ================= SORTING =================
    def sort_by_comparable(self):
        self._items.sort(key=lambda x: x.calculate_power(), reverse=False)
        return self

    def sort_by_level(self, reverse=False):
        self._items.sort(key=lambda p: p.level, reverse=reverse)
        return self

    def sort_by_name(self, reverse=False):
        self._items.sort(key=lambda p: p.name, reverse=reverse)
        return self

    # ================= POLYMORPHISM HELPERS =================
    def print_all(self):
        for item in self._items:
            print(item.to_string() if hasattr(item, "to_string") else str(item))

    def total_power(self):
        return sum(item.calculate_power() for item in self._items)

    # ================= MAGIC METHODS =================
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            new = PlayerCollection()
            for p in self._items[index]:
                new.add(p)
            return new
        return self._items[index]

    def __str__(self):
        return "\n".join(str(p) for p in self._items)
# from lab03.model import Player

# class PlayerCollection:
#     def __init__(self):
#         self._items = [] 
        

#     # --- БАЗОВЫЕ ---
#     def add(self, item: Player):
#         if not isinstance(item, Player):
#             raise TypeError("Можно добавлять только Player")

#         if any(p.id == item.id for p in self._items):
#             raise ValueError("Игрок с таким id уже существует")

#         self._items.append(item)

#     def remove(self, item: Player):
#         self._items.remove(item)

#     def remove_at(self, index: int):
#         self._items.pop(index)

#     def get_all(self):
#         return self._items

#     # --- ПОИСК ---
#     def find_by_name(self, name: str):
#         result = PlayerCollection()
#         for p in self._items:
#             if p.name == name:
#                 result.add(p)
#         return result

#     def find_by_level_range(self, min_lvl, max_lvl):
#         result = PlayerCollection()
#         for p in self._items:
#             if min_lvl <= p.level <= max_lvl:
#                 result.add(p)
#         return result

#     def find_by_status(self, status: str):
#         result = PlayerCollection()
#         for p in self._items:
#             if p.status == status:
#                 result.add(p)
#         return result

#     # --- МАГИЯ ---
#     def __len__(self):
#         return len(self._items)

#     def __iter__(self):
#         return iter(self._items)#позволяет использовать for in

#     def __getitem__(self, index):#делает объект коллекции похожим на список
#         if isinstance(index, slice):
#             new = PlayerCollection()
#             for p in self._items[index]:
#                 new.add(p)
#             return new
#         return self._items[index]

#     def __str__(self):
#         return "\n".join(str(p) for p in self._items)

#     # --- СОРТИРОВКА ---
#     def sort(self, key, reverse=False):
#         self._items.sort(key=key, reverse=reverse)
#         return self

#     def sort_by_level(self, reverse=False):
#         return self.sort(key=lambda p: p.level, reverse=reverse)

#     def sort_by_name(self, reverse=False):
#         return self.sort(key=lambda p: p.name, reverse=reverse)

#     # --- ФИЛЬТРАЦИЯ ---
#     def get_active(self):#возвращает новую коллекцию 
#         return self.find_by_status("active")

#     def get_inactive(self):
#         return self.find_by_status("inactive")

#     def get_high_level(self, threshold):
#         result = PlayerCollection()
#         for p in self._items:
#             if p.level >= threshold:
#                 result.add(p)
#         return result