import csv


class StudentManager:
    """
    Class for managing student data stored in a CSV file.
    Provides methods for reading, writing, and calculating average grade.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def read_students(self):
        students = []
        with open(self.filename, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["Вік"] = int(row["Вік"])
                row["Оцінка"] = int(row["Оцінка"])
                students.append(row)
        return students

    def average_grade(self):
        students = self.read_students()
        if not students:
            return 0
        return sum(s["Оцінка"] for s in students) / len(students)

    def add_student(self, name: str, age: int, grade: int):
        with open(self.filename, "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, age, grade])
        print(f"Додано студента: {name}, {age} років, оцінка {grade}")


manager = StudentManager("students.csv")

# Середня оцінка студентів: 89.50
avg = manager.average_grade()
print(f"Середня оцінка студентів: {avg:.2f}")

# Додано студента: Олександр, 35 років, оцінка 100
manager.add_student("Олександр", 35, 100)

# Нова середня оцінка студентів: 91.60
new_avg = manager.average_grade()
print(f"Нова середня оцінка студентів: {new_avg:.2f}")
