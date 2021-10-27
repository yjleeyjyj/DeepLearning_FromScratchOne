#
# mnist 손글씨 숫자 데이터셋으로 신경망의 추론 과정 재현하기
#

import os, sys

from numpy.core.numeric import identity
from mnist import load_mnist
import numpy as np
import pickle
sys.path.append(os.pardir)
from sigmoid_function import sigmoid
from CNN_with_matrix import identity_function

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = x @ W1 + b1
    z1 = sigmoid(a1)
    a2 = z1 @ W2 + b2
    z2 = sigmoid(a2)
    a3 = z2 @ W3 + b3
    y = identity_function(a3)

    return y

if __name__ == '__main__':
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y) # 확률이 가장 높은 인덱스의 원소 찾기
        if p == t[i]:
            accuracy_cnt += 1
    
    print('Accuracy: '+ str(float(accuracy_cnt) / len(x)))

#
# batch를 사용하여 mnist 데이터셋 신경망 구현하기
#

x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy: " + str( float(accuracy_cnt) / len(x) ))

