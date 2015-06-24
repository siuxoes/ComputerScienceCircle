__author__ = 'Siuxoes'

import math

L = float(input())
A = float(input())

def pendulum(T):
    return L * math.cos(A * math.cos(T * math.sqrt(9.8 / L))) - L * math.cos(A)

for x in range(10):
    print(pendulum(x))

