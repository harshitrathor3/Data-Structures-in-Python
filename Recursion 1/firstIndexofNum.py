def find(i, x):
    if i>=len(arr):
        return -2
    if arr[i]==x:
        return i
    else:
        return find(i+1, x)

def find1(arr, x):
    if len(arr)<1:
        return -1
    if arr[0]==x:
        return 1
    else:
        ans = find1(arr[1:], x)+1
        if ans==0:
            return -1
        else:
            return ans

arr = list(map(int, input().split()))
x = int(input())
# print(find(0, x)+1)
print(find1(arr, x))