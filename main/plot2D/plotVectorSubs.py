import matplotlib.pyplot as plt
import numpy as np

A = np.array([5,-1])
B = np.array([2,7])
C = A + B

plt.plot([0, A[0]], [0, A[1]], 'b', label='A')
plt.plot([0, B[0]] + A[0], [0, B[1]] + A[1], 'r', label='B')
plt.plot([0, C[0]], [0, C[1]], 'y', label='A+B')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Vector addition')

plt.legend()
plt.axis('square')
plt.axis((-10,10,-10,10))
plt.grid()
plt.show()
