class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

myCircle = Circle(8)

print(myCircle.area())