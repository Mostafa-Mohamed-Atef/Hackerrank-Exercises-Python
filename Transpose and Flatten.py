import numpy as np 

n,m = map(int,input().strip().split(' '))
arr = np.array([input().strip().split(' ') for m in range(n)],dtype=int)
print(arr.transpose(),arr.flatten(),sep='\n')