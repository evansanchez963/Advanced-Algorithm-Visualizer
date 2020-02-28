count = 0

def exp_DB1(a, n):
    global count
    if n == 0:
        return 1
    count = count + 1
    return a * exp_DB1(a, n-1)

def exp_DBC(a, n):
    global count
    if n == 0:
        return 1
    if(n%2 == 0):
        count = count + 1
        return exp_DBC(a, n/2)**2
    count = count + 2
    return a*exp_DBC(a,(n-1)/2)**2

def exp_DaC(a,n):
    global count
    if n == 0:
        return 1
    if(n%2 == 0):
        count = count + 1
        return exp_DaC(a,n/2) * exp_DaC(a,n/2)
    count = count + 2
    return a*exp_DaC(a,(n-1)/2)*exp_DaC(a,(n-1)/2)

def retcount():
    global count
    temp = count
    count = 0
    return temp
