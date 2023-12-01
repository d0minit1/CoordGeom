import Structures as STRUCTURES

"""

https://www.mathsisfun.com/algebra/line-equation-2points.html

Equation of a line intersects two specific points -> y-y1 = m(x-x1) 

Proof by inspection:

 Lets have two points (x1;y1)(x2;y2) set on a line thus are collinear to one another. Taking the point is closer to the the base(0;0), 
 we can reach the farther point by moving x-units along and y-units up forming a right-angled triangle. The slope (gradient) of the line is relative to the x-axis
 The angle it closes with this axis is defined by the arctangent of the corresponding legs of the triangle. Taken this angle the arctangent would look like this:
 arctan = (y2-y1)/(x2-x1) --> will give the value of the slope in angles.
 Let call that 'm'
 m = (y2-y1)/(x2-x1)
 y-y1 = (y2-y1)/(x2-x1)(x-x1)
 (y-y1)/(x-x1) = (y2-y1)/(x2-x1) --> another way to calculate the equation of a line, but the above-mentioned is more elegant to use

"""

def equationOrder(x1, y1, x2, y2):
    try:
        m = (y2-y1)/(x2-x1)
        return f'y - {round(y1, 1)} = {round(m, 1)}x + {round(m*(-x1), 1)}'
    except:
        print('The points are identical')

def createPoints():
    pointCom = input("Give the components of a point\nFormat: x, y\n")
    components = pointCom.split(',')

    if len(components) == 2:
        x = float(components[0])
        y = float(components[1])

        return STRUCTURES.Point(x, y)
    else:
        print(f'Invalid input format. Provide exactly {len(components)} components separated by commas.')

point1 = createPoints()
point2 = createPoints()

x1, y1 = point1.x, point1.y
x2, y2 = point2.x, point2.y

result = equationOrder(x1, y1, x2, y2)
print(result)