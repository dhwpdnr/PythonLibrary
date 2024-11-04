# Special Method (Magic Method)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(f"int 의 자료형 : {int}")
print(f"float 의 자료형 : {float}")

print()
print()

# 모든 속성 및 메소드 출력
print(f"dir(int) : {dir(int)}")
print(f"dir(float) : {dir(float)}")

print()
print()
n = 10
# print(f"n.__doc__ : {n.__doc__}")
print("n = 10")

print(f"n + 100 = {n + 100}")
print(f"n.__add__(100) : {n.__add__(100)}")

print()

print(f"n.__bool__() : {n.__bool__()}")
print(f"bool(n) : {bool(n)}")

print()

print(f"n * 100 = {n * 100}")
print(f"n.__mul__(100) : {n.__mul__(100)}")

print()
print()


# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit Class Info: {self._name}, {self._price}"

    def __add__(self, x):
        print("Called >> __add__")
        return self._price + x._price

    def __sub__(self, x):
        print("Called >> __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("Called >> __le__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("Called >> __ge__")
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# 일반적 계산
print("일반적 계산 - s1._price + s2._price ")
print(s1._price + s2._price)

print()

# 매직 메소드 사용
print("매직 메소드 사용 - s1 + s2 ")
print(s1 + s2)

print()
print()

# 일반적 계산
print("일반적 계산 - s1._price - s2._price ")
print(s1._price - s2._price)

print()

# 매직 메소드 사용
print("매직 메소드 사용 - s1 - s2 ")
print(s1 - s2)

print()
print()

# 일반적 계산
print("일반적 계산 - s1._price <= s2._price ")
print(s1._price <= s2._price)

print()

# 매직 메소드 사용
print("매직 메소드 사용 - s1 <= s2 ")
print(s1 <= s2)

print()
print()

# 일반적 계산
print("일반적 계산 - s1._price >= s2._price ")
print(s1._price >= s2._price)

print()

# 매직 메소드 사용
print("매직 메소드 사용 - s1 >= s2 ")
print(s1 >= s2)
