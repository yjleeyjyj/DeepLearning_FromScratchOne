#
# 활성화 함수로 '계단 함수 step function'을 사용하는 신경망, '퍼셉트론 perceptron' 구현하기.
#

import numpy as np
import matplotlib.pyplot as plt

# 실수 부동소수점 범위 내의 인자만 받을 수 있는 계단함수
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# numpy 배열도 입력 받을 수 있는 계단함수
def step_function_numpy(x):
    y = x > 0
    return y.astype(np.int)

# 계단 함수의 그래프 그리기
x = np.arange(-5.0, 5.0, 0.01)
y = step_function_numpy(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
