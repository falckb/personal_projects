import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy
from numpy import linspace
import scipy
from scipy import stats

def func_computation(x):
    answer = 4-(4*x)
    print('The answer is: ' + str(answer))

def graph_lineq():
    x = linspace(0, 1000, 50) #refers to start, stop, number of values to plug into the function between start and stop (print(x)) to show
    y = 24000+18*x
    z = 120*x
    plot(x,y)
    plot(x,z)
    legend(('C(x)=24000+18x', 'R(x)=120x'))
    title('Breakeven Analysis')
    show()

def values_table():
    for i in range(-10, 11):
        value = 4-i
        print(str(i) + '    ' + str(value))

def slope_intercept_form():
    x = 0
    x1 = 1
    x2 = 2
    y1 = 36
    y2 = 58
    slope = (y2-y1)/(x2-x1)
    y = y1 + slope*(x-x1)
    print('The slope is ' + str(slope))
    print('The y intercept is ' + str(y))


def scatterplot_func():
    x = []
    for i in range(4, 19):
        x.append(i)
    y = [42.96, 41.32, 39.88, 38.14, 36.1, 34.76, 34.52, 30.28, 28.14, 29.3, 26.76, 26.52, 22.68, 21.74, 20.9]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    predict_20 = 20*slope + intercept
    print('Slope = ' + str(round(slope, 3)))
    print('We predict ' + str(predict_20) + ' for x=20')
    print('Intercept = ', str(round(intercept, 1)))
    print('Correlation coefficient = ', str(round(r_value, 3)))
    scatter(x,y)
    show()

def scatterplot_func2():
    x = []
    for i in range(0,6):
        x.append(i)
    y = [177, 193, 211, 223, 250, 286]
    print(x)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    predict_2024 = 13*slope + intercept
    predict_2044 = 31*slope + intercept
    print('Slope: ' + str(round(slope, 2)) + ' and Intercept: ' + str(round(intercept, 2)))
    print('In 2024, sales will be ' + str(predict_2024))
    print('In 2044, sales will be ' + str(predict_2044))


graph_lineq()