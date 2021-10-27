#
# SoftMax function 소프트맥스 함수 구현하기
#

import numpy as np
import matplotlib.pyplot as plt

# softmax function
a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)
print(exp_a)

exp_sum_a = np.sum(exp_a)

y = exp_a / exp_sum_a
print(y)

def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x

    return y

# overflow 오버플로우 문제 해결하기

a = np.array([1010, 1000, 990])
exp_a = np.exp(a)
# np.exp(a) / np.sum(np.exp(a)) 제대로 계산 안됨. OVERFLOW

a = np.array([1010, 1000, 990])
c = np.max(a)
exp_a = np.exp(a - c)

sum_exp_a = np.sum(exp_a)
y = exp_a / sum_exp_a
print(y)

def softmax_overflow_control(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x

    return y