#
# 활성화 함수 '시그모이드 함수 sigmoid' 구현하기
#

import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 시그모이드 함수 그래프에 표현하기
x = np.arange(-5.0, 5.0, 0.01)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
