import calendar 

x = list(map(int,input().strip().split()))
print(calendar.day_name[calendar.weekday(x[2],x[0],x[1])].upper())
