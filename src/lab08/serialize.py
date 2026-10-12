import json
from src.lab08.models import Student


def students_to_json(students: list[Student], path: str) -> None:
    """Сохраняет студентов как JSON-массив."""
    data = []
    for student in students:
        if not isinstance(student, Student):
            raise ValueError("Нужен список студентов")
        student.__post_init__()
        data.append(student.to_dict())
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[Student]:
    """Читает массив и создаёт проверенные объекты Student."""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    students = []
    for record in data:
        students.append(Student.from_dict(record))
    return students


if __name__ == "__main__":
    students = students_from_json("data/lab08/students_input.json")
    for student in students:
        print(student)
        print("Полных лет:", student.age())
        print("Словарь:", student.to_dict())
    students_to_json(students, "data/lab08/students_output.json")
    print("Сохранено: data/lab08/students_output.json")
