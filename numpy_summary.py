import numpy as np

# Numpy 는 Python에서 벡터, 행렬 등 수치 연산을 수행하는 선형대수(Linear algebra) 라이브러리

# Numpy에서 오브젝트는 동차 다차원 배열이라고 한다.
# Numpy에서는 모든 배열의 값이 기본적으로 같은 타입이어야 한다.
# Numpy에서는 각 차원(Dimension)을 축(axis)이라고 표현합니다.

a = np.arange(15).reshape(3, 5)
# ndarray.shape : 배열의 각 축(axis)의 크기
# ndarray.ndim : 축의 개수(Dimension)
# ndarray.dtype : 각 요소(Element)의 타입
# ndarray.itemsize : 각 요소(Element)의 타입의 bytes 크기
# ndarray.size : 전체 요소(Element)의 개수
print("Numpy objecct")
print(a)
print()

print("array 속성")
print(f"a.shape : {a.shape}")
print(f"a.ndim : {a.ndim}")
print(f"a.dtype : {a.dtype}")
print(f"a.itemsize : {a.itemsize}")
print(f"a.size : {a.size}")

# a = np.array(1, 2, 3, 4)  # WRONG
# print(a)
# ValueError: only 2 non-keyword arguments accepted

a = np.array([1, 2, 3, 4])  # RIGHT
print(a)
print()

print("np.zeros(shape): 0으로 된 n차원 배열 생성")
# [3,4] 크기의 배열을 생성하여 0으로 채움
print(np.zeros((3, 4)))
print()

print("np.ones(shape) : 1로 구성된 n차원 배열 생성")
# [2,3,4] 크기의 배열을 생성하여 1로 채움
print(np.ones((2, 3, 4), dtype=np.int16))
print()

print("np.empty(shape) : 초기화되지 않은 n차원 배열 생성")
# 초기화 되지 않은 [2,3] 크기의 배열을 생성
print(np.empty((2, 3)))
print()
print()

print("연속적인 데이터 생성")
print()
print("np.arange(): N 만큼 차이나는 숫자 생성")
# 10이상 30미만 까지 5씩 차이나게 생성
print(np.arange(10, 30, 5))
print()

# 0이상 2미만 까지 0.3씩 차이나게 생성
print(np.arange(0, 2, 0.3))
print()

# 0~99까지 100등분
x = np.linspace(0, 99, 100)
print(x)
print()

print("ndarray.reshape() : 데이터는 그대로 유지한 채 차원을 변경")
# 변경전 데이터 개수와 차원 변경후 데이터 개수가 일치 해야함
a = np.arange(6)
print(a)
print()

b = np.arange(12).reshape(4, 3)
print(b)
print()

c = np.arange(24).reshape(2, 3, 4)
print(c)
print()

print("numpy 수치 연산")
# Numpy 는 기본적으로 행렬의 연산을 함

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(f"a : {a}")
print(f"b : {b}")

# a에서 b에 각각의 원소를 -연산
c = a - b
print(f"a - b : {c}")

# b 각각의 원소에 제곱 연산
print(f"b ** 2 : {b ** 2}")

# a 각각의 원소에 *10 연산
print(f"10 * np.sin(a) : {10 * np.sin(a)}")

# a 각각의 원소가 35보다 작은지 Boolean 결과
print(f"a < 35 : {a < 35}")
print()

print("2차원 배열의 곱")
# * : 각각의 원소끼리 곱셈 (Elementwise product, Hadamard product)
# @ : 행렬 곱셈 (Matrix product)
# dot() : 행렬 내적 (dot product)

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(f"A : {A}")
print(f"B : {B}")
print()
print("A * B")
print(A * B)
print("A @ B")
print(A @ B)
print("A.dot(B)")
print(A.dot(B))
print()

print("수치연산 진행할 때 각각의 .dtype이 다르면 타입이 큰쪽(int < float < complex)으로 자동으로 변경")

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
print(f"a : {a}")
print(f"b : {b}")
print(f"b.dtype.name : {b.dtype.name}")

# a(int), b(float) 연산 시 float로 upcasting
c = a + b
print(f"c = a+b => {c}")

print(f"c.dtype.name : {c.dtype.name}")

d = np.exp(c * 1j)
print(f"d = np.exp(c * 1j) : {np.exp(c * 1j)}")
# 복소수 연산 시 complex(복소수)로 upcasting

print(f"d.dtype.name : {d.dtype.name}")
print()

print(".sum(), .min(), .max(), .cumsum() 연산")
a = np.arange(8).reshape(2, 4) ** 2
print(f"a : {a}")

# 모든 요소의 합
print(f"a.sum() : {a.sum()}")

# 모든 요소 중 최소값
print(f"a.min() : {a.min()}")

# 모든 요소 중 최대값
print(f"a.max() : {a.max()}")

# 모든 요소 중 최대값의 인덱스
print(f"a.argmax() : {a.argmax()}")

# 모든 요소의 누적합
print(f"a.cumsum() : {a.cumsum()}")

print("axis 값을 통해 축을 기준으로 연산이 가능하다")
# axis=0은 shape에서 첫번째부터 순서대로 해당
b = np.arange(12).reshape(3, 4)
print(f"b : {b}")

print(f"b.sum(axis=0) : {b.sum(axis=0)}")

print(f"b.sum(axis=1) : {b.sum(axis=1)}")
print()

print("범용 함수")
B = np.arange(3)
print(f"B : {B}")

# y = e^x
print(f"np.exp(B) : {np.exp(B)}")

# y = sqrt(x)
print(f"np.sqrt(B) : {np.sqrt(B)}")
print()

print("인덱싱, 슬라이싱, 반복")
a = np.arange(10) ** 3
print(f"a : {a}")

print(f"a[2] : {a[2]}")

print(f"a[2:5] : {a[2:5]}")

a[:6:2] = 1000
print(f"a[:6:2] = 1000 => a = {a}")

# reverse
a[::-1]
for i in a:
    print(i ** (1 / 3.))

# np.eye(), np.diag(), np.vander(), np.indices()
