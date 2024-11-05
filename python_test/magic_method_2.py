# 클래스 예제
# Vector 클래스
class Vector(object):
    """
    A class for 2D vectors
    """

    def __init__(self, *args):
        """
        Create a vector, example: v = Vector(1,2)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """Returns the vector Information"""
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """Returns the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        """Returns the vector multiplication of self and other"""
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        """Returns the magnitude of the vector"""
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(f"Vector __init__ docs : {Vector.__init__.__doc__}")

# 매직 메소드 출력
print(f"v1 : {v1}")
print(f"v2 : {v2}")
print(f"v3 : {v3}")

print()
print()

# 매직 매소드 docs 출력
print(f"Vector __add__ docs : {Vector.__add__.__doc__}")
print(f"Vector __mul__ docs : {Vector.__mul__.__doc__}")
print(f"Vector __bool__ docs : {Vector.__bool__.__doc__}")

print()
print()

# 연산
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 10 = {v1 * 10}")
print(f"v2 * 5 = {v2 * 5}")
print(f"bool(v1) : {bool(v1)}")
print(f"bool(v2) : {bool(v2)}")
print(f"bool(v3) : {bool(v3)}")
