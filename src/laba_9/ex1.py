import csv
from pathlib import Path
from typing import List, Dict, Any

try:
    from src.laba_8.models import Student
except ImportError:

    class Student:
        def __init__(self, fio: str, birthdate: str, group: str, gpa: float):
            self.fio = fio
            self.birthdate = birthdate
            self.group = group
            self.gpa = gpa

        def __repr__(self):
            return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', group='{self.group}', gpa={self.gpa})"

        def __str__(self):
            return f"{self.fio}, {self.birthdate}, {self.group}, GPA: {self.gpa}"

        def to_dict(self):
            return {
                "fio": self.fio,
                "birthdate": self.birthdate,
                "group": self.group,
                "gpa": str(self.gpa),
            }

        @classmethod
        def from_dict(cls, data):
            return cls(
                data["fio"], data["birthdate"], data["group"], float(data["gpa"])
            )


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создаёт файл с заголовком, если его нет."""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                csv.DictWriter(f, fieldnames=self.HEADER).writeheader()

    def _read_rows(self) -> List[Dict]:
        with open(self.path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def _write_rows(self, rows: List[Dict]):
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def exists(self, fio: str) -> bool:
        """Проверяет, существует ли студент с таким ФИО."""
        return any(row["fio"] == fio for row in self._read_rows())

    def list(self) -> List[Student]:
        return [Student.from_dict(row) for row in self._read_rows()]

    def add(self, student: Student):
        rows = self._read_rows()
        if any(row["fio"] == student.fio for row in rows):
            raise ValueError(f"Студент '{student.fio}' уже существует")
        rows.append(student.to_dict())
        self._write_rows(rows)

    def find(self, substr: str) -> List[Student]:
        rows = [r for r in self._read_rows() if substr.lower() in r["fio"].lower()]
        return [Student.from_dict(row) for row in rows]

    def remove(self, fio: str) -> bool:
        rows = self._read_rows()
        new_rows = [r for r in rows if r["fio"] != fio]
        if len(new_rows) != len(rows):
            self._write_rows(new_rows)
            return True
        return False

    def update(self, fio: str, **fields) -> bool:
        rows = self._read_rows()
        updated = False

        for row in rows:
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in self.HEADER:
                        row[key] = str(value) if key == "gpa" else value
                updated = True

        if updated:
            self._write_rows(rows)
        return updated

    def print_with_age(self, current_year: int = 2025):
        """Выводит всех студентов с возрастом"""
        students = self.list()
        for student in students:
            birth_year = int(student.birthdate.split(".")[0])
            age = current_year - birth_year
            print(
                f"Студент: {student.fio}, Группа: {student.group}, GPA: {student.gpa}, Возраст: {age}"
            )

    def stats(self) -> Dict[str, Any]:
        students = self.list()
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [s.gpa for s in students]
        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": round(sum(gpas) / len(students), 2),
            "groups": groups,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]
            ],
        }

    def __str__(self):
        students = self.list()
        if not students:
            return "Группа пуста"
        return "\n".join(
            [
                f"Всего студентов: {len(students)}",
                *[
                    f"{i+1}. {s.fio} | {s.birthdate} | {s.group} | GPA: {s.gpa}"
                    for i, s in enumerate(students)
                ],
            ]
        )


if __name__ == "__main__":
    group = Group("data/lab09/students.csv")
    group._write_rows([])

    # СПИСОК ДЛЯ ДОБАВЛЕНИЯ
    students_to_add = [
        Student("Макаров Георгий Васильевич", "2006.12.16", "BIVT-25", 4.6),
        Student("Ильин Илья Ильич", "2007.03.16", "BIVT-24", 4.5),
        Student("Петрова София Алексеевна", "2005.01.01", "BIVT-23", 4.9),
    ]

    # БЕЗОПАСНОЕ ДОБАВЛЕНИЕ (без ошибок)
    for s in students_to_add:
        if not group.exists(s.fio):
            group.add(s)
            print(f"Добавлен: {s.fio}")
        else:
            print(f"Студент {s.fio} уже существует — пропускаю.")

    group.print_with_age()
    # group.remove("Алексеев Алексей Алексеевич")
    # print(f"\nПосле удаления Алексеева, всего студентов: {len(group.list())}")
    # group.print_with_age()

    # group.remove("Петров Пётр Петрович")
    # group.print_with_age()

    # group.update("Николаев Николай Николаевич", gpa=4.9)
    # group.print_with_age()
    group.remove("Алексеев Алексей Алексеевич")
    print(f"\nПосле удаления Алексеева, всего студентов: {len(group.list())}")
    print("Студенты:")
    for student in group.list():
        print(f"  {student}")

    print("\nПоиск по 'Петрова':")
    for student in group.find("Петрова"):
        print(f"  {student}")

    print("\nСтатистика:")
    stats = group.stats()
    for key, value in stats.items():
        if key == "top_5_students":
            print(f"  {key}:")
            for student in value:
                print(f"    {student['fio']} - GPA: {student['gpa']}")
        else:
            print(f"  {key}: {value}")
