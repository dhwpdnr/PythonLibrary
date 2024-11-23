# Dict -> Key 중복 불가능
# Set -> 중복 불가능, 순서 없음

# Dict 및 Set 테스트

# immutable Dict

from types import MappingProxyType

d = {"key1": "value1"}

# Read Only
d_frozen = MappingProxyType(d)

print("d = {'key1': 'value1'}")
print("d_frozen = MappingProxyType(d)")
print(f"d : {d}, id(d) : {id(d)}")
print(f"d_frozen : {d_frozen}, id(d_frozen) : {id(d_frozen)}")

print()

# 수정 가능
d["key2"] = "value2"
print("d['key2'] = 'value2' 수정 가능")

# 수정 불가능
try:
    d_frozen["key2"] = "value2"
except Exception as e:
    print("d_frozen 수정 불가능")

print()
print()

# Set : 중복 불가능, 순서 없음
# set 선언
s1 = {"apple", "banana", "cherry", "apple", "orange", "banana"}
s2 = set(["apple", "banana", "cherry", "apple", "orange", "banana"])
s3 = {"apple"}
s4 = set()  # 빈 set 선언 ({} 로 선언 불가능)
s5 = frozenset({"apple", "banana", "cherry", "apple", "orange", "banana"})  # 수정 불가능

print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s3 : {s3}")
print(f"s4 : {s4}")
print(f"s5 : {s5} (수정 불가능)")

print()

s1.add("grape")
print("s1.add('grape')")
print(f"s1 : {s1}")

print()

print("s5.add('grape')")
try:
    s5.add("grape")
except Exception as e:
    print("s5 수정 불가능")

print()

print("type(s1) : ", type(s1))
print("type(s2) : ", type(s2))
print("type(s3) : ", type(s3))
print("type(s4) : ", type(s4))
print("type(s5) : ", type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print("-----------------------------------------------")
print("dis('{10}')")
print(dis("{10}"))
print("-----------------------------------------------")
print("dis('set([10])')")
print(dis("set([10])"))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

a = {name(chr(i), "") for i in range(0, 256)}
print("a = {name(chr(i), '') for i in range(0, 256)}")
print(f"a : {a}")
