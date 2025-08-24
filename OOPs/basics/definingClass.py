class Cat:
    def __init__(self,name, brand):
        self.name = name
        self.brand = brand

    def meow(self):
        return f"{self.name} says meow"


myCat = Cat("Aslan","Persian Black Cat")
print(myCat.meow())
print(myCat.name,"brand is",myCat.brand)
