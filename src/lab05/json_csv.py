import csv
import json
from pathlib import Path


def check_extension(path, extension):
    """Проверяет расширение файла."""
    if Path(path).suffix.lower() != extension:
        raise ValueError(f"Нужен файл {extension}")


def read_csv(csv_path):
    """Читает CSV с непустым уникальным заголовком."""
    check_extension(csv_path, ".csv")
    with open(csv_path, encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if not header or any(not name.strip() for name in header):
            raise ValueError("CSV пуст или заголовок неверный")
        if len(set(header)) != len(header):
            raise ValueError("В заголовке повторяются колонки")
        rows = []
        for row in reader:
            if not row:
                continue
            if len(row) != len(header):
                raise ValueError("Неверная длина строки CSV")
            rows.append(row)
    return header, rows


def json_to_csv(json_path: str, csv_path: str) -> None:
    """JSON-массив словарей в CSV. Колонки в порядке появления."""
    check_extension(json_path, ".json")
    check_extension(csv_path, ".csv")
    with open(json_path, encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list) or not data:
        raise ValueError("Нужен непустой список словарей")
    header = []
    for row in data:
        if not isinstance(row, dict):
            raise ValueError("Каждая запись должна быть словарём")
        for key, value in row.items():
            if not key.strip() or isinstance(value, (dict, list)):
                raise ValueError("Нужны непустые ключи и простые значения")
            if key not in header:
                header.append(key)
    if not header:
        raise ValueError("Нет колонок")
    with open(csv_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """CSV в JSON; все значения остаются строками."""
    check_extension(json_path, ".json")
    header, rows = read_csv(csv_path)
    data = []
    for row in rows:
        data.append(dict(zip(header, row)))
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
