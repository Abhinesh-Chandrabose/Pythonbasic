def rectangle_area(l, b):
    return l * b
def highest(a,b):
    if (a>b):
        return a
    else:
        return b
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True