count = 0

def selectionSort(L,n):
    global count
    for i in range(n-1):
        bigindex = 0
        for j in range(n-i):
            count = count + 1
            if(L[j] > L[bigindex]):
                bigindex = j
        L[j], L[bigindex] = L[bigindex], L[j]
    return L

def insertionSort(L,n):
    global count
    for i in range(1,n):
        index = L[i]
        j = i-1
        while(j >= 0 and index < L[j]):
            count = count + 1
            L[j+1] = L[j]
            j = j - 1
        count = count + 1
        L[j+1] = index
    return L

def retcount():
    global count
    temp = count
    count = 0
    return temp
