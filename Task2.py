def exp_DB1(a, n):
    if n == 0:
        return 1
    return a * exp_DB1(a, n-1)

def exp_DBC(a, n):
    if n == 0:
        return 1
    if(n%2 == 0):
        return exp_DBC(a, n/2)**2
    return a*exp_DBC(a,(n-1)/2)**2

def exp_DaC(a,n):
    if n == 0:
        return 1
    if(n%2 == 0):
        return exp_DaC(a,n/2) * exp_DaC(a,n/2)
    return a*exp_DaC(a,(n-1)/2)*exp_DaC(a,(n-1)/2)

def M_DB1(a,n):
    if n == 0:
        return 1
    return exp_DB1(a, n-1) + 1

def M_DBC(a, n):
    if n == 0:
        return 1
    if(n%2 == 0):
        return exp_DBC(a, n/2) + 1
    return exp_DBC(a,(n-1)/2) + 2

def M_DaC(a, n):
    if n == 0:
        return 1
    if(n%2 == 0):
        return exp_DaC(a,n/2) + exp_DaC(a,n/2) + 1
    return exp_DaC(a,(n-1)/2) + exp_DaC(a,(n-1)/2) + 2
