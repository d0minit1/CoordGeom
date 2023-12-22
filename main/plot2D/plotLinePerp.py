import matplotlib.pyplot as plt
import numpy as np

slope_line1 = 2
intercept_line1 = 1

slope_line2 = -0.5
intercept_line2 = 6

x_values = np.array([1, 2, 3, 4, 5])

y_values_line1 = slope_line1 * x_values + intercept_line1
y_values_line2 = slope_line2 * x_values + intercept_line2

plt.plot(x_values, y_values_line1, label='Line 1', color='blue', marker='o')

plt.plot(x_values, y_values_line2, label='Line 2', color='red', marker='s')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Perpendicular Lines')

plt.gca().set_aspect('equal', adjustable='box')

A = np.array([[slope_line1, -1], [slope_line2, -1]])
B = np.array([-intercept_line1, -intercept_line2])

intersection_point = np.linalg.solve(A, B)

plt.scatter(*intersection_point, color='black', marker='x', label='Intersection Point')

plt.legend()

plt.xlim(0, 6)
plt.ylim(0, 8)

plt.grid()
plt.show()

print(f"Intersection Point: {intersection_point}")
