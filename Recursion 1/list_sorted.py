def check(arr):
    if len(arr)<2:
        return True
    if arr[0]<=arr[1]:
        return check(arr[1:])
    else:
        return False

arr = list(map(int, input().split()))
print(check(arr))
# if check(arr):
#     print('Yes')
# else:
#     print('No')