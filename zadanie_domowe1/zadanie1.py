
result = None

result = list()

for x in range(0,1000):
    result.append(x)

for x in range(0,len(result)):
    if x % 5 == 0 and x % 3 == 0:
	    result[x] = 'trzypięć'
    elif x % 3 == 0:
	    result[x] = 'trzy'
    elif x % 5 == 0:
	    result[x] = 'pięć'

assert result[15] == 'trzypięć'












#assert result[15] == 'trzypięć'