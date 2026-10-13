# ЛР5 — JSON, CSV, XLSX

Работа с форматом JSON, сериализацией и конвертацией JSON ↔ CSV и CSV → XLSX.

### A — JSON в CSV

```powershell
python -c "from src.lab05.json_csv import json_to_csv; json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv'); print(open('data/out/people_from_json.csv', encoding='utf-8').read())"
```

Фактический вывод:

```text
name,age,city
Алиса,22,Москва
Боб,25,СПб
```

![ЛР5, A — JSON в CSV: изображение фактического вывода](../../images/lab05/run01.png)

### A — CSV в JSON

```powershell
python -c "from src.lab05.json_csv import csv_to_json; csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json'); print(open('data/out/people_from_csv.json', encoding='utf-8').read())"
```

Фактический вывод:

```text
[
  {
    "name": "Алиса",
    "age": "22",
    "city": "Москва"
  },
  {
    "name": "Боб",
    "age": "25",
    "city": "СПб"
  }
]
```

![ЛР5, A — CSV в JSON: изображение фактического вывода](../../images/lab05/run02.png)

### B — CSV в XLSX

```powershell
python -c "from src.lab05.csv_xlsx import csv_to_xlsx; from openpyxl import load_workbook; csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx'); w=load_workbook('data/out/people.xlsx'); print('Листы:', w.sheetnames); print('Строки:', list(w.active.values)); print('Ширины:', [(k, v.width) for k, v in w.active.column_dimensions.items()])"
```

Фактический вывод:

```text
Листы: ['Sheet1']
Строки: [('name', 'age', 'city'), ('Алиса', '22', 'Москва'), ('Боб', '25', 'СПб')]
Ширины: [('A', 8.0), ('B', 8.0), ('C', 8.0)]
```

![ЛР5, B — CSV в XLSX: изображение фактического вывода](../../images/lab05/run03.png)

## Код

### src/lab05/csv_xlsx.py

```python
from src.lab05.json_csv import check_extension, read_csv


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Переносит CSV в Sheet1; ширина колонок не меньше 8."""
    from openpyxl import Workbook
    from openpyxl.utils import get_column_letter

    check_extension(xlsx_path, ".xlsx")
    header, rows = read_csv(csv_path)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"
    sheet.append(header)
    for row in rows:
        sheet.append(row)
    for i in range(len(header)):
        width = 8
        for row in [header] + rows:
            width = max(width, len(str(row[i])) + 2)
        sheet.column_dimensions[get_column_letter(i + 1)].width = width
    workbook.save(xlsx_path)

```

### src/lab05/json_csv.py

```python
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

```

## Вывод

Обязательные задания выполнены. Задания со звёздочками пропущены. Изображения выше сформированы из сохранённого фактического stdout/stderr; это не снимки окна терминала.
