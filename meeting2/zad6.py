
#zwracanie ile gwaizdek rysujemy


def draw_tree(wysokosc, symbol='*'):
    symbol_count = 0
    for i in range(wysokosc):
        symbol_count += 2 * i + 1
        print((wysokosc - i - 1) * ' ' + (1 + 2 * i) * str(symbol))
    return symbol_count


syn = draw_tree(4)
draw_tree(4, 'Y')
draw_tree(5, 'y')

print(syn)

#print(__name__)
if(__name__=='__main__'):
    print("main")
else:
    print("Nie main")