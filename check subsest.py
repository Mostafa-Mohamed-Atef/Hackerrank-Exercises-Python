test_cases = int(input())
for i in range(test_cases):
    a_elements = int(input())
    A = set(map(int,input().strip().split()))
    b_elements = int(input())
    B = set(map(int,input().strip().split()))
    print (A.issubset(B))
