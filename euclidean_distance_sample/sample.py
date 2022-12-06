import numpy as np

a = np.array([1, 2])
b = np.array([2, 3])
distance = np.linalg.norm(b-a)
print(distance)