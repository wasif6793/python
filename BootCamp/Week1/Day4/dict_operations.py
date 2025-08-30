student = {'name':"Wasif","age":24,"grade":"A"}

student["subject"] = "Maths"
del student["age"]

student.pop("grade")

print(student)

for key, value in student.items():
    print(key, value)