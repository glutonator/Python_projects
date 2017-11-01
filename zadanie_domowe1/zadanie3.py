result = None

list_of_lists = list()
for y in range(1, 101):
    inside_list = list()
    for x in range(1, 101):
        inside_list.append(x)
    list_of_lists.append(inside_list)

j = 1
for temp_list in list_of_lists:
    i = 0
    suma = 0
    for x in temp_list:
        if i < j:
            suma = suma + x
            i = i + 1
        else:
            break
    j = j + 1
    temp_list.append(suma)
   

result = list_of_lists
assert result[-1][-1] == 5050