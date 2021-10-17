#
# 함수로 AND perceptron 논리회로 구현하기
#

# 가중치 weight & 임계값 theta를 도입한 AND 게이트 구현하기
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp > theta:
        return 1
    else:
        return 0

AND(0, 0)
AND(0, 1)
AND(1, 0)
AND(1, 1)

# 가중치 weight & 편향 bias b을 도입한 AND 게이트 구현하기
import numpy as np

def AND_bias(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w*x) + b
    if tmp > 0:
        return 1
    else:
        return 0

AND_bias(0, 0)
AND_bias(0, 1)
AND_bias(1, 0)
AND_bias(1, 1)
