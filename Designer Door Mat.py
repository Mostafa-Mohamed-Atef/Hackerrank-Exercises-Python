n, m = map(int, input().strip().split())
welcome = [ 'WELCOME'.center(m, '-') ]
x = [('.|.'*(2*i+1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(x +welcome+ x[::-1]))