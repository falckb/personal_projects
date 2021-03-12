import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d, linspace
from sympy import Symbol, solveset, lambdify, Interval, oo  # oo is sympys representation of Infinity
from sympy.plotting import plot
from math import floor

x = Symbol('x')  # Set a symbol
F = 7*(x-3)**(2/3)  #function to take derivative of
F_fun = lambdify(x, F)
der_F = F.diff(x)  # derivative of F

dRoots = solveset(der_F, x, Interval(-oo, oo)) # Find the roots of our derivative where x is between interval
y_vals = [F_fun(r) for r in dRoots]
print(f"Extreme values are {dRoots} at y values of {y_vals} respectively") # gives a set with a single extrema, this is our answer