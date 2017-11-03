
def add_one(lista=None):
    if lista == None:
        lista = [1]
    else:
        lista.append(1)
    return lista


test_list = [5, 6, 7]
result1 = add_one(test_list)
print(result1)
assert result1 == [5, 6, 7, 1]

result2 = add_one()
assert result2 == [1]
print(result2)

result3 = add_one()
assert result3 == [1]
print(result3)
