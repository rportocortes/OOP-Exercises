class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grades(self, value):
        self.grades.append(value)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def status(self):
        avg = self.calculate_average()
        if avg >= 60:
            return "Passing"
        elif avg >= 50:
            return "Recovery"
        else:
            return "Failing"

    def __str__(self):
        return f"Name: {self.name} | Id: {self.student_id} | Average: {self.calculate_average():.2f} | Status: {self.status()}"


class Classroom:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def show(self):
        for student in self.students:
            print(student)

    def class_average(self):
        total = 0
        for s in self.students:
            total += s.calculate_average()
        return total / len(self.students)

    def top_students(self):
        result = []
        for s in self.students:
            if s.calculate_average() >= 70:
                result.append(s)
        return result


s1 = Student("Rafael", 1784083)
s1.add_grades(56)
s1.add_grades(89)
s1.add_grades(70)
s1.add_grades(65)

s2 = Student("Ana", 2291847)
s2.add_grades(80)
s2.add_grades(90)
s2.add_grades(75)

turma = Classroom()
turma.enroll(s1)
turma.enroll(s2)

turma.show()
print(f"Class average: {turma.class_average():.2f}")
print("Top students:")
for s in turma.top_students():
    print(s)