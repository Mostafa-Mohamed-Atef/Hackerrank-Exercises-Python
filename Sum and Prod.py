import numpy as np 

n,m = map(int,input().strip().split(' '))
arr = np.array([input().strip().split(' ') for m in range(n)],dtype=int)
sum = np.sum(arr,axis=0)
print(np.prod(sum,axis=0))
