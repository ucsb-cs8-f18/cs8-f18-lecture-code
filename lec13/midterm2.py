def indexOfSmallestOdd_a(alist):
    if type(alist)!=list:
        return False
    if alist==[]:
        return False

    soFar = 0
    for i in range(0,len(alist)): 
        if type(alist[i])!=int:     
            return False
        if alist[i] %2 == 1:
            soFar = i
    return soFar


def indexOfSmallestOdd_b(alist):
    if type(alist)!=list:
        return False
    if alist==[]:
        return False

    soFar = False
    for i in range(0,len(alist)): 
        if type(alist[i])!=int:   
            return False
        if alist[i] %2 == 1:
            soFar = i
            return soFar


def indexOfSmallestOdd_c(alist):
    if type(alist)!=list:
        return False
    if alist==[]:
        return False

    soFar = False
    for i in range(0,len(alist)): 
        if type(alist[i])!=int:     
            return False
        if alist[i] %2 == 1:
            if soFar == False:
                soFar = i
            if alist[i] < alist[soFar]:
                soFar = i
    return soFar

print("Set 1")
print(indexOfSmallestOdd_a([9,10,20,40]))
print(indexOfSmallestOdd_a([2,10,11,7]))
print(indexOfSmallestOdd_a([2,7,5,10]))
print(indexOfSmallestOdd_a([2,4,6,8]))


print("Set 2")
print(indexOfSmallestOdd_b([9,10,20,40]))
print(indexOfSmallestOdd_b([2,10,11,7]))
print(indexOfSmallestOdd_b([2,7,5,10]))
print(indexOfSmallestOdd_b([2,4,6,8]))

print("Set 3")
print(indexOfSmallestOdd_c([9,10,20,40]))
print(indexOfSmallestOdd_c([2,10,11,7]))
print(indexOfSmallestOdd_c([2,7,5,10]))
print(indexOfSmallestOdd_c([2,4,6,8]))
