"""
Week 03 - OOP (Class & Object)
Epic Learn - Python Master Course
"""

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(self.name, "is studying")

    def show_grade(self):
        print(self.name, "grade:", self.grade)

    def show_age(self):
        print(self.name, "age:", self.age)

    def exam_result(self, score):
        if score >= 75:
            print(self.name, "passed the exam")
        else:
            print(self.name, "failed the exam")


student1 = Student("Nimal", 16, 10)
student2 = Student("Dilan", 17, 11)

student1.study()
student1.show_age()
student1.exam_result(80)

student2.study()
student2.show_grade()
student2.exam_result(30)
