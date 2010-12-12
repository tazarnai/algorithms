__author__ = 'Tarik'

def swap(A, a, b):
    print "swap:", a, "<==>",b
    temp = A[a]
    print temp, "<==>", A[b]
    A[a] = A[b]
    A[b] = temp

def sort(A):
    """
        A is the array that wants to be sorted
    """
    last = len(A)
    for i in range(last):
        minPos = i
        minKey = A[minPos]
        for j in range(i+1, last):
            if (A[j] < minKey):
                minPos = j
                minKey = A[minPos]
        swap(A, i, minPos)
    return A
