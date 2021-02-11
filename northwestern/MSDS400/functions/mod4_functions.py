import numpy as np
from itertools import combinations

def bayes_thm(P_A, P_B_given_A, P_B):

    numer = P_B_given_A*P_A
    denom = P_B

    answer = numer/denom
    print(answer)

pop=np.array([.13,.22,.47,.18])
collision=np.array([.14,.05,.02,.08])
weightedsum=sum(pop*collision)

bayes_thm(0.13, 0.14, weightedsum)


def ques9():
    prob_covid = 0.86
    true_pos = 0.93
    false_pos = 0.03
    numer = prob_covid*true_pos
    denom = (prob_covid*true_pos)+((1-prob_covid)*false_pos)
    answer = numer/denom

    print(answer)

