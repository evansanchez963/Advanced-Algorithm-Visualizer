from matplotlib import pyplot as plt
from random import randrange
import Task1
import Task2
import Task3

def main():
    task = int(input("Select a task(1, 2, or 3): "))
    mode = int(input("Select mode(1 for User Testing, 2 for Scatter Plot): "))

    if task == 1:
        if mode == 1:
            print("Task 1")
            k = int(input("Choose value of k: "))
            print("Fib(k) = ",Task1.Fib(k))
            print("GCD(Fib(k+1), Fib(k)) = ",Task1.GCD(Task1.Fib(k+1),Task1.Fib(k)))
        elif mode == 2:
            values = []
            Fib_ops = []
            Euclid_ops = []
            print("Task 1")

            for i in range(10):
                values.append(i)
                Fib_ops.append(Task1.A(i))
                Euclid_ops.append(Task1.Euclid(Task1.Fib(i+1),Task1.Fib(i)))

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
        if mode == 1:
            print("Task 2")
            a = int(input("Choose a value for a: "))
            n = int(input("Choose a value for n: "))
            print("Decrease by One: ",Task2.exp_DB1(a,n))
            print("Decrease by Constant Factor: ",Task2.exp_DBC(a,n))
            print("Divide and Conquer: ",Task2.exp_DaC(a, n))

        elif mode == 2:
            values = []
            DB1_ops = []
            DBC_ops = []
            DaC_ops = []
            a = 2
            n = 15

            for i in range(n + 1):
                values.append(i)
                DB1_ops.append(Task2.M_DB1(a,i))
                DBC_ops.append(Task2.M_DBC(a,i))
                DaC_ops.append(Task2.M_DaC(a,i))

            plt.scatter(values, DB1_ops, c='r', label='Decrease By One')
            plt.scatter(values, DBC_ops, c='g', label='Decrease By Constant')
            plt.scatter(values, DaC_ops, c='b', label='Divide and Conquer')
            plt.title("Exponentiation")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Operations")
            plt.legend(loc=2)
            plt.show()

    elif task==3:
        if mode == 1:
            print("Task 3")
            n = int(input("Choose the size of a list: "))
            list = []
            for i in range(n):
                list.append(randrange(100))
            print("Original list: ",list)
            a = list.copy()
            print("List sorted by selection sort: ",Task3.selectionSort(a,len(a)))
            b = list.copy()
            print("List sorted by insertion sort:",Task3.insertionSort(b,len(b)))

        elif mode == 2:
            values = []
            selectionOps = []
            insertionOps = []
            worst_case = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            avg_case = [5, 3, 10, 7, 1, 8, 2, 6, 4, 9]
            best_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            'Show Worst Case'
            for i in range(len(worst_case)):
                a = worst_case.copy()
                b = worst_case.copy()
                values.append(i)
                selectionOps.append(Task3.CselectionSort(a,i))
                insertionOps.append(Task3.CinsertionSort(b,i))
            plt.scatter(values, selectionOps, c='r', label='Selection Sort')
            plt.scatter(values, insertionOps, c='b', label='Insertion Sort')
            plt.title("Worst Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Operations")
            plt.legend(loc=2)
            plt.show()
            selectionOps.clear()
            insertionOps.clear()

            'Show Average Case'
            for i in range(len(avg_case)):
                a = avg_case.copy()
                b = avg_case.copy()
                selectionOps.append(Task3.CselectionSort(a, i))
                insertionOps.append(Task3.CinsertionSort(b, i))
            plt.scatter(values, selectionOps, c='r', label='Selection Sort')
            plt.scatter(values, insertionOps, c='b', label='Insertion Sort')
            plt.title("Average Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Operations")
            plt.legend(loc=2)
            plt.show()
            selectionOps.clear()
            insertionOps.clear()

            'Show Best Case'
            for i in range(len(worst_case)):
                a = best_case.copy()
                b = best_case.copy()
                selectionOps.append(Task3.CselectionSort(a, i))
                insertionOps.append(Task3.CinsertionSort(b, i))
            plt.scatter(values, selectionOps, c='r', label='Selection Sort')
            plt.scatter(values, insertionOps, c='b', label='Insertion Sort')
            plt.title("Best Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Operations")
            plt.legend(loc=2)
            plt.show()

main()

