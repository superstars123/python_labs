import re  # библиотека для работы с регулярными выражениями


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
