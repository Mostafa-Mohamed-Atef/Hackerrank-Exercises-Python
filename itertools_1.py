from itertools import product
A = map(int,input().strip().split())
B = map(int,input().strip().split())
x = list(product(A,B))
[print(i, end=' ') for i in x]