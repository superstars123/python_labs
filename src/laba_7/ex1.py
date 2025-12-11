import sys
import pytest

sys.path.append("C:/Users/1/python_labs")

from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("", []),
        ("   ", []),
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
    result = top_n(freq, 2)
    expected = [("cherry", 7), ("apple", 5)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"banana": 3, "apple": 3, "cherry": 3}
    result = top_n(freq, 3)
    expected = [("apple", 3), ("banana", 3), ("cherry", 3)]
    assert result == expected


def test_top_n_empty():
    assert top_n({}, 5) == []


def test_full_pipeline():
    text = "Привет мир! Привет всем. Мир прекрасен."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "привет мир! привет всем. мир прекрасен."
    assert tokens == [
        "привет",
        "мир",
        "привет",
        "всем",
        "мир",
        "прекрасен",
    ]
    assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
    assert top_words == [("мир", 2), ("привет", 2)]


# import sys
# import os
# import pytest

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))# путь к папке src

# from src.lib.stats_text import normalize, tokenize, count_freq, top_n


# # тесты для normalize
# @pytest.mark.parametrize(
#     "source, expected",
#     [
#         ("ПрИвЕт\nМИр\t", "привет мир"),
#         ("ёжик, Ёлка", "ежик, елка"),
#         ("Hello\r\nWorld", "hello world"),
#         ("  двойные   пробелы  ", "двойные пробелы"),
#         ("", ""),  # пустая строка
#         ("   ", ""),  # только пробелы
#     ],
# )
# def test_normalize(source, expected):
#     assert normalize(source) == expected


# # тесты для tokenize
# @pytest.mark.parametrize(
#     "text, expected",
#     [
#         ("привет мир", ["привет", "мир"]),
#         ("hello world test", ["hello", "world", "test"]),
#         ("", []),
#         ("   ", []),
#         ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
#     ],
# )
# def test_tokenize(text, expected):
#     assert tokenize(text) == expected


# # тесты для count_freq
# @pytest.mark.parametrize(
#     "tokens, expected",
#     [
#         (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
#         ([], {}),
#         (["word"], {"word": 1}),
#     ],
# )
# def test_count_freq(tokens, expected):
#     assert count_freq(tokens) == expected


# # тесты для top_n
# @pytest.mark.parametrize(
#     "freq_dict, n, expected",
#     [
#         ({"a": 3, "b": 2, "c": 1}, 3, [("a", 3), ("b", 2), ("c", 1)]),
#         ({"яблоко": 2, "апельсин": 2, "банан": 2}, 3,
#          [("апельсин", 2), ("банан", 2), ("яблоко", 2)]),
#         ({}, 5, []),
#         ({"a": 5, "b": 4, "c": 3, "d": 2, "e": 1, "f": 1}, 3,
#          [("a", 5), ("b", 4), ("c", 3)]),
#         ({"a": 1, "b": 2}, 0, []),
#     ],
# )
# def test_top_n(freq_dict, n, expected):
#     assert top_n(freq_dict, n) == expected
# if __name__ == "__main__":
#     text = "ПрИвЕт, МИр!"
#     print("Normalize:", normalize(text))
#     tokens = tokenize(normalize(text))
#     print("Tokenize:", tokens)
#     freq = count_freq(tokens)
#     print("Count freq:", freq)
#     print("Top 2:", top_n(freq, 2))
# import pytest
# from src.lib.stats_text import normalize, tokenize, count_freq, top_n

# def test_normalize():
#     assert normalize("ПрИвЕт") == "привет"

# def test_tokenize():
#     assert tokenize("привет мир") == ["привет", "мир"]
