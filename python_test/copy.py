"""
Shallow copy, Deep copy
객체 복사의 종류 : copy, shallow copy, deep copy
정확한 이해를 하고 사용해야 한다.
"""

# Ex1 - Copy
# Call by Value, Call by Reference
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print("직접 대입")
print("Ex1 > id(a_list)", id(a_list))
print("Ex1 > id(b_list)", id(b_list))
print("Ex1 > id(a_list) == id(b_list) :", id(a_list) == id(b_list))

print()

b_list[1] = 100

print("Ex1 > a_list :", a_list)
print("Ex1 > b_list :", b_list)

print()

b_list[3][2] = 100

print("Ex1 > a_list :", a_list)
print("Ex1 > b_list :", b_list)

print()
print()

# Ex2 - Shallow Copy
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print("얕은 복사")
print("Ex2 > id(c_list)", id(c_list))
print("Ex2 > id(d_list)", id(d_list))
print("Ex2 > id(c_list) == id(d_list) :", id(c_list) == id(d_list))

print()

d_list[1] = 100

print("Ex2 > c_list :", c_list)
print("Ex2 > d_list :", d_list)

print()

# 리스트 객체의 주소값은 다르지만, 리스트 내부의 리스트 객체는 같은 주소값을 가지고 있다.
d_list[3].append(1000)
d_list[4][1] = 1000

print("Ex2 > c_list :", c_list)
print("Ex2 > d_list :", d_list)

print()
print()

# Ex3 - Deep Copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print("깊은 복사")
print("Ex3 > id(e_list)", id(e_list))
print("Ex3 > id(f_list)", id(f_list))
print("Ex3 > id(e_list) == id(f_list) :", id(e_list) == id(f_list))

print()

f_list[3].append(1000)
f_list[4][1] = 1000

# 리스트 객체의 주소값이 다르고, 리스트 내부의 리스트 객체도 다른 주소값을 가지고 있다.
print("Ex3 > e_list :", e_list)
print("Ex3 > f_list :", f_list)

print()
