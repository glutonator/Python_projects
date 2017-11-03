
result = None
A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
result = set()

temp = set()
for x in A:
    temp.add(x)
    result.add(frozenset(temp))

print(result)
assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result