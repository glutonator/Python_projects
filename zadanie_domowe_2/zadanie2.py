
def copy_reversed(list_a, list_b):
    temp = list(list_a)
    temp.reverse()
    list_b.extend(temp)
    return None


x = [1, 2, 3]
y = [4, 5, 6]

result = copy_reversed(x, y)
print(x, y)
assert y == [4, 5, 6, 3, 2, 1]
assert result is None
