__author__ = 'Tarik'

def getIntArray():
    return [5,3,2,8,23,21,2,0,30,10,10,4,1,9,11,10]

def getStringArray():
    return [
        "Jacob",
        "Isabella",
        "Ethan",
        "Emma",
        "Michael",
        "Olivia",
        "Alexander",
        "Sophia",
        "William",
        "Ava",
        "Joshua",
        "Emily",
        "Daniel",
        "Madison",
        "Jayden",
        "Abigail",
        "Noah",
        "Chloe",
        "Anthony",
        "Mia",
    ]

def sort(method, A):
    print "From", A
    B = method(A)
    print "Get", B