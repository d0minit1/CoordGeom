import structures.Structures as STRUCTURES

"""

https://www.mathsisfun.com/algebra/line-parallel-perpendicular.html

Two lines are perpendicular if the product of their slopes gives -1 (me*mf = -1)
In addition, two lines are paralell whether their slopes are equivalent (me=mf)

"""

def LineSlope1():
    cLineSlope1 = float(input('Give the slope of a line!\n m \n'))
    return cLineSlope1

def LineSlope2():
   cLineSlope2 = float(input('Give the slope a line!\n m \n'))
   return cLineSlope2

def compare(Slope1, Slope2):
    
    if Slope1 == Slope2:
        print('The two lines are paralell to each other!')
    elif Slope1 * Slope2 == -1:
        print('The two lines are perpendicular to each other!')
    else:
        print('Neither')

compare(LineSlope1(), LineSlope2())