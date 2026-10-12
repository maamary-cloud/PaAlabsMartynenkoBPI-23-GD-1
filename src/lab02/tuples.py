def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует студента. Неверные значения — ValueError/TypeError."""
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    parts = fio.split()
    if len(parts) not in (2, 3) or not group.strip() or not 0 <= gpa <= 5:
        raise ValueError("Неверное ФИО, группа или GPA")
    initials = ""
    for name in parts[1:]:
        initials += name[0].upper() + "."
    return f"{parts[0].capitalize()} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


if __name__ == "__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
