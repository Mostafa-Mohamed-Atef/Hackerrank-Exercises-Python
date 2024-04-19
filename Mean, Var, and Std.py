import numpy as np 

n,m = map(int,input().strip().split(' '))
arr = np.array([input().strip().split(' ') for m in range(n)],dtype=int)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr,axis=None),11))
