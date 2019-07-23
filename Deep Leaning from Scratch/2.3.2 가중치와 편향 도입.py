#2.3.2 가중치와 편향 도입
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(w * x)

print(np.sum(w * x))

print(np.sum(w * x) + b)