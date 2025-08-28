class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Dog(Animal):
    def sound(self):
        return "BArk"

def make_sound(Animal):
    print(Animal.sound())

dog  = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)