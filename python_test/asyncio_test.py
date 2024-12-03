# Async IO
# Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때 까지 제어권을 가지고 있음
# Non-Blocking I/O : 호출된 함수가 return 후 호출한 함수에게 즉시 제어권을 넘겨주며, 호출한 함수는 다른 작업을 진행 할 수 있음

# 쓰레드 단점 : 디버깅, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 공유 메모리 문제 해결을 위해 -> 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# 코루틴 장점 : 하나의 쓰레드에서 스위칭으로 멀티태스킹 처리 -> 공유 메모리 문제 해결, 자원 소비 감소, 비동기 프로그래밍에 적합

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습
urls = [
    "http://daum.net",
    "https://naver.com",
    "http://mlbpark.donga.com",
    "https://tistory.com",
    "https://wemakeprice.com/",
]


async def fetch(url, executor):
    # 쓰레드명 출력
    print("Thread Name : ", threading.current_thread().name, "Start", url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)

    # BeautifulSoup
    soup = BeautifulSoup(res.read(), "html.parser")

    # 전체 페이지 소스 확인
    # print(soup.prettify())

    result_data = soup.title

    print("Thread Name : ", threading.current_thread().name, "Done", url)
    # 결과 반환
    return result_data


async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    # 결과 취합
    result = await asyncio.gather(*futures)

    print()
    print("Result : ", result)


if __name__ == "__main__":
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print(f"Total Running Time: {duration}")
