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
    init_practice_function

def cross_entropy_error(y, t):
    delta = 1e-7
    
    return -np.sum(t * np.log(y + delta))

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)