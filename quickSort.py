__author__ = 'Tarik'

def swap(A, a, b):
    print "swap:", a, "<==>",b
    temp = A[a]
    print temp, "<==>", A[b]
    A[a] = A[b]
    A[b] = temp

def quickSort(A, first, last):
    print "call quickSort", A, first, last
    if first < last:
        x = A[(first + last)/2]
        print "x = ", x, "from", (first + last)/2
        i = first
        j = last
        while i <= j:
            print "i:",i
            while A[i] < x:
                i = i + 1
                print "i:",i
            print "j:",j
            while A[j] > x:
                j = j - 1
                print "j:",j
            print "i:",i, "j:",j
            if i <= j:
                swap(A, i, j)
                i = i + 1
                j = j - 1
        quickSort(A, first, j)
        quickSort(A, i, last)
    return A

def sort(A):
    first = 0
    last = len(A)-1
    return quickSort(A, first, last)