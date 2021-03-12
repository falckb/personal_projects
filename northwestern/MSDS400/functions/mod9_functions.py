from sympy import symbols, ln, linsolve, Abs, lambdify, S, nonlinsolve, E, sqrt, Derivative
from sympy.solvers import solve
from mpmath import pi

def partial_derivatives():
    """Input function, get partial derivatives with respect to each
    """
    x, y = symbols('x, y')
    f_x_y = x**4+y**4-x*y #function

    partial_f_x = f_x_y.diff(x)
    print(f'Partial derivative of {f_x_y} with respect to x: {partial_f_x}')

    partial_f_y = f_x_y.diff(y)
    print(f'Partial derivative of {f_x_y} with respect to y: {partial_f_y}')

partial_derivatives()



def critical_points():
    x, y = symbols('x, y')

    f_x_y = 90*x**0.84*y**0.16 #function
    partial_x = f_x_y.diff(x)
    partial_y = f_x_y.diff(y)

    results = linsolve([partial_x, partial_y], x, y)

    print(f"The x and y value for critical points are {results}")

#critical_points()



def D(func, x_sym, y_sym, x_crit, y_crit):
    # Calculate the discriminant for a given function
    f_x_x = func.diff(x_sym, x_sym)
    f_y_y = func.diff(y_sym, y_sym)
    f_x_y = func.diff(x_sym, y_sym)
    
    # Create callable functions for each of the derivitives we created
    lambd_x_x = lambdify([x_sym, y_sym], f_x_x)
    lambd_y_y = lambdify([x_sym, y_sym], f_y_y)
    lambd_x_y = lambdify([x_sym, y_sym], f_x_y)

    fxx_ab = lambd_x_x(x_crit, y_crit)
    fyy_ab = lambd_y_y(x_crit, y_crit) 
    fxy_ab = lambd_x_y(x_crit, y_crit)

    d = fxx_ab * fyy_ab - Abs(fxy_ab)**2

    print(f"The discriminant of our critical value is {d}")

    if d < 0:
        print("This is a saddle point")
    elif d > 0:
        if fxx_ab < 0:
            print("This is relative maxima")
        else:
            print("This is a relative minima")


def nonlinear_critical_points():
    x, y = symbols('x, y', real=True)

    f_x_y = 90*(x**0.84)*(y**0.16)
    partial_x = f_x_y.diff(x)
    partial_y = f_x_y.diff(y)

    # Get nonlinear solution and remove imaginary numbers
    results = nonlinsolve([partial_x, partial_y], [x, y])

    print(f"The x and y value for critical points are {results}")

    for result in list(results):
        if result[0].is_real and result[1].is_real:  # Ignore any solutions that are not real numbers
            print(f"Analyzing critical point {result}")
            D(f_x_y, x, y, result[0], result[1])  

#nonlinear_critical_points()


def max_min():

    x, y = symbols('x y')
    x = 1800 - y #solve constraint equation in terms of x

    # Plug in the equation of x in the z equation
    z = 2*(1800-y)**2+(1800-y)*y+8*y**2+600
    dz = Derivative(z, y).doit()

    # To calculate the maximum we have to find where dz = 0
    # We will use the equation of dz above and the sympy solve function to 
    # solve for y
    y_value = solve(dz, y)
    print("y =", round(y_value[0]))

    # Calculate x by substituting the value for y
    x_value = x.subs({y:y_value[0]})
    print("x =",round(x_value))

    # Calculate z by substituting the value for y
    z_value = z.subs({y:y_value[0]})
    print("z = ",round(z_value))
    print('Note position of x and y in answer...\n')

#max_min()