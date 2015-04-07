# anna's code

def fibonacci(n):
    F1 = 0
    F2 = 1
    F = 0

    for i in range(1,(n+1)):
        F1 = F2
        F2 = F
        F = F2 + F1
    return F

def lucas(m):
    F1 = 2
    F2 = 1
    F = 2

    if m == 0:
        F = 2
    elif m == 1:
        F = 1
    else:
        for i in range(1,m):
            F1 = F2
            F2 = F
            F = F2 + F1
    return F

print fibonacci(5)
