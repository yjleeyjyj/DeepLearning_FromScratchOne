# 1-5-1. 넘파이 가져오기
import numpy as np

# 1-5-2. 넘파이 배열 생성하기
x = np.array([1.0, 2.0, 3.0])
print(x)

type(x)

# 1-5-3. 넘파이의 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

x + y
x - y
x * y
x / y

    # Broadcast
x = np.array([3.0, 4.0, 5.5])
x % 2

# 1-5-4. 넘파이의 N차원 배열
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)

a.shape
a.dtype
    # 형상이 같은 행렬이면, 행렬의 산술 연산 가능. (대응되는 원소별로 계산)
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[3.0, 0.0], [0.0, 6.0]])

a + b
a * b
    # Broadcast
a = np.array([[1.0, 2.0], [3.0, 4.0]])
a % 2.5

# 브로드캐스트 Broadcast : 형상이 다른 numpy 배열 간의 연산을 지원. 똑똑하구먼!
a = np.array([[1,2],[3,4]])

a * 10

a = np.array([[1,2],[3,4]])
b = np.array([20, 10])

a * b

# 1-5-6. 원소 접근
x = np.array([[51,55], [14, 19], [0, 4]])

x[0][0]
x[1]

    # for문으로도 접근 가능
for row in x:
    print(row)
    for ele in row:
        print(ele)

    # 인덱스를 배열로 지정하여 처리
x1 = x.flatten()
print(x1)

        # 인덱스가 0, 2, 4인 row 배열만 얻기
x1[np.array([0,2,4])]

    # 특정 조건을 만족하는 원소만 얻기
x > 15
x[x>15]

x1 > 15
x1[x1 > 15]
