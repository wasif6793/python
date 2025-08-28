class X:
    def greet(self):
        return "Hello Bhaiya"

class Y:
    def greet(self):
        return "Hello Y"

class Z(X,Y):
    pass

obj = Z()
print(obj.greet())
print(Z.mro())