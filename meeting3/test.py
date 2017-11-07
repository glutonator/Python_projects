
class Surprise():
    a = 44
    b = []
    def __init__(self, name):
        self.name = name
        
sup1 = Surprise('pierwsza')
sup2 = Surprise('druga')

def print_surprises():
    print(Surprise, Surprise.a, Surprise.b) # ,Surprise.name) <- tego się nie da bo jeszcze nie jest dostępne
    print(sup1, sup1.a, sup1.b, sup1.name)
    print(sup2, sup2.a, sup2.b, sup2.name)
    
print_surprises()