#class - Blueprint, object - Instance of class
class Student:
    name = "Wasif"
    grade = 10
    def __init__(self,fullname, class_grade):
        self.name = fullname
        self.grade = class_grade

#object
student1 = Student("Wasif Sheikh","MTech")
print(student1.name,student1.grade)
student2 = Student(24,22)
print(student2.grade,student2.grade)