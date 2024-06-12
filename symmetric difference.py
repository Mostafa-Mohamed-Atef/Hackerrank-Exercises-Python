m = int(input())
a = set(map(int,input().strip().split()))
n = int(input())
b = set(map(int,input().strip().split()))
d1 = set(sorted(a.difference(b)))
d2 = set(sorted(b.difference(a)))
x = sorted(d1.union(d2))
[print(i) for i in x]   