n = int(input())
alphabet = [chr(i) for i in range(97,123)]
alphabet = alphabet[:n]
x = list(range(n)) #0, 1, 2 , 1, 0
x = x[:-1]+x[::-1]
for i in x:
    start = i+1
    original = alphabet[-start:]
    reversed = original[::-1]
    row =reversed+original[1:]
    row = '-'.join(row).center(n * 4 - 3, '-') 
    print(row)