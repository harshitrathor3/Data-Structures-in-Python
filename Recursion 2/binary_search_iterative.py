def search(x):
    l = 0
    r = len(arr)-1

    while l<=r:
        m = (l+r)//2
        if arr[m]==x:
            return m
        elif arr[m]>x:
            r = m-1
        else:
            l = m+1
    return -1


arr = list(map(int, input().split()))
x = int(input())
print(search(x))