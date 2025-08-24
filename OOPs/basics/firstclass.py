class Car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year = year

    def start(self):
        return f"{self.model} is starting"

    def stop(self):
        return f"{self.model} is stopping"

myCar = Car("Red","Volvo","2025")
print(myCar)
print(myCar.model)
print(myCar.start())
print(myCar.stop())
