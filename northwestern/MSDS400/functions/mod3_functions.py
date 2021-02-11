from scipy.optimize import linprog
import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy as np
from numpy import *
import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

def max_ff():

    # Coefficients of the objective function (convert to -f(x) if maximizing)
    z = [-2,-3,-3,-1]

    # Coefficients of the left-hand side of the inequalities
    lhs = [[1,2,2,1],[0,2,2,0]]

    # Coefficients of the right-hand side of the inequalities
    rhs = [91,70]

    # Set variable bounds
    q_bounds = (5,15)
    r_bounds = (8,26)
    w_bounds = (7,21)
    t_bounds = (3,9)

    # Not sure what this does, ask about it
    method='simplex'

    # Does the thing
    res = linprog(c=z, A_ub=lhs, b_ub=rhs, bounds=(q_bounds,r_bounds,w_bounds,t_bounds))
    print('SciPy Optimize Optimal value: ', res.fun, '\n q, r, w, t : ', res.x)
    print('\n')

def graph_ineq():
    #Use arange instead of linspace, same deal
    x = arange(-10,10,1)
    y = x-3
    z = -.6*x-3
    #Create plot area
    xlim(-10,10)
    xlabel('x-axis')
    ylabel('y-axis')
    #Axis lines
    hlines(0,-10,10,color='black')
    vlines(0,-10,10,color='black')
    grid(True)
    
    plot(x,y)
    plot(x,z)

    fill_between(x,y,z, color='b')
    title('Shaded Area is the solution to the set of inequalities')
    show()

def max_graphically():

    #Set graph limits
    x=arange(0,100,10)
    y=arange(0,100,10)

    #Constraint Equations
    y1=(841/43)-(11/43)*x
    y2=35+0*x
    x1=23+0*y
    
    # Plot limits must be set for the graph.
    xlim(0,50)
    ylim(0,50)
    # Plot axes need to be labled,title specified and legend shown.
    xlabel('x-axis')
    ylabel('y-axis')
    title('Shaded Area Shows the Feasible Region')

    # Plot all lines
    plot(x,y1, 'b', label='Sugar Inequality')
    plot(x,y2, 'r', label='r=33')
    plot(x1,y,'p', label='n=25')
    legend()

    x=[0,0,23,23]
    y=[0,(841/43),(588/43),0]

    fill(x,y, color='grey', alpha=0.2)
    show()

    #Find optimal solution
    obj= matrix([6250,6900])
    obj= transpose(obj)
    corners= matrix([x,y])
    corners= transpose(corners)
    result= dot(corners,obj)
    print ('Value of Objective Function at Each Corner Point:\n', result)

def scipy_max_general():

    # Coefficients of the objective function (convert to -f(x) if maximizing)
    z = [-11,-13,-15]

    # Coefficients of the left-hand side of the inequalities
    lhs = [[5,8,10],[6,9,13]]

    # Coefficients of the right-hand side of the inequalities
    rhs = [6980,8520]

    # Set variable bounds
    a_bounds = (0,None)
    b_bounds = (0,None)
    c_bounds = (0,None)

    # Just a solving algorithm, there are others. Need the method=method to make it work
    method='simplex'

    # Does the thing
    res = linprog(c=z, A_ub=lhs, b_ub=rhs, bounds=(a_bounds,b_bounds,c_bounds), method=method)
    print('SciPy Optimize Optimal value: ', res.fun, '\n a, b, c : ', res.x)
    print('\n')

def pulp_method():
    # declare your variables
    A = LpVariable("A", 0, None) # x1>=0
    B = LpVariable("B", 0, None) # x2>=0
    C = LpVariable("C", 30, None) # x2>=0

    # defines the problem
    prob = LpProblem("problem", LpMaximize)

    # defines the constraints
    prob += A + B + C <= 210  # total item stock
    prob += A == 2*B  # exactly twice as many DVD players as Tonos

    # defines the objective function to minimize
    prob += 450*A + 2000*B + 750*C

    # solve the problem
    status = prob.solve()
    LpStatus[status]

    # print the results
    print('Pulp Solution for A and B')
    print('A: ',value(A))
    print('B: ',value(B))
    print('C: ',value(C))

    # print optimal solution
    print(f'The Optimal Solution is: {450*value(A) + 2000*value(B) + 750*value(C)}')
    print(LpStatus[status])

pulp_method()
