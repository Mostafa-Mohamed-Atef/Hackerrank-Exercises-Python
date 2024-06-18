m,n = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))
happ = 0
for i in arr:
    if i in A:
        happ+=1
    if i in B:
        happ-=1
print(happ)

