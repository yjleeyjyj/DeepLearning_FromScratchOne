#
# numpy로 다차원 배열 = 행렬 matrix 구현하기
#

import numpy as np
import matplotlib.pyplot as plt

# first dimension
A = np.array([1,2,3,4])
print(A)
np.ndim(A)
A.shape
A.shape[0]

# second dimension
B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape
B.shape[1]
