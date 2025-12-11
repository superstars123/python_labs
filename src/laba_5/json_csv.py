import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV."""
    json_path_obj = Path(json_path)
    csv_path_obj = Path(csv_path)

    # Проверка расширений
    if json_path_obj.suffix != ".json" or csv_path_obj.suffix != ".csv":
        raise ValueError("Неверное расширение файла")

    # Создаём папку для CSV, если её нет
    csv_path_obj.parent.mkdir(parents=True, exist_ok=True)

    with open(json_path_obj, encoding="utf-8") as f:
        data = json.load(f)

    if (
        not data
        or not isinstance(data, list)
        or not all(isinstance(item, dict) for item in data)
    ):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Собираем все уникальные ключи из всех объектов
    fieldnames = sorted({key for item in data for key in item.keys()})

    with open(csv_path_obj, "w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {field: item.get(field, "") for field in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей)."""
    csv_path_obj = Path(csv_path)
    json_path_obj = Path(json_path)

    # Проверка расширений
    if csv_path_obj.suffix != ".csv" or json_path_obj.suffix != ".json":
        raise TypeError("Неверное расширение файла")

    # Создаём папку для JSON, если её нет
    json_path_obj.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_path_obj, "r", encoding="utf-8", newline="") as cf:
        reader = csv.DictReader(cf)
        lt_rows = list(reader)

    if not lt_rows:
        raise ValueError("CSV файл пуст или содержит только заголовок")

    with open(json_path_obj, "w", encoding="utf-8") as jf:
        json.dump(lt_rows, jf, ensure_ascii=False, indent=2)


# Пример использования с путями внутри проекта
json_to_csv(
    "C:/Users/1/python_labs/data/samples/people.json",
    "C:/Users/1/python_labs/data/out/people_from_json.csv",
)
csv_to_json(
    "C:/Users/1/python_labs/data/samples/people.csv",
    "C:/Users/1/python_labs/data/out/people_from_csv.json",
)
