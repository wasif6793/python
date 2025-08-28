class Person:
    _count = 0

    def __init__(self,name):
        self.name = name
        Person._count += 1

    @classmethod

    def get_count(cls):
        return cls._count

p1 = Person("Wasif")
p2 = Person("Nishu")
print((Person.get_count()))