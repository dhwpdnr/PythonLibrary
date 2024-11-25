# 파이썬 변수 범위 (scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)


# 에러 발생
try:
    print("call func_v1(10)")
    func_v1(10)
except Exception as e:
    print(e)

print()
print()

# Ex2
b = 20


def func_v2(a):
    print(a)
    print(b)


print("call func_v2(10)")
func_v2(10)

print()
print()

# Ex3
c = 30


def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40


print("c : ", c)
print("call func_v3(10)")
func_v3(10)
print("c : ", c)

print()
print()

# Closure (클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 데코레이터나 클로저 사용
# 클로저는 공유하되 변경되지 않는(Immutable, Read-Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100
print(a + 100)
print(a + 1000)

print()

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

print()
print()


# 클래스 이용
class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print("inner >> {} / {}".format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()
print("Averager class")
print("dir(averager_cls) : ", dir(averager_cls))

print()

# 누적
print("averager_cls(10) : ", averager_cls(10))
print()
print("averager_cls(30) : ", averager_cls(30))
print()
print("averager_cls(50) : ", averager_cls(50))

print()
print()


# 클로저(Closure) 사용
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능


def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print("inner >> {} / {}".format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()

print("avg_closure1 : ", avg_closure1)

print("avg_closure1(10) : ", avg_closure1(10))
print()
print("avg_closure1(30) : ", avg_closure1(30))
print()
print("avg_closure1(50) : ", avg_closure1(50))

print()
print()

# function inspection
print("dir(avg_closure1) : ", dir(avg_closure1))
print()
print("dir(avg_closure1.__code__) : ", dir(avg_closure1.__code__))
print()
print("avg_closure1.__code__.co_freevars : ", avg_closure1.__code__.co_freevars)
print()
print(
    "avg_closure1.__closure__[0].cell_contents : ",
    avg_closure1.__closure__[0].cell_contents,
)

print()
print()


# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()

try:
    print("avg_closure2(10)")
    print(avg_closure2(10))
except Exception as e:
    print(e)


def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()

print("avg_closure3(10) : ", avg_closure3(10))
print()
print("avg_closure3(30) : ", avg_closure3(30))
print()
print("avg_closure3(50) : ", avg_closure3(50))
