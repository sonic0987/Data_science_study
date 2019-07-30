#3.2.2 계단 함수 구현하기
import numpy as np

def step_function1(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([1, -1, 0])

print(step_function2(x))

#step_function2 상세
x = np.array([-1.0, 1.0, 2.0])

y = x > 0

print(y)

y = y.astype(np.int)

print(y)