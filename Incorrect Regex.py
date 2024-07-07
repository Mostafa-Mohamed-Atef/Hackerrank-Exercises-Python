import re 

t = int(input())
s = [input().strip() for _ in range(t)]
for i in s:
    try:
        re.compile(i)
        print(True)
    except re.error:
        print(False)