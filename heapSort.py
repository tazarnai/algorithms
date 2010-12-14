import sys

__author__ = 'Tarik'

def upHeap(A, n):
    e = A[n]
    print "e:", e
    k = n
    while A[k / 2] <= e:
        A[k] = A[k / 2]
        print "Ak",A[k]
        k = k / 2
        print "Ak/2",A[k / 2]
        print "<=", e
    A[k] = e

def insert(A, n, e):
    n = n + 1
    A[n] = e
    upHeap(A, n)
    return n

def swap(A, a, b):
    print "swap:", a, "<==>",b
    temp = A[a]
    print temp, "<==>", A[b]
    A[a] = A[b]
    A[b] = temp

def downHeap(A, n, k):
    e = A[k]
    while k <= n / 2:
        j = 2 * k
        if j < n and A[j] < A[j + 1]:
            j = j + 1
        if e >= A[j]:
            break
        print j, "to", k
        print A[j], "to", A[k]
        A[k] = A[j]
        k = j
    print "set", k, "to", e
    A[k] = e

def removeMax(A, n):
    swap(A, 1, n)
    n = n - 1
    downHeap(A, n, 1)
    return n

def sort(A):
    if isinstance(A[0],int):
        A.insert(0,sys.maxint)
        print "int"
    elif isinstance(A[0],type("")):
        print "string"
        A.insert(0,"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
        print A
    else:
        return A

    first = 1
    last = len(A)
    n = 0
    for i in range(first,last):
        n = insert(A, n, A[i])
    print "Middle",A
    for i in range(last, first, -1):
        n = removeMax(A, n)
    return A


