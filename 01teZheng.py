import numpy as np
from numpy.linalg import eig

A = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
values, vectors = eig(A)  # 求特征值与特征向量
print(values)
print(vectors)
print(A @ vectors.T[0])  # 验证是否满足
print(values[0] * vectors.T[0])
