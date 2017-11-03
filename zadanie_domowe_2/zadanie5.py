def no_arg():
    return 5

def ident(x):
    return x

def mult(x, y):
    return x * y

def function_results_sum(*args, **kwargs):
    suma =0
    for x in args:       
        #print(x.__name__)
        if (x.__name__ in kwargs):
            #print(kwargs[x.__name__]) 
            if type(kwargs[x.__name__])==tuple:         
                suma+=x(*kwargs[x.__name__])
                print(x(*kwargs[x.__name__]))
            else: 
                suma+=x(kwargs[x.__name__])
                print(x(kwargs[x.__name__]))
        else:
            suma+=x()
            print(x())
    return suma
    

#function_results_sum(no_arg, ident, mult, ident=9, mult=(4,5))
#function_results_sum(mult, mult=(4,5,2))
assert function_results_sum(no_arg, ident, mult, ident=2, mult=(3, 4)) == 19
