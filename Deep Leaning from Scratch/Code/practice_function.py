import numpy as np

def sigmoid(value):
    return 1 / (1 + np.exp(-value))

def relu(value):
    return np.maximum(0, value)

def identity_function(value):
    return value

def softmax(value):
    c = np.max(value)
    exp_a = np.exp(value - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def softmax2(value):
    exp_a = np.exp(value)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y 

if __name__ == "__main__":
    aowiega = 1

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size - 1):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad