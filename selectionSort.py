__author__ = 'Tarik'

def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

def sort(A):
    """
        A is the array that wants to be sorted
    """
    first = 0
    last = len(A)
    for i in range(first, last):
        minPos = i
        minKey = A[minPos]
        for j in range(i+1, last):
            if (A[j] < minKey):
                minPos = j
                minKey = A[minPos]
        swap(A, i, minPos)
    return A
