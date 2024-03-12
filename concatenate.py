import numpy as np 

n,m,p = map(int,input().strip().split(' '))
arr1 = np.array([input().strip().split(' ') for p in range(n)],dtype=int)
arr2 = np.array([input().strip().split(' ') for p in range(m)],dtype=int)
arr3 = np.concatenate((arr1,arr2))
print(arr3)