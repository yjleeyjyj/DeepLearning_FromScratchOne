#
# matplotlib 사용 매뉴얼
#

# 1-6-1. 단순한 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

    # 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 벡터 생성 
y = np.sin(x)

    # 그래프 그리기
plt.plot(x, y)
plt.show()

# 1-6-2. pyplot의 기능
 
import numpy as np
import matplotlib.pyplot as plt

    # 데이터 준비
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

    # 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") # cos함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend()
plt.show()

# 1-6-3. 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:\\Users\\yjlee\\OneDrive\\Programming_Study\\DeepLearning_FromScratch1\\Chapter1\\cactus.jpg')

plt.imshow(img)
plt.show()
