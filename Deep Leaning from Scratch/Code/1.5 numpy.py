#1.5 넘파이
import numpy as np

"""#1.5.2 넘파이 배열 생성하기
x = np.array([1.0, 2.0, 3.0])

print(x)

print(type(x))

#1.5.3 넘파이의 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

#1.5.4 넘파이의 N차원 배열
A = np.array([[1, 2], [3, 4]])

print(A)

print(A.shape)

print(A.dtype)

B = np.array([[3, 0], [0, 6]])

print(A + B)

print(A * B)

#1.5.5 브로드캐스트
A = np.array([[1, 2], [3, 4]])

B = np.array([10, 20])

print(A * B)"""

#1.5.6 원소 접근
X = np.array([[51, 55], [14, 19], [0, 4]])

print(X)

print(X[0])

print(X[0][1])

for row in X:
    print(row)

X = X.flatten()

print(X)

print(X[np.array([0, 2, 4])])

print(X > 15)

print(X[X > 15])