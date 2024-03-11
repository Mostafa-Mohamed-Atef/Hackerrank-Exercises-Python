import numpy

def arrays(arr):
    arr1 = numpy.array(arr,dtype=float)
    return arr1[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)