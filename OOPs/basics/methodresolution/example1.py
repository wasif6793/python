class A:
    def greet(self):
        return "Hello A"


class B(A):
    pass

class C(B):
    pass

obj = C()
print(obj.greet())
print(C.mro())
