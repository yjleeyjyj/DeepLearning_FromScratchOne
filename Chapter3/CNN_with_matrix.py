#
# 행렬 곱으로 각 층의 신호전달 구현하기 (page85-88)
#

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import identity

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
W1 = np.array([ [0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = X @ W1 + B1

Z1 = sigmoid(A1)

W2 = np.array([ [0.1, 0.4], [0.2, 0.5], [0.3, 0.6] ])
B2 = np.array([0.1, 0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = Z1 @ W2 + B2
Z2 = sigmoid(A2)

def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = Z2 @ W3 + B3
Y = identity_function(A3)

#
# 행렬 곱으로 각 층의 신호전달 구현하기 종합 (page89)
#

def init_network():
    network = {}
    network['W1'] = np.array([ [0.1, 0.3, 0.5], [0.2, 0.4, 0.6] ])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([ [0.1, 0.4], [0.2, 0.5], [0.3, 0.6] ])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = x @ W1 + b1
    z1 = sigmoid(a1)
    a2 = z1 @ W2 + b2
    z2 = sigmoid(a2)
    a3 = z2 @ W3 + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
