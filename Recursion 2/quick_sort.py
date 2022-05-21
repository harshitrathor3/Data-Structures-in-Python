def f(arr, s, e):
    cnt=0
    n = arr[s]
    for i in arr[s:e+1]:
        if i<n:
            cnt+=1
    arr[s], arr[s+cnt] = arr[s+cnt], arr[s]
    i = s
    j = e
    while i<cnt+s:
        if arr[i]>=n and arr[j]<n:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        if arr[i]<n:
            i+=1
        if arr[j]>=n:
            j-=1
    return cnt+s


def sort(arr, s, e):
    if s>=e:
        return
    n= f(arr, s, e)
    sort(arr, s, n-1)
    sort(arr, n+1, e)
    
# int(input())
arr = list(map(int, input().split()))
sort(arr, 0, len(arr)-1)
print(arr)
