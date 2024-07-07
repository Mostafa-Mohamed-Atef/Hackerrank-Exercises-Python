from itertools import *
s,n = input().strip().split()
[print(''.join(j)) for i in range(1,int(n)+1) for j in combinations(sorted(s),i)]
