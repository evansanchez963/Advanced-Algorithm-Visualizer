def A(k):
    if k == 0 or k == 1:
        return 1;
    return A(k-1) + A(k-2) + 1

def Fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return Fib(k-2) + Fib(k-1)

def Euclid(m, n):
    if m == 0:
        return 0
    return 1 + Euclid(n%m, m)

def GCD(m, n):
    if m == 0:
        return n
    return GCD(n%m, m)
