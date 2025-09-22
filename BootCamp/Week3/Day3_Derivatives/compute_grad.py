import  sympy as sp

x, y = sp.symbols('x y')

f = x**2 + 3*y**2 -4*x*y

print("Partial Derivative: ", sp.diff(f,x)," & ", sp.diff(f,y))