from sympy import Symbol, limit, diff, lambdify, log, exp, sin, pi, sqrt
from IPython.display import display
import numpy as np
from numpy import log

def get_limit(goesto):
    """
    Input the number the limit converges to
    Outputs limit if it exists
    """
    x = Symbol('x')
    numerator = x**3 - 5*x**2 + 9*x - 20
    denominator = x-4
    f_x = numerator / denominator
    li = limit(f_x, x, goesto)
    print(li)

#get_limit(4)

def simple_fcn(x):
    z = ((2*np.pi)/3)*np.cos((np.pi/3)(x+8))
    print(z)

#simple_fcn(3)

def simple_deriv(ipt):
    """
    Input the number you'd like to evaluate the derivative on
    """
    x = Symbol('x')
    f_x = 170*x*(x+2)**(-2) #function to take derivative of
    deriv_f = f_x.diff(x)
    print(deriv_f) #print derivative
    func_deriv_f = lambdify(x, deriv_f) #evaluate derivative for value
    print(func_deriv_f(ipt))

simple_deriv(3)