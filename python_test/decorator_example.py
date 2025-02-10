import time

"""
데코레이터
데코레이터는 함수를 장식하다라는 의미로 사용되며, 함수의 앞뒤에 코드를 추가하여 함수의 기능을 확장할 수 있다
"""


# 데코레이터 실습

# 함수 시작 시간과 종료 시간을 출력하는 데코레이터
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[알림] 함수명 <{func.__name__}> 실행에 {end_time - start_time:.6f}초 소요되었습니다.")
        return result

    return wrapper


def sleep_function():
    time.sleep(1)
    print("1초 sleep")


# @decorator 문법 없이 사용
sleep_function = timing_decorator(sleep_function)
sleep_function()

print()


# 데코레이터 사용
@timing_decorator
def loop_function(n):
    for _ in range(n):
        pass
    print(f"{n}번 반복")


loop_function(1000000)

print()


# 양수 확인
def validate_positive(func):
    def wrapper(arg):
        if arg < 0:
            raise ValueError("음수는 허용되지 않습니다.")
        return func(arg)

    return wrapper


# 정수 확인
def validate_integer(func):
    def wrapper(arg):
        if not isinstance(arg, int):
            raise ValueError("정수가 아닙니다.")
        return func(arg)

    return wrapper


# 데코레이터 중첩 사용
@validate_integer
@validate_positive
def positive_integer_printer(value):
    print(f"입력한 값은 {value}입니다.")


try:
    positive_integer_printer(100)
except ValueError as e:
    print(e)

try:
    positive_integer_printer(-100)
except ValueError as e:
    print(e)

try:
    positive_integer_printer(1.1)
except ValueError as e:
    print(e)

print()


# 파라미터를 받는 데코레이터
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


# 데코레이터에 파라미터 사용
@repeat(3)
def say_hi():
    print("Hi!")


say_hi()
