from matplotlib import pyplot as plt

"Task 1 Functions"
def A(k):
    if k == 0 or k == 1:
        return 0;
    return A(k-1) + A(k-2) + 1

def Fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return Fib(k-2) + Fib(k-1)

def Euclid(m, n):
    if n == 0 or n == 1:
        return 0
    return 1 + Euclid(n, m % n)

"Task 2 Functions"
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

"Main"
def main():
    "Task 1"
    task = int(input("Select a task: "))

    if task==1:
        values = []
        Fib_ops = []
        Euclid_ops = []
        print("Task 1")
        input1 = int(input("Enter a value for k: "))

        for i in range(input1):
            values.append(i)
            Fib_ops.append(A(i))
            Euclid_ops.append(Euclid(Fib(i+1),Fib(i)))


        plt.scatter(values,Fib_ops)
        plt.title("Fibonnaci Sequence")
        plt.xlabel("Value of k")
        plt.ylabel("Number of Operations")
        plt.show()

        plt.scatter(values,Euclid_ops)
        plt.title("Euclid's Algorithm")
        plt.xlabel("Value of k")
        plt.ylabel("Number of Operations")
        plt.show()

    elif task==2:
        values = []
        DB1_ops = []
        DBC_ops = []
        DaC_ops = []
        print("Task 2")
        input1 = int(input("Enter a value for a: "))
        input2 = int(input("Enter a value for n: "))

        for i in range(input2 + 1):
            values.append(i)
            DB1_ops.append(M_DB1(input1,i))
            DBC_ops.append(M_DBC(input1,i))
            DaC_ops.append(M_DaC(input1,i))

        plt.scatter(values, DB1_ops, c='r', label='Decrease By One')
        plt.scatter(values, DBC_ops, c='g', label='Decrease By Constant')
        plt.scatter(values, DaC_ops, c='b', label='Divide and Conquer')
        plt.title("Exponentiation")
        plt.xlabel("Value of n")
        plt.ylabel("Number of Operations")
        plt.legend(loc=2)
        plt.show()

    else:
        print("Choose 1, 2, or 3.")
        exit(1)

main()


