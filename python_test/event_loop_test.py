# 이벤트 루프는 비동기 프로그래밍의 핵심 메커니즘으로, 비동기 작업을 효율적으로 관리
import asyncio

# 이벤트 루프는 작업들을 일정 순서로 실행하고, 작업이 완료되거나 준비될 때까지 기다리지 않고 다른 작업을 진행하여 시스템 자원을 최대한 활용


async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # 비동기적으로 1초 대기
    print("Goodbye!")


# 이벤트 루프 실행
asyncio.run(say_hello())

print()
print()


# asyncio.gather() 함수를 사용하면 여러 개의 작업을 동시에 실행할 수 있음
async def task1():
    print("Task 1: Start")

    print("Task 2 : sleep 2 seconds")
    await asyncio.sleep(2)  # 2초 대기

    print("Task 1: Done")


async def task2():
    print("Task 2: Start")

    print("Task 2 : sleep 1 second")
    await asyncio.sleep(1)  # 1초 대기

    print("Task 2: Done")


async def test_2():
    await asyncio.gather(task1(), task2())


asyncio.run(test_2())

# 여러 HTTP 요청 동시에 처리
import httpx
import timeit


async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        start = timeit.default_timer()
        response = await client.get(url)
        print(
            f"Fetched {url}: {response.status_code}, Time : {timeit.default_timer() - start}"
        )


async def test_3():
    start = timeit.default_timer()
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
    ]
    await asyncio.gather(*(fetch_url(url) for url in urls))
    print(f"Total time: {timeit.default_timer() - start}")


def test_3_sync():
    start = timeit.default_timer()
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
    ]
    for url in urls:
        task_start = timeit.default_timer()
        response = httpx.get(url)
        print(
            f"Fetched {url}: {response.status_code}, Time : {timeit.default_timer() - task_start}"
        )
    print(f"Total time: {timeit.default_timer() - start}")


print("Async http request")
asyncio.run(test_3())

print()

# 동기 방식으로 실행
print("Sync http request")
test_3_sync()

print()
print()

# 비동기와 동기 코드 혼합
from asgiref.sync import sync_to_async


def blocking_task():
    print("This is a blocking task")
    return "Task complete"


async def async_task():
    print("This is an async task")
    result = await sync_to_async(blocking_task)()  # 동기 함수를 비동기로 호출
    print(result)


asyncio.run(async_task())

print()
print()


# 작업 재시도 및 시간 초과 처리
async def slow_task():
    await asyncio.sleep(5)  # 5초 동안 대기
    return "Finished"


async def test_4():
    try:
        print("Starting slow task")
        result = await asyncio.wait_for(slow_task(), timeout=3)  # 3초 제한
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")


asyncio.run(test_4())

print()
print()


# 이벤트 루프에서 큐 활용
async def producer(queue):
    for i in range(5):
        print(f"Producing {i}")
        await queue.put(i)  # 작업 큐에 데이터 추가
        await asyncio.sleep(1)


async def consumer(queue):
    while True:
        item = await queue.get()  # 작업 큐에서 데이터 가져오기
        print(f"Consuming {item}")
        queue.task_done()


async def test_5():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(test_5())

print()
print()


# 주기적으로 작업 실행
async def periodic_task(interval):
    while True:
        print("Running periodic task...")
        await asyncio.sleep(interval)  # 주기적으로 실행


async def test_6():
    await asyncio.gather(periodic_task(2), periodic_task(3))  # 다른 주기로 실행


loop = asyncio.get_event_loop()
loop.run_until_complete(test_6())
