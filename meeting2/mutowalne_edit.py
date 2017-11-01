

list_slow = ['AAA', 'BBB', 'Cccc']
def my_func(a):
    a.append('fggdd')
    for x in a:
        print(x)

my_func(list_slow)
print(list_slow)