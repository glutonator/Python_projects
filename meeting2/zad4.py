
def draw_tree(o, w):
    for i in range(o):
        print((o-i-1)*' '+(1+2*i)*w)


draw_tree(3,'T')
draw_tree(4,'Y')
draw_tree(5,'y')

