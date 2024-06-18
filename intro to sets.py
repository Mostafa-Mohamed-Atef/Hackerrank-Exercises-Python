def average(array):
    x = set(array)
    return round(sum(x) / len(x),3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)