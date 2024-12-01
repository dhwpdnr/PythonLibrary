# 코루틴(Coroutine) 테스트

# 코루틴 : 단일(싱글) 스레드, 스택 기반의 코루틴(Coroutine) 사용
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡(공유되는 자원) -> 교착상태 발생 가능성 증가, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await

# 코루틴 Ex1
def coroutine1():
    print(">>> coroutine started.")
    i = yield
    print(">>> coroutine received : {}".format(i))
    yield


# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()

print("cr1 : ", cr1)
print("type : ", type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)
# next(cr1)  # 예외 발생


# 값 전송 (default : None)
cr1.send(100)

# 잘못된 사용
cr2 = coroutine1()

# 예외 발생
try:
    cr2.send(100)
except Exception as e:
    print(e)

print()
print()


# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print(">>> coroutine started : {}".format(x))
    y = yield x
    print(">>> coroutine received : {}".format(y))
    z = yield x + y
    print(">>> coroutine received : {}".format(z))
    yield z


from inspect import getgeneratorstate

# 제네레이터 선언
cr3 = coroutine2(10)
print(getgeneratorstate(cr3))
print(next(cr3))

print()

print(getgeneratorstate(cr3))
print(cr3.send(20))

print()

print(getgeneratorstate(cr3))
print(cr3.send(30))

print()
print()


# 코루틴 Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리


def generator1():
    for x in "AB":
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

print()
t2 = generator1()
print("list generator1 : ", list(t2))

print()
print()


def generator2():
    yield from "AB"
    yield from range(1, 4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))

print()

t4 = generator2()
print("list generator2 : ", list(t4))
