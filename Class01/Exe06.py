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
        if self.calculate_average() >= 60:
            return "Passing"
        elif self.calculate_average() >= 50:
            return "recovery"
        else:
            return "Failing"
        
    def __str__(self):
        return f"Name: {self.name} | Id: {self.student_id} | Average: {self.calculate_average():.2f} | Status: {self.status()}"


s1 = Student("Rafael", 1784083)
s1.add_grades(56)
s1.add_grades(89)
s1.add_grades(70)
s1.add_grades(65)
s1.calculate_average()
print(s1)