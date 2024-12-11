"""
Property - Underscore, access modifier (접근 지정자)
"""

# Ex1
# Use UnderScore
# 1. 인터프리터 내부에서 사용
# 2. 값을 무시할때 사용
# 3. 네이밍(국제화, 자릿수)에 사용
x, _, y = (10, 20, 30)
print("Ex1 > x, y :", x, y)

a, *_, b = (1, 2, 3, 4, 5)
print("Ex1 > a, b :", a, b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# Ex2
"""
접근 지정자
name : public
_name : protected
__name : private
파이썬 네이밍 강제는 아님, 약속된 규약에 따라 사용
Name Mangling : __name -> _classname__name
타 클래스에서 __ 로 시작하는 변수에 접근 하지 않는다
"""


# Not use Property
class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 1
        self._z = 10


a = SampleA()
a.x = 10

print("Ex2 > x :", a.x)
try:
    print("Ex2 > y :", a.__y)
except AttributeError as e:
    print(e)
print("Ex2 > z :", a._z)
print("Ex2 > dir(a) :", dir(a))
print("Ex2 > __y in dir(a) :", "__y" in dir(a))
print("Ex2 > _SampleA__y in dir(a) :", "_SampleA__y" in dir(a))
print("Ex2 > _SampleA__y :", a._SampleA__y)

a._SampleA__y = 100  # 수정이 가능하긴하다
print("Ex2 > _SampleA__y :", a._SampleA__y)


# Ex3
# Use Method(Getter, Setter)
class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()
print("Ex3 > b.x :", b.x)
print("Ex3 > b.get_y() :", b.get_y())
print("b.set_y(100)")
b.set_y(100)
print("Ex3 > b.get_y() :", b.get_y())
print("Ex3 > dir(b) :", dir(b))
