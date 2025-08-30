#Manipulate data in a dictionary
from numpy.f2py.symbolic import as_ge

dict = {"name": "Wasif","age":24,"grade":"MTech"}

dict["subject"] ="aaaa"
dict["grade"] = "Masters"
dict.pop("age")

print(dict)

#Remove grade
if "grade " in dict:
    del dict["grade"]
print(dict)


