from collections import ChainMap, Counter

# dictionary나 key-value 매핑을 묶어 하나의 view로 보여줌
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(f"collections.ChainMap(adjustments, baseline) : {ChainMap(adjustments, baseline)}")
print(f"list(collections.ChainMap(adjustments, baseline)) : {list(ChainMap(adjustments, baseline))}")
print()

# Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(f"cnt : {cnt}")

c = Counter(a=4, b=2, c=0, d=-2)
print(f"sorted counter object:{sorted(c.elements())}")

print(f"Counter('abracadabra').most_common(3) : {Counter('abracadabra').most_common(3)}")

c = Counter(a=4, b=2, c=0, d=-2)
print(f"c : {c}")
d = Counter(a=1, b=2, c=3, d=4)
print(f"d : {d}")
c.subtract(d)
print(f"c.subtract(d) : {c}")

c = Counter(a=10, b=5, c=0)
print(f"c : {c}")
print(f"c.total() : {c.total()}")
