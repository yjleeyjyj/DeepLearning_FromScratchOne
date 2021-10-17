#
# AND OR NAND sigle-layer perceptron 쌓아서
# XOR multi-layer perceptron 만들기
#

import numpy as np
from NAND_OR_perceptron import NAND, OR
from AND_perceptron import AND

# XOR 구현
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

XOR(0, 0)
XOR(0, 1)
XOR(1, 0)
XOR(1, 1)
