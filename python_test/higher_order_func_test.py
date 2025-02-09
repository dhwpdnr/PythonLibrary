"""
고차 함수 (Higher-order function)
함수를 인자로 받거나 함수를 결과로 반환하는 함수
"""


def apply_function(func, value):
    """함수를 인수로 받아 그 함수에 값을 적용"""
    return func(value)


# Example
print(apply_function(abs, -5))  # abs(-5)를 호출 -> 결과: 5
print(apply_function(lambda x: x * 2, 10))  # 익명 함수 호출 -> 결과: 20


def multiplier(factor):
    """곱셈 연산을 수행하는 함수 반환"""

    def multiply(value):
        return value * factor

    return multiply


# Example usage
double = multiplier(2)  # factor=2인 함수 반환
print(double(5))  # 5 * 2 -> 결과: 10
triple = multiplier(3)  # factor=3인 함수 반환
print(triple(5))  # 5 * 3 -> 결과: 15
