from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    """Студент: ФИО, дата рождения, группа и средний балл 0–5."""

    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        if not isinstance(self.fio, str) or not self.fio.strip():
            raise ValueError("ФИО должно быть непустой строкой")
        if not isinstance(self.group, str) or not self.group.strip():
            raise ValueError("Группа должна быть непустой строкой")
        if not isinstance(self.birthdate, str):
            raise ValueError("Дата должна быть строкой YYYY-MM-DD")
        birthday = date.fromisoformat(self.birthdate)
        if birthday.isoformat() != self.birthdate or birthday > date.today():
            raise ValueError("Нужна дата YYYY-MM-DD, не позже сегодняшней")
        if isinstance(self.gpa, bool) or not isinstance(self.gpa, (int, float)):
            raise ValueError("Средний балл должен быть числом")
        if not 0 <= self.gpa <= 5:
            raise ValueError("Средний балл должен быть от 0 до 5")

    def age(self) -> int:
        """Возвращает полные годы с учётом дня рождения."""
        birthday = date.fromisoformat(self.birthdate)
        today = date.today()
        years = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        """Возвращает четыре поля в словаре."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создаёт студента из словаря с проверкой полей."""
        if not isinstance(data, dict) or set(data) != {
            "fio",
            "birthdate",
            "group",
            "gpa",
        }:
            raise ValueError("Нужны поля fio, birthdate, group, gpa")
        return cls(data["fio"], data["birthdate"], data["group"], data["gpa"])

    def __str__(self) -> str:
        return f"{self.fio}, гр. {self.group}, GPA {self.gpa:.2f}"
