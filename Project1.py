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

            for i in range(30):
                values.append(i)
                Task1.Fib(i)
                Fib_ops.append(Task1.retcount())
                Task1.GCD(Task1.Fib(i+1),Task1.Fib(i))
                Euclid_ops.append(Task1.retcount2())

            plt.plot(values,Fib_ops, '-o')
            plt.title("Fibonacci Sequence")
            plt.xlabel("Value of k")
            plt.ylabel("Number of Operations")
            plt.show()

            plt.plot(values,Euclid_ops, '-o')
            plt.title("Euclid's Algorithm")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Modulo Divisions")
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
            n = 30

            for i in range(n + 1):
                values.append(i)
                Task2.exp_DB1(a,i)
                DB1_ops.append(Task2.retcount())
                Task2.exp_DBC(a,i)
                DBC_ops.append(Task2.retcount())
                Task2.exp_DaC(a,i)
                DaC_ops.append(Task2.retcount())

            plt.plot(values, DB1_ops, '-o', c='r', label='Decrease By One')
            plt.plot(values, DBC_ops, '-o', c='g', label='Decrease By Constant')
            plt.plot(values, DaC_ops, '-o', c='b', label='Divide and Conquer')
            plt.title("Exponentiation")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Multiplications")
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
            worst_case = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            avg_case = [5, 3, 11, 14, 18, 10, 7, 19, 1, 15, 20, 8, 12, 2, 16, 6, 13, 17, 4, 9]
            best_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

            'Show Worst Case'
            for i in range(len(worst_case)):
                a = worst_case.copy()
                b = worst_case.copy()
                values.append(i)
                Task3.insertionSort(a,i)
                insertionOps.append(Task3.retcount())
                Task3.selectionSort(b,i)
                selectionOps.append(Task3.retcount())

            plt.plot(values, selectionOps, '-o', c='r', label='Selection Sort')
            plt.plot(values, insertionOps, '-o', c='b', label='Insertion Sort')
            plt.title("Worst Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Comparisons")
            plt.legend(loc=2)
            plt.show()
            selectionOps.clear()
            insertionOps.clear()

            'Show Average Case'
            for i in range(len(avg_case)):
                a = avg_case.copy()
                b = avg_case.copy()
                Task3.insertionSort(a, i)
                insertionOps.append(Task3.retcount())
                Task3.selectionSort(b, i)
                selectionOps.append(Task3.retcount())

            plt.plot(values, selectionOps, '-o', c='r', label='Selection Sort')
            plt.plot(values, insertionOps, '-o', c='b', label='Insertion Sort')
            plt.title("Average Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Comparisons")
            plt.legend(loc=2)
            plt.show()
            selectionOps.clear()
            insertionOps.clear()

            'Show Best Case'
            for i in range(len(worst_case)):
                a = best_case.copy()
                b = best_case.copy()
                Task3.insertionSort(a, i)
                insertionOps.append(Task3.retcount())
                Task3.selectionSort(b, i)
                selectionOps.append(Task3.retcount())

            plt.plot(values, selectionOps, '-o', c='r', label='Selection Sort')
            plt.plot(values, insertionOps, '-o', c='b', label='Insertion Sort')
            plt.title("Best Case")
            plt.xlabel("Value of n")
            plt.ylabel("Number of Comparisons")
            plt.legend(loc=2)
            plt.show()

main()
