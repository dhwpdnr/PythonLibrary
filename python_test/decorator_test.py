# 데코레이터
# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용 용이
# 단점
# 1. 가독성 감소?
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

import time


# 데코레이터 실습
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter()
        # 경과 시간 계산
        elapsed_time = et - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ", ".join(repr(arg) for arg in args)
        # 결과 출력
        print("[%0.5fs] %s(%s) -> %r" % (elapsed_time, name, arg_str, result))
        return result

    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print("none_deco1", none_deco1)
print("none_deco1.__code__.co_freevars", none_deco1.__code__.co_freevars)

print("none_deco2", none_deco2)
print("none_deco2.__code__.co_freevars", none_deco2.__code__.co_freevars)

print("-" * 40, "Called None Decorator -> time_func")
print()
none_deco1(1.5)
print("-" * 40, "Called None Decorator -> sum_func")
print()
none_deco2(100, 200, 300, 400, 500)


print()
print()

# 데코레이터 사용

print("-" * 40, "Called Decorator -> time_func")
time_func(1.5)
print()
print("-" * 40, "Called Decorator -> sum_func")
sum_func(100, 200, 300, 400, 500)
