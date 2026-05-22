from lab03.base import Character


class PlayerCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Character):
            raise TypeError("Можно добавлять только Character")
        self._items.append(item)

    def get_all(self):
        return self._items

    # ================= STRATEGY METHODS =================

    def sort_by(self, key_func, reverse=False):
        self._items = sorted(self._items, key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        result = PlayerCollection()
        for item in filter(predicate, self._items):
            result.add(item)
        return result

    def apply(self, func):
        result = PlayerCollection()
        for item in self._items:
            result.add(func(item))
        return result

    # ================= MAGIC METHODS =================

    def __iter__(self):
        return iter(self._items)

    def __len__(self):          
        return len(self._items)

    def __str__(self):
        return "\n".join(str(x) for x in self._items)
  