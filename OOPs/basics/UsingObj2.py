class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        return f"My name is {self.name} and i am in grade {self.grade} "

stu1 = Student(input("Write your name: "),input("Write your grade: "))
stu2 = Student("Wasif","MTech")

print(stu1.introduce())
print(stu2.introduce())