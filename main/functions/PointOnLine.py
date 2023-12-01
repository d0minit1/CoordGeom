import Structures as STRUCTURES

#https://www.mathsisfun.com/algebra/linear-equations.html

def createLine():
     cLine = input('Give the parameters of a line!\n m, b\n')
     parameters = cLine.split(',')

     
     if len(parameters) == 2:
        m = float(parameters[0])
        b = float(parameters[1])
     else:
        print(f'Invalid input format. Provide exactly {len(parameters)} components separated by commas.')

     return STRUCTURES.Line(m, b)

def createPoint():
     cPoint = input('Give the parameters of a point!\n x, y\n')
     parameters = cPoint.split(',')
     
     if len(parameters) == 2:
        x = float(parameters[0])
        y = float(parameters[1])
     else: 
        print(f'Invalid input format. Provide exactly {len(parameters)} components separated by commas.')

     return STRUCTURES.Point(x, y)

def isPointOnLine(x, y, Line):
        if Line is not None:
            m = Line.m
            b = Line.b

            if y == m * x + b:
                print(f'Point ({x};{y}) is on the line!')
            else:
                print(f'Point ({x};{y}) is not on the line!')

line = createLine()
point = createPoint()
isPO = isPointOnLine(point.x, point.y, line)