import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sympy as syp

Kw = syp.symbols("Kw")
Ka1 = syp.symbols("Ka1")
Ka2 = syp.symbols("Ka2")

c = syp.symbols("c")
x = syp.symbols("x")
y = syp.symbols("y")
z = syp.symbols("z")

eq1 = syp.Eq(Ka1**(-1)*z*x,c-z-x+Kw/x)
eq2 = syp.Eq(Ka2*z,x**2-x*Kw/x+Ka1**(-1)*z*x**2)

ans1 = syp.solve(eq1,x)
ans2 = syp.solve(eq2,x)

zeq3 = ans1[0] - ans2[0]

print(zeq3)
