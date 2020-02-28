count = 0

def Fib(k):
    global count
    if k == 0:
        return 0
    if k == 1:
        return 1
    count = count + 1
    return Fib(k-2) + Fib(k-1)

def GCD(m, n):
    global count
    if m == 0:
        return n
    count = count + 1
    return GCD(n%m, m)

def retcount():
    global count
    temp = count
    count = 0
    return temp
