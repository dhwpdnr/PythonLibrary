# 해시 테이블
# Key와 Value를 가지는 데이터 구조
# 파이썬 딕셔너리 타입이 해시 테이블의 예
# Key 값의 연산을 통해 직접 접근이 가능한 구조
# Key 값을 해싱 함수를 통해 해시 주소로 변환 후, 이를 기반으로 데이터 저장 및 검색

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(f"hash(t1) : {hash(t1)}")
# print(f"hash(t2) : {hash(t2)}")  # 예외 발생

print()
print()

# Dict Setdefault 예제
source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
)

print(f"source : {source}")
new_dict1 = {}
new_dict2 = {}

print()

# No use Setdefault
print("No use Setdefault")
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(f"new_dict1 : {new_dict1}")

print()

# Use Setdefault
print("Use Setdefault")
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(f"new_dict2 : {new_dict2}")

print()

# 주의사항
new_dict3 = {k: v for k, v in source}
print("new_dict3 = {k: v for k, v in source}}")
print(f"new_dict3 : {new_dict3}")
