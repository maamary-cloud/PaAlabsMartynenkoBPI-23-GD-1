from src.lab08.models import Student
from src.lab09.group import Group


def main():
    # Отдельный файл демонстрации; исходная база students.csv не меняется.
    group = Group("data/lab09/demo_students.csv")
    group.remove("Петров Пётр")
    group.add(Student("Петров Пётр", "2005-01-15", "БИВТ-25-1", 4.5))
    print("После добавления:")
    for student in group.list():
        print(student)
    print("Поиск:", group.find("петр"))
    group.update("Петров Пётр", gpa=4.8)
    print("После обновления:", group.list())
    group.remove("Петров Пётр")
    print("После удаления:", group.list())


if __name__ == "__main__":
    main()
