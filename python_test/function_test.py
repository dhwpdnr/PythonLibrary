# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과로 반환 가능

# 함수 객체
def factorial(n):
    """Factorial Function -> n: int"""
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(f"factorial(5) : {factorial(5)}")
print(f"factorial.__doc__ : {factorial.__doc__}")
print(f"type(factorial) : {type(factorial)}")

print()

print("함수만의 속성")
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

print()

print(f"factorial.__name__ : {factorial.__name__}")
print(f"factorial.__code__ : {factorial.__code__}")

print()
print()

# 변수 할당
var_func = factorial
print("var_func = factorial")
print(f"var_func : {var_func}")
print(f"var_func(5) : {var_func(5)}")
print(f"map(var_func, range(1, 6)) : {list(map(var_func, range(1, 6)))}")

print()

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)
# map, filter, reduce
print("map, filter, reduce test")

print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce
from functools import reduce
from operator import add

print(
    "reduce(add, range(1, 11)) : ", reduce(add, range(1, 11))
)  # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print("sum(range(1, 11)) : ", sum(range(1, 11)))

print()
print()

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 일반 함수 사용
print("lambda function")
print(
    "reduce(lambda x, t: x + t, range(1, 11))", reduce(lambda x, t: x + t, range(1, 11))
)

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print("callable")
print("callable(str) : ", callable(str))
print("callable(A) : ", callable(A))
print("callable(var_func) : ", callable(var_func))
print("callable(factorial) : ", callable(factorial))
print("callable(3.14) : ", callable(3.14))

print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from functools import partial
from operator import mul

print("partial")
print("mul(10, 10) : ", mul(10, 10))

print()

print("인수 고정")
five = partial(mul, 5)

print("five = partial(mul, 5)")
print("five(10) : ", five(10))

print()

six = partial(five, 6)
print("six = partial(five, 6)")
print("six()", six())

print()

try:
    print("six(1)")
    print(six(1))
except Exception as e:
    print("인수 고정 오류")
    print(e)
