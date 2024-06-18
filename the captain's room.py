import collections
n = int(input())
rooms = map(int,input().strip().split())
counter = dict(collections.Counter(rooms))
for k,v in counter.items():
    if v==1:
        print(k)
        break