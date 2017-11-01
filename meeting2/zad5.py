
#domyślne argumenty _zmienna='*'
def draw_tree(wysokosc, symbol='*'):
    for i in range(wysokosc):
        print((wysokosc-i-1)*' '+(1+2*i)*str(symbol))


draw_tree(3)
draw_tree(4,'Y')
draw_tree(5,'y')

