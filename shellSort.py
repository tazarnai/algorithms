__author__ = 'Tarik'

def sort(A):
    first = 0
    last = len(A)
    h = last - first / 2
    while (h > 0):
        print "h =", h
        for i in range(last-h):
            e = A[i+h]
            print "e = ", e, "from position",i+h
            j = i
            while j >= first and e < A[j]:
                A[j + h] = A[j]
                print A[j], "from", j, "to", j+h
                j = j - h
            A[j + h] = e
            print e, "from e to", h + j
        h = h / 2
        print "\n"
    return A