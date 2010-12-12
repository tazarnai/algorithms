__author__ = 'Tarik'

def swap(A, a, b):
    print "swap:", a, "<==>",b
    temp = A[a]
    print temp, "<==>", A[b]
    A[a] = A[b]
    A[b] = temp

def sort(A):
    first = 0
    last = len(A)
    noSwaps = False
    gap = last - first + 1
    while gap > 1 or not noSwaps:
        gap = gap * 10 / 13
        if gap == 0:
            gap = 1
        print "gap = ", gap
        noSwaps = True
        for i in range(last - gap):
            print "compare", A[i], "to", A[i + gap]
            if A[i] > A[i + gap]:
                noSwaps = False
                swap(A , i, i+gap)
        print "temp result", A
    return A    






