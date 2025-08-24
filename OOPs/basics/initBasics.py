class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def description(self):
        return f"This car is a  {self.brand} and {self.model}"

myCar = Car("Tata","Safari")
print(myCar.description())