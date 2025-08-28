class Dog:
    species = "Canis "

    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy",5)
dog2 = Dog("Milo",3)

print(dog1.name)
print(dog2.age)
print(dog2.species)
