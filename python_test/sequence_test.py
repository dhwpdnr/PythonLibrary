# 시퀀스형
# 컨테이너 (Container: 서로 다른 자료형(list, tuple, collections.deque)을 담을 수 있는 것)
# 플랫 (Flat : 한 개의 자료형(str, bytes, bytearray, array.array, memoryview)만 담을 수 있는 것)
# 가변 (Mutable : list, bytearray, array.array, memoryview, deque)
# 불변 (Immutable : tuple, str, bytes)

# 지능형 리스트
chars = "+_)(*&^%$#@!"
code_list1 = []

# ord(): 문자의 유니코드 코드 리턴
for s in chars:
    code_list1.append(ord(s))

print("유니코드 리스트")
print(code_list1)
print([chr(s) for s in code_list1])

print()

# Comprehending lists
code_list2 = [ord(s) for s in chars]
print("Comprehending lists")
print(code_list2)
print([chr(s) for s in code_list2])

print()

# Comprehending lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print("Comprehending lists")
print(code_list3)
print([chr(s) for s in code_list3])

print()

# filter + map 사용
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print("filter + map")
print(code_list4)
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
print(f"tuple_g : ord(s) for s in chars : {tuple_g}")
print(f"type(tuple_g) : {type(tuple_g)}")
print(f"next(tuple_g) : {next(tuple_g)}")
print(f"next(tuple_g) : {next(tuple_g)}")
print(f"next(tuple_g) : {next(tuple_g)}")
print(f"next(tuple_g) : {next(tuple_g)}")

print()

array_g = array.array("I", (ord(s) for s in chars))
print(f"array_g : {array_g}")
print(f"type(array_g) : {type(array_g)}")
print(f"array_g.tolist() : {array_g.tolist()}")

print()
print()

# 제네레이터 예제
print(("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)))

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의
marks1 = [["~"] * 3 for _ in range(3)]
marks2 = [["~"] * 3] * 3
print("marks1")
print(marks1)

print()

print("marks2")
print(marks2)

# 수정
marks1[0][1] = "X"
print("marks1[0][1] = 'X'")
print(marks1)

print()

marks2[0][1] = "X"
print("marks2[0][1] = 'X'")
print(marks2)

print()

# 증명
print("marks1 아이디 값")
print([id(i) for i in marks1])
print("marks2 아이디 값")
print([id(i) for i in marks2])
