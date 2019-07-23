#3.3 다차원 배열의 계산
import numpy as np

#3.3.1 다차원 배열
A = np.array([1, 2, 3, 4])
"""print(A)

print(np.ndim(A))

print(A.shape)

print(A.shape[0])"""

B = np.array([[1, 2], [3, 4], [5, 6]])

"""print(B)

print(np.ndim(B))

print(B.shape)"""

#3.3.2 행렬의 곱
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

"""print(np.dot(A, B))"""

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])

"""print(np.dot(A, B))"""

#3.3.3 신경망에서의 행렬 곱
X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])

Y = np.dot(X, W)

print(Y)