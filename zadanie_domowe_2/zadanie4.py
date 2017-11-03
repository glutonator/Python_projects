
def factorial(n):
    out = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        out = n * factorial(n - 1)
        return out


assert factorial(5) == 120

for i in range(0, 10):
    print(factorial(i))
