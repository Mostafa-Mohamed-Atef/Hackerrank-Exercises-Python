A = set(map(int,input().strip().split()))
n = int(input())
print(all([A.issuperset(set(map(int, input().split()))) for i in range(n)]))
