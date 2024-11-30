# 제너레이터 함수(generator function)는 yield 키워드를 사용하여 작성된 함수로, 호출될 때 한 번에 모든 결과를 반환하지 않고 하나씩 값을 생성
# 일반 함수와 다르게, 제너레이터 함수는 실행될 때 제너레이터 객체를 반환
# 이 객체는 이터레이터로 동작하며, 값을 필요로 할 때마다 하나씩 생성해 반환

# 제너레이터 함수의 동작

# 1. yield를 사용: 제너레이터 함수는 return 대신 yield를 사용해 값을 반환
# 2. 상태 유지: 함수가 호출될 때마다 이전 상태를 기억하고, yield 뒤에서 다시 실행을 시작
# 3. StopIteration 예외: 더 이상 생성할 값이 없으면 StopIteration 예외가 발생

# 제너레이터 함수와 일반 함수의 차이
# 일반 함수
# 호출될 때마다 실행되고 종료
# 결과값을 반환하며, 상태를 기억하지 않는다

# 제너레이터 함수
# 호출될 때 값을 생성하며, 함수의 실행 상태를 기억
# 필요할 때 값을 하나씩 반환하므로 메모리 효율적


def simple_generator():
    yield 1
    yield 2
    yield 3


# 제너레이터 객체 생성
gen = simple_generator()

# 값을 하나씩 출력
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
try:
    print("next(gen) 호출")
except Exception as e:
    print(e)  # StopIteration


# count down 제너레이터
def countdown(n):
    while n > 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)


# 무한 제너레이터
def infinite_sequence():
    n = 0
    while True:
        yield n
        n += 1


# 제너레이터를 사용하여 무한 루프를 생성
gen = infinite_sequence()

# 값을 제한적으로 출력
for _ in range(5):
    print(next(gen))  # 0, 1, 2, 3, 4


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for num in fibonacci(100):
    print(num)


def numbers():
    for i in range(10):
        yield i


def square(nums):
    for num in nums:
        yield num**2


def even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num


# 파이프라인 처리
pipeline = even(square(numbers()))

for result in pipeline:
    print(result)


def bill_calculator(items):
    """
    청구 금액 계산 로직.
    각 항목에 대해 단계별로 계산합니다.
    """
    for item in items:
        yield f"Processing item: {item['name']}"
        total = item["quantity"] * item["price"]
        yield f"Subtotal for {item['name']}: ${total:.2f}"


# 사용 예시
items = [
    {"name": "Apple", "quantity": 3, "price": 1.2},
    {"name": "Banana", "quantity": 2, "price": 0.5},
    {"name": "Cherry", "quantity": 10, "price": 0.2},
]

for message in bill_calculator(items):
    print(message)
