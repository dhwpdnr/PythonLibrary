# 튜플 패킹
packed_tuple = 1, 2, 3, 4, 5
print(f"packed_tuple : {packed_tuple}")  # (1, 2, 3, 4, 5)

# 리스트 패킹
packed_list = [10, 20, 30, 40, 50]
print(f"packed_list : {packed_list}")  # [10, 20, 30, 40, 50]

print()

# 튜플 언패킹
a, b, c, d, e = packed_tuple
print(a, b, c, d, e)  # 1 2 3 4 5

# 리스트 언패킹
x, y, z = [100, 200, 300]
print(x, y, z)  # 100 200 300

print()

first, *middle, last = [1, 2, 3, 4, 5]
print(first)  # 1
print(middle)  # [2, 3, 4] -> 중간 값들은 리스트로 그룹화
print(last)  # 5


# 함수의 가변 인자
def add(*numbers):
    return sum(numbers)


print()

print(add(1, 2, 3, 4, 5))  # 15


def show_info(name, age, **extra_info):
    print(f"Name: {name}, Age: {age}")
    print("Extra Info:", extra_info)


show_info("Alice", 25, country="USA", hobby="Reading")

print()


# 튜플 언패킹
def multiply(a, b, c):
    return a * b * c


numbers = (2, 3, 4)
print(multiply(*numbers))  # 24  (튜플을 언패킹하여 함수에 전달)

print()


# 딕셔너리 언패킹
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")


person_info = {"name": "Bob", "age": 30}
greet(**person_info)  # 딕셔너리의 키-값을 함수의 인자로 언패킹

print()

# 리스트 확장
a = [1, 2, 3]
b = [4, 5, 6]

combined = [*a, *b]  # 리스트를 병합
print(combined)  # [1, 2, 3, 4, 5, 6]

# 딕셔너리 확장
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}

merged_dict = {**dict1, **dict2}
print(merged_dict)  # {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

print()
