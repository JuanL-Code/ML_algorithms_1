import numpy as np
C = np.array([[2.0, -1.0, 3.0, 5.0], 
[2, 2, 3, 7],
[-2, 3, 0, -3]])
T = np.copy(C)

print(T)

T[2] = T[2] + T[1]
print(T)

T[1] -= T[0]
print(T)

T[2] = T[2] - (5.0/3.0)*T[1]
print(T)