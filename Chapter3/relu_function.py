#
# ReLU (Rectified Linear Unit) 함수 구현
#

import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

