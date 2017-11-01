##dowolna liczba arg do funckcji
#numbers jest to zmienna typu tupla
def sum_numbers(*numbers):
    result = 0
    for x in numbers:
        result += x
    return result

#wszystkie argumenty które są przekazane przez nazwę
def print_kargs(**kwargs):
    #k,w to stringi
    for k,v in kwargs.items():
        print(k)
        print(v)
        
def sum_numbesdsdrs(*numbers, **kwargs):
    result = 0
    for x in numbers:
        result += x
    
    for k,v in kwargs.items():
        print(k)
        print(v)
    
    return result

print_kargs(k=1,t=8,y="dssd")
sum_numbesdsdrs(1,2,3,4,5,k=1,t=8,y="dssd")
print(sum_numbers(1,2,3,4,5,6,7))

def sum_numbessdffdsdsdrs(a,*numbers, **kwargs):
    print(a)
    print(numbers)
    print(kwargs)

sum_numbessdffdsdsdrs("sda",1,2,3,4,5,k=1,t=8,y="dssd")
