class Car:
    wheels = 4

    def __init__(self,name, model):
        self.name = name
        self.model = model


car1 = Car("Tata","ABd")
car2 = Car("Volvo","Accc")

car1.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)
