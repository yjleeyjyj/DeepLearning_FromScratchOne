#
# NAND OR perceptron 구현하기
#

import numpy as np
import matplotlib.pyplot as plt

# NAND
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

NAND(0, 0)
NAND(0, 1)
NAND(1, 0)
NAND(1, 1)

# OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3

    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0

OR(0, 0)
OR(0, 1)
OR(1, 0)
OR(1, 1)

