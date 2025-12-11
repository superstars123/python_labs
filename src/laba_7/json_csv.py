import json
import csv
from pathlib import Path


def check_json_file(path: str):
    if not path.endswith(".json"):
        raise ValueError("Ожидается JSON файл")
    if not Path(path).exists():
        raise FileNotFoundError("Файл не найден")


def check_csv_file(path: str):
    if not path.endswith(".csv"):
        raise ValueError("Ожидается CSV файл")
    if not Path(path).exists():
        raise FileNotFoundError("Файл не найден")


def convert_value(value: str):
    """Преобразует строку в число, если это возможно."""
    if value.isdigit():
        return int(value)

    try:
        return float(value)
    except ValueError:
        return value


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path_obj = Path(json_path)
    csv_path_obj = Path(csv_path)

    if json_path_obj.suffix != ".json" or csv_path_obj.suffix != ".csv":
        raise ValueError("Неверное расширение файла")

    check_json_file(json_path)

    with open(json_path, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    if not isinstance(data, list) or not data:
        raise ValueError("JSON должен содержать список объектов")

    fieldnames = data[0].keys()

    with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path_obj = Path(csv_path)
    json_path_obj = Path(json_path)

    if csv_path_obj.suffix != ".csv" or json_path_obj.suffix != ".json":
        raise ValueError("Неверное расширение файла")  # ← фикс ошибки №3

    check_csv_file(csv_path)

    with open(csv_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        data = []
        for row in reader:
            converted = {k: convert_value(v) for k, v in row.items()}
            data.append(converted)

    with open(json_path, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

      