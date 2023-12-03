import structures.Structures as STRUCTURES
from functions import PointOnLine as CL
from sympy import symbols, Eq, solve

def system_of_eqs(m1, b1, m2, b2):

    x,y = symbols('x y')

    eq1 = Eq(y = m1*x + b1)
    eq2 = Eq(y = m2*x + b2)

    return solve((eq1, eq2), (x, y))

Line1 = CL.createLine(); Line2 = CL.createLine()

system_of_eqs(Line1.m, Line1.b, Line2.m, Line2.b) # A common point that is both on Line1 and Line2
