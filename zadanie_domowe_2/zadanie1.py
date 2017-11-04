
def power(n, p=2):
    if ((n == 0) & (p < 0)):
        out = "n lub p mniejsze od 0"
    elif ((n >= 0) & (p >= 0)):
        out = n ** p
    else:
        out = "n lub p mniejsze od 0"
    return out


print(power(0, -5), power(5), power(5, 3), power(2, 10))

print(power(0, 5), power(5, 0), power(0, 0),
      power(-5, 0), power(0, -5), power(-8, -6))
assert power(5) == 25
assert power(5, 3) == 125
