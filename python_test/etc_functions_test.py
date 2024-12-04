"""
Lambda, Reduce, Filter, Map Functions
lambda : 익명 함수, 힙 메모리에 저장되지 않고 일회성으로 사용, 파이썬 가비지 컬렉션(count=0)
일반함수 : 재사용을 위해 메모리에 저장

시퀀스형 전처리에 Reduce, Filter, Map 함수 사용
"""

# Ex1
cul = lambda x, y, z: x * y + z
print("Ex1 > ", cul(10, 15, 20))

print()
print()

# Ex2
digits = [i * 10 for i in range(1, 11)]
print("Ex2 > digits :", digits)
result = list(map(lambda x: x**2, digits))
print("Ex2 > result :", result)


def also_square(nums):
    def double(x):
        return x**2

    return map(double, nums)


print("Ex2 > list(also_square) :", list(also_square(digits)))

print()
print()

# Ex3
digits2 = [i for i in range(1, 11)]
print("Ex3 > digits2 :", digits2)
result = list(filter(lambda x: x % 2 == 0, digits2))
print("Ex3 > result :", result)


def also_filter(nums):
    def is_even(x):
        return x % 2 == 0

    return filter(is_even, nums)


print("Ex3 > list(also_filter) :", list(also_filter(digits2)))

print()
print()

# Ex4
from functools import reduce

digits3 = [i for i in range(1, 101)]
print("Ex4 > digits3 :", digits3)
result = reduce(lambda x, y: x + y, digits3)
print("Ex4 > result :", result)


def also_reduce(nums):
    def add(x, y):
        return x + y

    return reduce(add, nums)


print("Ex4 > also_reduce :", also_reduce(digits3))
