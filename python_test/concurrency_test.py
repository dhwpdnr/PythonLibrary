# 병행성(Concurrency)
# iterator, generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args, **kwargs ... : iterable

t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("t : ", t)
print("dir(t) : ", dir(t))  # __iter__ 가 있으면 반복 가능한 객체
print("t is iterable : ", "__iter__" in dir(t))

print()

w = iter(t)
print("w : ", w)
print("dir(w) : ", dir(w))  # __iter__, __next__ 가 있으면 반복 가능한 객체

print("w 의 next 를 계속 호출")
while True:
    try:
        print(next(w))
    except StopIteration:
        print("StopIteration 예외 발생")
        break

print()
print()

from collections import abc

# 반복형 확인
print("iterable 한지 확인")
print("hasattr(t, '__iter__') : ", hasattr(t, "__iter__"))  # __iter__ 가 있으면 반복 가능한 객체
print(
    "isinstance(t, abc.Iterable) : ", isinstance(t, abc.Iterable)
)  # abc.Iterable 을 상속받으면 반복 가능한 객체

print()
print()

# next 사용
print("Word Spliter")


class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        # print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("StopIteration")
        self._idx += 1
        return word

    def __repr__(self):
        return f"WordSplitter({self._text})"

    def __iter__(self):
        print("Called __iter__")
        return self


wi = WordSplitter("Do today what you could do tomorrow")
print("wi : ", wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

# while True:
#     try:
#         print(next(wi))
#     except StopIteration:
#         break

print()
print()


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가시 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word
        return

    def __repr__(self):
        return f"WordSplitGenerator({self._text})"


wg = WordSplitGenerator("Do today what you could do tomorrow")
print("wg : ", wg)
wt = iter(wg)
print("wt : ", wt)

# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))

while True:
    try:
        print(next(wt))
    except StopIteration:
        break
