import numpy as np
from sympy import Symbol, integrate, sqrt, E, oo
import matplotlib.pyplot as plt


#Integration function using subintervals
def integration(a,b,n):
    """
    Input start of interval, end of interval, number of subintervals, and the function
    Outputs the area under f between a and b
    """
    def f(x):
        f = x**2 #function to integrate
        return f

    total = 0.0
    delta = (b-a)/n
    for i in range(n):
        total = total + delta * (f(a+delta*(i+1)) + f(a+delta*i)) / 2
    return total


def ftc(lower, upper):
    x = Symbol('x')
    f_x = 200+1000*x-180*x**2 #function to integrate
    area = integrate(f_x, lower, upper)
    print(area)

t = Symbol('t')
r_t = (5)*E**(-5*t)

flow_rate = integrate(r_t, (t,0,(2/3)))
flow_rate = flow_rate.evalf()
# a = integrate(r_prime, (t, 0, 1))
#print(f"{flow_rate} cars")

def indefintegral():
    x = Symbol('x')
    function = x*E**(3*x**2) #function to integrate
    answer = integrate(function, x)
    print(answer)


x = np.arange(0,16,0.1) #interval for breakeven point

c = 6*np.sqrt(x)
r = (3/16)*x**2

a = np.maximum(c,r)
b = np.minimum(c,r)

plt.plot(x, c, color='black', linewidth='2', label='C\'(x)') 
plt.plot(x, r, color='red', linewidth='2', label='R\'(x)')
plt.fill_between(x,a,b, color='green', alpha=0.4)
plt.legend()
plt.show()


