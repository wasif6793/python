class Bird:
    def fly(self):
        return "Bird is flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Ostrich(Bird):
    def fly(self):
        return "Can't fly"

def make_fly(bird):
    print(bird.fly())

sparrow = Sparrow()
ostrich = Ostrich()

make_fly(sparrow)
make_fly(ostrich)