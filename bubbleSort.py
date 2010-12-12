__author__ = 'Tarik'

def swap(A, a, b):
    print "swap:", a, "<==>",b
    temp = A[a]
    print temp, "<==>", A[b]
    A[a] = A[b]
    A[b] = temp

def sort(A):
    first = 0
    last = len(A) - 1
    for i in range(last, first, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
        print "temp result = ", A
    return A