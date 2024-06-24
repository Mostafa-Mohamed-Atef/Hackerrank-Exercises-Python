from itertools import *
s,n = input().strip().split()
x = list(permutations(sorted(s),int(n)))
[print(''.join(i)) for i in x]
