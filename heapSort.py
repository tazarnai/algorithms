import sys

__author__ = 'Tarik'

def upHeap(A, n):
    e = A[n]
    A[0] = sys.maxint
    k = n
    while A[k / 2] <= e:
        A[k] = A[k / 2]
        k = k / 2
    A[k] = e

def insert(A, n, e):
    n = n + 1
    A[n] = e
    upHeap(A, n)
    return n

def downHeap(A, n, k):
    e = A[k]
    while k <= n / 2:
        j = 2 * k
        if j < n and A[j] < A[j + 1]:
            j = j + 1
        if e >= A[j]:
            break
        A[k] = A[j]
        k = j
    A[k] = e

def removeMax(A, n):
    A[1] = A[n]
    n = n - 1
    downHeap(A, n, 1)
    return n

def sort(A):
    A.insert(0,sys.maxint)
    first = 1
    last = len(A)
    n = 0
    for i in range(first,last):
        n = insert(A, n, A[i])
    for i in range(last, first - 1, -1):
        n = removeMax(A, n)
    return A


