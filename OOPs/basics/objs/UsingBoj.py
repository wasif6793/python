class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model= model

my_car = Car("Tata","Safari")
print(my_car.brand)

my_car.model = "Sumo"
print(my_car.model)

