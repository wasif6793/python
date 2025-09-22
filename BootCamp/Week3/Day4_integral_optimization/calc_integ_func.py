
# Calculating integrals of simple functions

import sympy as sp

x = sp.Symbol('x')

f = x**2 + 3*x + 7

integ = sp.integrate(f,x)
print("Integrated function: ", integ)
