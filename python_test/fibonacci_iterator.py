class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0  # 첫 번째 피보나치 수 (F(0) = 0)
        self.next_val = 1  # 두 번째 피보나치 수 (F(1) = 1)
        self.count = 0  # 현재까지 생성된 피보나치 수의 개수

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration  # 반복 종료

        if self.count == 0:
            self.count += 1
            return self.current
        elif self.count == 1:
            self.count += 1
            return self.next_val

        # 다음 피보나치 수 계산
        fib = self.current + self.next_val
        self.current = self.next_val
        self.next_val = fib
        self.count += 1
        return fib


if __name__ == "__main__":
    n = int(input().strip())

    result = FibonacciIterator(n)

    if type(result).__name__ != "FibonacciIterator":
        print("Class is not implemented properly\n")

    for num in result:
        print(str(num) + "\n")
