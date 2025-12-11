def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if text == "":
        return ""
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = " ".join(text.split())
    return text


# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))
# print('#'*18)
# print(' '*18)


def tokenize(text: str) -> list[str]:
    tokenn = []
    perederz = []
    for simv in text + " ":
        if simv.isalnum() or simv == "_":
            perederz.append(simv)
        elif simv == "-" and len(perederz) >= 1 and perederz[-1].isalnum():
            perederz.append(simv)
        else:
            if len(perederz) >= 1:
                tokenn.append("".join(perederz))
                perederz = []
    return tokenn


# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))
# print('#'*18)
# print(' '*18)


def count_freq(tokens: list[str]) -> dict[str, int]:
    slovar = {}
    for token in tokens:
        slovar[token] = slovar.get(token, 0) + 1
    return slovar


# print(count_freq(["a","b","a","c","b","a"]))
# print('#'*18)
# print(' '*18)


def top_n(freq_dict, n):
    if n <= 0:
        return []

    sorted_items = sorted(
        freq_dict.items(),
        key=lambda x: (-x[1], x[0]),  # по частоте ↓, затем по алфавиту ↑
    )

    return sorted_items[:n]


# print(top_n({"bb":2,"aa":2,"cc":3}))
# print('#'*18)
# print(' '*18)


# import re


# def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
#     text = text.casefold()
#     if yo2e:
#         text = text.replace("ё", "е").replace("Ё", "Е")
#     text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
#     text = " ".join(text.split())
#     text = text.strip()
#     return text


# def tokenize(text: str) -> list[str]:
#     return re.findall(r"\w+(?:-\w+)*", text)


# def count_freq(tokens: list[str]) -> dict[str, int]:
#     c = {}
#     for w in tokens:
#         cu = c.get(w, 0)
#         c[w] = cu + 1
#     return c


# def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
#     t = []
#     for w, count in freq.items():
#         t.append((-count, w))
#     t.sort()
#     result = []
#     for neg_count, w in t:
#         result.append((w, -neg_count))
#     return result[:n]
