# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(f"pt1 : {pt1}, pt2 : {pt2}")
print(f"l_leng1 : {l_leng1}")

print()
print()

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple("Point", "x y")
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)
print("네임드 튜플 선언")
print(f"pt3 : {pt3}, pt4 : {pt4}")
print(f"pt3.x : {pt3.x}, pt3.y : {pt3.y}")
print(f"pt4.x : {pt4.x}, pt4.y : {pt4.y}")
print(f"pt3[0] : {pt3[0]}, pt3[1] : {pt3[1]}")
print(f"pt4[0] : {pt4[0]}, pt4[1] : {pt4[1]}")

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(f"l_leng2 : {l_leng2}")

print()
print()

# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")
# Point4 = namedtuple("Point", "x y x class") # 중복되는 변수명 사용 불가, 예약어 사용 불가
Point4 = namedtuple(
    "Point", "x y _x class", rename=True
)  # 중복되는 변수명 사용 가능, Default = False
print(Point1, Point2, Point3, Point4)

print()

# Dict to Unpacking
temp_dict = {"x": 75, "y": 55}
print(f"temp_dict : {temp_dict}")

# 네임트 튜플 사용
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(30, y=45)
p4 = Point4(40, 50, 60, 70)
p5 = Point3(**temp_dict)
print()

print(f"p1 : {p1}")
print(f"p2 : {p2}")
print(f"p3 : {p3}")
print(f"p4 : {p4}")  # x, class 는 _2, _3으로 변경됨
print(f"p5 : {p5}")  # dict to unpacking

print()

# 사용
print(f"p1[0] + p2[1] : {p1[0] + p2[1]}")
print(f"p1.x + p2.y : {p1.x + p2.y}")

x, y = p2
print("x, y = p2")
print(f"x : {x}, y : {y}")

print()
print()

# 네임드 튜플 메소드
temp = [52, 38]
# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print("p4 = Point1._make(temp)")
print(f"p4 : {p4}")

print()

# _fields : 필드 네임 확인
print(f"p1._fields : {p1._fields}")
print(f"p2._fields : {p2._fields}")
print(f"p3._fields : {p3._fields}")
print(f"p4._fields : {p4._fields}")

print()

# _asdict() : OrderedDict 반환
print(f"p1._asdict() : {p1._asdict()}")
print(f"p2._asdict() : {p2._asdict()}")
print(f"p3._asdict() : {p3._asdict()}")
print(f"p4._asdict() : {p4._asdict()}")

print()
print()

# 실 사용 실습
# 반20명, 4개의 반(A, B, C, D)
print("실 사용 실습")
Classes = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

print(f"numbers : {numbers}")
print(f"ranks : {ranks}")

print()

students = [Classes(rank, number) for rank in ranks for number in numbers]

print(f"len(students) : {len(students)}")
print(f"students : {students}")

print()

students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]
print(f"len(students2) : {len(students2)}")
print(f"students2 : {students2}")

print()

# 출력
for s in students:
    print(s)
