import sympy as sp

x = sp.Symbol('x')
f = x** 2
# differentiation
derivative = sp.diff(f,x)
print(derivative)

y, z = sp.symbols('y z')

f2 = y**2 + z ** 2
grad_y = sp.diff(f2,y)
grad_z = sp.diff(f2,z)

print("Partial Derivatives: ",grad_y, grad_z)


