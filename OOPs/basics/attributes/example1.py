class Employee:
    def __init__(self,name, salary):
        self.name = name
        self._salary = salary

    def display(self):
        return f"Name: {self.name} and Salar {self._salary}"

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name,salary)
        self.department = department

    def display_manager(self):
        return f"Name {self.name} salary {self._salary} Department {self.department}"

emp = Employee("Wasif", 95000)
mgr = Manager("Amjad",50000,"MTech")
print(mgr.display_manager())
print(emp.display())

print(emp._salary)
print(mgr.name)