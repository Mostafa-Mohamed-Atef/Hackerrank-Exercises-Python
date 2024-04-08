import numpy as np
n,m=map(int,input().strip().split(' '))
a = [np.array(input().strip().split(' '),dtype=int) for i in range(n)]
b = [np.array(input().strip().split(' '),dtype=int) for i in range(n)]
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))