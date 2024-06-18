n1 = int(input())
set1 = set(map(int,input().strip().split()))
n2 = int(input())
for i in range(n2):
    command = input().split()
    try:
        if 'intersection_update' in command:
            set2=set(map(int,input().strip().split()))
            set1.intersection_update(set2)
        elif 'update' in command:
            set2=set(map(int,input().strip().split()))
            set1.update(set2)
        elif 'symmetric_difference_update' in command:
            set2=set(map(int,input().strip().split()))
            set1.symmetric_difference_update(set2)
        elif 'difference_update' in command:
            set2=set(map(int,input().strip().split()))
            set1.difference_update(set2)
    except KeyError:
        pass
print(sum(set1))