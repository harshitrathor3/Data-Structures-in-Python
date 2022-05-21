def check(i):
    if i>=len(arr)-1:
        return True
    if arr[i]<=arr[i+1]:
        return check(i+1)
    else:
        return False

arr= list(map(int, input().split()))

print(check(0))