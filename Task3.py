def selectionSort(L,n):
    for i in range(n-1):
        bigindex = 0
        for j in range(n-i):
            if(L[j] > L[bigindex]):
                bigindex = j
        L[j], L[bigindex] = L[bigindex], L[j]
    return L

def insertionSort(L,n):
    for i in range(1,n):
        index = L[i]
        j = i-1
        while(j >= 0 and index < L[j]):
            L[j+1] = L[j]
            j = j - 1
        L[j+1] = index
    return L

def CselectionSort(L,n):
    count = 0
    for i in range(n-1):
        bigindex = 0
        for j in range(n-i):
            if(L[j] > L[bigindex]):
                count = count + 1
                bigindex = j
        L[j], L[bigindex] = L[bigindex], L[j]
    return count

def CinsertionSort(L,n):
    count = 0
    for i in range(1,n):
        index = L[i]
        j = i-1
        while(j >= 0 and index < L[j]):
            count = count + 1
            L[j+1] = L[j]
            j = j - 1
        L[j+1] = index
    return count
