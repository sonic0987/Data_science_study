#3.5 출력층 설계하기
import numpy as np

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)

"""print(exp_a)"""

sum_exp_a = np.sum(exp_a)

"""print(sum_exp_a)"""

y = exp_a / sum_exp_a

"""print(y)"""

def softmax2(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y 

a = np.array([1010, 1000, 990])
b = np.exp(a) / np.sum(np.exp(a))

"""print(b)"""

c = np.max(a)
b = np.exp(a - c) / np.sum(np.exp(a - c))

"""print(b)"""

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)

print(y)
print(np.sum(y))