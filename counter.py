import collections
num_shoes = int(input()) #number of shoes
sizes = list(map(int,input().split()))
counter = collections.Counter(sizes)
num_customers = int(input())
money = 0
for i in range(num_customers):
    customer_size = list(map(int,input().split()))
    if counter[customer_size[0]] !=0:
        money+=customer_size[1]
        counter[customer_size[0]] -= 1
print(money)
