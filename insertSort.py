__author__ = 'Tarik'

def sort(A):
    first = 0
    secondLast = len(A)-1
    for i in range(secondLast):
        print "startWith=", A
        e = A[i+1]
        print "e=", e
        j = i
        while (j >= first and e < A[j]):
            A[j + 1] = A[j]
            print A[j], "to", j+1
            j = j-1
        A[j + 1] = e
        print "finally", e, "to", j+1
        print "result=",A
        print "\n"
    return A
  