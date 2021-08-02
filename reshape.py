import numpy as np

a = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]], order='C')

print(a.reshape(12, 1))
print(a.reshape(3, 4))
print(a.reshape(2, 6))
print(a.reshape(6, 2))
