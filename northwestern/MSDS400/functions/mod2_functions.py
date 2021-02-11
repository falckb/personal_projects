import numpy as np
from numpy.linalg import linalg, inv

def system_solver_mod2():
    answers_matrix = [252,0,0]
    answers_matrix = np.matrix(answers_matrix)
    answers_matrix = np.transpose(answers_matrix)

    coeffs_matrix = [[1,1,1,1],[-1,3,0,0],[0,0,-1,2]]
    coeffs_matrix = np.matrix(coeffs_matrix)

    inv_coeff = inv(coeffs_matrix)
    print('Inverse is : \n' , inv_coeff)
    check = np.dot(inv_coeff, coeffs_matrix)
    check = np.rint(check)
    print('Just to verify: \n' , check)

    result = np.dot(inv_coeff, answers_matrix)
    print('\n Solution is: \n' , result)

def better_system_solver_mod2():
    answers_matrix = [15000,76000,44000]
    answers_matrix = np.matrix(answers_matrix)
    answers_matrix = np.transpose(answers_matrix)

    coeffs_matrix = [[1,1,1],[8,6,4],[4,6,2]]
    coeffs_matrix = np.matrix(coeffs_matrix)

    result = linalg.solve(coeffs_matrix, answers_matrix)
    print('The solution is: \n' , result)

better_system_solver_mod2()

def simple_dot_prod_mod2():
    m1 = np.matrix([[6,8,1],[6,4,1],[5,7,1]])
    m1 = np.transpose(m1)
    print(m1)
    m2 = np.matrix([[4,3],[4,5],[2,2]])
    print(m2)
    result = np.dot(m1, m2)
    result = np.transpose(result)
    print(result)

def cramers_rule_2x2():
    # Pay attention to order of variables!!!
    a1 = -5
    a2 = -2
    b1 = -1
    b2 = 2
    c1 = -28
    c2 = -4
    Dx = [[c1,b1],[c2,b2]]
    Dx = np.matrix(Dx)
    Dx = np.linalg.det(Dx)
    Dx = np.rint(Dx)
    Dy = [[a1,c1],[a2,c2]]
    Dy = np.matrix(Dy)
    Dy = np.linalg.det(Dy)
    Dy = np.rint(Dy)
    D = [[a1,b1],[a2,b2]]
    D = np.matrix(D)
    D = np.linalg.det(D)
    D = np.rint(D)
    x = Dx / D
    y = Dy / D
    print('\nDx = ',Dx,'     Dy = ',Dy,'     and D = ',D)
    print('x = ' ,x,'     y = ',y,'\n')

def det_fix(A):
    A = np.matrix(A)
    A = np.linalg.det(A)
    A = np.rint(A)
    return A

def cramers_rule_3x3():
    a1=2
    a2=4
    a3=-4
    b1=-3 
    b2=-2
    b3=-1
    c1=6
    c2=-6
    c3=-5
    d1=-8
    d2=-26
    d3=9
    D = [[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]]
    det_fix(D)
    print(D)


def calc_det_3x3():
    a11=2
    a12=-3
    a13=-8
    a21=4
    a22=-2
    a23=-26
    a31=-4
    a32=-1
    a33=9
    A = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
    A = np.matrix(A)
    detA = np.linalg.det(A)
    detA = np.rint(detA)
    print(A)
    print(detA)
