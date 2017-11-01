
result = None
result = list()
for x in range(0,100):
    if x % 5 == 0 and x % 3 == 0:
	    result.append('trzypięć')
    elif x % 3 == 0:
	    result.append('trzy')
    elif x % 5 == 0:
	    result.append('pięć')
    else:
        result.append(x)

for x in result:
    print(x)

assert result[15] == 'trzypięć'