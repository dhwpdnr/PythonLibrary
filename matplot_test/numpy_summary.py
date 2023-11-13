import numpy as np
import numpy.random as npr

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

print("np.fromfunction()")


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(f"b : {b}")
print(f"b[2, 3] : {b[2, 3]}")

print(f"b[0:5, 1] : {b[0:5, 1]}")

print(f"b[:, 1] : {b[:, 1]}")

print(f"b[1:3, :] : {b[1:3, :]}")

print(f"b[-1] : {b[-1]}")
print()

c = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(f"c : {c}")
print(f"c.shape : {c.shape}")
print(f"c[1, ...] : {c[1, ...]}")  # same as c[1,:,:] or c[1]

print(f"c[..., 2] : {c[..., 2]}")  # same as c[:,:,2]
print()

print("for row in b:")
for row in b:
    print(row)

print("for element in b.flat:")
for element in b.flat:
    print(element)

print("Shape 변경")
# .ravel()은 1차원으로
# .reshape()는 지정한 차원으로
# .T는 전치(Transpose) 변환을 할 수 있다
# 데이터 원본은 변경시키지 않고 복사하여 연산한 결과가 return
a = np.floor(10 * npr.random((3, 4)))
print(f"a : {a}")
print(f"a.shape : {a.shape}")
print(f"a.ravel() : {a.ravel()}")

# [3,4] => [2,6]로 변경
print(f"a.reshape(2, 6) : {a.reshape(2, 6)}")

# [3,4]의 전치(transpose)변환으로 [4,3]
print(f"a.T : {a.T}")
print(f"a.T.shape : {a.T.shape}")
print(f"a.shape : {a.shape}")
print()

print("resize")
print(f"a : {a}")

a.resize((2, 6))
print("a.resize((2, 6))")
print(f"a : {a}")
print(f"a.reshape(3, -1) : {a.reshape(3, -1)}")

print("데이터 쌓기")
# np.vstack(): axis=0 기준으로 쌓음
# np.hstack(): axis=1 기준으로 쌓음
a = np.floor(10 * npr.random((2, 2)))
print(f"a: {a}")

b = np.floor(10 * npr.random((2, 2)))
print(f"b : {b}")

# [2,2] => [4,2]
print(f"np.vstack((a, b)) : {np.vstack((a, b))}")

# [2,2] => [2,4]
print(f"np.hstack((a, b)) : {np.hstack((a, b))}")
print()

print("데이터 쪼개기")
# np.hsplit()을 통해 숫자1개가 들어갈 경우 X개로 등분
# 리스트로 넣을 경우 axis=1 기준 인덱스로 데이터를 분할
a = np.floor(10 * npr.random((2, 12)))
print(f"a : {a}")

# [2,12] => [2,4] 데이터 3개로 등분
print(f"np.hsplit(a, 3) : {np.hsplit(a, 3)}")

# [2,12] => [:, :3], [:, 3:4], [:, 4:]로 분할
print(f"np.hsplit(a, (3, 4)) : {np.hsplit(a, (3, 4))}")
print()

print("데이터 복사")
# array를 변수에 넣는다고 해서 복사가 되지 않는다
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
# 두 개가 사실상 같습니다. (복사가 아님)
b = a
print(b is a)
print(id(a))
print(id(b))

print("얕은 복사")
c = a.view()
# c와 a의 참조값은 다름
print(c is a)

c = c.reshape((2, 6))
print(a.shape)
# (3, 4)

c[0, 4] = 1234
print(a)

s = a[:, 1:3]
s[:] = 10
print(a)
print()

print("깊은 복사")
# 참조값 뿐만 아니라 각각의 데이터 전부가 새로운 객체로 생성
d = a.copy()
print(d is a)

# a와 d의 데이터의 참조값도 다름
d[0, 0] = 9999
print(a)

# 2차원 정방단위행렬 생성
D = np.identity(3)
print(D)

E1 = np.eye(3, dtype=int)
print(E1)
E2 = np.eye(3, k=1, dtype=int)
print(E2)
E3 = np.eye(3, k=-1, dtype=int)
print(E3)

b = np.array(([[1, 1], [2, 2], [3, 3]]))
np.insert(b, 1, [1, 2, 3], axis=1)
print(f"b : {b}")

# flatten
b = np.array([[1, 1], [2, 2], [3, 3]])
b.flatten()
print(f"b.flatten() : {b.flatten()}")

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(np.append(a, b))
print(np.append([a], b, axis=0))

rnd = npr.randn(5) * 10 + 165
print(rnd)
print(rnd.round(2))

np_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(np_array % 2 == 0)
print(np_array[np_array % 2 == 0])
# np.diag(), np.vander(), np.indices()
