from typing import TypeVar, Generic, Callable, Optional, Protocol


# ================= PROTOCOLS =================

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# ================= TYPE VARS =================

T = TypeVar("T")
R = TypeVar("R")

D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


# ================= GENERIC COLLECTION =================

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    # ================= BASIC =================

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def remove_at(self, index: int) -> None:
        self._items.pop(index)

    def get_all(self) -> list[T]:
        return self._items

    # ================= GENERIC METHODS =================

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]

    # ================= DISPLAY =================

    def display_all(self) -> None:
        for item in self._items:
            if hasattr(item, "display"):
                print(item.display())
            else:
                print(item)

    # ================= MAGIC METHODS =================

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]