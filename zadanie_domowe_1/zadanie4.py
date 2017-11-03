
result = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

a = list(result.keys())
#a.reverse()

for x in a:
    if x % 2 == 1:
        temp = result.get(x)
        result[temp] = x

    del result[x]
print(result)
assert 'Poniedziałek' in result
