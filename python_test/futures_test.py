# Future 동시성
# 비동기 작업 실행
# 지연시간 (block) CPU 및 리소스 낭비 방지 -> (File) Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상
# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선

# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 확인, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 가능 -> Promise 개념
# 3. 진행 중인 작업 실행 중 다른 작업 추가 가능

# GIL(Global Interpreter Lock)
# 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 실행-> 문제점을 방지하기 위해
# 리소스 전체에 락이 걸림 -> Context Switch(문맥교환)
# 멀티 프로세싱 사용, CPython


# 사용법 1 (map)
import os
import time
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
    wait,
    as_completed,
)

WORK_LIST = [100000, 1000000, 10000000, 100000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제레네이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = "\n Result -> {} Time: {:.2f}s"

    print(msg.format(list(result), end_tm))


# if __name__ == "__main__":
#     main()


# 사용법 2 (wait, as_completed)
def main2():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()

    # futures list
    futures_list = []

    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환(아직 실행되지 않음)
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print("Scheduled for {} : {}".format(work, future))
            print()

        # wait 결과 출력
        # result = wait(futures_list, timeout=2)
        #
        # # 성공
        # print("Completed Tasks : ", str(result.done))
        #
        # # 실패
        # print("Pending ones before wait: ", str(result.not_done))
        #
        # # 결과 값 출력
        # print("Result", [future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print("Future Result : {}, Done : {}".format(result, done))
            print("Future Cancelled : {}".format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = "\n Time: {:.2f}s"

    print(msg.format(end_tm))


if __name__ == "__main__":
    main2()
