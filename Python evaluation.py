var = input().strip().lstrip("print(").rstrip(")")
result = eval(var)
print(result)