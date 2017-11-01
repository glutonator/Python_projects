
result = None
A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#A = {0, 1, 2, 3}

result = set()
# ttttt= set()
# ttttt.add({ })
# r= frozenset(ttttt)
# result. add(r)

result. add(frozenset({}))

for x in A:
    ttt = set(result)
    for y in result:
        temp = set(y)
        temp.add(x)
        ttt.add(frozenset(temp))
        #print(y)
    result.update(ttt)
print(result)
    
    


#result.add(frozenset(temp2))

#print(result)
for x in result:
    print(x)
print(len(result))
#assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result
