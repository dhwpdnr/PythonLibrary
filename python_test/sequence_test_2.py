# Tuple Advanced
# Unpacking

print("divmod(100, 9)")
print(divmod(100, 9))
print("divmod(*(100, 8))")
print(divmod(*(100, 8)))
print("*(divmod(100, 7))")
print(*(divmod(100, 7)))

print()
print()

x, y, *rest = range(10)
print("x, y, *rest = range(10)")
print(f"x : {x}, y : {y}, rest : {rest}")

print()

x, y, *rest = range(2)
print("x, y, *rest = range(2)")
print(f"x : {x}, y : {y}, rest : {rest}")

print()

x, y, *rest = 1, 2, 3, 4, 5
print("x, y, *rest = 1, 2, 3, 4, 5")
print(f"x : {x}, y : {y}, rest : {rest}")

print()
print()

# Mutable(가변) vs Immutable(불변)
# 불변형은 재할당
# 가변형은 기존 메모리 사용
l = (15, 20, 25)  # tuple(불변)
m = [15, 20, 25]  # list(가변)

print(f"l : {l}, id(l) : {id(l)}")
print(f"m : {m}, id(m) : {id(m)}")

print()

print("l = l * 2")
print("m = m * 2")

l = l * 2
m = m * 2

print(f"l : {l}, id(l) : {id(l)}")
print(f"m : {m}, id(m) : {id(m)}")

print()

print("l *= 2")
print("m *= 2")

l *= 2
m *= 2

print(f"l : {l}, id(l) : {id(l)}")
print(f"m : {m}, id(m) : {id(m)}")

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 X)
f_list = ["orange", "apple", "mango", "papaya", "lemon", "strawberry", "coconut"]
print("sorted test")
print(f"f_list : {f_list}")
print(f"sorted(f_list) : {sorted(f_list)}")
print(f"sorted(f_list, reverse=True) : {sorted(f_list, reverse=True)}")
print(f"sorted(f_list, key=len) : {sorted(f_list, key=len)}")  # 길이 순 정렬
print(
    f"sorted(f_list, key=lambda x: x[-1]) : {sorted(f_list, key=lambda x: x[-1])}"
)  # 마지막 글자 기준 정렬(함수 사용)
print(
    f"sorted(f_list, key=lambda x: x[-1], reverse=True) : {sorted(f_list, key=lambda x: x[-1], reverse=True)}"
)  # 마지막 글자 기준 정렬(함수 사용)

print(f"f_list : {f_list}")  # 원본 확인

print()

# sort : 정렬 후 객체 직접 변경 (원본 수정 O)
print("sort test")
print(f"f_list : {f_list}")
print(f"f_list.sort() : {f_list.sort()}")
print(
    f"f_list.sort(reverse=True) : {f_list.sort(reverse=True)}, f_list : {f_list}"
)  # None 반환
print(f"f_list.sort(key=len) : {f_list.sort(key=len)}, f_list : {f_list}")  # None 반환
print(
    f"f_list.sort(key=lambda x: x[-1]) : {f_list.sort(key=lambda x: x[-1])}, f_list : {f_list}"
)  # None 반환
print(
    f"f_list.sort(key=lambda x: x[-1], reverse=True) : {f_list.sort(key=lambda x: x[-1], reverse=True)}, f_list : {f_list}"
)  # None 반환
print(f"f_list : {f_list}")  # 원본이 수정

# List vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# Array 기반 : 숫자 기반 연산, 리스트와 호환 가능
