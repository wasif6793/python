import sympy as sp

x, y = sp.symbols('x y')

f = x**2 + y**3
f2 = x**3 -x**2 + 7
print("FUnction: ",f2)
print("Derivative: ", sp.diff(f2,x))
deriv = sp.diff(f,(x, y))
print("First order derivative: ",deriv)
deriv2 = sp.diff(sp.diff(f2,x),x)
print("Second order derivative: ",deriv2)