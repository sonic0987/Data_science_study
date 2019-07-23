#3.6.3 배치 처리
import sys, os
sys.path.append(os.pardir)
from MNIST.mnist import load_mnist
import numpy as np
import pickle

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)

    return x_test, t_test

def init_network():
    with open("MNIST\\mnist.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):    
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = pr.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = pr.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = pr.softmax(a3)

    return y

x, _ = get_data()
network = init_network()

W1, W2, W3 = network['W1'], network['W2'], network['W3']

"""print(x.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)"""

x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)

    p = np.argmax(y_batch, axis = 1)
    
    accuracy_cnt += np.sum(p == t[i:i+batch_size])