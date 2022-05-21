def search(x, l, r):
    if l>r:
        return -1
    m = (l+r)//2
    if arr[m]==x:
        return m
    elif arr[m]>x:
        return search(x, l, m-1)
    else:
        return search(x, m+1, r)
    

arr = list(map(int, input().split()))
n = int(input())
print(search(n, 0, len(arr)-1))