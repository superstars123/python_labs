class PlayerNotFoundError(Exception):
    """Игрок не найден."""
    pass


class DuplicatePlayerError(Exception):
    """Игрок уже существует."""
    pass