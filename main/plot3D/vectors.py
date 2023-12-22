import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

A = np.array([1, 2, 3])
B = np.array([-2, 1, 4])
C = A+B

#Vector 1 A
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='r', arrow_length_ratio=0.1, label='A')
#Vector 2 B
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='b', arrow_length_ratio=0.1, label='B')
#Vector1 A + Vector2 B
ax.quiver(0, 0, 0, C[0], C[1], C[2], color='y', label='A+B')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Vector Plot')

plt.show()