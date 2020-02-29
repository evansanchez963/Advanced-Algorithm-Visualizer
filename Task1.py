count = 0
count2 = 0

def Fib(k):
    global count
    if k == 0:
        return 0
    if k == 1:
        return 1
    count = count + 1
    return Fib(k-2) + Fib(k-1)

def GCD(m, n):
    global count2
    if m == 0:
        count2 = count2 + 1
        return n
    count2 = count2 + 1
    return GCD(n%m, m)

def retcount():
    global count
    temp = count
    count = 0
    return temp

def retcount2():
    global count2
    temp = count2
    count2 = 0
    return temp
