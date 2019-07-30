#4.4 기울기
import numpy as np

def function_2(x):

    return x[0] ** 2 + x[1] ** 2

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

grad1 = numerical_gradient(function_2, np.array([3.0, 4.0]))
grad2 = numerical_gradient(function_2, np.array([0.0, 2.0]))
grad3 = numerical_gradient(function_2, np.array([3.0, 0.0]))

"""print(grad1)
print(grad2)
print(grad3)"""

#4.4.1 경사 하강법
def gradient_descent(f, init_x, lr = 0.01, step_num = 100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

init_x = np.array([-3.0, 4.0])

grad_desc = gradient_descent(function_2, init_x= init_x, lr= 0.1, step_num= 100)

"""print(grad_desc)"""

#4.4.2 신경망에서의 기울기
import sys, os
sys.path.append(os.pardir)
import practice_function as pr

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):

        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = pr.softmax(z)
        loss = pr.cross_entropy_error(y, t)

        return loss

net = simpleNet()
"""print(net.W)"""

x = np.array([0.6, 0.9])
p = net.predict(x)

"""print(p)"""

arg = np.argmax(p)

"""print(arg)"""

t = np.array([0, 0, 1])
net_loss = net.loss(x, t)

"""print(net_loss)"""

def f(W):

    return net.loss(x, t)

dW = numerical_gradient(f, net.W)

print(dW)