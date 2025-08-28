class MathOperation:
    def add(self,a , b = 0, c = 0):
        return a + b+ c

math_op = MathOperation()
print(math_op.add(2))
print(math_op.add(2,3))
print(math_op.add(2,3,5))