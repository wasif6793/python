class Vehicle:
    def __init__(self,brand, name):
        self.brand = brand
        self.name = name

    def descr(self):
        return f"{self.name} {self.brand}"

class Car(Vehicle):
    def wheels(self):
        return 4

mycar = Car('Tata',"Sumo")
print(mycar.descr())
print(mycar.wheels())