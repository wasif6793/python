class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

myCircle = Circle(int(input("Enter radius of a circle:")))
areaCircle = myCircle.area()

print(f"Area of a cirlce is {areaCircle}")