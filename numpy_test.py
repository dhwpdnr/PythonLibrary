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



