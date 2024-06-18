n = int(input())
for i in range(n):
    try:
        values = list(map(int,input().strip().split()))
        print(values[0]//values[1])
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:' , e) 
