#
# j
#

import numpy as np
import matplotlib.pyplot as plt

# matrix multiply 행렬 곱 2x2 @ 2x2
A = np.array([ [1,2], [3,4] ])
A.shape

B = np.array([ [5,6], [7,8] ])
B.shape

np.dot(A, B)

# 2x3 @ 3x2
A = np.array([ [1,2,3], [4,5,6] ])
B = np.array([ [1,2], [3,4], [5,6] ])

A.shape
B.shape

np.matmul(A, B)
A @ B

(A @ B).shape

# 3x2 @ 2
A = np.array([[1,2], [3,4], [5,6]])
A.shape

B = np.array([7,8])
B.shape

A @ B
(A @ B).shape

# 신경망 행렬 곱으로 구현하기
X = np.array([1,2])
X.shape

W = np.array([[1,3,5], [2,4,6]])
print(W)
W.shape

Y = X @ W
print(Y)
