from itertools import combinations, combinations_with_replacement, permutations

l = [1, 2, 3]
print("조합 뽑기")
print("combinations([1,2,3], 2)")
for i in combinations(l, 2):
    print(i)
print()

l = ['A', 'B', 'C']
print("중복 조합 뽑기")
print(f"l : {l}")
print("combinations_with_replacement(l, 2)")
for i in combinations_with_replacement(l, 2):
    print(i)
print()

print("순열 뽑기")
l = ['A', 'B', 'C']
print(f"l : {l}")
print(permutations(l))
for i in permutations(l):
    print(i)
