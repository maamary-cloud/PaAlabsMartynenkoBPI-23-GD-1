import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает целиком; другую кодировку задают encoding='cp1251'.

    FileNotFoundError и UnicodeDecodeError не перехватываются.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Пишет CSV. Неодинаковая длина строк — ValueError."""
    width = len(header) if header is not None else None
    for row in rows:
        if width is None:
            width = len(row)
        if len(row) != width:
            raise ValueError("Строки CSV должны иметь одинаковую длину")
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
